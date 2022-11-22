import logging
import os
import re
import subprocess
import xml.etree.ElementTree as ET

import elasticapm
from celery import shared_task
from celery.utils.log import get_task_logger

from api_v3.logging.ErrorTypes import (WRInlineStructureError, WREndStructureError, MSInlineStructureError, MSEndStructureError, ORDInlineStructureError, ORDEndStructureError, MCInlineStructureError, MCEndStructureError, TFInlineStructureError, TFEndStructureError, FIBInlineStructureError, FIBEndStructureError, MATInlineStructureError, MATEndStructureError, InlineNoTypeError, EndAnswerNoTypeError, NoTypeDeterminedError, MarkDownConversionError)
from api_v3.logging.WarningTypes import (RespondusTypeEWarning, RespondusTypeMRWarning, RespondusTypeFMBWarning, RespondusTypeMTWarning)

from .logging.logging_adapter import FilenameLoggingAdapter
from .models import EndAnswer, Question, QuestionLibrary
from .process.process_helper import (add_error_message, add_warning_message, html_to_plain, markdown_to_plain, markdown_to_html, trim_md_to_html, trim_text)
from .process.questionbuilder.fib import build_endanswer_FIB, build_inline_FIB
from .process.questionbuilder.matching import (build_endanswer_MAT, build_inline_MAT)
from .process.questionbuilder.multiplechoice import (build_endanswer_MC, build_inline_MC)
from .process.questionbuilder.multipleselect import (build_endanswer_MS, build_inline_MS)
from .process.questionbuilder.ordering import (build_endanswer_ORD, build_inline_ORD)
from .process.questionbuilder.truefalse import (build_endanswer_TF, build_inline_TF)
from .process.questionbuilder.writtenresponse import (build_endanswer_WR_with_list, build_inline_WR_with_keyword, build_inline_WR_with_list)

logger = logging.getLogger(__name__)
loggercelery = get_task_logger(__name__)
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

    if marked_answers_count == 1 and (question.questiontype != 'MS' and question.questiontype != 'MR'):
        # ====================  MC confirmed  ====================
        return 'inline_MC'

    if marked_answers_count > 1 or (question.questiontype == 'MS' or question.questiontype == 'MR'):
        # ====================  MS confirmed  ====================
        return 'inline_MS'

    if matching_answers_count == answers_length and matching_answers_count > 1 :
        # ====================  MAT confirmed  ====================
        return 'inline_MAT'

    if (unmarked_answers_count == 1 and answers_length == 1) or (question.questiontype == 'WR' or question.questiontype == 'E'):
        # ====================  WR confirmed  ====================
        return 'inline_WR_list'

    if answers_length > 0 and unmarked_answers_count == answers_length:
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
                    return 'endanswer_NO_TYPE'


            if answer_text == 'true':
                KeywordTrueFound = True

            if answer_text == 'false':
                KeywordFalseFound = True
        
        if answers_length == 2 and KeywordTrueFound == True and KeywordFalseFound == True:
            # ====================  TF confirmed  ====================
            return 'endanswer_TF'
            
        if answer_key_length == 1 and (question.questiontype != 'MS' and question.questiontype != 'MR'):
            # ====================  MC confirmed  ====================
            return 'endanswer_MC'

        if (question.questiontype == 'MS' or question.questiontype == 'MR') or answer_key_length > 1:
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
    questionlibrary = question.section.question_library

    logger = FilenameLoggingAdapter(loggercelery, {
        'filename': questionlibrary.temp_file.name,
        'user_ip': questionlibrary.user_ip
        })

    try:
        endanswer = EndAnswer.objects.get(pk=endanswer)
    except EndAnswer.DoesNotExist:
        logger.info("No End answer found")

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
    except Exception as e:
        logger.warning(f"Empty question: {question.id}")
        return "Empty question: " + str(e) 

