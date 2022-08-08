from ...models import WrittenResponse
from ..process_helper import trim_md_to_html

def build_writtenresponse_from_answer(question, answers):
    wr_object = WrittenResponse.objects.create(question=question)
    for answer in answers:
        try:
            wr_object.answer_key = trim_md_to_html(answer.find('content').text)
        except:
            pass

    wr_object.save()
    question.questiontype = 'WR'
    question.save()

def build_writtenresponse_from_keyword(question, wr_answer):
    wr_object = WrittenResponse.objects.create(question=question)
    try:
        wr_object.answer_key = trim_md_to_html(wr_answer.find('content').text)
    except:
        pass

    wr_object.save()
    question.questiontype = 'WR'
    question.save()