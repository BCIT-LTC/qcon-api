import os
from xml.dom.minidom import TypeInfo
import xml.etree.ElementTree as ET
import logging
import subprocess
import sys
import re
import pypandoc
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

from .models import Section, Question, MultipleChoice, MultipleChoiceAnswer, MultipleSelect, \
MultipleSelectAnswer, Ordering, TrueFalse, Matching, MatchingAnswer, MatchingChoice, Image, \
WrittenResponse, EndAnswer, Fib


def create_main_title():
    pass

class FormatterError(Exception):
    pass

def extract_images(questionlibrary):
    x = re.findall(r"<img src=.*/>", questionlibrary.pandoc_output)

    if len(x) == 0:
        return 0

    for image in x:
        image_object = Image.objects.create(question_library=questionlibrary)
        image_object.save()
        image_object.image = image
        image_object.save()

    model_images = Image.objects.filter(question_library=questionlibrary)

    for modelimage in model_images:
        val = re.escape(modelimage.image)          
        x = re.sub(val, "<<<<"+ str(modelimage.id) +">>>>" , questionlibrary.pandoc_output)
        questionlibrary.pandoc_output = x
        questionlibrary.save()

    return len(model_images)  
# This is to split end_answers and body and trim the unused data at the top
def run_formatter(questionlibrary):

    os.chdir('/formatter/jarfile')
    result = subprocess.run('java -cp formatter.jar:* formatter',
                            shell=True,
                            input=questionlibrary.pandoc_output.encode(),
                            capture_output=True)
    os.chdir('/code')

    root = None
    try:
        root = ET.fromstring(result.stdout.decode("utf-8"))
    except:
        raise FormatterError("Not valid")

    try:
        if root[0].tag == "body":
            questionlibrary.formatter_output = root[0].text
            questionlibrary.save()
            pass
        else:
            logger.error("Body not found")
            raise FormatterError("Body not found")
    except:
        logger.error("Body not found")
        raise FormatterError("Body not found")

    try:
        if root[1].tag == "end_answers":
            questionlibrary.end_answers_raw = root[1].text
            questionlibrary.save()
        else:
            # logger.warning("Answer Section not found")
            pass
    except:
        # logger.warning("Answer section not found")
        pass

# This is to split sections into separate objects
def run_sectioner(questionlibrary):

    os.chdir('/sectioner/jarfile')
    result = subprocess.run(
        'java -cp sectioner.jar:* sectioner',
        shell=True,
        input=questionlibrary.formatter_output.encode("utf-8"),
        capture_output=True)
    os.chdir('/code')

    # print(result.stdout.decode("utf-8"))
    questionlibrary.sectioner_output = result.stdout.decode("utf-8")
    questionlibrary.save()

    root = None
    try:
        root = ET.fromstring(result.stdout.decode("utf-8"))
    except:
        return

    subsection_count = 0
    for section in root:

        sectionobject = Section.objects.create(
            question_library=questionlibrary)

        sectionobject.save()

        sectionobject.order = section.attrib.get("id")

        sectiontitle = section.find('title')
        if sectiontitle is not None:
            section_title_text = markdown_to_plain(sectiontitle.text)
            section_title_text = section_title_text.replace('\n', ' ')
            sectionobject.title = trim_text(section_title_text)

        maincontent = section.find('maincontent')
        if maincontent is not None:
            sectionobject.raw_content = maincontent.text
            sectionobject.is_main_content = True
            sectionobject.title = questionlibrary.main_title

        sectioncontent = section.find('sectioncontent')
        if sectioncontent is not None:
            sectionobject.raw_content = sectioncontent.text
            sectionobject.is_main_content = False
            sub_section += 1

        sectionobject.save()
    return subsection_count



def run_splitter(questionlibrary):

    sections = Section.objects.filter(question_library=questionlibrary)

    questions_count = 0
    for section in sections:
        questions_count_section = split_questions(section)
        questions_count += questions_count_section

        # remove empty sections
        if questions_count_section == 0:        
            section.delete()

    return questions_count

