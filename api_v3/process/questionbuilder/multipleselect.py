from ...models import MultipleSelect, MultipleSelectAnswer
from ..process_helper import trim_md_to_html, trim_md_to_plain

def build_multipleselect(question, answers, questionlibrary):

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