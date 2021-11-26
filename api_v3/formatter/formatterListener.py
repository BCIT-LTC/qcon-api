# Generated from formatter.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .formatterParser import formatterParser
else:
    from formatterParser import formatterParser

# This class defines a complete listener for a parse tree produced by formatterParser.
class formatterListener(ParseTreeListener):

    def __init__(self, question_library):
        # self.questions = []
        pass

    # Enter a parse tree produced by formatterParser#formatter.
    def enterFormatter(self, ctx:formatterParser.FormatterContext):
        print("ENTER Formatter")
        pass

    # Exit a parse tree produced by formatterParser#formatter.
    def exitFormatter(self, ctx:formatterParser.FormatterContext):
        pass


    # Enter a parse tree produced by formatterParser#rootheading.
    def enterRootheading(self, ctx:formatterParser.RootheadingContext):
        pass

    # Exit a parse tree produced by formatterParser#rootheading.
    def exitRootheading(self, ctx:formatterParser.RootheadingContext):
        pass


    # Enter a parse tree produced by formatterParser#rootbody.
    def enterRootbody(self, ctx:formatterParser.RootbodyContext):
        pass

    # Exit a parse tree produced by formatterParser#rootbody.
    def exitRootbody(self, ctx:formatterParser.RootbodyContext):
        print("ROOTBODY FOUND")
        pass


    # Enter a parse tree produced by formatterParser#section.
    def enterSection(self, ctx:formatterParser.SectionContext):
        pass

    # Exit a parse tree produced by formatterParser#section.
    def exitSection(self, ctx:formatterParser.SectionContext):
        pass


    # Enter a parse tree produced by formatterParser#sectionbody.
    def enterSectionbody(self, ctx:formatterParser.SectionbodyContext):
        pass

    # Exit a parse tree produced by formatterParser#sectionbody.
    def exitSectionbody(self, ctx:formatterParser.SectionbodyContext):
        pass


    # Enter a parse tree produced by formatterParser#rootlist.
    def enterRootlist(self, ctx:formatterParser.RootlistContext):
        pass

    # Exit a parse tree produced by formatterParser#rootlist.
    def exitRootlist(self, ctx:formatterParser.RootlistContext):
        pass


    # Enter a parse tree produced by formatterParser#numlist.
    def enterNumlist(self, ctx:formatterParser.NumlistContext):
        pass

    # Exit a parse tree produced by formatterParser#numlist.
    def exitNumlist(self, ctx:formatterParser.NumlistContext):
        pass


    # Enter a parse tree produced by formatterParser#letterlist.
    def enterLetterlist(self, ctx:formatterParser.LetterlistContext):
        pass

    # Exit a parse tree produced by formatterParser#letterlist.
    def exitLetterlist(self, ctx:formatterParser.LetterlistContext):
        pass


    # Enter a parse tree produced by formatterParser#question_header.
    def enterQuestion_header(self, ctx:formatterParser.Question_headerContext):
        pass

    # Exit a parse tree produced by formatterParser#question_header.
    def exitQuestion_header(self, ctx:formatterParser.Question_headerContext):
        pass


    # Enter a parse tree produced by formatterParser#letterlist_prefix_regular.
    def enterLetterlist_prefix_regular(self, ctx:formatterParser.Letterlist_prefix_regularContext):
        pass

    # Exit a parse tree produced by formatterParser#letterlist_prefix_regular.
    def exitLetterlist_prefix_regular(self, ctx:formatterParser.Letterlist_prefix_regularContext):
        pass


    # Enter a parse tree produced by formatterParser#letterlist_prefix_correct.
    def enterLetterlist_prefix_correct(self, ctx:formatterParser.Letterlist_prefix_correctContext):
        pass

    # Exit a parse tree produced by formatterParser#letterlist_prefix_correct.
    def exitLetterlist_prefix_correct(self, ctx:formatterParser.Letterlist_prefix_correctContext):
        pass


    # Enter a parse tree produced by formatterParser#question_header_parameter.
    def enterQuestion_header_parameter(self, ctx:formatterParser.Question_header_parameterContext):
        pass

    # Exit a parse tree produced by formatterParser#question_header_parameter.
    def exitQuestion_header_parameter(self, ctx:formatterParser.Question_header_parameterContext):
        pass


    # Enter a parse tree produced by formatterParser#end_answers_block.
    def enterEnd_answers_block(self, ctx:formatterParser.End_answers_blockContext):
        pass

    # Exit a parse tree produced by formatterParser#end_answers_block.
    def exitEnd_answers_block(self, ctx:formatterParser.End_answers_blockContext):
        pass


    # Enter a parse tree produced by formatterParser#wr_answers_block.
    def enterWr_answers_block(self, ctx:formatterParser.Wr_answers_blockContext):
        pass

    # Exit a parse tree produced by formatterParser#wr_answers_block.
    def exitWr_answers_block(self, ctx:formatterParser.Wr_answers_blockContext):
        pass


    # Enter a parse tree produced by formatterParser#sectionheader.
    def enterSectionheader(self, ctx:formatterParser.SectionheaderContext):
        pass

    # Exit a parse tree produced by formatterParser#sectionheader.
    def exitSectionheader(self, ctx:formatterParser.SectionheaderContext):
        pass


    # Enter a parse tree produced by formatterParser#end_answer_token.
    def enterEnd_answer_token(self, ctx:formatterParser.End_answer_tokenContext):
        pass

    # Exit a parse tree produced by formatterParser#end_answer_token.
    def exitEnd_answer_token(self, ctx:formatterParser.End_answer_tokenContext):
        pass


    # Enter a parse tree produced by formatterParser#wr_answer_token.
    def enterWr_answer_token(self, ctx:formatterParser.Wr_answer_tokenContext):
        pass

    # Exit a parse tree produced by formatterParser#wr_answer_token.
    def exitWr_answer_token(self, ctx:formatterParser.Wr_answer_tokenContext):
        pass


    # Enter a parse tree produced by formatterParser#end_answers_item.
    def enterEnd_answers_item(self, ctx:formatterParser.End_answers_itemContext):
        pass

    # Exit a parse tree produced by formatterParser#end_answers_item.
    def exitEnd_answers_item(self, ctx:formatterParser.End_answers_itemContext):
        pass


    # Enter a parse tree produced by formatterParser#title.
    def enterTitle(self, ctx:formatterParser.TitleContext):
        pass

    # Exit a parse tree produced by formatterParser#title.
    def exitTitle(self, ctx:formatterParser.TitleContext):
        pass


    # Enter a parse tree produced by formatterParser#points.
    def enterPoints(self, ctx:formatterParser.PointsContext):
        pass

    # Exit a parse tree produced by formatterParser#points.
    def exitPoints(self, ctx:formatterParser.PointsContext):
        pass


    # Enter a parse tree produced by formatterParser#questiontype.
    def enterQuestiontype(self, ctx:formatterParser.QuestiontypeContext):
        pass

    # Exit a parse tree produced by formatterParser#questiontype.
    def exitQuestiontype(self, ctx:formatterParser.QuestiontypeContext):
        pass


    # Enter a parse tree produced by formatterParser#randomize.
    def enterRandomize(self, ctx:formatterParser.RandomizeContext):
        pass

    # Exit a parse tree produced by formatterParser#randomize.
    def exitRandomize(self, ctx:formatterParser.RandomizeContext):
        pass


    # Enter a parse tree produced by formatterParser#content.
    def enterContent(self, ctx:formatterParser.ContentContext):
        pass

    # Exit a parse tree produced by formatterParser#content.
    def exitContent(self, ctx:formatterParser.ContentContext):
        pass



del formatterParser