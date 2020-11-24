# Generated from Qcon.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .QconParser import QconParser
else:
    from QconParser import QconParser
import re
import pypandoc
from api_v1.models import Question, Answer
from datetime import datetime


# This class defines a complete listener for a parse tree produced by QconParser.
class QconListener(ParseTreeListener):
    def __init__(self, question_library):
        self.questions = []
        self.question = None
        self.temp_answers = []
        self.answer = None
        self.question_library = question_library

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
        pass


    # Enter a parse tree produced by QconParser#question.
    def enterQuestion(self, ctx:QconParser.QuestionContext):
        # print("enterQuestion===>")
        print(datetime.now().strftime("%H:%M:%S"), "Processing question", len(self.questions)+1)
        self.question = Question()
        self.question.question_library = self.question_library
        self.question.save()

        pass

    # Exit a parse tree produced by QconParser#question.
    def exitQuestion(self, ctx:QconParser.QuestionContext):
        # print("exitQuestion===>")

        # TODO INSERT LOGIC HEREEEEEEEEEEEEE

        # self.question.answers = self.temp_answers
        self.question.save()
        self.process_question(self.question)
        self.question.save()
        self.questions.append(self.question)
        pass


    # Enter a parse tree produced by QconParser#questionbody.
    def enterQuestionbody(self, ctx:QconParser.QuestionbodyContext):
        # print("enterQuestionbody===>")
        pass

    # Exit a parse tree produced by QconParser#questionbody.
    def exitQuestionbody(self, ctx:QconParser.QuestionbodyContext):
        question_body = self.trim_text(ctx.content().getText())
        question_body = self.markdown_to_html(question_body)
        self.question.question_body = question_body

        if ctx.questiontype() != None:
            questionType = self.trim_text(ctx.questiontype().getText()).split(":")[1]
            questionType = self.markdown_to_html(questionType)
            self.question.question_type = questionType
        
        if ctx.title() != None:
            title = self.trim_text(ctx.title().getText()).split(":")[1]
            title = self.markdown_to_plain_text(title)
            self.question.title = title

        if ctx.point() != None:
            points = self.trim_text(ctx.point().getText()).split(":")[1]
            points = self.markdown_to_plain_text(points)
            self.question.points = points

        if ctx.feedback() != None:
            question_feedback = self.trim_text(ctx.feedback().getText())[1:]
            question_feedback = self.markdown_to_html(question_feedback)
            self.question.question_feedback = question_feedback
        # print("exitQuestionbody===>")
        pass


    # Enter a parse tree produced by QconParser#answerlist.
    def enterAnswerlist(self, ctx:QconParser.AnswerlistContext):
        # print("enterAnswerlist===>")
        self.temp_answers = []
        pass

    # Exit a parse tree produced by QconParser#answerlist.
    def exitAnswerlist(self, ctx:QconParser.AnswerlistContext):
        # print("exitAnswerlist===>")
        pass


    # Enter a parse tree produced by QconParser#answeritem.
    def enterAnsweritem(self, ctx:QconParser.AnsweritemContext):
        # print("enterAnsweritem===>")
        self.answer = Answer()
        # self.question.answer_index += 1
        pass

    # Exit a parse tree produced by QconParser#answeritem.
    def exitAnsweritem(self, ctx:QconParser.AnsweritemContext):
        # print("exitAnsweritem===>")
        self.answer.question = self.question
        self.answer.save()
        self.temp_answers.append(self.answer)
        pass


    # Enter a parse tree produced by QconParser#listitem.
    def enterListitem(self, ctx:QconParser.ListitemContext):
        # print("enterListitem===>")
        pass

    # Exit a parse tree produced by QconParser#listitem.
    def exitListitem(self, ctx:QconParser.ListitemContext):
        # print("exitListitem===>")
        answer_body = self.trim_text(ctx.content().getText())
        answer_body = self.markdown_to_html(answer_body)
        self.answer.answer_body = answer_body

        self.answer.is_correct = False
        if ctx.feedback() != None:
            answer_feedback = self.trim_text(ctx.feedback().getText())[1:]
            answer_feedback = self.markdown_to_html(answer_feedback)
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
        self.answer.answer_body = answer_body

        self.answer.is_correct = True
        self.question.correct_answers_length += 1
        if ctx.feedback() != None:
            answer_feedback = self.trim_text(ctx.feedback().getText())[1:]
            answer_feedback = self.markdown_to_html(answer_feedback)
            self.answer.answer_feedback = answer_feedback
        pass

    def process_question(self, question):
        if question.question_type != '':
            if question.question_type == 'MC':
                if self.is_multiple_choice(question) == True:
                    # BUILD MC
                    print("is_multiple_choice")
                    pass
                else:
                    # TODO PRINT WRONG QUESTION FORMAT
                    print("Wrong question Format: MC")
                    pass
            elif question.question_type == 'TF':
                if self.is_true_false(question) == True:
                    # BUILD TF
                    print("is_true_false")
                    pass
                else:
                    # TODO PRINT WRONG QUESTION FORMAT
                    print("Wrong question Format: TF")
                    pass
            elif question.question_type == 'MS':
                if self.is_multi_select(question) == True:
                    # BUILD MS
                    print("is_multi_select")   
                    pass
                else:
                    # TODO PRINT WRONG QUESTION FORMAT
                    print("Wrong question Format: MS")
                    print("NOT MC/TF/MS")
                    pass
            else:
                    # TODO PRINT WRONG QUESTION FORMAT
                    print(question.question_type)
                    print("NOT MC/TF/MS")
                    pass
        else:
            is_TF = self.is_true_false(question)
            is_MC = self.is_multiple_choice(question)
            is_MS = self.is_multi_select(question)

            if is_TF == True:
                question.question_type = "TF"
            elif is_MC == True:
                question.question_type = "MC"
            elif is_MS == True:
                question.question_type = "MS"

            print(datetime.now().strftime("%H:%M:%S"), question.question_type)


    def is_multiple_choice(self, question):
        if question.correct_answers_length == 1:
            return True
        else:
            return False
    
    def is_true_false(self, question):
        if question.correct_answers_length == 1:
            if len(question.get_answers()) == 2:
                is_true_exist = False
                is_false_exist = False

                for answer in question.get_answers():
                    if "true" in answer.answer_body.lower():
                        is_true_exist = True
                    elif "false" in answer.answer_body.lower():
                        is_false_exist = True
                
                if is_true_exist == True:
                    if is_false_exist == True:
                        for answer in question.get_answers():
                            if "true" in answer.answer_body.lower():
                                answer.answer_body = "True"
                            elif "false" in answer.answer_body.lower():
                                answer.answer_body = "False"
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def is_multi_select(self, question):
        if len(question.get_answers()) >= 1:
            return True
        else:
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

del QconParser