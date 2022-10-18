import os
import subprocess
from time import sleep
from celery import shared_task
from .models import EndAnswer, Question, QuestionLibrary
import xml.etree.ElementTree as ET
import re
from .process.process_helper import trim_text, markdown_to_plain, trim_md_to_html

from .process.questionbuilder.truefalse import build_inline_TF, build_endanswer_TF
from .process.questionbuilder.multiplechoice import build_inline_MC, build_endanswer_MC
from .process.questionbuilder.multipleselect import build_inline_MS, build_endanswer_MS
from .process.questionbuilder.fib import build_inline_FIB, build_endanswer_FIB
from .process.questionbuilder.matching import build_inline_MAT, build_endanswer_MAT
from .process.questionbuilder.ordering import build_inline_ORD, build_endanswer_ORD
from .process.questionbuilder.writtenresponse import build_inline_WR_with_keyword, build_inline_WR_with_list, build_endanswer_WR_with_list

import logging
logger = logging.getLogger(__name__)
from .logging.contextfilter import QuestionlibraryFilenameFilter
logger.addFilter(QuestionlibraryFilenameFilter())

import elasticapm
elastic_client = elasticapm.get_client()

def check_inline_questiontype(question, answers, wr_answer):
    answers_length = len(answers)
    marked_answers_count = 0
    unmarked_answers_count = 0
    matching_answers_count = 0
    KeywordTrueFound = False
    KeywordFalseFound = False

    is_fib = re.search(r"\[(.*?)\]", question.text)
    
    if answers_length == 0:
        if is_fib:
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

    if marked_answers_count == 1 and question.questiontype != 'MS':
        # ====================  MC confirmed  ====================
        return 'inline_MC'

    if marked_answers_count > 1 or question.questiontype == 'MS':
        # ====================  MS confirmed  ====================
        return 'inline_MS'

    if matching_answers_count == answers_length and matching_answers_count > 1 :
        # ====================  MAT confirmed  ====================
        return 'inline_MAT'

    if (unmarked_answers_count == 1 and answers_length == 1) or question.questiontype == 'WR':
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
            
        if answer_key_length == 1 and question.questiontype != 'MS':
            # ====================  MC confirmed  ====================
            return 'endanswer_MC'

        if question.questiontype == 'MS' or answer_key_length > 1:
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

