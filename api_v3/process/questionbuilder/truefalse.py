from ...models import TrueFalse
from ..process_helper import trim_text, trim_md_to_html, markdown_to_plain


def build_truefalse(question, answers):
    tf_object = TrueFalse.objects.create(question=question)

    KeywordTrueFound = False
    KeywordFalseFound = False

    for answer in answers:
        answer_text = markdown_to_plain(answer.find('content').text.lower())
        answer_text = trim_text(answer_text)
        if answer_text == 'true':
            KeywordTrueFound = True
            try:
                tf_object.true_feedback = trim_md_to_html(answer.find('feedback').text)
            except:
                pass
            if answer.attrib['correct'] == 'true':
                tf_object.true_weight = 100

        if answer_text == 'false':
            KeywordFalseFound = True
            try:
                tf_object.false_feedback = trim_md_to_html(answer.find('feedback').text)
            except:
                pass
            if answer.attrib['correct'] == 'true':
                tf_object.false_weight = 100

    if KeywordTrueFound == True and KeywordFalseFound == True:
    # =========================  TF confirmed =======================
    # TF confirmed here so the TF object is saved to db
        tf_object.error = ""
        tf_object.save()
        question.questiontype = 'TF'
        question.save()
        return True
    
    return False