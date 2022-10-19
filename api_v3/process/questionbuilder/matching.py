from ...models import Matching, MatchingChoice, MatchingAnswer
from ..process_helper import trim_text, markdown_to_html
import re
from celery.utils.log import get_task_logger

loggercelery = get_task_logger(__name__)

def build_inline_MAT(question, answers):
    mat_object = Matching.objects.create(question=question)
    mat_object.save()
        
    for answer in answers:
        answercontent = trim_text(answer.find('content').text)
        regpattern = r"(\\`(.+)\\`\s*=\s*\\`(.+)\\`)|((.+)==(.+))|((.+)=(.+))"
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
                loggercelery.error("MATNoMatchError -> No match in MAT answer")

            mat_choice_text = choice_answer_groups_regex.group(group_num[0]).strip()
            mat_choice_text = re.sub(r"^\\\`|\\\`$", '', mat_choice_text)
            mat_choice_text = markdown_to_html(mat_choice_text)

            mat_answer_text = choice_answer_groups_regex.group(group_num[1]).strip()
            mat_answer_text = re.sub(r"^\\\`|\\\`$", '', mat_answer_text)
            mat_answer_text = markdown_to_html(mat_answer_text)

            if mat_choice_text == "":
                error_message = "MissingMATChoiceError -> one or more matching choice is missing"
                if error_message not in question.error:
                    question.error = question.error + "\n" + error_message if question.error else error_message
                    question.save()
                    loggercelery.error(error_message)

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
                error_message = "MissingMATAnswerError -> one or more matching answer is missing"
                if error_message not in question.error:
                    question.error = question.error + "\n" + error_message if question.error else error_message
                    question.save()
                    loggercelery.error(error_message)
            else:

                mat_answer.answer_text = mat_answer_text

        else:
            mat_choice = MatchingChoice.objects.create(matching=mat_object)
            mat_answer = MatchingAnswer.objects.create(matching_choice=mat_choice)
            error_message = "MissingMATOptionError -> one or more matching choice/answer choices missing"
            if error_message not in question.error:
                question.error = question.error + "\n" + error_message if question.error else error_message
                question.save()
                loggercelery.error(error_message)

        mat_choice.save()
        mat_answer.save()

    mat_object.save()
    question.questiontype = 'MAT'
    question.save()
    
def build_endanswer_MAT(question, endanswer):
    mat_object = Matching.objects.create(question=question)
    mat_object.save()

    answer_list = list(map(str.strip, endanswer.answer.split(";")))

    for answer in answer_list:
        answercontent = trim_text(answer)
        regpattern = r"(\\`(.+)\\`\s*=\s*\\`(.+)\\`)|((.+)==(.+))|((.+)=(.+))"
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
                loggercelery.debug("No match in MAT answer")

            mat_choice_text = choice_answer_groups_regex.group(group_num[0]).strip()
            mat_choice_text = re.sub(r"^\\\`|\\\`$", '', mat_choice_text)
            mat_choice_text = markdown_to_html(mat_choice_text)

            mat_answer_text = choice_answer_groups_regex.group(group_num[1]).strip()
            mat_answer_text = re.sub(r"^\\\`|\\\`$", '', mat_answer_text)
            mat_answer_text = markdown_to_html(mat_answer_text)

            if mat_choice_text == "":
                error_message = "MissingMATChoiceError -> one or more matching choice is missing"
                if error_message not in question.error:
                    question.error = question.error + "\n" + error_message if question.error else error_message
                    question.save()
                    loggercelery.error(error_message)
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
                error_message = "MissingMATChoiceError -> one or more matching answer is missing"
                if error_message not in question.error:
                    question.error = question.error + "\n" + error_message if question.error else error_message
                    question.save()
                    loggercelery.error(error_message)
            else:

                mat_answer.answer_text = mat_answer_text

        else:
            mat_choice = MatchingChoice.objects.create(matching=mat_object)
            mat_answer = MatchingAnswer.objects.create(matching_choice=mat_choice)
            error_message = "MissingMATOptionError -> one or more matching choice/answer choices missing"
            if error_message not in question.error:
                question.error = question.error + "\n" + error_message if question.error else error_message
                question.save()
                loggercelery.error(error_message)

        mat_choice.save()
        mat_answer.save()

    mat_object.save()
    question.questiontype = 'MAT'
    question.save()