# ================================# ================================
#   GET QUESTION DATA FROM XML
# ================================# ================================

    try:
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

        # Filter out the last letter enumerated list so that it can be set as the answerlist
        start_of_list_found = False
        answer_list = []
        part_of_question_list = []
        # Start iterating from the last item going up untill the index "a" is found and continue adding the rest of the lists as question content
        for answer in reversed(answers):
            if not start_of_list_found:
                answer_list.append(answer)
            else:
                part_of_question_list.append(answer)
            check_index = ''.join(filter(str.isalpha, answer.find('index').text.lower()))
            if check_index == "a":
                start_of_list_found = True

        # because we started from the last item we need to reverse the list to bring in correct order
        answers = answer_list[::-1]
        part_of_question_list = part_of_question_list[::-1]

        # add the remaining lists as content by appending the the question content
        add_to_question_content = ""
        for question_list_item in part_of_question_list:
            add_to_question_content += f"{question_list_item.find('index').text}{question_list_item.find('content').text}"
        question_from_xml.text += add_to_question_content


    except Exception as e:  
        logger.error(f"Failed to get question data from xml {str(e)}") 
        return "#" + str(question.number_provided) + " " + str(e)

    # Re-init logging adapter with available question number 

    logger = FilenameLoggingAdapter(loggercelery, {
        'filename': questionlibrary.temp_file.name,
        'user_ip': questionlibrary.user_ip,
        'question': str(question.number_provided)
        })

# ================================# ================================
#   CHECK TYPES AND BUILD QUESTION
# ================================# ================================
 
    try:
        if question_from_xml is not None:
            question_text = trim_md_to_html(question_from_xml.text)
            question.text = question_text

            if question.title is None:
                title_text = re.sub(r"<table(.|\n)+?</table>", "[TABLE]", question_text)
                title_text = html_to_plain(title_text)
                title_text = re.sub(r"<<<<\d+>>>>", "[IMG]", title_text)
                title_text = title_text.replace('\n', ' ')
                title_text = trim_text(title_text)
                prefix = ''
                if '[TABLE]' in title_text:
                    prefix = '[TABLE]' + prefix
                if '[IMG]' in title_text:
                    prefix = '[IMG]' + prefix
                if prefix:
                    prefix = prefix + ' '
                    title_text = re.sub("\s*\[IMG\]", "", title_text).strip()
                    title_text = re.sub("\s*\[TABLE\]", "", title_text).strip()
                    
                title_text = prefix + title_text
                question.title = title_text[0:127]
            question.save()
    except Exception as e:
        return str(question.number_provided) + " " + str(e) 


# ================================# ================================
#   Written Response
# ================================# ================================
    question_type = None

    try:
        if question.questiontype == 'WR' or question.questiontype == 'E':
            try:
                if question.questiontype == 'E':
                    warning_message = 'Respondus format "Type: E" was found on the file. Please use "Type: WR" instead.'
                    add_warning_message(question, warning_message)
                    raise RespondusTypeEWarning(question.warning)
            except Exception as e:
                logger.error(e)
                # raise Exception(e)
            
            try:
                if endanswer == None:
                    question_type = check_inline_questiontype(question, answers, wr_answer)

                    if question_type == 'inline_WR_keyword':
                        build_inline_WR_with_keyword(question, wr_answer)
                    elif question_type == 'inline_WR_list':
                        build_inline_WR_with_list(question, answers)
                    else:
                        error_message = "Inline question structure doesn't conform to WR type question format."
                        add_error_message(question, error_message)
                        raise WRInlineStructureError(question.error)
                else:
                    question_type = check_endanswer_questiontype(question, answers, endanswer)

                    if question_type == 'endanswer_WR':
                        build_endanswer_WR_with_list(question, endanswer, wr_answer)
                    else:
                        error_message = "End answer question structure doesn't conform to WR type question format."
                        add_error_message(question, error_message)
                        raise WREndStructureError(question.error)
            except Exception as e:
                logger.error(e)
                # raise Exception(e)

