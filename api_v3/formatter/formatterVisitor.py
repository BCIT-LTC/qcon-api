# Generated from formatter.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .formatterParser import formatterParser
else:
    from formatterParser import formatterParser

# This class defines a complete generic visitor for a parse tree produced by formatterParser.

class formatterVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by formatterParser#formatter.
    def visitFormatter(self, ctx:formatterParser.FormatterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formatterParser#rootheading.
    def visitRootheading(self, ctx:formatterParser.RootheadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formatterParser#rootbody.
    def visitRootbody(self, ctx:formatterParser.RootbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formatterParser#section.
    def visitSection(self, ctx:formatterParser.SectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formatterParser#sectionbody.
    def visitSectionbody(self, ctx:formatterParser.SectionbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formatterParser#rootlist.
    def visitRootlist(self, ctx:formatterParser.RootlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formatterParser#numlist.
    def visitNumlist(self, ctx:formatterParser.NumlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formatterParser#letterlist.
    def visitLetterlist(self, ctx:formatterParser.LetterlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formatterParser#question_header.
    def visitQuestion_header(self, ctx:formatterParser.Question_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formatterParser#letterlist_prefix_regular.
    def visitLetterlist_prefix_regular(self, ctx:formatterParser.Letterlist_prefix_regularContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formatterParser#letterlist_prefix_correct.
    def visitLetterlist_prefix_correct(self, ctx:formatterParser.Letterlist_prefix_correctContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formatterParser#question_header_parameter.
    def visitQuestion_header_parameter(self, ctx:formatterParser.Question_header_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formatterParser#end_answers_block.
    def visitEnd_answers_block(self, ctx:formatterParser.End_answers_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formatterParser#wr_answers_block.
    def visitWr_answers_block(self, ctx:formatterParser.Wr_answers_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formatterParser#sectionheader.
    def visitSectionheader(self, ctx:formatterParser.SectionheaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formatterParser#end_answer_token.
    def visitEnd_answer_token(self, ctx:formatterParser.End_answer_tokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formatterParser#wr_answer_token.
    def visitWr_answer_token(self, ctx:formatterParser.Wr_answer_tokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formatterParser#end_answers_item.
    def visitEnd_answers_item(self, ctx:formatterParser.End_answers_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formatterParser#title.
    def visitTitle(self, ctx:formatterParser.TitleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formatterParser#points.
    def visitPoints(self, ctx:formatterParser.PointsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formatterParser#questiontype.
    def visitQuestiontype(self, ctx:formatterParser.QuestiontypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formatterParser#randomize.
    def visitRandomize(self, ctx:formatterParser.RandomizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by formatterParser#content.
    def visitContent(self, ctx:formatterParser.ContentContext):
        return self.visitChildren(ctx)



del formatterParser