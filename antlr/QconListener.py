# Generated from Qcon.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .QconParser import QconParser
else:
    from QconParser import QconParser
import re


class Question(object):
    def __init__(self):
        self.question_type = None
        self.question_number = None 
        self.title = None
        self.questionbody = None
        self.feedback = None
        self.hint = None
        self.randomizeAnswers = None
        self.points = None
        self.image = []
        self.answers = [] #ctx.getChildCount()
        self.answer_index = 0
        self.countCorrectAnswers = 0
        self.preview = ''
        self.messages = {}

        # =============
        # self.answerindex = 0

    def printquestion(self):
        # print ( 
        # "=================" +
        # "\nquestion_type: " + str(self.question_type) + 
        # "\nquestion_number: " + str(self.question_number) + 
        # "\ntitle: " + str(self.title) + 
        # "\nquestionbody: " + str(self.questionbody)  +
        # "\nfeedback: " + str(self.feedback) + 
        # "\nhint: " + str(self.hint) + 
        # "\nrandomizeAnswers: " + str(self.randomizeAnswers) +
        # "\npoints: " + str(self.points) +
        # "\n=================")
        pass

    def pushAnswer(self, answer):

        self.answers.append(answer)

        return None

class Answer(object):
    def __init__(self): # answer_index, answer_body, feedback, isCorrect, matchLeft, matchRight, order
        self.answer_body = None
        self.feedback = None
        self.isCorrect = None
        self.matchLeft = None
        self.matchRight = None
        self.order = None

        return None

    def showtitle():
        return None

    def findType():
        return None
    
    
# This class defines a complete listener for a parse tree produced by QconParser.
class QconListener(ParseTreeListener):
    def __init__(self):
        self.questions = []
        self.question = None
        self.temp_answers = []
        self.answer = None
        self.testvariable = "empty"
        # self.isready = False

    # TODO Add logic to populate and check the fields (e.g: questionType)
    def getresults(self):
        # if self.isready == True:
        #     print(len(self.questions[0]))
        # else:
        #     print("NOT REEADY")
        print("##########################################################################################")
        return self.questions

    # Enter a parse tree produced by QconParser#qcon.
    def enterQcon(self, ctx:QconParser.QconContext):

        # print(self.testvariable)
        # self.testvariable = "I chjanged this"
        # self.questions.append(self.testvariable)
        pass

    # Exit a parse tree produced by QconParser#qcon.
    def exitQcon(self, ctx:QconParser.QconContext):  
        # print(self.questions[0].title)
        # print("exitQcon===>")
        # print(len(self.temp_answers))
        # self.isready = True
        pass


    # Enter a parse tree produced by QconParser#question.
    def enterQuestion(self, ctx:QconParser.QuestionContext):
        # print("enterQuestion===>")
        self.question = Question()
        pass

    # Exit a parse tree produced by QconParser#question.
    def exitQuestion(self, ctx:QconParser.QuestionContext):
        # print("exitQuestion===>")
        # self.question.printquestion()
        # TODO INSERT LOGIC HEREEEEEEEEEEEEE

        self.question.answers = self.temp_answers
        self.processQuestion(self.question)
        self.questions.append(self.question)
        pass


    # Enter a parse tree produced by QconParser#questionbody.
    def enterQuestionbody(self, ctx:QconParser.QuestionbodyContext):
        # print("enterQuestionbody===>")
        pass

    # Exit a parse tree produced by QconParser#questionbody.
    def exitQuestionbody(self, ctx:QconParser.QuestionbodyContext):
        self.question.questionbody = ctx.content().getText()

        if ctx.questiontype() != None:
            self.question.question_type = self.trimText(ctx.questiontype().getText())
        
        if ctx.title() != None:
            self.question.title = self.trimText(ctx.title().getText())

        if ctx.point() != None:
            self.question.points = self.trimText(ctx.point().getText())

        if ctx.feedback() != None:
            self.question.feedback = self.trimText(ctx.feedback().getText())
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
        self.question.answer_index += 1
        pass

    # Exit a parse tree produced by QconParser#answeritem.
    def exitAnsweritem(self, ctx:QconParser.AnsweritemContext):
        # print("exitAnsweritem===>")
        self.temp_answers.append(self.answer)   
        pass


    # Enter a parse tree produced by QconParser#listitem.
    def enterListitem(self, ctx:QconParser.ListitemContext):
        # print("enterListitem===>")
        pass

    # Exit a parse tree produced by QconParser#listitem.
    def exitListitem(self, ctx:QconParser.ListitemContext):
        # print("exitListitem===>")
        self.answer.answer_body = ctx.content().getText()
        self.answer.isCorrect = False
        if ctx.feedback() != None:
            self.answer.feedback = ctx.feedback().getText()
        pass

    # Enter a parse tree produced by QconParser#listansweritem.
    def enterListansweritem(self, ctx:QconParser.ListansweritemContext):
        # print("enterListansweritem===>")
        pass

    # Exit a parse tree produced by QconParser#listansweritem.
    def exitListansweritem(self, ctx:QconParser.ListansweritemContext):
        self.answer.answer_body = ctx.content().getText()
        self.answer.isCorrect = True
        self.question.countCorrectAnswers += 1
        if ctx.feedback() != None:
            self.answer.feedback = ctx.feedback().getText()
        # print("exitListansweritem===>")
        pass

    def processQuestion(self, question):
        if question.question_type != None:
            if question.question_type == 'MC':
                if self.isMultipleChoice(question) == True:
                    # BUILD MC
                    print("isMultipleChoice")
                    pass
                else:
                    # TODO PRINT WRONG QUESTION FORMAT
                    print("Wrong question Format: MC")
                    pass
            elif question.question_type == 'TF':
                if self.isTrueFalse(question) == True:
                    # BUILD TF
                    print("isTrueFalse")
                    pass
                else:
                    # TODO PRINT WRONG QUESTION FORMAT
                    print("Wrong question Format: TF")
                    pass
            elif question.question_type == 'MS':
                if self.isMultiSelect(question) == True:
                    # BUILD MS
                    print("isMultiSelect")   
                    pass
                else:
                    # TODO PRINT WRONG QUESTION FORMAT
                    print("Wrong question Format: MS")
                    print("NOT MC/TF/MS")
                    pass
            else:
                    # TODO PRINT WRONG QUESTION FORMAT
                    print("NOT MC/TF/MS")
                    pass
        else:
            print("NO QUESTION TYPE")


    def isMultipleChoice(self, question):
        if question.countCorrectAnswers == 1:
            return True
        else:
            return False
    
    def isTrueFalse(self, question):
        if question.countCorrectAnswers == 1:
            print("question.countCorrectAnswers == 1")
            print(len(question.answers))
            if len(question.answers) == 2:
                print("len(question.answers) == 2")
                isTrueExist = False
                isFalseExist = False

                for answer in question.answers:
                    if "true" in answer.answer_body.lower():
                        isTrueExist = True
                    elif "false" in answer.answer_body.lower():
                        isFalseExist = True
                
                if isTrueExist == True:
                    if isFalseExist == True:
                        for answer in question.answers:
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

    def isMultiSelect(self, question):
        if len(question.answers) >= 1:
            return True
        else:
            return False
    
    def trimText(self, txt):
        text = txt.split(":")[1]
        text = text.strip()
        text = re.sub(' +', ' ', text)
        return text
    

del QconParser