# ================================# ================================
#   Multi Select
# ================================# ================================


        elif question.questiontype == 'MS' or question.questiontype == 'MR':
            try:
                if question.questiontype == 'MR':
                    warning_message = 'Respondus format "Type: MR" was found on the file. Please use "Type: MS" instead.'
                    add_warning_message(question, warning_message)
                    raise RespondusTypeMRWarning(question.warning)
            except Exception as e:
                logger.error(e)
                # raise Exception(e)

            try:
                if endanswer == None:
                    question_type = check_inline_questiontype(question, answers, wr_answer)
                    if question_type == 'inline_MS':
                        build_inline_MS(question, answers, is_random)
                    else:
                        error_message = "Inline question structure doesn't conform to MS type question format."
                        add_error_message(question, error_message)
                        raise MSInlineStructureError(question.error)
                else:
                    question_type = check_endanswer_questiontype(question, answers, endanswer)

                    if question_type == 'endanswer_MS':
                        build_endanswer_MS(question, answers, endanswer, is_random)
                    else:
                        error_message = "End answer question structure doesn't conform to MS type question format."
                        add_error_message(question, error_message)
                        raise MSEndStructureError(question.error)
            except Exception as e:
                logger.error(e)
                # raise Exception(e)

# ================================# ================================
#   ORDERING
# ================================# ================================

        elif question.questiontype == 'ORD':
            try:
                if endanswer == None:
                    question_type = check_inline_questiontype(question, answers, wr_answer)
                    if question_type == 'inline_ORD':
                        build_inline_ORD(question, answers)
                    else:
                        error_message = "Inline question structure doesn't conform to ORD type question format."
                        add_error_message(question, error_message)
                        raise ORDInlineStructureError(question.error)
                else:
                    question_type = check_endanswer_questiontype(question, answers, endanswer)

                    if question_type == 'endanswer_ORD':
                        build_endanswer_ORD(question, endanswer)
                    else:
                        error_message = "End answer question structure doesn't conform to ORD type question format."
                        add_error_message(question, error_message)
                        raise ORDEndStructureError(question.error)
            except Exception as e:
                logger.error(e)
                # raise Exception(e)

# ================================# ================================
#   MULTIPLE CHOICE
# ================================# ================================

        elif question.questiontype == 'MC':
            try:
                if endanswer == None:
                    question_type = check_inline_questiontype(question, answers, wr_answer)
                    if question_type == 'inline_MC':
                        build_inline_MC(question, answers, is_random)
                    else:
                        error_message = "Inline question structure doesn't conform to MC type question format."
                        add_error_message(question, error_message)
                        raise MCInlineStructureError(question.error)
                else:
                    question_type = check_endanswer_questiontype(question, answers, endanswer)

                    if question_type == 'endanswer_MC':
                        build_endanswer_MC(question, answers, endanswer, is_random)
                    else:
                        error_message = "End answer question structure doesn't conform to MC type question format."
                        add_error_message(question, error_message)
                        raise MCEndStructureError(question.error)
            except Exception as e:
                logger.error(e)
                # raise Exception(e)

# ================================# ================================
#   TRUE-FALSE
# ================================# ================================

        elif question.questiontype == 'TF':
            try:
                if endanswer == None:
                    question_type = check_inline_questiontype(question, answers, wr_answer)
                    if question_type == 'inline_TF':
                        build_inline_TF(question, answers)
                    else:
                        error_message = "Inline question structure doesn't conform to TF type question format."
                        add_error_message(question, error_message)
                        raise TFInlineStructureError(question.error)
                else:
                    question_type = check_endanswer_questiontype(question, answers, endanswer)

                    if question_type == 'endanswer_TF':
                        build_endanswer_TF(question, answers, endanswer)
                    else:
                        error_message = "End answer question structure doesn't conform to TF type question format."
                        add_error_message(question, error_message)
                        raise TFEndStructureError(question.error)
            except Exception as e:
                logger.error(e)
                # raise Exception(e)

