import os
import subprocess
import re
import xml.etree.ElementTree as ET
from ..models import EndAnswer, Section, Question
from .process_helper import trim_text, markdown_to_plain, trim_md_to_html
from .questionbuilder.truefalse import build_inline_TF, build_endanswer_TF
from .questionbuilder.multiplechoice import build_inline_MC, build_endanswer_MC
from .questionbuilder.multipleselect import build_inline_MS, build_endanswer_MS
from .questionbuilder.fib import build_inline_FIB, build_endanswer_FIB
from .questionbuilder.matching import build_inline_MAT, build_endanswer_MAT
from .questionbuilder.ordering import build_inline_ORD, build_endanswer_ORD
from .questionbuilder.writtenresponse import build_inline_WR_with_keyword, build_inline_WR_with_list, build_endanswer_WR_with_list


from django.conf import settings
import logging
logger = logging.getLogger(__name__)
from api_v3.logging.contextfilter import QuestionlibraryFilenameFilter

def run_parser(questionlibrary):
    loggingfilter = QuestionlibraryFilenameFilter(questionlibrary=questionlibrary)
    logger.addFilter(loggingfilter)
    import time
    sections = Section.objects.filter(question_library=questionlibrary)
    if len(sections) == 0:
        raise ParserError("No sections found for the parser to work on")
    endanswers = EndAnswer.objects.filter(question_library=questionlibrary)    
    question_count = 0
    section_count = 0
    start_time = time.time()
    for section in sections:
        questions = Question.objects.filter(section=section)
        if section.is_main_content:
            if settings.DEBUG:
                print("\nRoot section:")
        else:
            section_count += 1
            if settings.DEBUG:
                print("\nSection", section_count, ":", section.title )

        section.questions_expected = len(questions) - 1
        section_start_time = time.time()
        section_question_count = 0
        for idx, question in enumerate(questions):
            # discard empty question
            if question.raw_content is None:
                question.delete()
            else:
                if len(endanswers) != 0:
                    parse_question(questionlibrary, question, endanswers[idx])
                else:
                    parse_question(questionlibrary, question)
            
            section_question_count += 1
            if settings.DEBUG:
                print("    question : " + str(question_count + section_question_count))
        question_count += section_question_count
        section_end_time = time.time()
        section.processing_time = section_end_time - section_start_time
        section.save()
        if settings.DEBUG:
            print("  Section total questions :", section_question_count)
            print("  Section processing time :", section.processing_time)
    logger.info(f'Total Processing time for Parser : {time.time() - start_time}')
    if settings.DEBUG:
        print("\nProccessing Time Total :", time.time() - start_time)

def parse_question(questionlibrary, question, endanswer=None):

    os.chdir('/questionparser/jarfile')
    result = subprocess.run(
        'java -cp questionparser.jar:* questionparser',
        shell=True,
        input=question.raw_content.encode("utf-8"),
        capture_output=True)
    os.chdir('/code')

    # print(result.stdout.decode("utf-8"))
    question.parser_output_xml = result.stdout.decode("utf-8")
    question.save()

    root = None
    try:
        root = ET.fromstring(result.stdout.decode("utf-8"))
    except:
        pass

    questiontype = root.find('type')
    if questiontype is not None:
        question.questiontype = trim_text(questiontype.text)

    title = root.find('title')
    if title is not None:
        title_text = markdown_to_plain(title.text)
        title_text = title_text.replace('\n', ' ')
        question.title = trim_text(title_text)

    points = root.find('points')
    if points is not None:
        filterpoint = re.search("\d+((.|,)\d+)?", points.text)
        question.points = float(filterpoint.group())

    question_number = root.find('question_number')
    if question_number is not None:
        filter_question_number = re.search("\d+", question_number.text)
        question.number_provided = filter_question_number.group()

    question_feedback = root.find('question_feedback')
    if question_feedback is not None:
        question.feedback = trim_md_to_html(question_feedback.text)

    if question.questiontype == 'MS':
        # TODO MS is required
        # COUNT total number of answers and correct_answer. it should be >= 2
        # answer = root.find('answer')

        pass
    else:
    # all other types try autodetect and compare if the given type is correct. if not then notify user

        question_from_xml = root.find('question')
        if question_from_xml is not None:
            question.text = trim_md_to_html(question_from_xml.text)

            if question.title is None:
                title_text = re.sub(r"<<<<\d+>>>>", "[IMG]", question_from_xml.text)
                title_text = markdown_to_plain(title_text)
                title_text = title_text.replace('\n', ' ')
                title_text = trim_text(title_text)
                question.title = title_text[0:127]
            question.save()

            answers = root.findall("answer")
            is_random = questionlibrary.randomize_answer
            wr_answer = root.find("wr_answer")

            question_type = None
            
            if endanswer == None:
                question_type = check_inline_questiontype(question, answers, wr_answer)
            else:
                question_type = check_endanswer_questiontype(question, answers, endanswer)
                
            # print("question_type:", question_type)
            match question_type:
                case 'inline_MC':
                    build_inline_MC(question, answers, is_random)
                case 'endanswer_MC':
                    build_endanswer_MC(question, answers, endanswer, is_random)
                case 'inline_TF':
                     build_inline_TF(question, answers)
                case 'endanswer_TF':
                     build_endanswer_TF(question, answers, endanswer)
                case 'inline_MS':
                    build_inline_MS(question, answers, is_random)
                case 'endanswer_MS':
                    build_endanswer_MS(question, answers, endanswer, is_random)
                case 'inline_WR_keyword':
                    build_inline_WR_with_keyword(question, wr_answer)
                case 'inline_WR_list':
                    build_inline_WR_with_list(question, answers)
                case 'endanswer_WR':
                    build_endanswer_WR_with_list(question, endanswer, wr_answer)
                case 'inline_FIB':
                    build_inline_FIB(question, question_from_xml.text)
                case 'endanswer_FIB':
                    build_endanswer_FIB(question, endanswer, question_from_xml.text)
                case 'inline_MAT':
                    build_inline_MAT(question, answers)
                case 'endanswer_MAT':
                    build_endanswer_MAT(question, endanswer)
                case 'inline_ORD':
                    build_inline_ORD(question, answers)
                case 'endanswer_ORD':
                    build_endanswer_ORD(question, endanswer)
                case 'inline_NO_TYPE':
                    print("inline_NO_TYPE")
                case 'endanswer_NO_TYPE':
                    print("endanswer_NO_TYPE")
    


