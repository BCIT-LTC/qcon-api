# Generated from L1.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .L1Parser import L1Parser
else:
    from L1Parser import L1Parser

# This class defines a complete generic visitor for a parse tree produced by L1Parser.

class L1Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by L1Parser#l1.
    def visitL1(self, ctx:L1Parser.L1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by L1Parser#sectionheading.
    def visitSectionheading(self, ctx:L1Parser.SectionheadingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by L1Parser#rootlist.
    def visitRootlist(self, ctx:L1Parser.RootlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by L1Parser#numlist.
    def visitNumlist(self, ctx:L1Parser.NumlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by L1Parser#letterlist.
    def visitLetterlist(self, ctx:L1Parser.LetterlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by L1Parser#question_header.
    def visitQuestion_header(self, ctx:L1Parser.Question_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by L1Parser#numlist_prefix.
    def visitNumlist_prefix(self, ctx:L1Parser.Numlist_prefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by L1Parser#letterlist_prefix_regular.
    def visitLetterlist_prefix_regular(self, ctx:L1Parser.Letterlist_prefix_regularContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by L1Parser#letterlist_prefix_correct.
    def visitLetterlist_prefix_correct(self, ctx:L1Parser.Letterlist_prefix_correctContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by L1Parser#endoflist.
    def visitEndoflist(self, ctx:L1Parser.EndoflistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by L1Parser#question_header_parameter.
    def visitQuestion_header_parameter(self, ctx:L1Parser.Question_header_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by L1Parser#end_answers.
    def visitEnd_answers(self, ctx:L1Parser.End_answersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by L1Parser#end_answers_item.
    def visitEnd_answers_item(self, ctx:L1Parser.End_answers_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by L1Parser#title.
    def visitTitle(self, ctx:L1Parser.TitleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by L1Parser#points.
    def visitPoints(self, ctx:L1Parser.PointsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by L1Parser#questiontype.
    def visitQuestiontype(self, ctx:L1Parser.QuestiontypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by L1Parser#randomize.
    def visitRandomize(self, ctx:L1Parser.RandomizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by L1Parser#content.
    def visitContent(self, ctx:L1Parser.ContentContext):
        return self.visitChildren(ctx)



del L1Parser