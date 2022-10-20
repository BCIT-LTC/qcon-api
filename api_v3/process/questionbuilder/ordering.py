from ...models import Ordering
from ..process_helper import trim_md_to_html

def build_inline_ORD(question, answers):
    iterator = 1

    for answer in answers:
        ord_object = Ordering.objects.create(question=question)
        ord_object.order = iterator
        iterator += 1
        # ord_object.text = trim_md_to_html(answer.find('content').text)
        ord_object.text = answer.find('content').text
        answer_feedback = answer.find('feedback')

        if answer_feedback != None:
            # ord_object.ord_feedback = trim_md_to_html(answer_feedback.text)
            ord_object.ord_feedback = answer_feedback.text

        ord_object.save()

    question.questiontype = 'ORD'
    question.save()


def build_endanswer_ORD(question, endanswer):
    iterator = 1
    answer_list = list(map(str.strip, endanswer.answer.split(";")))

    for answer in answer_list:
        ord_object = Ordering.objects.create(question=question)
        ord_object.order = iterator
        iterator += 1
        # ord_object.text = trim_md_to_html(answer)
        ord_object.text = answer

        ord_object.save()
    
    question.questiontype = 'ORD'
    question.save()
