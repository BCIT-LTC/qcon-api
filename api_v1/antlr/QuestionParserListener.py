# Generated from QuestionParser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .QuestionParser import QuestionParser
else:
    from QuestionParser import QuestionParser

# This class defines a complete listener for a parse tree produced by QuestionParser.
class QuestionParserListener(ParseTreeListener):

    # Enter a parse tree produced by QuestionParser#parse_question.
    def enterParse_question(self, ctx:QuestionParser.Parse_questionContext):
        pass

    # Exit a parse tree produced by QuestionParser#parse_question.
    def exitParse_question(self, ctx:QuestionParser.Parse_questionContext):
        pass


    # Enter a parse tree produced by QuestionParser#QuestionWithAnswers.
    def enterQuestionWithAnswers(self, ctx:QuestionParser.QuestionWithAnswersContext):
        pass

    # Exit a parse tree produced by QuestionParser#QuestionWithAnswers.
    def exitQuestionWithAnswers(self, ctx:QuestionParser.QuestionWithAnswersContext):
        pass


    # Enter a parse tree produced by QuestionParser#QuestionWithoutAnswers.
    def enterQuestionWithoutAnswers(self, ctx:QuestionParser.QuestionWithoutAnswersContext):
        pass

    # Exit a parse tree produced by QuestionParser#QuestionWithoutAnswers.
    def exitQuestionWithoutAnswers(self, ctx:QuestionParser.QuestionWithoutAnswersContext):
        pass


    # Enter a parse tree produced by QuestionParser#question_body.
    def enterQuestion_body(self, ctx:QuestionParser.Question_bodyContext):
        pass

    # Exit a parse tree produced by QuestionParser#question_body.
    def exitQuestion_body(self, ctx:QuestionParser.Question_bodyContext):
        pass


    # Enter a parse tree produced by QuestionParser#question_header.
    def enterQuestion_header(self, ctx:QuestionParser.Question_headerContext):
        pass

    # Exit a parse tree produced by QuestionParser#question_header.
    def exitQuestion_header(self, ctx:QuestionParser.Question_headerContext):
        pass


    # Enter a parse tree produced by QuestionParser#TypeMc.
    def enterTypeMc(self, ctx:QuestionParser.TypeMcContext):
        pass

    # Exit a parse tree produced by QuestionParser#TypeMc.
    def exitTypeMc(self, ctx:QuestionParser.TypeMcContext):
        pass


    # Enter a parse tree produced by QuestionParser#TypeTf.
    def enterTypeTf(self, ctx:QuestionParser.TypeTfContext):
        pass

    # Exit a parse tree produced by QuestionParser#TypeTf.
    def exitTypeTf(self, ctx:QuestionParser.TypeTfContext):
        pass


    # Enter a parse tree produced by QuestionParser#TypeMs.
    def enterTypeMs(self, ctx:QuestionParser.TypeMsContext):
        pass

    # Exit a parse tree produced by QuestionParser#TypeMs.
    def exitTypeMs(self, ctx:QuestionParser.TypeMsContext):
        pass


    # Enter a parse tree produced by QuestionParser#TypeMt.
    def enterTypeMt(self, ctx:QuestionParser.TypeMtContext):
        pass

    # Exit a parse tree produced by QuestionParser#TypeMt.
    def exitTypeMt(self, ctx:QuestionParser.TypeMtContext):
        pass


    # Enter a parse tree produced by QuestionParser#TypeOrd.
    def enterTypeOrd(self, ctx:QuestionParser.TypeOrdContext):
        pass

    # Exit a parse tree produced by QuestionParser#TypeOrd.
    def exitTypeOrd(self, ctx:QuestionParser.TypeOrdContext):
        pass


    # Enter a parse tree produced by QuestionParser#TypeFib.
    def enterTypeFib(self, ctx:QuestionParser.TypeFibContext):
        pass

    # Exit a parse tree produced by QuestionParser#TypeFib.
    def exitTypeFib(self, ctx:QuestionParser.TypeFibContext):
        pass


    # Enter a parse tree produced by QuestionParser#TypeWr.
    def enterTypeWr(self, ctx:QuestionParser.TypeWrContext):
        pass

    # Exit a parse tree produced by QuestionParser#TypeWr.
    def exitTypeWr(self, ctx:QuestionParser.TypeWrContext):
        pass


    # Enter a parse tree produced by QuestionParser#TypeOther.
    def enterTypeOther(self, ctx:QuestionParser.TypeOtherContext):
        pass

    # Exit a parse tree produced by QuestionParser#TypeOther.
    def exitTypeOther(self, ctx:QuestionParser.TypeOtherContext):
        pass


    # Enter a parse tree produced by QuestionParser#title.
    def enterTitle(self, ctx:QuestionParser.TitleContext):
        pass

    # Exit a parse tree produced by QuestionParser#title.
    def exitTitle(self, ctx:QuestionParser.TitleContext):
        pass


    # Enter a parse tree produced by QuestionParser#points.
    def enterPoints(self, ctx:QuestionParser.PointsContext):
        pass

    # Exit a parse tree produced by QuestionParser#points.
    def exitPoints(self, ctx:QuestionParser.PointsContext):
        pass


    # Enter a parse tree produced by QuestionParser#RandomTrue.
    def enterRandomTrue(self, ctx:QuestionParser.RandomTrueContext):
        pass

    # Exit a parse tree produced by QuestionParser#RandomTrue.
    def exitRandomTrue(self, ctx:QuestionParser.RandomTrueContext):
        pass


    # Enter a parse tree produced by QuestionParser#RandomFalse.
    def enterRandomFalse(self, ctx:QuestionParser.RandomFalseContext):
        pass

    # Exit a parse tree produced by QuestionParser#RandomFalse.
    def exitRandomFalse(self, ctx:QuestionParser.RandomFalseContext):
        pass


    # Enter a parse tree produced by QuestionParser#Media.
    def enterMedia(self, ctx:QuestionParser.MediaContext):
        pass

    # Exit a parse tree produced by QuestionParser#Media.
    def exitMedia(self, ctx:QuestionParser.MediaContext):
        pass


    # Enter a parse tree produced by QuestionParser#Hyperlink.
    def enterHyperlink(self, ctx:QuestionParser.HyperlinkContext):
        pass

    # Exit a parse tree produced by QuestionParser#Hyperlink.
    def exitHyperlink(self, ctx:QuestionParser.HyperlinkContext):
        pass


    # Enter a parse tree produced by QuestionParser#FibAnswer.
    def enterFibAnswer(self, ctx:QuestionParser.FibAnswerContext):
        pass

    # Exit a parse tree produced by QuestionParser#FibAnswer.
    def exitFibAnswer(self, ctx:QuestionParser.FibAnswerContext):
        pass


    # Enter a parse tree produced by QuestionParser#ContentCharacters.
    def enterContentCharacters(self, ctx:QuestionParser.ContentCharactersContext):
        pass

    # Exit a parse tree produced by QuestionParser#ContentCharacters.
    def exitContentCharacters(self, ctx:QuestionParser.ContentCharactersContext):
        pass


    # Enter a parse tree produced by QuestionParser#ListNoAnswer.
    def enterListNoAnswer(self, ctx:QuestionParser.ListNoAnswerContext):
        pass

    # Exit a parse tree produced by QuestionParser#ListNoAnswer.
    def exitListNoAnswer(self, ctx:QuestionParser.ListNoAnswerContext):
        pass


    # Enter a parse tree produced by QuestionParser#ListWithAnswer.
    def enterListWithAnswer(self, ctx:QuestionParser.ListWithAnswerContext):
        pass

    # Exit a parse tree produced by QuestionParser#ListWithAnswer.
    def exitListWithAnswer(self, ctx:QuestionParser.ListWithAnswerContext):
        pass


    # Enter a parse tree produced by QuestionParser#list_item.
    def enterList_item(self, ctx:QuestionParser.List_itemContext):
        pass

    # Exit a parse tree produced by QuestionParser#list_item.
    def exitList_item(self, ctx:QuestionParser.List_itemContext):
        pass


    # Enter a parse tree produced by QuestionParser#list_answer_item.
    def enterList_answer_item(self, ctx:QuestionParser.List_answer_itemContext):
        pass

    # Exit a parse tree produced by QuestionParser#list_answer_item.
    def exitList_answer_item(self, ctx:QuestionParser.List_answer_itemContext):
        pass


    # Enter a parse tree produced by QuestionParser#question_prefix.
    def enterQuestion_prefix(self, ctx:QuestionParser.Question_prefixContext):
        pass

    # Exit a parse tree produced by QuestionParser#question_prefix.
    def exitQuestion_prefix(self, ctx:QuestionParser.Question_prefixContext):
        pass


    # Enter a parse tree produced by QuestionParser#list_prefix.
    def enterList_prefix(self, ctx:QuestionParser.List_prefixContext):
        pass

    # Exit a parse tree produced by QuestionParser#list_prefix.
    def exitList_prefix(self, ctx:QuestionParser.List_prefixContext):
        pass


    # Enter a parse tree produced by QuestionParser#answer_prefix.
    def enterAnswer_prefix(self, ctx:QuestionParser.Answer_prefixContext):
        pass

    # Exit a parse tree produced by QuestionParser#answer_prefix.
    def exitAnswer_prefix(self, ctx:QuestionParser.Answer_prefixContext):
        pass


    # Enter a parse tree produced by QuestionParser#feedback.
    def enterFeedback(self, ctx:QuestionParser.FeedbackContext):
        pass

    # Exit a parse tree produced by QuestionParser#feedback.
    def exitFeedback(self, ctx:QuestionParser.FeedbackContext):
        pass



del QuestionParser