import os
import subprocess
import re
import xml.etree.ElementTree as ET
from ..models import Section, Question, Matching, MatchingChoice, MatchingAnswer, TrueFalse
from ..models import MultipleChoice, MultipleChoiceAnswer, MultipleSelect, MultipleSelectAnswer
from ..models import Ordering, WrittenResponse, Fib
from .process_helper import trim_text, markdown_to_plain, trim_md_to_html, markdown_to_html, trim_md_to_plain

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
                list_of_answers = re.findall(r"\[(.*?)\]", question.text)
                replaced_answers = re.sub(r"\[(.*?)\]", "_______", question.text)
                fib_title = re.sub(r"\\\[(.*?)\\\]", "_______", question_from_xml.text)
                fib_title = re.sub('<!-- NewLine -->', '', fib_title)
                fib_title = re.sub(r"<<<<\d+>>>>", "[IMG]", fib_title)
                question.title = fib_title
                list_of_text = replaced_answers.split("_______")
                if answer_at_start:
                    list_of_text.pop(0)

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


                question.questiontype = 'FIB'
                question.save()
