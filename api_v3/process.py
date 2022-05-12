import os
from xml.dom.minidom import TypeInfo
import xml.etree.ElementTree as ET
import logging
import subprocess
import sys
import re

logger = logging.getLogger(__name__)

from .models import Section, Question, MultipleChoice, MultipleChoiceAnswer, MultipleSelect, MultipleSelectAnswer


def create_main_title():
    pass

class FormatterError(Exception):
    pass

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
            questionlibrary.end_answers = root[1].text
            questionlibrary.save()
        else:
            # logger.warning("Answer Section not found")
            pass
    except:
        # logger.warning("Answer section not found")
        pass

    return True

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
        pass

    

    for section in root:

        sectionobject = Section.objects.create(
            question_library=questionlibrary)

        sectionobject.save()

        sectionobject.order = section.attrib.get("id")

        sectiontitle = section.find('title')
        if sectiontitle is not None:
            sectionobject.title = sectiontitle.text

        maincontent = section.find('maincontent')
        if maincontent is not None:
            sectionobject.raw_content = maincontent.text
            sectionobject.is_main_content = True

        sectioncontent = section.find('sectioncontent')
        if sectioncontent is not None:
            sectionobject.raw_content = sectioncontent.text
            sectionobject.is_main_content = False

        sectionobject.save()



def run_splitter(questionlibrary):

    sections = Section.objects.filter(question_library=questionlibrary)

    for section in sections:
        split_questions(section)

    pass


def split_questions(sectionobject):

    os.chdir('/splitter/jarfile')
    result = subprocess.run(
        'java -cp splitter.jar:* splitter',
        shell=True,
        input=sectionobject.raw_content.encode("utf-8"),
        capture_output=True)
    os.chdir('/code')

    # print(result.stdout.decode("utf-8"))

    root = None
    try:
        root = ET.fromstring(result.stdout.decode("utf-8"))
    except:
        pass

    for question in root:

        questionobject = Question.objects.create(
            section=sectionobject)

        questionobject.save()

        # questiontype = question.find('type')
        # if questiontype is not None:
        #     questionobject.questiontype = questiontype.text.strip()

        # title = question.find('title')
        # if title is not None:
        #     questionobject.title = title.text.strip()  

        # randomize = question.find('randomize')
        # if questiontype is not None:
        #     questionobject.title = randomize.text    

        # points = question.find('points')
        # if points is not None:
        #     filterpoint = re.search("\d+((.|,)\d+)?", points.text)
        #     questionobject.points = float(filterpoint.group()) 

        content = question.find('content')
        if content is not None:
            questionobject.raw_content = content.text

        # question_start = question.find('question_start')
        # if question_start is not None:
        #     filter_question_number = re.search("\d+", question_start.text)
        #     questionobject.number_provided = filter_question_number.group()

        questionobject.save()
    pass



# This function will most likely writes directly to model. Might need to move to model instead
def run_parser(questionlibrary):

    sections = Section.objects.filter(question_library=questionlibrary)

    for section in sections:
        questions = Question.objects.filter(section=section)

        for question in questions:
            # discard empty question
            if question.raw_content is None:
                question.delete()
            else:
                parse_question(question)
    pass

def parse_question(question):

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
    
    '''

    root = None
    try:
        root = ET.fromstring(result.stdout.decode("utf-8"))
    except:
        pass

    if question.questiontype == 'MS':
        # MS is required 
        # COUNT total number of answers and correct_answer. it should be >= 2
        # answer = root.find('answer')
        
        pass
    else:
    # all other types try autodetect and compare if the given type is correct. if not then notify user 

       # Autodetect 
        print("detecting question")
        # look for FIB question
        fib_question = root.find('fib_question')
        if fib_question is not None:
            print("fib question found")
            # TODO CREATE FIB INSTANCE

        # look for regular question
        regular_question = root.find('question')
        if regular_question is not None:
            question.text = regular_question.text
            question.save()

            answer = root.findall('answer')
            correct_answer = root.findall('correct_answer')
            
            # Check if answers are included
            if (len(answer) + len(correct_answer)) > 0:
                # Only one correct answer provided?
                if len(correct_answer) == 1:                    
                    # 2 options provided?
                    if len(answer) == 1:
                        # TODO: UPDATE GRAMMAR TO CATCH TRUE AND FALSE TOKENS
                        # Are the options each true and false?

                        true_unmarked_answer_element = answer[0].find('true_answer')
                        false_unmarked_answer_element = answer[0].find('false_answer')
                        true_marked_answer_element = correct_answer[0].find('true_answer')
                        false_marked_answer_element = correct_answer[0].find('false_answer')
                        total_unmarked_TF = len(true_unmarked_answer_element) + len(false_unmarked_answer_element)
                        total_marked_TF = len(true_marked_answer_element) + len(false_marked_answer_element)

                        if total_unmarked_TF == 1:
                            if total_marked_TF == 1:
                                pass         
                                # =========================  TF confirmed =======================

                    if len(answer) > 1:
                        # =========================  MC confirmed =======================
                        
                        mc_object = MultipleChoice.objects.create(question=question)
                        mc_object.save()
                        # grab all answers

                        for answer_item in answer:
                            mc_answerobject = MultipleChoiceAnswer.objects.create(multiple_choice=mc_object)
                            mc_answerobject.answer = answer_item.text
                            mc_answerobject.weight = 0
                            mc_answerobject.save()

                        # grab the correct answer
                        for correct_answer_item in correct_answer:
                            mc_correct_answerobject = MultipleChoiceAnswer.objects.create(multiple_choice=mc_object)
                            mc_correct_answerobject.answer = correct_answer_item.text
                            mc_correct_answerobject.weight = 100
                            mc_correct_answerobject.save()

                        # TODO: Check if the user given type is similar to detected type:

                        question.questiontype = 'MC'
                        mc_object.save()
                        question.save()

                elif len(correct_answer) > 1:
                        # =========================  MS confirmed =======================
                        ms_object = MultipleSelect.objects.create(question=question)
                        ms_object.save()
                        # grab all answers

                        for answer_item in answer:
                            ms_answerobject = MultipleSelectAnswer.objects.create(multiple_select=ms_object)
                            ms_answerobject.answer = answer_item.text
                            ms_answerobject.is_correct = False
                            ms_answerobject.save()

                        # grab the correct answer
                        for correct_answer_item in correct_answer:
                            ms_correct_answerobject = MultipleSelectAnswer.objects.create(multiple_choice=ms_object)
                            ms_correct_answerobject.answer = correct_answer_item.text
                            ms_answerobject.is_correct = True
                            ms_correct_answerobject.save()
                        
                        ms_object.save()
            else:
                # answer list not included
                # This is most likely an essay type question. check if "correct_answer" token is present
                pass

    '''





    pass

def process(questionlibrary):

    # ======================
    run_formatter(questionlibrary)
    run_sectioner(questionlibrary)
    run_splitter(questionlibrary)

    pass