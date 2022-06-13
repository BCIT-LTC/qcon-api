import os
from xml.dom.minidom import TypeInfo
import xml.etree.ElementTree as ET
import logging
import subprocess
import sys
import re

logger = logging.getLogger(__name__)

from .models import Section, Question, MultipleChoice, MultipleChoiceAnswer, MultipleSelect, \
MultipleSelectAnswer, Ordering, TrueFalse, Matching, MatchingAnswer, MatchingChoice, Image, EndAnswer


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

    questions_count = 0
    for section in sections:
        questions_count += split_questions(section)

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

    for question in root:

        questionobject = Question.objects.create(
            section=sectionobject)

        questionobject.save()

        content = question.find('content')
        if content is not None:
            questionobject.raw_content = content.text

        questionobject.save()
    
    return len(root)

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

    sections = Section.objects.filter(question_library=questionlibrary)

    for section in sections:
        questions = Question.objects.filter(section=section)

        section.questions_expected = len(questions) - 1
        import time
        start = time.time()
        count = 0
        for question in questions:
            # discard empty question
            if question.raw_content is None:
                question.delete()
            else:
                parse_question(question)
            print("question : " + str(count))
            count += 1
        end = time.time()
        section.processing_time = end - start
        section.save()
        print(end - start)
    

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

    root = None
    try:
        root = ET.fromstring(result.stdout.decode("utf-8"))
    except:
        pass


    questiontype = root.find('type')
    if questiontype is not None:
        question.questiontype = questiontype.text.strip()

    title = root.find('title')
    if title is not None:
        question.title = title.text.strip()  

    points = root.find('points')
    if points is not None:
        filterpoint = re.search("\d+((.|,)\d+)?", points.text)
        question.points = float(filterpoint.group()) 

    question_number = root.find('question_number')
    if question_number is not None:
        filter_question_number = re.search("\d+", question_number.text)
        question.number_provided = filter_question_number.group()


    if question.questiontype == 'MS':
        # TODO MS is required 
        # COUNT total number of answers and correct_answer. it should be >= 2
        # answer = root.find('answer')
        
        pass
    else:
    # all other types try autodetect and compare if the given type is correct. if not then notify user 

       # Autodetect 
        # look for FIB question
        fib_question = root.find('fib_question')
        if fib_question is not None:
            print("fib question found")
            # TODO CREATE FIB INSTANCE

        # look for other NON FIB question
        regular_question = root.find('question')
        if regular_question is not None:
            question.text = regular_question.text
            question.save()

            answers = root.findall("answer")            
            marked_answers_count = 0
            unmarked_answers_count = 0
            matching_answers_count = 0
            for answer in answers:
                if answer.attrib['correct'] == 'true':
                    marked_answers_count+=1
                if answer.attrib['correct'] == 'false':
                    unmarked_answers_count+=1

                matchanswers = re.search(r"(.*)=(.*)", answer.find('content').text)

                if matchanswers is not None:
                    matching_answers_count += 1        

            # Check if answers are included
            if len(answers) > 0:

                if matching_answers_count > 0 :
                    # =========================  MAT confirmed =======================
                    
                    mat_object = Matching.objects.create(question=question)        

                    for answer in answers:
                        answercontent  = answer.find('content').text
                        choice_answer_groups_regex = re.search(r"(.*)=(.*)", answercontent)

                        mat_choice = MatchingChoice.objects.create(matching=mat_object)                        
                        mat_answer = MatchingAnswer.objects.create(matching_choice=mat_choice)

                        if choice_answer_groups_regex is not None:
                           
                            mat_choice.choice_text = choice_answer_groups_regex.group(1)
                            mat_answer.answer_text = choice_answer_groups_regex.group(2)

                            if mat_choice.choice_text.strip() == "":
                                mat_choice.error = "matching choice missing"
                                mat_object.error = "one or more matching or answer choices missing"
                            if mat_answer.answer_text.strip() == "":
                                mat_answer.error = "matching answer missing"
                                mat_object.error = "one or more matching or answer choices missing"

                        else:
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
                            if answer.find('content').text.strip().lower() == 'true' :
                                KeywordTrueFound = True
                                try:
                                    tf_object.true_feedback = answer.find('feedback').text.strip()
                                except:
                                    pass
                                if answer.attrib['correct'] == 'true':
                                    tf_object.true_weight = 100

                            if answer.find('content').text.strip().lower() == 'false' :
                                KeywordFalseFound = True
                                try:
                                    tf_object.false_feedback = answer.find('feedback').text.strip()
                                except:
                                    pass
                                if answer.attrib['correct'] == 'true':
                                    tf_object.false_weight = 100
                        
                        if KeywordTrueFound == True and KeywordFalseFound == True :
                        # =========================  TF confirmed =======================
                        # TF confirmed here so the TF object is saved to db
                            print("TF COnfirmed")
                            tf_object.error = ""
                            tf_object.save()
                            question.questiontype = 'TF'
                            question.save()
                        else:
                        # One or More Keywords "true" or "false" not found. fallback to MC 

                        # TODO CREATE MC type
                            pass

                    if unmarked_answers_count > 1:
                        # =========================  MC confirmed =======================
                        mc_object = MultipleChoice.objects.create(question=question)
                        mc_object.save()
                        # grab all answers

                        for answer_item in answers:
                            mc_answerobject = MultipleChoiceAnswer.objects.create(multiple_choice=mc_object)
                            mc_answerobject.answer = answer_item.find('content').text
                            mc_answerobject.index = (answer_item.find('index').text).strip()
                            if answer_item.attrib['correct'] == 'true':
                                mc_answerobject.weight = 100
                            if answer_item.attrib['correct'] == 'false':
                                mc_answerobject.weight = 0
                            mc_answerobject.save()

                        # TODO: Check if the user given type is similar to detected type:

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
                        ms_answerobject.answer = answer_item.find('content').text
                        ms_answerobject.index = (answer_item.find('index').text).strip()
                        if answer_item.attrib['correct'] == 'true':
                            ms_answerobject.is_correct = True
                        if answer_item.attrib['correct'] == 'false':
                            ms_answerobject.is_correct = False

                        ms_answerobject.save()
                    
                    question.questiontype = 'MS'
                    ms_object.save()
                    question.save()

                elif marked_answers_count == 0:
                    # =========================  ORD confirmed =======================

                    iterator = 0
                    for answer in answers:
                    #     print(answer.find('index').text.strip())
                        ord_object = Ordering.objects.create(question=question)
                        ord_object.order = iterator
                        iterator += 1
                        ord_object.text = answer.find('content').text.strip()
                        try:
                            ord_object.ord_feedback = answer.find('feedback').text.strip()
                        except:
                            pass
                        ord_object.save()
                    
                    question.questiontype = 'ORD'
                    question.save()
            else:
                # answer list not included
                # This is most likely an essay type question. check if "correct_answer" token is present
                pass

    pass

def process(questionlibrary):

    # ======================
    run_formatter(questionlibrary)
    run_sectioner(questionlibrary)
    run_splitter(questionlibrary)

    pass