# ================================# ================================
#   FILL IN BLANK
# ================================# ================================

        elif question.questiontype == 'FIB' or question.questiontype == 'FMB':
            try:
                if question.questiontype == 'FMB':
                    warning_message = 'Respondus format "Type: FMB" was found on the file. Please use "Type: FIB" instead.'
                    add_warning_message(question, warning_message)
                    raise RespondusTypeFMBWarning(question.warning)
            except Exception as e:
                logger.error(e)
                # raise Exception(e)

            try:
                if endanswer == None:
                    question_type = check_inline_questiontype(question, answers, wr_answer)
                    if question_type == 'inline_FIB':
                        build_inline_FIB(question, question_from_xml.text)
                    else:
                        error_message = "Inline question structure doesn't conform to FIB type question format."
                        add_error_message(question, error_message)
                        raise FIBInlineStructureError(question.error)
                else:
                    question_type = check_endanswer_questiontype(question, answers, endanswer)

                    if question_type == 'endanswer_FIB':
                        build_endanswer_FIB(question, endanswer, question_from_xml.text)
                    else:
                        error_message = "End answer question structure doesn't conform to FIB type question format."
                        add_error_message(question, error_message)
                        raise FIBEndStructureError(question.error)
            except Exception as e:
                logger.error(e)
                # raise Exception(e)

# ================================# ================================
#   MATCHING
# ================================# ================================

        elif question.questiontype == 'MAT' or question.questiontype == 'MT':
            try:
                if question.questiontype == 'MT':
                    warning_message = 'Respondus format "Type: MT" was found on the file. Please use "Type: MAT" instead.'
                    add_warning_message(question, warning_message)
                    raise RespondusTypeMTWarning(question.warning)
            except Exception as e:
                logger.error(e)
                # raise Exception(e)
                
            try:
                if endanswer == None:
                    question_type = check_inline_questiontype(question, answers, wr_answer)
                    if question_type == 'inline_MAT':
                        build_inline_MAT(question, answers)
                    else:
                        error_message = "Inline question structure doesn't conform to MAT type question format."
                        add_error_message(question, error_message)
                        raise MATInlineStructureError(question.error)
                else:
                    question_type = check_endanswer_questiontype(question, answers, endanswer)

                    if question_type == 'endanswer_MAT':
                        build_endanswer_MAT(question, endanswer)
                    else:
                        error_message = "End answer question structure doesn't conform to MAT type question format."
                        add_error_message(question, error_message)
                        raise MATEndStructureError(question.error)
            except Exception as e:
                logger.error(e)
                # raise Exception(e)

# ================================# ================================
#   TYPE NOT GIVEN, TRY TO DETERMINE IT
# ================================# ================================

        else:
        # all other types try autodetect and compare if the given type is correct. if not then notify user.
            try:    
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
                        error_message = "Cannot determined the inline question type."
                        add_error_message(question, error_message)
                        raise InlineNoTypeError(error_message)
                    case 'endanswer_NO_TYPE':
                        error_message = "Cannot determined the end answer question type."
                        add_error_message(question, error_message)
                        raise EndAnswerNoTypeError(error_message)
            except Exception as e:
                logger.error(e)
                raise NoTypeDeterminedError("Cannot determine the question type.")
    except Exception as e:
        logger.error(str(e))
        return "#" + str(question.number_provided) + " " + str(e)

    elastic_client.end_transaction('parse')
    return "success"


