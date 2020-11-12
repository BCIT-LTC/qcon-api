# Generated from Qcon.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .QconParser import QconParser
else:
    from QconParser import QconParser

# This class defines a complete listener for a parse tree produced by QconParser.
class QconListener(ParseTreeListener):

    # Enter a parse tree produced by QconParser#qcon.
    def enterQcon(self, ctx:QconParser.QconContext):
        pass

    # Exit a parse tree produced by QconParser#qcon.
    def exitQcon(self, ctx:QconParser.QconContext):
        pass


    # Enter a parse tree produced by QconParser#question.
    def enterQuestion(self, ctx:QconParser.QuestionContext):
        pass

    # Exit a parse tree produced by QconParser#question.
    def exitQuestion(self, ctx:QconParser.QuestionContext):
        pass


    # Enter a parse tree produced by QconParser#questionbody.
    def enterQuestionbody(self, ctx:QconParser.QuestionbodyContext):
        pass

    # Exit a parse tree produced by QconParser#questionbody.
    def exitQuestionbody(self, ctx:QconParser.QuestionbodyContext):
        pass


    # Enter a parse tree produced by QconParser#questiontype.
    def enterQuestiontype(self, ctx:QconParser.QuestiontypeContext):
        pass

    # Exit a parse tree produced by QconParser#questiontype.
    def exitQuestiontype(self, ctx:QconParser.QuestiontypeContext):
        pass


    # Enter a parse tree produced by QconParser#title.
    def enterTitle(self, ctx:QconParser.TitleContext):
        pass

    # Exit a parse tree produced by QconParser#title.
    def exitTitle(self, ctx:QconParser.TitleContext):
        pass


    # Enter a parse tree produced by QconParser#point.
    def enterPoint(self, ctx:QconParser.PointContext):
        pass

    # Exit a parse tree produced by QconParser#point.
    def exitPoint(self, ctx:QconParser.PointContext):
        pass


    # Enter a parse tree produced by QconParser#content.
    def enterContent(self, ctx:QconParser.ContentContext):
        pass

    # Exit a parse tree produced by QconParser#content.
    def exitContent(self, ctx:QconParser.ContentContext):
        pass


    # Enter a parse tree produced by QconParser#answerlist.
    def enterAnswerlist(self, ctx:QconParser.AnswerlistContext):
        pass

    # Exit a parse tree produced by QconParser#answerlist.
    def exitAnswerlist(self, ctx:QconParser.AnswerlistContext):
        pass


    # Enter a parse tree produced by QconParser#listitem.
    def enterListitem(self, ctx:QconParser.ListitemContext):
        pass

    # Exit a parse tree produced by QconParser#listitem.
    def exitListitem(self, ctx:QconParser.ListitemContext):
        pass


    # Enter a parse tree produced by QconParser#answeritem.
    def enterAnsweritem(self, ctx:QconParser.AnsweritemContext):
        pass

    # Exit a parse tree produced by QconParser#answeritem.
    def exitAnsweritem(self, ctx:QconParser.AnsweritemContext):
        print(ctx.answerprefix().getText())
        print(ctx.isEmpty())
        print(ctx.answerprefix().isEmpty())
        
        print("--------------------")
        pass


    # Enter a parse tree produced by QconParser#questionprefix.
    def enterQuestionprefix(self, ctx:QconParser.QuestionprefixContext):
        pass

    # Exit a parse tree produced by QconParser#questionprefix.
    def exitQuestionprefix(self, ctx:QconParser.QuestionprefixContext):
        pass


    # Enter a parse tree produced by QconParser#listprefix.
    def enterListprefix(self, ctx:QconParser.ListprefixContext):
        pass

    # Exit a parse tree produced by QconParser#listprefix.
    def exitListprefix(self, ctx:QconParser.ListprefixContext):
        print(ctx.LIST_PREFIX().getText())
        print("______________________")
        pass


    # Enter a parse tree produced by QconParser#answerprefix.
    def enterAnswerprefix(self, ctx:QconParser.AnswerprefixContext):
        pass

    # Exit a parse tree produced by QconParser#answerprefix.
    def exitAnswerprefix(self, ctx:QconParser.AnswerprefixContext):
        pass


    # Enter a parse tree produced by QconParser#feedback.
    def enterFeedback(self, ctx:QconParser.FeedbackContext):
        pass

    # Exit a parse tree produced by QconParser#feedback.
    def exitFeedback(self, ctx:QconParser.FeedbackContext):
        pass



del QconParser