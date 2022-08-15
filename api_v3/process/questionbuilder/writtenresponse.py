from ...models import WrittenResponse
from ..process_helper import trim_md_to_html

def build_inline_WR_with_keyword(question, wr_answer):
    wr_object = WrittenResponse.objects.create(question=question)
    answer_key = wr_answer.find('content')

    if answer_key != None:
        wr_object.answer_key = trim_md_to_html(answer_key.text)

    wr_object.save()
    question.questiontype = 'WR'
    question.save()


def build_inline_WR_with_list(question, answers):
    wr_object = WrittenResponse.objects.create(question=question)

    for answer in answers:
        answer_key = answer.find('content')

        if answer_key != None:
            wr_object.answer_key = trim_md_to_html(answer_key.text)

    wr_object.save()
    question.questiontype = 'WR'
    question.save()

def build_endanswer_WR_with_list(question, endanswer, wr_answer):
    wr_object = WrittenResponse.objects.create(question=question)

    wr_object.answer_key = trim_md_to_html(endanswer.answer)
    
    if wr_answer != None:
        wr_object.error = "Correct answer in the question is ignored because of existing Answer Key."
    
    wr_object.save()
    question.questiontype = 'WR'
    question.save()