def check_inline_questiontype(question, answers, wr_answer):
    answers_length = len(answers)
    marked_answers_count = 0
    unmarked_answers_count = 0
    matching_answers_count = 0
    KeywordTrueFound = False
    KeywordFalseFound = False

    is_fib = re.search(r"\[(.*?)\]", question.text)
    
    if answers_length == 0:
        if is_fib != None:
            # ====================  FIB confirmed  ====================
            return 'inline_FIB'
        
        if wr_answer != None:
            # ====================  WR confirmed  ====================
            return 'inline_WR_keyword'

    for answer in answers:
        answer_text = markdown_to_plain(answer.find('content').text.lower())
        answer_text = trim_text(answer_text)
        is_correct = answer.attrib['correct']

        if is_correct == 'true':
            marked_answers_count += 1
        if is_correct == 'false':
            unmarked_answers_count += 1


        if answer_text == 'true':
            KeywordTrueFound = True

        if answer_text == 'false':
            KeywordFalseFound = True

        matching_answers = re.search(r"(.*)=(.*)", answer_text)

        if matching_answers is not None:
            matching_answers_count += 1
        

    if answers_length == 2 and KeywordTrueFound == True and KeywordFalseFound == True:
        # ====================  TF confirmed  ====================
        return 'inline_TF'

    if marked_answers_count == 1:
        # ====================  MC confirmed  ====================
        return 'inline_MC'

    if marked_answers_count > 1:
        # ====================  MS confirmed  ====================
        return 'inline_MS'

    if matching_answers_count == answers_length and matching_answers_count > 1 :
        # ====================  MAT confirmed  ====================
        return 'inline_MAT'

    if unmarked_answers_count == 1 and answers_length == 1:
        # ====================  WR confirmed  ====================
        return 'inline_WR_list'

    if unmarked_answers_count == answers_length:
        # ====================  ORD confirmed  ====================
        return 'inline_ORD'
    
    return 'inline_NO_TYPE'


def check_endanswer_questiontype(question, answers, endanswer):
    answers_length = len(answers)
    endanswer_text = markdown_to_plain(endanswer.answer.lower())
    endanswer_text = trim_text(endanswer_text)

    if answers_length > 0:
        # possible TF, MC, MS
        answer_list = list(map(str.strip, endanswer_text.split(',')))
        answer_key_length = len(answer_list)
        KeywordTrueFound = False
        KeywordFalseFound = False
    
        for answer in answers:
            answer_text = markdown_to_plain(answer.find('content').text.lower())
            answer_text = trim_text(answer_text)

            for choice_answer in answer_list:
                correctanswer_index =  (ord(choice_answer)-97)
                
                if correctanswer_index <= (answers_length-1):
                    # answer index exist
                    pass
                else:
                    question.error = "Selected answer does NOT exist"
                    question.save()
                    return 'endanswer_NO_TYPE'


            if answer_text == 'true':
                KeywordTrueFound = True

            if answer_text == 'false':
                KeywordFalseFound = True
        
        if answers_length == 2 and KeywordTrueFound == True and KeywordFalseFound == True:
            # ====================  TF confirmed  ====================
            return 'endanswer_TF'
            
        if answer_key_length == 1:
            # ====================  MC confirmed  ====================
            return 'endanswer_MC'

        if answer_key_length > 1:
            # ====================  MS confirmed  ====================
            return 'endanswer_MS'
    
    else:
        # possible FIB, MAT, ORD, WR
        matching_answers_count = 0
        is_fib = re.findall(r"\[(.*?)\]", question.text)
        answer_list = list(map(str.strip, endanswer_text.split(';')))
        answer_key_length = len(answer_list)
        for answer in answer_list:
            matching_answer = re.search(r"(.*)=(.*)", answer)

            if matching_answer is not None:
                matching_answers_count += 1
        
        if matching_answers_count == answer_key_length and matching_answers_count > 1 :
            # =========================  MAT confirmed =======================
            return 'endanswer_MAT'
            
        if len(is_fib) == answer_key_length:
            # =========================  FIB confirmed =======================
            return 'endanswer_FIB'

        if answer_key_length > 1:
            # =========================  ORD confirmed =======================
            return 'endanswer_ORD'

        if answer_key_length == 1:
            # =========================  WR confirmed =======================
            return 'endanswer_WR'

    return 'endanswer_NO_TYPE'

class ParserError(Exception):
    def __init__(self, message="ParserError error"):
        super().__init__(message)
    def __str__(self):
        return f'{self.message}'
