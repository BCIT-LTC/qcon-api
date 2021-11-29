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


    # Visit a parse tree produced by formatterParser#end_answers_block.
    def visitEnd_answers_block(self, ctx:formatterParser.End_answers_blockContext):
        return self.visitChildren(ctx)



del formatterParser