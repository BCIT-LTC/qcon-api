# Generated from formatter.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .formatterParser import formatterParser
else:
    from formatterParser import formatterParser

# This class defines a complete listener for a parse tree produced by formatterParser.
class formatterListener(ParseTreeListener):
    def __init__(self, question_library):
        self.header = None
        self.sections = []
        self.answers = None

    def get_results(self):
        return [self.header,self.sections,self.answers]
        pass


    # Enter a parse tree produced by formatterParser#formatter.
    def enterFormatter(self, ctx:formatterParser.FormatterContext):
        print("enter formatter")
        pass

    # Exit a parse tree produced by formatterParser#formatter.
    def exitFormatter(self, ctx:formatterParser.FormatterContext):
        if ctx.rootheading() != None:
            self.header = ctx.rootheading().getText()       
        if ctx.end_answers_block() != None:
            self.answers = ctx.end_answers_block().getText()    

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
        print("body found")
        if ctx.section() != None:
            for val in ctx.section():
                self.sections.append(val.getText())
        pass


    # Enter a parse tree produced by formatterParser#section.
    def enterSection(self, ctx:formatterParser.SectionContext):
        pass

    # Exit a parse tree produced by formatterParser#section.
    def exitSection(self, ctx:formatterParser.SectionContext):
        # print("section found")
        # print(ctx.SectionContext().getText())
        pass


    # Enter a parse tree produced by formatterParser#end_answers_block.
    def enterEnd_answers_block(self, ctx:formatterParser.End_answers_blockContext):
        pass

    # Exit a parse tree produced by formatterParser#end_answers_block.
    def exitEnd_answers_block(self, ctx:formatterParser.End_answers_blockContext):
        pass



del formatterParser