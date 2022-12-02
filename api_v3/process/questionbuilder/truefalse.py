from ...models import TrueFalse
from ..process_helper import add_error_message, trim_text, trim_md_to_html, markdown_to_plain
from api_v3.logging.ErrorTypes import TFNoAnswerError, TFSelectedAnswerError

def build_inline_TF(question, answers, enumeration):
    question.questiontype = 'TF'
    question.save()

    tf_object = TrueFalse.objects.create(question=question)
    if enumeration:
        tf_object.enumeration = enumeration
    
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

        tf_object.save()

    if correctanswer_count == 0:
        error_message = "No answer selected in True/False question."
        add_error_message(question, error_message)
        raise TFNoAnswerError(error_message)
            
    elif correctanswer_count > 1:
        error_message = "More than one answer selected in True/False question."
        add_error_message(question, error_message)
        raise TFSelectedAnswerError(error_message)

    


def build_endanswer_TF(question, answers, endanswer, enumeration):
    question.questiontype = 'TF'
    question.save()

    tf_object = TrueFalse.objects.create(question=question)
    if enumeration:
        tf_object.enumeration = enumeration
    
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

        tf_object.save()

    if correctanswer_count == 0:
        error_message = "No answer selected in True/False question."
        add_error_message(question, error_message)
        raise TFNoAnswerError(error_message)

    elif correctanswer_count > 1:
        error_message = "More than one answer selected in True/False question."
        add_error_message(question, error_message)
        raise TFSelectedAnswerError(error_message)
