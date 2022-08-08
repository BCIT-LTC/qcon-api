import os
import subprocess
import re
import xml.etree.ElementTree as ET
from ..models import Section, Question, Matching, MatchingChoice, MatchingAnswer, TrueFalse
from ..models import MultipleChoice, MultipleChoiceAnswer, MultipleSelect, MultipleSelectAnswer
from ..models import Ordering, WrittenResponse, Fib
from .process_helper import trim_text, markdown_to_plain, trim_md_to_html, markdown_to_html, trim_md_to_plain

from .questionbuilder.matching import build_matching
from .questionbuilder.multiplechoice import build_multiplechoice
from .questionbuilder.truefalse import build_truefalse
from .questionbuilder.multipleselect import build_multipleselect
from .questionbuilder.ordering import build_ordering
from .questionbuilder.writtenresponse import build_writtenresponse_from_answer
from .questionbuilder.writtenresponse import build_writtenresponse_from_keyword
from .questionbuilder.fib import build_fib

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
                    build_matching(question,answers)
                    return

                if marked_answers_count == 1:
                    if unmarked_answers_count == 1:
                        # =========================  check TF =======================
                        # check if both false and true keyword are found
                        if build_truefalse(question, answers):
                            pass
                        else:
                        # One or More Keywords "true" or "false" not found. fallback to MC
                            # ========================= 2 option MC confirmed =======================
                            build_multiplechoice(question, answers, questionlibrary)
                            return
                    if unmarked_answers_count > 1:
                        # =========================  MC confirmed =======================
                        build_multiplechoice(question, answers, questionlibrary)
                        return

                elif marked_answers_count > 1:
                    # =========================  MS confirmed =======================
                    build_multipleselect(question, answers, questionlibrary)
                    return

                elif marked_answers_count == 0:
                    if unmarked_answers_count > 1:
                    # =========================  ORD confirmed =======================
                        build_ordering(question, answers)
                    elif unmarked_answers_count == 1:
                    # =========================  WR confirmed =======================
                        build_writtenresponse_from_answer(question, answers)
            elif len(answers) == 0:
                # answer list not included
                # This is most likely an essay type question or FIB. check if "correct_answer" token is present                
                wr_answer = root.find("wr_answer")   
                if wr_answer is not None:
                    # =========================  WR confirmed with correct answer keyword=======================
                    build_writtenresponse_from_keyword(question, wr_answer)
                    return
                
                # ========================= check fib =======================
                build_fib(question, question_from_xml)