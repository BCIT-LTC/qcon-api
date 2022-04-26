import os
import xml.etree.ElementTree as ET
import logging
import subprocess
import sys
import re

logger = logging.getLogger(__name__)

from .models import Section, Question


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
    # questionlibrary.sectioner_output = result.stdout.decode("utf-8")
    # questionlibrary.save()

    root = None
    try:
        root = ET.fromstring(result.stdout.decode("utf-8"))
    except:
        pass

    for question in root:

        questionobject = Question.objects.create(
            section=sectionobject)

        questionobject.save()

        questiontype = question.find('type')
        if questiontype is not None:
            questionobject.questiontype = questiontype.text.strip()

        title = question.find('title')
        if questiontype is not None:
            questionobject.title = title.text.strip()  

        # randomize = question.find('randomize')
        # if questiontype is not None:
        #     questionobject.title = randomize.text    

        points = question.find('points')
        filterpoint = re.search("\d+((.|,)\d+)?", points.text)
        if questiontype is not None:
            questionobject.points = float(filterpoint.group()) 


        content = question.find('content')
        if content is not None:
            questionobject.raw_content = content.text

        question_start = question.find('question_start')
        filter_question_number = re.search("\d+", question_start.text)
        if question_start is not None:
            questionobject.number_provided = filter_question_number.group()

        questionobject.save()
    pass



# This function will most likely writes directly to model. Might need to move to model instead
def run_parser(questionlibrary):

    sections = Section.objects.filter(question_library=questionlibrary)

    for section in sections:
        questions = Question.objects.filter(section=section)

        for question in questions:

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
    # questionlibrary.sectioner_output = result.stdout.decode("utf-8")
    # questionlibrary.save()

    # root = None
    # try:
    #     root = ET.fromstring(result.stdout.decode("utf-8"))
    # except:
    #     pass





    pass

def process(questionlibrary):

    # ======================
    run_formatter(questionlibrary)
    run_sectioner(questionlibrary)
    run_splitter(questionlibrary)

    pass