from ...models import MultipleChoice, MultipleChoiceAnswer
from ..process_helper import trim_text, trim_md_to_plain, trim_md_to_html

def build_inline_MC(question, answers, is_random):
    mc_object = MultipleChoice.objects.create(question=question)
    mc_object.save()

    # grab all answers
    for answer_item in answers:
        mc_answerobject = MultipleChoiceAnswer.objects.create(multiple_choice=mc_object)
        mc_answerobject.index = trim_md_to_plain(trim_text(answer_item.find('index').text)).strip("*.) \n")
        mc_answerobject.answer = trim_md_to_html(answer_item.find('content').text)
        answer_feedback = answer_item.find('feedback')
        is_correct = answer_item.attrib['correct']
        
        if answer_feedback != None:
            mc_answerobject.answer_feedback = trim_md_to_html(answer_feedback.text)

        if is_correct == 'true':
            mc_answerobject.weight = 100

        mc_answerobject.save()

    if is_random == True:
        mc_object.randomize = True

    question.questiontype = 'MC'
    mc_object.save()
    question.save()


def build_endanswer_MC(question, answers, endanswer, is_random):
    mc_object = MultipleChoice.objects.create(question=question)
    mc_object.save()

    endanswer_text = trim_md_to_plain(endanswer.answer)
    endanswer_text = trim_text(endanswer_text).lower()

    # grab all answers
    for idx, answer_item in enumerate(answers):
        mc_answerobject = MultipleChoiceAnswer.objects.create(multiple_choice=mc_object)
        mc_answerobject.index = trim_md_to_plain(trim_text(answer_item.find('index').text)).strip("*.) \n")
        mc_answerobject.answer = trim_md_to_html(answer_item.find('content').text)
        answer_feedback = answer_item.find('feedback')
        is_correct = answer_item.attrib['correct']

        if answer_feedback != None:
            mc_answerobject.answer_feedback = trim_md_to_html(answer_feedback.text)

        if idx == (ord(endanswer_text)-97):
            mc_answerobject.weight = 100
        
        if is_correct == 'true':
            mc_answerobject.error = "Correct answer in the question is ignored because of existing Answer Key."

        mc_answerobject.save()

    if is_random == True:
        mc_object.randomize = True

    question.questiontype = 'MC'
    mc_object.save()
    question.save()