def split_questions(sectionobject):

    os.chdir('/splitter/jarfile')
    result = subprocess.run(
        'java -cp splitter.jar:* splitter',
        shell=True,
        input=sectionobject.raw_content.encode("utf-8"),
        capture_output=True)
    os.chdir('/code')

    root = None
    try:
        root = ET.fromstring(result.stdout.decode("utf-8"))
    except:
        return 0

    questions_found = 0
    for question in root:

        questionobject = Question.objects.create(
            section=sectionobject)

        questionobject.save()

        content = question.find('content')
        if content is not None:
            # Filter out empty questions
            if len(trim_text(content.text)) > 0:
                questions_found += 1
                questionobject.raw_content = content.text
        questionobject.save()
    return questions_found

def get_endanswers(questionlibrary):

    if questionlibrary.end_answers_raw == None:
        return 0

    os.chdir('/endanswers/jarfile')
    result = subprocess.run(
        'java -cp endanswers.jar:* endanswers',
        shell=True,
        input=questionlibrary.end_answers_raw.encode("utf-8"),
        capture_output=True)
    os.chdir('/code')

    root = None
    try:
        root = ET.fromstring(result.stdout.decode("utf-8"))
    except:
        pass

    answers = root.findall("answer")   
    endanswers_found = 0
    if answers is not None:
        for answer in answers:
            endanswer = EndAnswer.objects.create(question_library=questionlibrary)      

            content = answer.find('content').text
            index  = answer.find('index').text
            indexdigit = re.search(r'\d+', index)

            endanswer.index = indexdigit.group(0)
            endanswer.answer = content
            endanswers_found += 1
            endanswer.save()

    questionlibrary.save()
    return endanswers_found

# This function will most likely writes directly to model. Might need to move to model instead
def run_parser(questionlibrary):
    import time
    sections = Section.objects.filter(question_library=questionlibrary)
    question_count = 0
    section_count = 0
    start_time = time.time()
    for section in sections:
        questions = Question.objects.filter(section=section)
        if section.is_main_content:
            print("\nRoot section:")
        else:
            section_count += 1
            print("\nSection", section_count, ":", section.title )

        section.questions_expected = len(questions) - 1
        section_start_time = time.time()
        section_question_count = 0
        for question in questions:
            # discard empty question
            if question.raw_content is None:
                question.delete()
            else:
                parse_question(questionlibrary, question)
            section_question_count += 1
            print("    question : " + str(question_count + section_question_count))
        question_count += section_question_count
        section_end_time = time.time()
        section.processing_time = section_end_time - section_start_time
        section.save()
        print("  Section total questions :", section_question_count)
        print("  Section processing time :", section.processing_time)
    print("\nProccessing Time Total :", time.time() - start_time)
    

