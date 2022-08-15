from ...models import MultipleSelect, MultipleSelectAnswer
from ..process_helper import trim_text, trim_md_to_html, trim_md_to_plain

def build_inline_MS(question, answers, is_random):
    ms_object = MultipleSelect.objects.create(question=question)
    ms_object.save()

    # grab all answers
    for answer_item in answers:
        ms_answerobject = MultipleSelectAnswer.objects.create(multiple_select=ms_object)
        ms_answerobject.answer = trim_md_to_html(answer_item.find('content').text)
        ms_answerobject.index = trim_md_to_plain(answer_item.find('index').text).strip("*.) \n")
        answer_feedback = answer_item.find('feedback')
        is_correct = answer_item.attrib['correct']

        if answer_feedback != None:
            ms_answerobject.answer_feedback = trim_md_to_html(answer_feedback.text)
        
        if is_correct == 'true':
            ms_answerobject.is_correct = True
        if is_correct == 'false':
            ms_answerobject.is_correct = False

        ms_answerobject.save()

    if is_random == True:
        ms_object.randomize = True

    question.questiontype = 'MS'
    ms_object.save()
    question.save()


def build_endanswer_MS(question, answers, endanswer, is_random):
    ms_object = MultipleSelect.objects.create(question=question)
    ms_object.save()

    endanswer_text = trim_md_to_plain(endanswer.answer)
    endanswer_text = trim_text(endanswer_text).lower()
    answer_list = list(map(str.strip, endanswer_text.split(',')))

    # grab all answers
    for idx, answer_item in enumerate(answers):
        ms_answerobject = MultipleSelectAnswer.objects.create(multiple_select=ms_object)
        ms_answerobject.answer = trim_md_to_html(answer_item.find('content').text)
        ms_answerobject.index = trim_md_to_plain(answer_item.find('index').text).strip("*.) \n")
        answer_feedback = answer_item.find('feedback')
        is_correct = answer_item.attrib['correct']

        if answer_feedback != None:
            ms_answerobject.answer_feedback = trim_md_to_html(answer_feedback.text)
        
        for endanswer_option in answer_list:
            if idx == (ord(endanswer_option)-97):
                ms_answerobject.is_correct = True

        if is_correct == 'true':
            ms_answerobject.error = "Correct answer in the question is ignored because of existing Answer Key."
        
        ms_answerobject.save()

    if is_random == True:
        ms_object.randomize = True

    question.questiontype = 'MS'
    ms_object.save()
    question.save()
