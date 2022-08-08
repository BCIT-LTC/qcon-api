from ...models import Ordering
from ..process_helper import trim_md_to_html

def build_ordering(question, answers):

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