@shared_task()
def parse_question(randomize_answer, question_id, endanswer=None):
    elastic_client.begin_transaction('parse')
    question = Question.objects.get(pk=question_id)
    try:
        endanswer = EndAnswer.objects.get(pk=endanswer)
    except EndAnswer.DoesNotExist:
        pass
    
    os.chdir('/questionparser/jarfile')
    popen = subprocess.Popen(
        'java -cp questionparser.jar:* questionparser', 
        shell=True,
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE
        )
    result, errors = popen.communicate(input=question.raw_content.encode("utf-8"))
    popen.stdout.close()
    return_code = popen.wait()
    os.chdir('/code')

    # print(result.stdout.decode("utf-8"))
    question.parser_output_xml = result.decode("utf-8")
    question.save()

    root = None
    try:
        root = ET.fromstring(result.decode("utf-8"))
    except:
        logger.error(f"Empty question: {question.id}")
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

    question_from_xml = root.find('question')
    answers = root.findall("answer")
    wr_answer = root.find("wr_answer")
    is_random = randomize_answer
    question_type = None
    if question_from_xml is not None:
        question.text = trim_md_to_html(question_from_xml.text)

        if question.title is None:
            title_text = re.sub(r"<<<<\d+>>>>", "[IMG]", question_from_xml.text)
            title_text = markdown_to_plain(title_text)
            title_text = title_text.replace('\n', ' ')
            title_text = trim_text(title_text)
            question.title = title_text[0:127]
        
        question.save()

    if question.questiontype == 'WR':
        if endanswer == None:
            question_type = check_inline_questiontype(question, answers, wr_answer)

            if question_type == 'inline_WR_keyword':
                build_inline_WR_with_keyword(question, wr_answer)
            elif question_type == 'inline_WR_list':
                build_inline_WR_with_list(question, answers)
            else:
                question.error = "Inline question structure doesn't conform to WR type question format." 
                question.save()
        else:
            question_type = check_endanswer_questiontype(question, answers, endanswer)

            if question_type == 'endanswer_WR':
                build_endanswer_WR_with_list(question, endanswer, wr_answer)
            else:
                question.error = "End answer question structure doesn't conform to WR type question format." 
                question.save()


    elif question.questiontype == 'MS':
        if endanswer == None:
            question_type = check_inline_questiontype(question, answers, wr_answer)
            if question_type == 'inline_MS':
                build_inline_MS(question, answers, is_random)
            else:
                question.error = "Inline question structure doesn't conform to MS type question format." 
                question.save()
        else:
            question_type = check_endanswer_questiontype(question, answers, endanswer)

            if question_type == 'endanswer_MS':
                build_endanswer_MS(question, answers, endanswer, is_random)
            else:
                question.error = "End answer question structure doesn't conform to MS type question format." 
                question.save()


    elif question.questiontype == 'ORD':
        if endanswer == None:
            question_type = check_inline_questiontype(question, answers, wr_answer)
            if question_type == 'inline_ORD':
                build_inline_ORD(question, answers)
            else:
                question.error = "Inline question structure doesn't conform to ORD type question format." 
                question.save()
        else:
            question_type = check_endanswer_questiontype(question, answers, endanswer)

            if question_type == 'endanswer_ORD':
                build_endanswer_ORD(question, endanswer)
            else:
                question.error = "End answer question structure doesn't conform to ORD type question format." 
                question.save()


    elif question.questiontype == 'MC':
        if endanswer == None:
            question_type = check_inline_questiontype(question, answers, wr_answer)
            if question_type == 'inline_MC':
                build_inline_MC(question, answers, is_random)
            else:
                question.error = "Inline question structure doesn't conform to MC type question format." 
                question.save()
        else:
            question_type = check_endanswer_questiontype(question, answers, endanswer)

            if question_type == 'endanswer_MC':
                build_endanswer_MC(question, answers, endanswer, is_random)
            else:
                question.error = "End answer question structure doesn't conform to MC type question format." 
                question.save()


    elif question.questiontype == 'TF':
        if endanswer == None:
            question_type = check_inline_questiontype(question, answers, wr_answer)
            if question_type == 'inline_TF':
                build_inline_TF(question, answers)
            else:
                question.error = "Inline question structure doesn't conform to TF type question format." 
                question.save()
        else:
            question_type = check_endanswer_questiontype(question, answers, endanswer)

            if question_type == 'endanswer_TF':
                build_endanswer_TF(question, answers, endanswer)
            else:
                question.error = "End answer question structure doesn't conform to TF type question format." 
                question.save()
    

    elif question.questiontype == 'FIB':
        if endanswer == None:
            question_type = check_inline_questiontype(question, answers, wr_answer)
            if question_type == 'inline_FIB':
                build_inline_FIB(question, question_from_xml.text)
            else:
                question.error = "Inline question structure doesn't conform to FIB type question format." 
                question.save()
        else:
            question_type = check_endanswer_questiontype(question, answers, endanswer)

            if question_type == 'endanswer_FIB':
                build_endanswer_FIB(question, endanswer, question_from_xml.text)
            else:
                question.error = "End answer question structure doesn't conform to FIB type question format." 
                question.save()
    

    elif question.questiontype == 'MAT':
        if endanswer == None:
            question_type = check_inline_questiontype(question, answers, wr_answer)
            if question_type == 'inline_MAT':
                build_inline_MAT(question, answers)
            else:
                question.error = "Inline question structure doesn't conform to MAT type question format." 
                question.save()
        else:
            question_type = check_endanswer_questiontype(question, answers, endanswer)

            if question_type == 'endanswer_MAT':
                build_endanswer_MAT(question, endanswer)
            else:
                question.error = "End answer question structure doesn't conform to MAT type question format." 
                question.save()

    
    else:
    # all other types try autodetect and compare if the given type is correct. if not then notify user.
            
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
                    # print("inline_NO_TYPE")
                    pass
                case 'endanswer_NO_TYPE':
                    # print("endanswer_NO_TYPE")
                    pass
    elastic_client.end_transaction('parse')
    return question_id


@shared_task()
def run_pandoc_task(questionlibrary_id):
    try:
        import pypandoc
        from django.core.files.base import ContentFile
        questionlibrary = QuestionLibrary.objects.get(pk=questionlibrary_id)
        mdblockquotePath = "./api_v3/pandoc-filters/mdblockquote.lua"
        emptyparaPath = "./api_v3/pandoc-filters/emptypara.lua"
        # listsPath = "./api_v3/pandoc-filters/lists.lua"
        pandoc_word_to_html = pypandoc.convert_file(questionlibrary.temp_file.path,
                                                    format='docx+empty_paragraphs',
                                                    to='html+empty_paragraphs+tex_math_single_backslash',
                                                    extra_args=['--no-highlight', '--self-contained', '--markdown-headings=atx', '--preserve-tabs', '--wrap=preserve', '--indent=false', '--mathml',
                                                    '--ascii'])
        pandoc_word_to_html = re.sub(r"(?!\s)<math>", " <math>", pandoc_word_to_html)
        pandoc_word_to_html = re.sub(r"</math>(?!\s)", "</math> ", pandoc_word_to_html)
        pandoc_html_to_md = pypandoc.convert_text(
            pandoc_word_to_html,
            'markdown_github+fancy_lists+emoji+hard_line_breaks+all_symbols_escapable+escaped_line_breaks+grid_tables+startnum+tex_math_dollars',
            format='html+empty_paragraphs',
            extra_args=['--no-highlight', '--self-contained', '--markdown-headings=atx', '--preserve-tabs', '--wrap=preserve', '--indent=false', '--mathml', '--ascii',
                        '--lua-filter=' + mdblockquotePath, '--lua-filter=' + emptyparaPath])
        # questionlibrary.pandoc_output_file = ContentFile("\n" + pandoc_html_to_md, name="pandoc_output.md")
        # questionlibrary.pandoc_output = "\n" + pandoc_html_to_md
        # questionlibrary.save()

        return "\n" + pandoc_html_to_md

    except Exception as e:
        raise MarkDownConversionError(e)

class MarkDownConversionError(Exception):
    def __init__(self, reason, message="File invalid"):
        self.reason = reason
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} -> {self.reason}'