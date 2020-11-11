# Generated from Grammar.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#prog.
    def enterProg(self, ctx:GrammarParser.ProgContext):
        pass

    # Exit a parse tree produced by GrammarParser#prog.
    def exitProg(self, ctx:GrammarParser.ProgContext):
        pass


    # Enter a parse tree produced by GrammarParser#question.
    def enterQuestion(self, ctx:GrammarParser.QuestionContext):
        pass

    # Exit a parse tree produced by GrammarParser#question.
    def exitQuestion(self, ctx:GrammarParser.QuestionContext):
        pass


    # Enter a parse tree produced by GrammarParser#questionbody.
    def enterQuestionbody(self, ctx:GrammarParser.QuestionbodyContext):
        pass

    # Exit a parse tree produced by GrammarParser#questionbody.
    def exitQuestionbody(self, ctx:GrammarParser.QuestionbodyContext):
        pass


    # Enter a parse tree produced by GrammarParser#questiontype.
    def enterQuestiontype(self, ctx:GrammarParser.QuestiontypeContext):
        pass

    # Exit a parse tree produced by GrammarParser#questiontype.
    def exitQuestiontype(self, ctx:GrammarParser.QuestiontypeContext):
        pass


    # Enter a parse tree produced by GrammarParser#title.
    def enterTitle(self, ctx:GrammarParser.TitleContext):
        pass

    # Exit a parse tree produced by GrammarParser#title.
    def exitTitle(self, ctx:GrammarParser.TitleContext):
        pass


    # Enter a parse tree produced by GrammarParser#point.
    def enterPoint(self, ctx:GrammarParser.PointContext):
        pass

    # Exit a parse tree produced by GrammarParser#point.
    def exitPoint(self, ctx:GrammarParser.PointContext):
        pass


    # Enter a parse tree produced by GrammarParser#content.
    def enterContent(self, ctx:GrammarParser.ContentContext):
        pass

    # Exit a parse tree produced by GrammarParser#content.
    def exitContent(self, ctx:GrammarParser.ContentContext):
        pass


    # Enter a parse tree produced by GrammarParser#answerlist.
    def enterAnswerlist(self, ctx:GrammarParser.AnswerlistContext):
        pass

    # Exit a parse tree produced by GrammarParser#answerlist.
    def exitAnswerlist(self, ctx:GrammarParser.AnswerlistContext):
        pass


    # Enter a parse tree produced by GrammarParser#listitem.
    def enterListitem(self, ctx:GrammarParser.ListitemContext):
        pass

    # Exit a parse tree produced by GrammarParser#listitem.
    def exitListitem(self, ctx:GrammarParser.ListitemContext):
        pass


    # Enter a parse tree produced by GrammarParser#answeritem.
    def enterAnsweritem(self, ctx:GrammarParser.AnsweritemContext):
        pass

    # Exit a parse tree produced by GrammarParser#answeritem.
    def exitAnsweritem(self, ctx:GrammarParser.AnsweritemContext):
        pass


    # Enter a parse tree produced by GrammarParser#questionprefix.
    def enterQuestionprefix(self, ctx:GrammarParser.QuestionprefixContext):
        pass

    # Exit a parse tree produced by GrammarParser#questionprefix.
    def exitQuestionprefix(self, ctx:GrammarParser.QuestionprefixContext):
        pass


    # Enter a parse tree produced by GrammarParser#listprefix.
    def enterListprefix(self, ctx:GrammarParser.ListprefixContext):
        pass

    # Exit a parse tree produced by GrammarParser#listprefix.
    def exitListprefix(self, ctx:GrammarParser.ListprefixContext):
        pass


    # Enter a parse tree produced by GrammarParser#answerprefix.
    def enterAnswerprefix(self, ctx:GrammarParser.AnswerprefixContext):
        pass

    # Exit a parse tree produced by GrammarParser#answerprefix.
    def exitAnswerprefix(self, ctx:GrammarParser.AnswerprefixContext):
        pass


    # Enter a parse tree produced by GrammarParser#feedback.
    def enterFeedback(self, ctx:GrammarParser.FeedbackContext):
        pass

    # Exit a parse tree produced by GrammarParser#feedback.
    def exitFeedback(self, ctx:GrammarParser.FeedbackContext):
        pass



del GrammarParser