def parse_question(questionlibrary, question):

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
            marked_answers_count = 0
            unmarked_answers_count = 0
            matching_answers_count = 0
            for answer in answers:
                if answer.attrib['correct'] == 'true':
                    marked_answers_count += 1
                if answer.attrib['correct'] == 'false':
                    unmarked_answers_count += 1

                matchanswers = re.search(r"(.*)=(.*)", answer.find('content').text)

                if matchanswers is not None:
                    matching_answers_count += 1

            # Check if answers are included
            if len(answers) > 0:

                if matching_answers_count == len(answers) and matching_answers_count > 1 :
                    # =========================  MAT confirmed =======================

                    mat_object = Matching.objects.create(question=question)
                    mat_object.save()

                    for answer in answers:
                        answercontent = trim_text(answer.find('content').text)
                        regpattern = r"((.+)\\?`\s*=\s*\\?`(.+))|((.+)==(.+))|((.+)=(.+))"
                        choice_answer_groups_regex = re.search(regpattern, answercontent)

                        if choice_answer_groups_regex is not None:
                            group_num = []
                            if choice_answer_groups_regex.group(1):
                                group_num.extend([2, 3])
                            elif choice_answer_groups_regex.group(4):
                                group_num.extend([5, 6])
                            elif choice_answer_groups_regex.group(7):
                                group_num.extend([8, 9])
                            else:
                                # This should be impossible as we made sure the answer would have an `=`
                                print("No match in MAT answer")

                            mat_choice_text = choice_answer_groups_regex.group(group_num[0]).strip()
                            mat_choice_text = markdown_to_html(mat_choice_text)

                            mat_answer_text = choice_answer_groups_regex.group(group_num[1]).strip()
                            mat_answer_text = markdown_to_html(mat_answer_text)

                            if mat_choice_text == "":
                                mat_choice.error = "matching choice missing"
                                mat_object.error = "one or more matching or answer choices missing"
                            else:
                                if mat_object.get_matching_choice_by_text(mat_choice_text):
                                    mat_choice = mat_object.get_matching_choice_by_text(mat_choice_text)
                                else:
                                    mat_choice = MatchingChoice.objects.create(matching=mat_object)
                                    mat_choice.choice_text = mat_choice_text
                                    mat_choice.save()

                            if mat_choice.has_matching_answer(mat_answer_text):
                                # duplicate matching_answer
                                pass
                            else:
                                mat_answer = MatchingAnswer.objects.create(matching_choice=mat_choice)

                            if mat_answer_text == "":
                                mat_answer.error = "matching answer missing"
                                mat_object.error = "one or more matching or answer choices missing"
                            else:

                                mat_answer.answer_text = mat_answer_text

                        else:
                            mat_choice = MatchingChoice.objects.create(matching=mat_object)
                            mat_answer = MatchingAnswer.objects.create(matching_choice=mat_choice)
                            mat_choice.error = "matching choice missing"
                            mat_answer.error = "matching answer missing"
                            mat_object.error = "one or more matching or answer choices missing"

                        mat_choice.save()
                        mat_answer.save()

                    mat_object.save()
                    question.questiontype = 'MAT'
                    question.save()
                    return

                if marked_answers_count == 1:
                    if unmarked_answers_count == 1:
                        # check if both false and true keyword are found
                        tf_object = TrueFalse.objects.create(question=question)

                        KeywordTrueFound = False
                        KeywordFalseFound = False

                        for answer in answers:
                            answer_text = markdown_to_plain(answer.find('content').text.lower())
                            answer_text = trim_text(answer_text)
                            if answer_text == 'true':
                                KeywordTrueFound = True
                                try:
                                    tf_object.true_feedback = trim_md_to_html(answer.find('feedback').text)
                                except:
                                    pass
                                if answer.attrib['correct'] == 'true':
                                    tf_object.true_weight = 100

                            if answer_text == 'false':
                                KeywordFalseFound = True
                                try:
                                    tf_object.false_feedback = trim_md_to_html(answer.find('feedback').text)
                                except:
                                    pass
                                if answer.attrib['correct'] == 'true':
                                    tf_object.false_weight = 100

                        if KeywordTrueFound == True and KeywordFalseFound == True:
                        # =========================  TF confirmed =======================
                        # TF confirmed here so the TF object is saved to db
                            tf_object.error = ""
                            tf_object.save()
                            question.questiontype = 'TF'
                            question.save()
                        else:
                        # One or More Keywords "true" or "false" not found. fallback to MC

                            # ========================= 2 option MC confirmed =======================
                            mc_object = MultipleChoice.objects.create(question=question)
                            mc_object.save()
                            # grab all answers

                            for answer_item in answers:
                                mc_answerobject = MultipleChoiceAnswer.objects.create(multiple_choice=mc_object)
                                mc_answerobject.index = trim_md_to_plain(trim_text(answer_item.find('index').text)).strip("*.) \n")
                                mc_answerobject.answer = trim_md_to_html(answer_item.find('content').text)

                                if(answer_item.find('feedback') is not None):
                                    mc_answerobject.answer_feedback = trim_md_to_html(answer_item.find('feedback').text)

                                if answer_item.attrib['correct'] == 'true':
                                    mc_answerobject.weight = 100
                                if answer_item.attrib['correct'] == 'false':
                                    mc_answerobject.weight = 0
                                mc_answerobject.save()

                            if questionlibrary.randomize_answer == True:
                                mc_object.randomize = True

                            question.questiontype = 'MC'
                            mc_object.save()
                            question.save()

                    if unmarked_answers_count > 1:
                        # =========================  MC confirmed =======================
                        mc_object = MultipleChoice.objects.create(question=question)
                        mc_object.save()
                        # grab all answers

                        for answer_item in answers:
                            mc_answerobject = MultipleChoiceAnswer.objects.create(multiple_choice=mc_object)
                            mc_answerobject.index = trim_md_to_plain(trim_text(answer_item.find('index').text)).strip("*.) \n")
                            mc_answerobject.answer = trim_md_to_html(answer_item.find('content').text)

                            if(answer_item.find('feedback') is not None):
                                mc_answerobject.answer_feedback = trim_md_to_html(answer_item.find('feedback').text)

                            if answer_item.attrib['correct'] == 'true':
                                mc_answerobject.weight = 100
                            if answer_item.attrib['correct'] == 'false':
                                mc_answerobject.weight = 0
                            mc_answerobject.save()

                        if questionlibrary.randomize_answer == True:
                            mc_object.randomize = True

                        question.questiontype = 'MC'
                        mc_object.save()
                        question.save()

                elif marked_answers_count > 1:
                    # =========================  MS confirmed =======================
                    ms_object = MultipleSelect.objects.create(question=question)
                    ms_object.save()
                    # grab all answers

                    for answer_item in answers:
                        ms_answerobject = MultipleSelectAnswer.objects.create(multiple_select=ms_object)
                        ms_answerobject.answer = trim_md_to_html(answer_item.find('content').text)
                        ms_answerobject.index = trim_md_to_plain(answer_item.find('index').text).strip("*.) \n")

                        if(answer_item.find('feedback') is not None):
                            ms_answerobject.answer_feedback = trim_md_to_html(answer_item.find('feedback').text)
                        if answer_item.attrib['correct'] == 'true':
                            ms_answerobject.is_correct = True
                        if answer_item.attrib['correct'] == 'false':
                            ms_answerobject.is_correct = False

                        ms_answerobject.save()

                    if questionlibrary.randomize_answer == True:
                        ms_object.randomize = True

                    question.questiontype = 'MS'
                    ms_object.save()
                    question.save()

                elif marked_answers_count == 0:

                    if unmarked_answers_count > 1:
                    # =========================  ORD confirmed =======================
                        iterator = 1
                        for answer in answers:
                        #     print(answer.find('index').text.strip())
                            ord_object = Ordering.objects.create(question=question)
                            ord_object.order = iterator
                            iterator += 1
                            ord_object.text = trim_md_to_html(answer.find('content').text)

                            if(answer.find('feedback') is not None):
                                ord_object.ord_feedback = trim_md_to_html(answer.find('feedback').text)

                            ord_object.save()

                        question.questiontype = 'ORD'
                        question.save()
                    elif unmarked_answers_count == 1:
                    # =========================  WR confirmed =======================
                        wr_object = WrittenResponse.objects.create(question=question)
                        for answer in answers:
                            try:
                                wr_object.answer_key = trim_md_to_html(answer.find('content').text)
                            except:
                                pass
                        wr_object.save()
                        question.questiontype = 'WR'
                        question.save()

            elif len(answers) == 0:
                # answer list not included
                # This is most likely an essay type question or FIB. check if "correct_answer" token is present                
                wr_answer = root.find("wr_answer")   
                if wr_answer is not None:
                    # =========================  WR confirmed with correct answer keyword=======================
                    wr_object = WrittenResponse.objects.create(question=question)
                    try:
                        wr_object.answer_key = trim_md_to_html(wr_answer.find('content').text)
                    except:
                        pass

                    wr_object.save()
                    question.questiontype = 'WR'
                    question.save()

                answer_at_start = False
                x = re.search(r"\\\[(.*?)\\\]", question_from_xml.text)

                if x is None:
                    # =========================  FIB not confirmed =======================
                    # TODO: FIB ERROR
                    return

                # =========================  FIB confirmed=======================

                if x.start() == 0:
                    answer_at_start = True
                
                list_of_answers = re.findall(r"\\\[(.*?)\\\]", question_from_xml.text)
                replaced_answers = re.sub(r"\\\[(.*?)\\\]", "_______", question_from_xml.text)

                list_of_text = replaced_answers.split("_______")
                if answer_at_start:
                    list_of_text.pop(0)

                # TODO: populate FIB models below

                order = 1
                while len(list_of_text) + len(list_of_answers) > 0:

                    if answer_at_start:
                        try:
                            # fib_list.append(list_of_answers.pop(0))
                            answer_found = list_of_answers.pop(0)
                            fib_object = Fib.objects.create(question=question)
                            fib_object.order = order
                            fib_object.text = answer_found
                            fib_object.type = "fibanswer"
                            fib_object.size = None
                            fib_object.weight = None
                            order += 1
                            fib_object.save()
                        except:
                            pass
                    
                        try:
                            # fib_list.append(list_of_text.pop(0))
                            text_found = list_of_text.pop(0)
                            fib_object = Fib.objects.create(question=question)
                            fib_object.order = order
                            fib_object.text = text_found
                            fib_object.type = "fibquestion"
                            fib_object.size = None
                            fib_object.weight = None
                            order += 1
                            fib_object.save()
                        except:
                            pass
                    else:
                        try:
                            # fib_list.append(list_of_answers.pop(0))
                            answer_found = list_of_answers.pop(0)
                            fib_object = Fib.objects.create(question=question)
                            fib_object.order = order
                            fib_object.text = answer_found
                            fib_object.type = "fibanswer"
                            fib_object.size = None
                            fib_object.weight = None
                            order += 1
                            fib_object.save()
                        except:
                            pass

                        try:
                            # fib_list.append(list_of_text.pop(0))
                            text_found = list_of_text.pop(0)
                            fib_object = Fib.objects.create(question=question)
                            fib_object.order = order
                            fib_object.text = text_found
                            fib_object.type = "fibquestion"
                            fib_object.size = None
                            fib_object.weight = None
                            order += 1
                            fib_object.save()
                        except:
                            pass

                question.questiontype = 'FIB'
                question.save()

