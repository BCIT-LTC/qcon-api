from ...models import WrittenResponse
from ..process_helper import trim_md_to_html
from celery.utils.log import get_task_logger

loggercelery = get_task_logger(__name__)

def build_inline_WR_with_keyword(question, wr_answer):
    wr_object = WrittenResponse.objects.create(question=question)
    answer_key = wr_answer.find('content')

    if answer_key != None:
        # wr_object.answer_key = trim_md_to_html(answer_key.text)
        wr_object.answer_key = answer_key.text

    wr_object.save()
    question.questiontype = 'WR'
    question.save()


def build_inline_WR_with_list(question, answers):
    wr_object = WrittenResponse.objects.create(question=question)

    for answer in answers:
        answer_key = answer.find('content')

        if answer_key != None:
            # wr_object.answer_key = trim_md_to_html(answer_key.text)
            wr_object.answer_key = answer_key.text

    wr_object.save()
    question.questiontype = 'WR'
    question.save()

def build_endanswer_WR_with_list(question, endanswer, wr_answer):
    wr_object = WrittenResponse.objects.create(question=question)

    # wr_object.answer_key = trim_md_to_html(endanswer.answer)
    wr_object.answer_key = endanswer.answer
    
    if wr_answer != None:
        warning_message = "WREndAnswerExistWarning -> Correct answer in the question is ignored because of existing Answer Key."
        if warning_message not in question.warning:
            question.warning = question.warning + "\n" + warning_message if question.warning else warning_message
            question.save()
            loggercelery.warning(warning_message)
        
    wr_object.save()
    question.questiontype = 'WR'
    question.save()
