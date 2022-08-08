from ...models import MultipleChoice, MultipleChoiceAnswer
from ..process_helper import trim_text, trim_md_to_plain, trim_md_to_html

def build_multiplechoice(question, answers, questionlibrary):

    mc_object = MultipleChoice.objects.create(question=question)
    mc_object.save()
    # grab all answers

    for answer_item in answers:
        mc_answerobject = MultipleChoiceAnswer.objects.create(multiple_choice=mc_object)
        mc_answerobject.index = trim_md_to_plain(trim_text(answer_item.find('index').text)).strip("*.) \n")
        mc_answerobject.answer = trim_md_to_html(answer_item.find('content').text)

        if(answer_item.find('feedback') is not None):
            mc_answerobject.answer_feedback = trim_md_to_html(answer_item.find('feedback').text)

        if answer_item.attrib['correct'] == 'true':
            mc_answerobject.weight = 100
        if answer_item.attrib['correct'] == 'false':
            mc_answerobject.weight = 0
        mc_answerobject.save()

    if questionlibrary.randomize_answer == True:
        mc_object.randomize = True

    question.questiontype = 'MC'
    mc_object.save()
    question.save()
    return