def trim_text(txt):
    text = txt.strip()
    text = re.sub('<!-- -->', '', text)
    text = re.sub('<!-- NewLine -->', '\n', text)
    text = text.strip("\n")
    return text

def markdown_to_plain(text):
    plain_text = pypandoc.convert_text(text, format="markdown_github+fancy_lists+emoji", to="plain", extra_args=['--wrap=none'])
    return plain_text

def markdown_to_html(text):
    html_text = pypandoc.convert_text(text, format="markdown_github+fancy_lists+emoji+task_lists+hard_line_breaks+all_symbols_escapable+tex_math_dollars", to="html", extra_args=['--mathjax', '--ascii'])
    # html_text = pypandoc.convert_text(text, format="markdown_github+fancy_lists+emoji+task_lists+hard_line_breaks+all_symbols_escapable+tex_math_dollars", to="html", extra_args=['--mathjax', '--ascii'])
    # soup_text = BeautifulSoup(html_text, "html.parser")
    # soup_text_math = soup_text.find_all("span", {"class": "math"})
            
    # if len(soup_text_math) > 0:
    #     for span_math in soup_text_math:
    #         # print(span_math)
    #         # math_text = re.sub(r"\\(?=[^a-zA-Z\(\)\d\s:])", "", span_math.string)
    #         mathml_text = pypandoc.convert_text(span_math, format="markdown_github+fancy_lists+emoji+task_lists+hard_line_breaks+all_symbols_escapable+tex_math_single_backslash", to="html", extra_args=['--mathml', '--ascii']).removeprefix('<p>').removesuffix('</p>')
    #         # print("\n", mathml_text)
    #         soup_math = BeautifulSoup(mathml_text, "html.parser")
    #         span_math.string = ''
    #         span_math.append(soup_math)
    return str(html_text)

def trim_md_to_plain(text):
    text_content = trim_text(text)
    text_content = markdown_to_plain(text_content)
    return text_content

def trim_md_to_html(text):
    text_content = trim_text(text)
    text_content = markdown_to_html(text_content)
    text_content = text_content.strip('\n')
    return text_content
