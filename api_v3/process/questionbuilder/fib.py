from ...models import Fib
import re 

def build_fib(question, question_from_xml):
    
    x = re.search(r"\\\[(.*?)\\\]", question_from_xml.text)

    if x is None:
        # =========================  FIB not confirmed =======================
        # TODO: FIB ERROR
        return

    # =========================  FIB confirmed=======================

    answer_at_start = False
    if x.start() == 0:
        answer_at_start = True
    list_of_answers = re.findall(r"\[(.*?)\]", question.text)
    replaced_answers = re.sub(r"\[(.*?)\]", "_______", question.text)
    fib_title = re.sub(r"\\\[(.*?)\\\]", "_______", question_from_xml.text)
    fib_title = re.sub('<!-- NewLine -->', '', fib_title)
    fib_title = re.sub(r"<<<<\d+>>>>", "[IMG]", fib_title)
    question.title = fib_title
    list_of_text = replaced_answers.split("_______")
    if answer_at_start:
        list_of_text.pop(0)

    order = 1
    while len(list_of_text) + len(list_of_answers) > 0:

        if answer_at_start:
            try:
                # fib_list.append(list_of_answers.pop(0))
                answer_found = list_of_answers.pop(0)
                fib_object = Fib.objects.create(question=question)
                fib_object.order = order
                fib_object.text = answer_found
                fib_object.type = "fibanswer"
                fib_object.size = None
                fib_object.weight = None
                order += 1
                fib_object.save()
            except:
                pass
        
            try:
                # fib_list.append(list_of_text.pop(0))
                text_found = list_of_text.pop(0)
                fib_object = Fib.objects.create(question=question)
                fib_object.order = order
                fib_object.text = text_found
                fib_object.type = "fibquestion"
                fib_object.size = None
                fib_object.weight = None
                order += 1
                fib_object.save()
            except:
                pass
        else:
            try:
                # fib_list.append(list_of_text.pop(0))
                text_found = list_of_text.pop(0)
                fib_object = Fib.objects.create(question=question)
                fib_object.order = order
                fib_object.text = text_found
                fib_object.type = "fibquestion"
                fib_object.size = None
                fib_object.weight = None
                order += 1
                fib_object.save()
            except:
                pass

            try:
                # fib_list.append(list_of_answers.pop(0))
                answer_found = list_of_answers.pop(0)
                fib_object = Fib.objects.create(question=question)
                fib_object.order = order
                fib_object.text = answer_found
                fib_object.type = "fibanswer"
                fib_object.size = None
                fib_object.weight = None
                order += 1
                fib_object.save()
            except:
                pass

    question.questiontype = 'FIB'
    question.save()
