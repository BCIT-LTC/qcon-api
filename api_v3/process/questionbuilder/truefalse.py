from ...models import TrueFalse
from ..process_helper import trim_text, trim_md_to_html, markdown_to_plain
from celery.utils.log import get_task_logger

loggercelery = get_task_logger(__name__)

def build_inline_TF(question, answers):
    tf_object = TrueFalse.objects.create(question=question)
    correctanswer_count = 0

    for answer in answers:
        answer_text = answer.find('content').text.lower()
        answer_feedback = answer.find('feedback')
        is_correct = answer.attrib['correct']

        if "true" in answer_text:
            if answer_feedback != None:
                tf_object.true_feedback = trim_md_to_html(answer_feedback.text)

            if is_correct == 'true':
                tf_object.true_weight = 100
                correctanswer_count += 1
        
        if "false" in answer_text:
            if answer_feedback != None:
                tf_object.false_feedback = trim_md_to_html(answer_feedback.text)
            
            if is_correct == 'true':
                tf_object.false_weight = 100
                correctanswer_count += 1

        if correctanswer_count == 0:
            error_message = "TFNoAnswerError -> No answer selected in True/False question"
            if error_message not in question.error:
                question.error = question.error + "\n" + error_message if question.error else error_message
                question.save()
        elif correctanswer_count > 1:
            error_message = "TFSelectedAnswerError -> More than one answer selected in True/False question"
            if error_message not in question.error:
                question.error = question.error + "\n" + error_message if question.error else error_message
                question.save()
        
        tf_object.save()
        question.questiontype = 'TF'
        question.save()


def build_endanswer_TF(question, answers, endanswer):
    tf_object = TrueFalse.objects.create(question=question)
    correctanswer_count = 0

    endanswer_text = markdown_to_plain(endanswer.answer)
    endanswer_text = trim_text(endanswer_text).lower()

    for idx, answer in enumerate(answers):
        answer_text = answer.find('content').text.lower()
        parsedanswer_index = ord(endanswer_text)-97
        answer_feedback = answer.find('feedback')

        if "true" in answer_text:
            if answer_feedback != None:
                tf_object.true_feedback = trim_md_to_html(answer_feedback.text)

            if idx == parsedanswer_index:
                tf_object.true_weight = 100
                correctanswer_count += 1

        if "false" in answer_text:
            if answer_feedback != None:
                tf_object.false_feedback = trim_md_to_html(answer_feedback.text)

            if idx == parsedanswer_index:
                tf_object.false_weight = 100
                correctanswer_count += 1


        if correctanswer_count == 0:
            error_message = "TFNoAnswerError -> No answer selected in True/False question"
            if error_message not in question.error:
                question.error = question.error + "\n" + error_message if question.error else error_message
                loggercelery.error(error_message)

        elif correctanswer_count > 1:
            error_message = "TFSelectedAnswerError -> More than one answer selected in True/False question"
            if error_message not in question.error:
                question.error = question.error + "\n" + error_message if question.error else error_message
                loggercelery.error(error_message)

        tf_object.save()
        question.questiontype = 'TF'
        question.save()
