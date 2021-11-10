# Generated from Qcon.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .QconParser import QconParser
else:
    from QconParser import QconParser
import re
import pypandoc
# from api_v2.models import Question, Answer, Fib
from datetime import datetime


# This class defines a complete listener for a parse tree produced by QconParser.
class QconListener(ParseTreeListener):
    def __init__(self, question_library):
        self.questions = []
        self.question = None
        self.answer = None
        self.question_library = question_library
        self.end_answers = None

    # TODO Add logic to populate and check the fields (e.g: questionType)
    def get_results(self):
        return self.questions

    # Enter a parse tree produced by QconParser#qcon.
    def enterQcon(self, ctx:QconParser.QconContext):
        # print("enterQcon===>")
        pass

    # Exit a parse tree produced by QconParser#qcon.
    def exitQcon(self, ctx:QconParser.QconContext):  
        # print("exitQcon===>")
        print('')
        if self.end_answers == None:
            for question_index, question in enumerate(self.questions):
                self.process_question(question)
                self.question.save()
                print(datetime.now().strftime("%H:%M:%S"), "Question", question_index+1, ":", question.question_type)
        else:
            for question_index, question in enumerate(self.questions):
                end_answer = self.end_answers[question_index]['answer']
                if question.question_type == 'FIB':
                    fib_answers = question.get_fib_answers()
                    if ';' in end_answer:
                        # Multi FIB
                        end_answers_split = end_answer.split(";")
                        for answer_index, answer_text in enumerate(end_answers_split):
                            fib_answer = fib_answers[answer_index]
                            fib_answer.type = "answer"
                            fib_answer.text = answer_text
                            fib_answer.save()
                    else:
                        # only one FIB
                        fib_answer = question.get_fib_answers()[0]
                        fib_answer.type = "answer"
                        fib_answer.text = end_answer
                        fib_answer.save()

                else:
                    answers = question.get_answers()

                    if len(answers) > 0:
                        if len(answers) == 2:
                            is_true_exist = False
                            is_false_exist = False
                            for answer_obj in answers:
                                answer_body = self.html_to_plain(answer_obj.answer_body).lower().strip()
                                if "true" == answer_body:
                                    is_true_exist = True
                                elif "false" == answer_body:
                                    is_false_exist = True
                            
                            if is_true_exist == True:
                                if is_false_exist == True:
                                    # TF
                                    question.question_type = 'TF'
                                    question.correct_answers_length = 1
                                    question.save()
                                    for answer_obj in answers:
                                        answer_body = self.html_to_plain(answer_obj.answer_body).lower().strip()
                                        if "true" == answer_body:
                                            answer_obj.answer_body = "True"
                                        elif "false" == answer_body:
                                            answer_obj.answer_body = "False"
                                        
                                        if end_answer[0] == answer_obj.prefix[0]:
                                            answer_obj.is_correct = True
                                        answer_obj.save()

                        if question.question_type == None:
                            if ';' in end_answer:
                                end_answers_split = end_answer.split(";")
                                if len(answers) == len(end_answers_split):
                                    count_ordering = 0
                                    
                                    for answer_obj in answers:
                                        answer_obj_text = self.html_to_plain(answer_obj.answer_body).lower().strip()
                                        for end_answer in end_answers_split:
                                            end_answer_text = end_answer.lower().strip()
                                            if end_answer_text == answer_obj_text:
                                                count_ordering = count_ordering + 1
                                    
                                    if count_ordering == len(end_answers_split):
                                        # ORD
                                        question.question_type = 'ORD'
                                        question.save()
                                        for ordering_index, answer in enumerate(answers):
                                            answer.answer_body = end_answers_split[ordering_index]
                                            answer.save()
                            elif ',' in end_answer:
                                end_answers_split = end_answer.split(",")
                                count_ms = 0
                                for answer_obj in answers:
                                    answer_obj_prefix = answer_obj.prefix[0].lower()
                                    for answer_text in end_answers_split:
                                        end_answer_text = answer_text.lower().strip()
                                        if end_answer_text == answer_obj_prefix:
                                            count_ms = count_ms + 1

                                if count_ms == len(end_answers_split):
                                    # MS
                                    question.question_type = 'MS'
                                    question.correct_answers_length = count_ms
                                    question.save()
                                    for answer_obj in answers:
                                        answer_obj_prefix = answer_obj.prefix[0].lower()
                                        for answer_text in end_answers_split:
                                            end_answer_text = answer_text.lower().strip()
                                            if end_answer_text == answer_obj_prefix:
                                                answer_obj.is_correct = True
                                                answer_obj.save()
                            else:
                                for answer_obj in answers:
                                    answer_obj_prefix = answer_obj.prefix[0].lower()
                                    end_answer_text = end_answer.lower().strip()
                                    if end_answer_text == answer_obj_prefix:
                                        # MC
                                        question.question_type = 'MC'
                                        question.correct_answers_length = 1
                                        question.save()
                                        answer_obj.is_correct = True
                                        answer_obj.save()

                    elif len(answers) == 0:
                        # either ordering or written response
                        is_wr = False
                        if ';' in end_answer:
                            end_answers_split = end_answer.split(";")
                            
                            count_matching = 0
                            for answer_text in end_answers_split:
                                if '=' in answer_text:
                                    count_matching = count_matching + 1

                            if count_matching == len(end_answers_split):
                                # MT
                                question.question_type = 'MT'
                                question.save()
                                for answer_text in end_answers_split:
                                    from api_v2.models import Answer
                                    new_answer = Answer()
                                    matching_answer = new_answer
                                    matching_answer.question = question
                                    matching_answer.answer_body = answer_text
                                    matching_answer.save()
                            else:
                                is_wr = True
                        else:
                            is_wr = True

                        if is_wr == True:
                            # WR
                            question.question_type = 'WR'
                            question.save()
                            from api_v2.models import Answer
                            new_answer = Answer()
                            wr_answer = new_answer
                            wr_answer.question = question
                            wr_answer.answer_body = end_answer
                            wr_answer.save()
                                
                    self.process_question(question)
                    self.question.save()
                    print(datetime.now().strftime("%H:%M:%S"), "Question", question_index+1, ":", question.question_type)
        print('')
                    

    # Enter a parse tree produced by QconParser#question.
    def enterQuestion(self, ctx:QconParser.QuestionContext):
        # print("enterQuestion===>")
        from api_v2.models import Question
        print("aslkdfhjlkds")
        new_question = Question()
        self.question = new_question
        self.question.question_library = self.question_library
        self.question.save()

        pass

    # Exit a parse tree produced by QconParser#question.
    def exitQuestion(self, ctx:QconParser.QuestionContext):
        # print("exitQuestion===>")
        self.question.save()
        self.questions.append(self.question)
        pass


    # Enter a parse tree produced by QconParser#questionbody.
    def enterQuestionbody(self, ctx:QconParser.QuestionbodyContext):
        # print("enterQuestionbody===>")
        pass

    # Exit a parse tree produced by QconParser#questionbody.
    def exitQuestionbody(self, ctx:QconParser.QuestionbodyContext):
        # print("exitQuestionbody===>")
        question_body = self.trim_text(ctx.content().getText())
        question_body = self.markdown_to_html(question_body)
        self.question.question_body = question_body

        if ctx.questiontype() != None:
            question_type = self.trim_text(ctx.questiontype().getText()).split(":")[1]
            question_type = self.markdown_to_plain_text(question_type)
            question_type = self.trim_text(question_type)
            self.question.question_type = question_type

        if ctx.title() != None:
            title = self.trim_text(ctx.title().getText()).split(":")[1]
            title = self.markdown_to_plain_text(title)
            title = self.trim_text(title)
            self.question.title = title

        if ctx.point() != None:
            points = self.trim_text(ctx.point().getText()).split(":")[1]
            points = self.markdown_to_plain_text(points)
            points = self.trim_text(points)
            self.question.points = points

        if ctx.feedback() != None:
            question_feedback = self.trim_text(ctx.feedback().getText())[1:]
            question_feedback = self.markdown_to_html(question_feedback)
            question_feedback = self.trim_text(question_feedback)
            self.question.question_feedback = question_feedback
        
        pass

        # Enter a parse tree produced by QconParser#fibquestionbody.
    def enterFibquestionbody(self, ctx:QconParser.FibquestionbodyContext):
        pass

    # Exit a parse tree produced by QconParser#fibquestionbody.
    def exitFibquestionbody(self, ctx:QconParser.FibquestionbodyContext):
        question_body = ''
        for context in ctx.fibcontent():
            blank = re.search(r"\\?\[(.*?)\\?\]", context.getText())
            if blank != None:
                from api_v2.models import Fib
                new_fib = Fib()
                fib = new_fib
                fib.question = self.question
                fib.type = "answer"
                fib.text = blank.group(1)
                fib.save()
                question_body = question_body + "_______ "
            else:
                from api_v2.models import Fib
                new_fib = Fib()
                fib = new_fib
                fib.question = self.question
                fib.type = "question"
                fib.text = context.getText()
                fib.save()
                question_body = question_body + context.getText() + " "

        question_body = self.trim_text(question_body)
        self.question.question_body = question_body
        self.question.question_type = 'FIB'
        
        if ctx.title() != None:
            title = self.trim_text(ctx.title().getText()).split(":")[1]
            title = self.markdown_to_plain_text(title)
            title = self.trim_text(title)
            self.question.title = title
        
        if ctx.point() != None:
            points = self.trim_text(ctx.point().getText()).split(":")[1]
            points = self.markdown_to_plain_text(points)
            points = self.trim_text(points)
            self.question.points = points
        
        if ctx.feedback() != None:
            question_feedback = self.trim_text(ctx.feedback().getText())[1:]
            question_feedback = self.markdown_to_html(question_feedback)
            question_feedback = self.trim_text(question_feedback)
            self.question.question_feedback = question_feedback
        
        pass
    
    # Enter a parse tree produced by QconParser#answerlist.
    def enterAnswerlist(self, ctx:QconParser.AnswerlistContext):
        # print("enterAnswerlist===>")
        pass

    # Exit a parse tree produced by QconParser#answerlist.
    def exitAnswerlist(self, ctx:QconParser.AnswerlistContext):
        # print("exitAnswerlist===>")
        pass


    # Enter a parse tree produced by QconParser#answeritem.
    def enterAnsweritem(self, ctx:QconParser.AnsweritemContext):
        # print("enterAnsweritem===>")
        from api_v2.models import Answer
        new_answer = Answer()
        self.answer = new_answer
        pass

    # Exit a parse tree produced by QconParser#answeritem.
    def exitAnsweritem(self, ctx:QconParser.AnsweritemContext):
        # print("exitAnsweritem===>")
        self.answer.question = self.question
        self.answer.save()
        pass


    # Enter a parse tree produced by QconParser#listitem.
    def enterListitem(self, ctx:QconParser.ListitemContext):
        # print("enterListitem===>")
        pass

    # Exit a parse tree produced by QconParser#listitem.
    def exitListitem(self, ctx:QconParser.ListitemContext):
        # print("exitListitem===>")
        prefix = ctx.listprefix().getText() or ctx.answerprefix().getText()
        prefix = self.trim_text(prefix)
        self.answer.prefix = prefix

        answer_body = self.trim_text(ctx.content().getText())
        answer_body = self.markdown_to_html(answer_body)
        answer_body = self.trim_text(answer_body)
        self.answer.answer_body = answer_body

        self.answer.is_correct = False
        if ctx.feedback() != None:
            answer_feedback = self.trim_text(ctx.feedback().getText())[1:]
            answer_feedback = self.markdown_to_html(answer_feedback)
            answer_feedback = self.trim_text(answer_feedback)
            self.answer.answer_feedback = answer_feedback
        pass

    # Enter a parse tree produced by QconParser#listansweritem.
    def enterListansweritem(self, ctx:QconParser.ListansweritemContext):
        # print("enterListansweritem===>")
        pass

    # Exit a parse tree produced by QconParser#listansweritem.
    def exitListansweritem(self, ctx:QconParser.ListansweritemContext):
        # print("exitListansweritem===>")
        answer_body = self.trim_text(ctx.content().getText())
        answer_body = self.markdown_to_html(answer_body)
        answer_body = self.trim_text(answer_body)
        self.answer.answer_body = answer_body

        self.answer.is_correct = True
        self.question.correct_answers_length += 1
        if ctx.feedback() != None:
            answer_feedback = self.trim_text(ctx.feedback().getText())[1:]
            answer_feedback = self.markdown_to_html(answer_feedback)
            answer_feedback = self.trim_text(answer_feedback)
            self.answer.answer_feedback = answer_feedback
        pass

    # Enter a parse tree produced by QconParser#endanswerstart.
    def enterEndanswers(self, ctx:QconParser.EndanswerstartContext):
        # print("enterEndanswerstart===>")
        pass

    # Exit a parse tree produced by QconParser#endanswerstart.
    def exitEndanswers(self, ctx:QconParser.EndanswerstartContext):
        # print("exitEndanswerstart===>")
        if len(self.questions) == len(ctx.endanswerlistitem()) :
            self.end_answers = []
            for idx, endanswerlistitem_context in enumerate(ctx.endanswerlistitem()):
                answer = {}
                answer['answer'] = self.trim_text(endanswerlistitem_context.content().getText())
                answer['feedback'] = None
                
                try:
                  answer['feedback'] = endanswerlistitem_context.feedback().content().getText()
                except:
                    # NO FEEDBACK
                    pass

                self.end_answers.append(answer)


    def process_question(self, question):
        if question.question_type != None:
            if question.question_type == 'MC':
                if self.is_multiple_choice(question) == True:
                    # BUILD MC
                    pass
                else:
                    # TODO PRINT WRONG QUESTION FORMAT
                    print("Wrong question Format: MC")
                    pass
            elif question.question_type == 'TF':
                if self.is_true_false(question) == True:
                    # BUILD TF
                    pass
                else:
                    # TODO PRINT WRONG QUESTION FORMAT
                    print("Wrong question Format: TF")
                    pass
            elif question.question_type == 'MS' or question.question_type == 'MR':
                if self.is_multi_select(question) == True:
                    # BUILD MS
                    pass
                elif self.is_ordering(question) == True:
                    print("is_multi_select with no answer")
                    pass
                else:
                    # TODO PRINT WRONG QUESTION FORMAT
                    print("Wrong question Format: MS")
                    pass
            elif question.question_type == 'MT':
                if self.is_matching(question) == True:
                    # BUILD MT
                    pass
                else:
                    print("Wrong question Format: MT")
                    pass
            elif question.question_type == 'ORD':
                if self.is_ordering(question) == True:
                    # BUILD ORD
                    pass
                else:
                    print("Wrong question Format: ORD")
                    pass
            elif question.question_type == 'FIB' or question.question_type == 'FMB':
                # if self.is_fill_in_the_blanks(question) == True:
                # BUILD FIB
                pass
            elif question.question_type == 'WR' or question.question_type == 'E':
                # TRUST USER & BUILD WR
                pass
            else:
                    # TODO LOG WRONG QUESTION FORMAT
                    print("UNKNOWN QUESTION FORMAT")
                    pass
        else:
            is_TF = self.is_true_false(question)
            is_MC = self.is_multiple_choice(question)
            is_MS = self.is_multi_select(question)
            is_MT = self.is_matching(question)
            is_ORD = self.is_ordering(question)
            is_WR = self.is_written_response(question)
            # is_FIB = self.is_fill_in_the_blanks(question)

            if is_TF == True:
                question.question_type = "TF"
            elif is_MC == True:
                question.question_type = "MC"
            elif is_MT == True:
                question.question_type = "MT"
            elif is_MS == True:
                question.question_type = "MS"
            elif is_ORD == True:
                question.question_type = "ORD"
            elif is_WR == True:
                question.question_type = "WR"
            # elif is_FIB == True:
            #     question.question_type = "FIB"

            # print(datetime.now().strftime("%H:%M:%S"), question.question_type)


    def is_multiple_choice(self, question):
        if question.correct_answers_length == 1:
            return True

        return False
    
    def is_true_false(self, question):
        if question.correct_answers_length == 1:
            if len(question.get_answers()) == 2:
                is_true_exist = False
                is_false_exist = False

                for answer in question.get_answers():
                    text_answer = self.html_to_plain(answer.answer_body.lower()).strip()
                    if "true" == text_answer:
                        is_true_exist = True
                    elif "false" == text_answer:
                        is_false_exist = True
                
                if is_true_exist == True:
                    if is_false_exist == True:
                        for answer in question.get_answers():
                            current_answer = self.html_to_plain(answer.answer_body.lower()).strip()
                            if "true" == current_answer:
                                answer.answer_body = "True"
                            elif "false" == current_answer:
                                answer.answer_body = "False"
                            answer.save()
                        return True
        return False

    def is_multi_select(self, question):
        if len(question.get_answers()) > 1:
            return True

        return False

    def is_matching(self, question):
        count_equal_sign = 0
        if len(question.get_answers()) >= 1:
            for answer in question.get_answers():
                if "=" in answer.answer_body:
                    count_equal_sign = count_equal_sign + 1
            
            if(len(question.get_answers()) == count_equal_sign):
                for answer in question.get_answers():
                    split_answer = answer.answer_body.split('=')
                    if len(split_answer) > 2:
                        return False
                    answer.match_left = split_answer[0] + '</p>'
                    answer.match_right = '<p>' + split_answer[1]
                    answer.save()
                return True
        return False

    def is_ordering(self, question):
        if len(question.get_answers()) > 1:
            if question.correct_answers_length == 0:
                return True

        return False
    

    def is_written_response(self, question):
        if len(question.get_answers()) == 1:
            if question.correct_answers_length == 0:
                return True
        return False

    def trim_text(self, txt):
        text = txt.strip()
        text = re.sub(' +', ' ', text)
        return text
    
    def markdown_to_html(self, text):
        html_text = pypandoc.convert_text(text, format="markdown_github+fancy_lists+emoji+task_lists+hard_line_breaks", to="html", extra_args=["--mathml", '--ascii'])
        return html_text

    def markdown_to_plain_text(self, text):
        plain_text = pypandoc.convert_text(text, format="markdown_github+fancy_lists+emoji", to="plain").replace('\n', ' ')
        return plain_text

    def html_to_plain(self, text):
        html_text = pypandoc.convert_text(text, format='html', to="plain")
        return html_text

del QconParser