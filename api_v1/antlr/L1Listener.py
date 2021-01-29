# Generated from L1.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .L1Parser import L1Parser
else:
    from L1Parser import L1Parser
import re
# This class defines a complete listener for a parse tree produced by L1Parser.
class L1Listener(ParseTreeListener):
    def __init__(self, question_library):
        self.questions = []
    
    def get_results(self):
        return self.questions

    # Enter a parse tree produced by L1Parser#l1.
    def enterL1(self, ctx:L1Parser.L1Context):
        pass

    # Exit a parse tree produced by L1Parser#l1.
    def exitL1(self, ctx:L1Parser.L1Context):
        if ctx.end_answers() != None:
            content = ctx.end_answers().getText()
            content = re.sub(r"\n\s*\>\s*", "", content)

            self.questions.append({'prefix':'', 'content': content +'\n', 'correctprefix': False, 'listitem': False, 'sectionheader':False, 'questionheader':False, 'endanswer': True})
            pass


    # Enter a parse tree produced by L1Parser#sectionheading.
    def enterSectionheading(self, ctx:L1Parser.SectionheadingContext):
        pass

    # Exit a parse tree produced by L1Parser#sectionheading.
    def exitSectionheading(self, ctx:L1Parser.SectionheadingContext):
        if ctx.content() != None:
            x = re.sub(r"\n\s*\>\s*", "", ctx.content().getText())
            self.questions.append({'prefix':'', 'content': x +'\n', 'correctprefix': False, 'listitem': False, 'sectionheader':True, 'questionheader':False, 'endanswer': False})
            pass


    # Enter a parse tree produced by L1Parser#rootlist.
    def enterRootlist(self, ctx:L1Parser.RootlistContext):
        pass

    # Exit a parse tree produced by L1Parser#rootlist.
    def exitRootlist(self, ctx:L1Parser.RootlistContext):
        pass


    # Enter a parse tree produced by L1Parser#numlist.
    def enterNumlist(self, ctx:L1Parser.NumlistContext):
        pass

    # Exit a parse tree produced by L1Parser#numlist.
    def exitNumlist(self, ctx:L1Parser.NumlistContext):
         # {'prefix':ctx.numlist_prefix().getText(), 'content':ctx.content().getText(), 'correctprefix': False, 'listseparator': False}
        prefix = re.sub(r"\n\s*\>\s*", "\n", ctx.numlist_prefix().getText())
        content = re.sub(r"\n\s*\>\s*", "\n", ctx.content().getText())
        # self.questions.append({'prefix':prefix, 'content':content, 'correctprefix': False, 'listitem': True})
        self.questions.append({'prefix':prefix, 'content':content, 'correctprefix': False, 'listitem': True, 'sectionheader':False, 'questionheader':False, 'endanswer': False})
        pass


    # Enter a parse tree produced by L1Parser#letterlist.
    def enterLetterlist(self, ctx:L1Parser.LetterlistContext):
        pass

    # Exit a parse tree produced by L1Parser#letterlist.
    def exitLetterlist(self, ctx:L1Parser.LetterlistContext):
        if ctx.letterlist_prefix_regular() != None:
            prefix = re.sub(r"\n\s*\>\s*", "\n", ctx.letterlist_prefix_regular().getText())
            content = re.sub(r"\n\s*\>\s*", "\n", ctx.content().getText())
            # self.questions.append({'prefix':prefix, 'content':content, 'correctprefix': False, 'listitem': True})
            self.questions.append({'prefix':prefix, 'content':content, 'correctprefix': False, 'listitem': True, 'sectionheader':False, 'questionheader':False, 'endanswer': False})

        if ctx.letterlist_prefix_correct() != None:
            prefix = re.sub(r"\n\s*\>\s*", "\n", ctx.letterlist_prefix_correct().getText())
            content = re.sub(r"\n\s*\>\s*", "\n", ctx.content().getText())
            # self.questions.append({'prefix':ctx.letterlist_prefix_correct().getText(), 'content':ctx.content().getText(), 'correctprefix': True, 'listitem': True})
            self.questions.append({'prefix':prefix, 'content':content, 'correctprefix': True, 'listitem': True, 'sectionheader':False, 'questionheader':False, 'endanswer': False})
        pass


    # Enter a parse tree produced by L1Parser#question_header.
    def enterQuestion_header(self, ctx:L1Parser.Question_headerContext):
        pass

    # Exit a parse tree produced by L1Parser#question_header.
    def exitQuestion_header(self, ctx:L1Parser.Question_headerContext):
        if ctx.question_header_parameter() != None:  
            content = ""
            for element in ctx.question_header_parameter():
                # content += element.getText()
                content += re.sub(r"\n\s*\>\s*", "\n", element.getText())
            # content = re.sub(r"\n\s*\>\s*", "\n", content)    
            # self.questions.append({'prefix':'', 'content': x, 'correctprefix': False, 'listitem': False})
            self.questions.append({'prefix':'', 'content':content, 'correctprefix': False, 'listitem': False, 'sectionheader':False, 'questionheader':True, 'endanswer': False})
        pass


    # Enter a parse tree produced by L1Parser#numlist_prefix.
    def enterNumlist_prefix(self, ctx:L1Parser.Numlist_prefixContext):
        pass

    # Exit a parse tree produced by L1Parser#numlist_prefix.
    def exitNumlist_prefix(self, ctx:L1Parser.Numlist_prefixContext):
        pass


    # Enter a parse tree produced by L1Parser#letterlist_prefix_regular.
    def enterLetterlist_prefix_regular(self, ctx:L1Parser.Letterlist_prefix_regularContext):
        pass

    # Exit a parse tree produced by L1Parser#letterlist_prefix_regular.
    def exitLetterlist_prefix_regular(self, ctx:L1Parser.Letterlist_prefix_regularContext):
        pass


    # Enter a parse tree produced by L1Parser#letterlist_prefix_correct.
    def enterLetterlist_prefix_correct(self, ctx:L1Parser.Letterlist_prefix_correctContext):
        pass

    # Exit a parse tree produced by L1Parser#letterlist_prefix_correct.
    def exitLetterlist_prefix_correct(self, ctx:L1Parser.Letterlist_prefix_correctContext):
        pass


    # Enter a parse tree produced by L1Parser#endoflist.
    def enterEndoflist(self, ctx:L1Parser.EndoflistContext):
        pass

    # Exit a parse tree produced by L1Parser#endoflist.
    def exitEndoflist(self, ctx:L1Parser.EndoflistContext):
        pass


    # Enter a parse tree produced by L1Parser#question_header_parameter.
    def enterQuestion_header_parameter(self, ctx:L1Parser.Question_header_parameterContext):
        pass

    # Exit a parse tree produced by L1Parser#question_header_parameter.
    def exitQuestion_header_parameter(self, ctx:L1Parser.Question_header_parameterContext):
        pass


    # Enter a parse tree produced by L1Parser#end_answers.
    def enterEnd_answers(self, ctx:L1Parser.End_answersContext):
        pass

    # Exit a parse tree produced by L1Parser#end_answers.
    def exitEnd_answers(self, ctx:L1Parser.End_answersContext):
        pass


    # Enter a parse tree produced by L1Parser#end_answers_item.
    def enterEnd_answers_item(self, ctx:L1Parser.End_answers_itemContext):
        pass

    # Exit a parse tree produced by L1Parser#end_answers_item.
    def exitEnd_answers_item(self, ctx:L1Parser.End_answers_itemContext):
        pass


    # Enter a parse tree produced by L1Parser#title.
    def enterTitle(self, ctx:L1Parser.TitleContext):
        pass

    # Exit a parse tree produced by L1Parser#title.
    def exitTitle(self, ctx:L1Parser.TitleContext):
        pass


    # Enter a parse tree produced by L1Parser#points.
    def enterPoints(self, ctx:L1Parser.PointsContext):
        pass

    # Exit a parse tree produced by L1Parser#points.
    def exitPoints(self, ctx:L1Parser.PointsContext):
        pass


    # Enter a parse tree produced by L1Parser#questiontype.
    def enterQuestiontype(self, ctx:L1Parser.QuestiontypeContext):
        pass

    # Exit a parse tree produced by L1Parser#questiontype.
    def exitQuestiontype(self, ctx:L1Parser.QuestiontypeContext):
        pass


    # Enter a parse tree produced by L1Parser#randomize.
    def enterRandomize(self, ctx:L1Parser.RandomizeContext):
        pass

    # Exit a parse tree produced by L1Parser#randomize.
    def exitRandomize(self, ctx:L1Parser.RandomizeContext):
        pass


    # Enter a parse tree produced by L1Parser#content.
    def enterContent(self, ctx:L1Parser.ContentContext):
        pass

    # Exit a parse tree produced by L1Parser#content.
    def exitContent(self, ctx:L1Parser.ContentContext):
        pass



del L1Parser