@shared_task()
def run_pandoc_task(questionlibrary_id):
    questionlibrary = QuestionLibrary.objects.get(pk=questionlibrary_id)
    logger = FilenameLoggingAdapter(loggercelery, {
        'filename': questionlibrary.temp_file.name,
        'user_ip': questionlibrary.user_ip
        })
    try:
        import pypandoc
        mdblockquotePath = "./api_v3/pandoc-filters/mdblockquote.lua"
        emptyparaPath = "./api_v3/pandoc-filters/emptypara.lua"
        imageFilterPath = "./api_v3/pandoc-filters/image.lua"
        tables = "./api_v3/pandoc-filters/tables.lua"
        # listsPath = "./api_v3/pandoc-filters/lists.lua"

        pandoc_word_to_html = pypandoc.convert_file(
            questionlibrary.temp_file.path,
            format='docx+empty_paragraphs',
            to='html+empty_paragraphs+tex_math_single_backslash',
            extra_args=['--no-highlight',
            '--embed-resources',
            '--markdown-headings=atx',
            '--preserve-tabs',
            '--wrap=preserve',
            '--indent=false',
            '--mathml',
            '--ascii',
            # '--lua-filter=' + imageFilterPath
            ])
        pandoc_word_to_html = re.sub(r"(?!\s)<math>", " <math>", pandoc_word_to_html)
        pandoc_word_to_html = re.sub(r"</math>(?!\s)", "</math> ", pandoc_word_to_html)
        pandoc_html_to_md = pypandoc.convert_text(
            pandoc_word_to_html,
            'markdown_github+fancy_lists+emoji+hard_line_breaks+all_symbols_escapable+escaped_line_breaks+pipe_tables+startnum+tex_math_dollars',
            format='html+empty_paragraphs',
            extra_args=['--no-highlight', 
                        '--embed-resources',
                        '--markdown-headings=atx', 
                        '--preserve-tabs', 
                        '--wrap=preserve', 
                        '--indent=false', 
                        '--mathml', 
                        '--ascii',
                        '--lua-filter=' + mdblockquotePath, 
                        '--lua-filter=' + emptyparaPath,
                        # '--lua-filter=' + tables
                        ])
        return "\n" + pandoc_html_to_md
    except Exception as e:
        logger.debug(e)
        raise MarkDownConversionError(e)

# @shared_task()
# def convert_html_to_md(questionlibrary_id):
#     questionlibrary = QuestionLibrary.objects.get(pk=questionlibrary_id)
#     logger = FilenameLoggingAdapter(loggercelery, {
#         'filename': questionlibrary.temp_file.name,
#         'user_ip': questionlibrary.user_ip
#         })
#     try:
#         logger.debug("pdf to markdown STARTING")
#         import pypandoc
#         from pathlib import Path

#         mdblockquotePath = "./api_v3/pandoc-filters/mdblockquote.lua"
#         emptyparaPath = "./api_v3/pandoc-filters/emptypara.lua"
#         tables = "./api_v3/pandoc-filters/tables.lua"

#         logger.debug(f"cehck filename : {questionlibrary.temp_file}")
#         docfilepath = Path("/code/temp/" + questionlibrary.temp_file.name)
#         if docfilepath.is_file():
#             html_file_path = Path("/code/temp/" + str(questionlibrary.id)+ "/" + docfilepath.stem + ".html")
#             if html_file_path.is_file():
#                 html_input_file_path = "/code/temp/" + str(questionlibrary.id)+ "/" + docfilepath.stem + ".html"
#                 logger.debug(f"cehck pdf path : {html_input_file_path}")

#                 pandoc_html_to_md = pypandoc.convert_file(html_input_file_path,
#                                                         format='html+empty_paragraphs',
#                                                         to='markdown_github+fancy_lists+emoji+hard_line_breaks+all_symbols_escapable+escaped_line_breaks+grid_tables+startnum+tex_math_dollars',
#                                                         extra_args=['--no-highlight', 
#                                                                     '--self-contained', 
#                                                                     '--markdown-headings=atx', 
#                                                                     '--preserve-tabs', 
#                                                                     '--wrap=preserve', 
#                                                                     '--indent=false', 
#                                                                     '--mathml', 
#                                                                     '--ascii',
#                                                                     '--lua-filter=' + mdblockquotePath, 
#                                                                     '--lua-filter=' + emptyparaPath,
#                                                                     '--lua-filter=' + tables
#                                                                     ])
#                 logger.debug("html to markdown finished")
#                 return "\n" + pandoc_html_to_md
#     except Exception as e:
#         logger.debug(e)
#         raise MarkDownConversionError(e)
