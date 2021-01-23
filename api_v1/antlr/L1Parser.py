# Generated from L1.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("k\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\5\2$\n\2\3\2\7\2")
        buf.write("\'\n\2\f\2\16\2*\13\2\3\2\3\2\3\3\3\3\3\4\5\4\61\n\4\3")
        buf.write("\4\3\4\5\4\65\n\4\3\4\5\48\n\4\3\5\3\5\3\5\3\6\3\6\5\6")
        buf.write("?\n\6\3\6\3\6\3\7\6\7D\n\7\r\7\16\7E\3\b\3\b\3\t\3\t\3")
        buf.write("\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\5\f\\\n\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20")
        buf.write("\3\20\3\21\6\21g\n\21\r\21\16\21h\3\21\2\2\22\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \2\3\3\2\6\b\2e\2#\3\2")
        buf.write("\2\2\4-\3\2\2\2\6\60\3\2\2\2\b9\3\2\2\2\n>\3\2\2\2\fC")
        buf.write("\3\2\2\2\16G\3\2\2\2\20I\3\2\2\2\22K\3\2\2\2\24M\3\2\2")
        buf.write("\2\26[\3\2\2\2\30]\3\2\2\2\32_\3\2\2\2\34a\3\2\2\2\36")
        buf.write("c\3\2\2\2 f\3\2\2\2\"$\5\4\3\2#\"\3\2\2\2#$\3\2\2\2$(")
        buf.write("\3\2\2\2%\'\5\6\4\2&%\3\2\2\2\'*\3\2\2\2(&\3\2\2\2()\3")
        buf.write("\2\2\2)+\3\2\2\2*(\3\2\2\2+,\7\2\2\3,\3\3\2\2\2-.\5 \21")
        buf.write("\2.\5\3\2\2\2/\61\5\f\7\2\60/\3\2\2\2\60\61\3\2\2\2\61")
        buf.write("\64\3\2\2\2\62\65\5\b\5\2\63\65\5\n\6\2\64\62\3\2\2\2")
        buf.write("\64\63\3\2\2\2\65\67\3\2\2\2\668\5\24\13\2\67\66\3\2\2")
        buf.write("\2\678\3\2\2\28\7\3\2\2\29:\5\16\b\2:;\5 \21\2;\t\3\2")
        buf.write("\2\2<?\5\20\t\2=?\5\22\n\2><\3\2\2\2>=\3\2\2\2?@\3\2\2")
        buf.write("\2@A\5 \21\2A\13\3\2\2\2BD\5\26\f\2CB\3\2\2\2DE\3\2\2")
        buf.write("\2EC\3\2\2\2EF\3\2\2\2F\r\3\2\2\2GH\7\4\2\2H\17\3\2\2")
        buf.write("\2IJ\7\5\2\2J\21\3\2\2\2KL\t\2\2\2L\23\3\2\2\2MN\7\3\2")
        buf.write("\2N\25\3\2\2\2OP\5\32\16\2PQ\5 \21\2Q\\\3\2\2\2RS\5\30")
        buf.write("\r\2ST\5 \21\2T\\\3\2\2\2UV\5\34\17\2VW\5 \21\2W\\\3\2")
        buf.write("\2\2XY\5\36\20\2YZ\5 \21\2Z\\\3\2\2\2[O\3\2\2\2[R\3\2")
        buf.write("\2\2[U\3\2\2\2[X\3\2\2\2\\\27\3\2\2\2]^\7\t\2\2^\31\3")
        buf.write("\2\2\2_`\7\n\2\2`\33\3\2\2\2ab\7\13\2\2b\35\3\2\2\2cd")
        buf.write("\7\f\2\2d\37\3\2\2\2eg\7\r\2\2fe\3\2\2\2gh\3\2\2\2hf\3")
        buf.write("\2\2\2hi\3\2\2\2i!\3\2\2\2\13#(\60\64\67>E[h")
        return buf.getvalue()


class L1Parser ( Parser ):

    grammarFileName = "L1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "ENDOFLIST", "NUMLIST_PREFIX", "LETTERLIST_PREFIX", 
                      "STAR_AFTER_DOT", "STAR_BEFORE_DOT", "STAR_BEFORE_LETTER", 
                      "TITLE", "POINTS", "TYPE", "RANDOMIZE", "ALL_CHARACTER" ]

    RULE_l1 = 0
    RULE_sectionheading = 1
    RULE_rootlist = 2
    RULE_numlist = 3
    RULE_letterlist = 4
    RULE_question_header = 5
    RULE_numlist_prefix = 6
    RULE_letterlist_prefix_regular = 7
    RULE_letterlist_prefix_correct = 8
    RULE_endoflist = 9
    RULE_question_header_parameter = 10
    RULE_title = 11
    RULE_points = 12
    RULE_questiontype = 13
    RULE_randomize = 14
    RULE_content = 15

    ruleNames =  [ "l1", "sectionheading", "rootlist", "numlist", "letterlist", 
                   "question_header", "numlist_prefix", "letterlist_prefix_regular", 
                   "letterlist_prefix_correct", "endoflist", "question_header_parameter", 
                   "title", "points", "questiontype", "randomize", "content" ]

    EOF = Token.EOF
    ENDOFLIST=1
    NUMLIST_PREFIX=2
    LETTERLIST_PREFIX=3
    STAR_AFTER_DOT=4
    STAR_BEFORE_DOT=5
    STAR_BEFORE_LETTER=6
    TITLE=7
    POINTS=8
    TYPE=9
    RANDOMIZE=10
    ALL_CHARACTER=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class L1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(L1Parser.EOF, 0)

        def sectionheading(self):
            return self.getTypedRuleContext(L1Parser.SectionheadingContext,0)


        def rootlist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(L1Parser.RootlistContext)
            else:
                return self.getTypedRuleContext(L1Parser.RootlistContext,i)


        def getRuleIndex(self):
            return L1Parser.RULE_l1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterL1" ):
                listener.enterL1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitL1" ):
                listener.exitL1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitL1" ):
                return visitor.visitL1(self)
            else:
                return visitor.visitChildren(self)




    def l1(self):

        localctx = L1Parser.L1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_l1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==L1Parser.ALL_CHARACTER:
                self.state = 32
                self.sectionheading()


            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << L1Parser.NUMLIST_PREFIX) | (1 << L1Parser.LETTERLIST_PREFIX) | (1 << L1Parser.STAR_AFTER_DOT) | (1 << L1Parser.STAR_BEFORE_DOT) | (1 << L1Parser.STAR_BEFORE_LETTER) | (1 << L1Parser.TITLE) | (1 << L1Parser.POINTS) | (1 << L1Parser.TYPE) | (1 << L1Parser.RANDOMIZE))) != 0):
                self.state = 35
                self.rootlist()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 41
            self.match(L1Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SectionheadingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def content(self):
            return self.getTypedRuleContext(L1Parser.ContentContext,0)


        def getRuleIndex(self):
            return L1Parser.RULE_sectionheading

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSectionheading" ):
                listener.enterSectionheading(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSectionheading" ):
                listener.exitSectionheading(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSectionheading" ):
                return visitor.visitSectionheading(self)
            else:
                return visitor.visitChildren(self)




    def sectionheading(self):

        localctx = L1Parser.SectionheadingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sectionheading)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.content()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RootlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numlist(self):
            return self.getTypedRuleContext(L1Parser.NumlistContext,0)


        def letterlist(self):
            return self.getTypedRuleContext(L1Parser.LetterlistContext,0)


        def question_header(self):
            return self.getTypedRuleContext(L1Parser.Question_headerContext,0)


        def endoflist(self):
            return self.getTypedRuleContext(L1Parser.EndoflistContext,0)


        def getRuleIndex(self):
            return L1Parser.RULE_rootlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRootlist" ):
                listener.enterRootlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRootlist" ):
                listener.exitRootlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRootlist" ):
                return visitor.visitRootlist(self)
            else:
                return visitor.visitChildren(self)




    def rootlist(self):

        localctx = L1Parser.RootlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_rootlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << L1Parser.TITLE) | (1 << L1Parser.POINTS) | (1 << L1Parser.TYPE) | (1 << L1Parser.RANDOMIZE))) != 0):
                self.state = 45
                self.question_header()


            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [L1Parser.NUMLIST_PREFIX]:
                self.state = 48
                self.numlist()
                pass
            elif token in [L1Parser.LETTERLIST_PREFIX, L1Parser.STAR_AFTER_DOT, L1Parser.STAR_BEFORE_DOT, L1Parser.STAR_BEFORE_LETTER]:
                self.state = 49
                self.letterlist()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==L1Parser.ENDOFLIST:
                self.state = 52
                self.endoflist()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numlist_prefix(self):
            return self.getTypedRuleContext(L1Parser.Numlist_prefixContext,0)


        def content(self):
            return self.getTypedRuleContext(L1Parser.ContentContext,0)


        def getRuleIndex(self):
            return L1Parser.RULE_numlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumlist" ):
                listener.enterNumlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumlist" ):
                listener.exitNumlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumlist" ):
                return visitor.visitNumlist(self)
            else:
                return visitor.visitChildren(self)




    def numlist(self):

        localctx = L1Parser.NumlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_numlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.numlist_prefix()
            self.state = 56
            self.content()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LetterlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def content(self):
            return self.getTypedRuleContext(L1Parser.ContentContext,0)


        def letterlist_prefix_regular(self):
            return self.getTypedRuleContext(L1Parser.Letterlist_prefix_regularContext,0)


        def letterlist_prefix_correct(self):
            return self.getTypedRuleContext(L1Parser.Letterlist_prefix_correctContext,0)


        def getRuleIndex(self):
            return L1Parser.RULE_letterlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetterlist" ):
                listener.enterLetterlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetterlist" ):
                listener.exitLetterlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetterlist" ):
                return visitor.visitLetterlist(self)
            else:
                return visitor.visitChildren(self)




    def letterlist(self):

        localctx = L1Parser.LetterlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_letterlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [L1Parser.LETTERLIST_PREFIX]:
                self.state = 58
                self.letterlist_prefix_regular()
                pass
            elif token in [L1Parser.STAR_AFTER_DOT, L1Parser.STAR_BEFORE_DOT, L1Parser.STAR_BEFORE_LETTER]:
                self.state = 59
                self.letterlist_prefix_correct()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 62
            self.content()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Question_headerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def question_header_parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(L1Parser.Question_header_parameterContext)
            else:
                return self.getTypedRuleContext(L1Parser.Question_header_parameterContext,i)


        def getRuleIndex(self):
            return L1Parser.RULE_question_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuestion_header" ):
                listener.enterQuestion_header(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuestion_header" ):
                listener.exitQuestion_header(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuestion_header" ):
                return visitor.visitQuestion_header(self)
            else:
                return visitor.visitChildren(self)




    def question_header(self):

        localctx = L1Parser.Question_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_question_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 64
                self.question_header_parameter()
                self.state = 67 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << L1Parser.TITLE) | (1 << L1Parser.POINTS) | (1 << L1Parser.TYPE) | (1 << L1Parser.RANDOMIZE))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Numlist_prefixContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMLIST_PREFIX(self):
            return self.getToken(L1Parser.NUMLIST_PREFIX, 0)

        def getRuleIndex(self):
            return L1Parser.RULE_numlist_prefix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumlist_prefix" ):
                listener.enterNumlist_prefix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumlist_prefix" ):
                listener.exitNumlist_prefix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumlist_prefix" ):
                return visitor.visitNumlist_prefix(self)
            else:
                return visitor.visitChildren(self)




    def numlist_prefix(self):

        localctx = L1Parser.Numlist_prefixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_numlist_prefix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(L1Parser.NUMLIST_PREFIX)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Letterlist_prefix_regularContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LETTERLIST_PREFIX(self):
            return self.getToken(L1Parser.LETTERLIST_PREFIX, 0)

        def getRuleIndex(self):
            return L1Parser.RULE_letterlist_prefix_regular

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetterlist_prefix_regular" ):
                listener.enterLetterlist_prefix_regular(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetterlist_prefix_regular" ):
                listener.exitLetterlist_prefix_regular(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetterlist_prefix_regular" ):
                return visitor.visitLetterlist_prefix_regular(self)
            else:
                return visitor.visitChildren(self)




    def letterlist_prefix_regular(self):

        localctx = L1Parser.Letterlist_prefix_regularContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_letterlist_prefix_regular)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(L1Parser.LETTERLIST_PREFIX)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Letterlist_prefix_correctContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR_AFTER_DOT(self):
            return self.getToken(L1Parser.STAR_AFTER_DOT, 0)

        def STAR_BEFORE_DOT(self):
            return self.getToken(L1Parser.STAR_BEFORE_DOT, 0)

        def STAR_BEFORE_LETTER(self):
            return self.getToken(L1Parser.STAR_BEFORE_LETTER, 0)

        def getRuleIndex(self):
            return L1Parser.RULE_letterlist_prefix_correct

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetterlist_prefix_correct" ):
                listener.enterLetterlist_prefix_correct(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetterlist_prefix_correct" ):
                listener.exitLetterlist_prefix_correct(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetterlist_prefix_correct" ):
                return visitor.visitLetterlist_prefix_correct(self)
            else:
                return visitor.visitChildren(self)




    def letterlist_prefix_correct(self):

        localctx = L1Parser.Letterlist_prefix_correctContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_letterlist_prefix_correct)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << L1Parser.STAR_AFTER_DOT) | (1 << L1Parser.STAR_BEFORE_DOT) | (1 << L1Parser.STAR_BEFORE_LETTER))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndoflistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENDOFLIST(self):
            return self.getToken(L1Parser.ENDOFLIST, 0)

        def getRuleIndex(self):
            return L1Parser.RULE_endoflist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndoflist" ):
                listener.enterEndoflist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndoflist" ):
                listener.exitEndoflist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndoflist" ):
                return visitor.visitEndoflist(self)
            else:
                return visitor.visitChildren(self)




    def endoflist(self):

        localctx = L1Parser.EndoflistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_endoflist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(L1Parser.ENDOFLIST)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Question_header_parameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def points(self):
            return self.getTypedRuleContext(L1Parser.PointsContext,0)


        def content(self):
            return self.getTypedRuleContext(L1Parser.ContentContext,0)


        def title(self):
            return self.getTypedRuleContext(L1Parser.TitleContext,0)


        def questiontype(self):
            return self.getTypedRuleContext(L1Parser.QuestiontypeContext,0)


        def randomize(self):
            return self.getTypedRuleContext(L1Parser.RandomizeContext,0)


        def getRuleIndex(self):
            return L1Parser.RULE_question_header_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuestion_header_parameter" ):
                listener.enterQuestion_header_parameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuestion_header_parameter" ):
                listener.exitQuestion_header_parameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuestion_header_parameter" ):
                return visitor.visitQuestion_header_parameter(self)
            else:
                return visitor.visitChildren(self)




    def question_header_parameter(self):

        localctx = L1Parser.Question_header_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_question_header_parameter)
        try:
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [L1Parser.POINTS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.points()
                self.state = 78
                self.content()
                pass
            elif token in [L1Parser.TITLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.title()
                self.state = 81
                self.content()
                pass
            elif token in [L1Parser.TYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.questiontype()
                self.state = 84
                self.content()
                pass
            elif token in [L1Parser.RANDOMIZE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 86
                self.randomize()
                self.state = 87
                self.content()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TitleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TITLE(self):
            return self.getToken(L1Parser.TITLE, 0)

        def getRuleIndex(self):
            return L1Parser.RULE_title

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTitle" ):
                listener.enterTitle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTitle" ):
                listener.exitTitle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTitle" ):
                return visitor.visitTitle(self)
            else:
                return visitor.visitChildren(self)




    def title(self):

        localctx = L1Parser.TitleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_title)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(L1Parser.TITLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PointsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POINTS(self):
            return self.getToken(L1Parser.POINTS, 0)

        def getRuleIndex(self):
            return L1Parser.RULE_points

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPoints" ):
                listener.enterPoints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPoints" ):
                listener.exitPoints(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPoints" ):
                return visitor.visitPoints(self)
            else:
                return visitor.visitChildren(self)




    def points(self):

        localctx = L1Parser.PointsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_points)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(L1Parser.POINTS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuestiontypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(L1Parser.TYPE, 0)

        def getRuleIndex(self):
            return L1Parser.RULE_questiontype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuestiontype" ):
                listener.enterQuestiontype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuestiontype" ):
                listener.exitQuestiontype(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuestiontype" ):
                return visitor.visitQuestiontype(self)
            else:
                return visitor.visitChildren(self)




    def questiontype(self):

        localctx = L1Parser.QuestiontypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_questiontype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(L1Parser.TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RandomizeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RANDOMIZE(self):
            return self.getToken(L1Parser.RANDOMIZE, 0)

        def getRuleIndex(self):
            return L1Parser.RULE_randomize

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRandomize" ):
                listener.enterRandomize(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRandomize" ):
                listener.exitRandomize(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRandomize" ):
                return visitor.visitRandomize(self)
            else:
                return visitor.visitChildren(self)




    def randomize(self):

        localctx = L1Parser.RandomizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_randomize)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(L1Parser.RANDOMIZE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALL_CHARACTER(self, i:int=None):
            if i is None:
                return self.getTokens(L1Parser.ALL_CHARACTER)
            else:
                return self.getToken(L1Parser.ALL_CHARACTER, i)

        def getRuleIndex(self):
            return L1Parser.RULE_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContent" ):
                listener.enterContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContent" ):
                listener.exitContent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContent" ):
                return visitor.visitContent(self)
            else:
                return visitor.visitChildren(self)




    def content(self):

        localctx = L1Parser.ContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 99
                self.match(L1Parser.ALL_CHARACTER)
                self.state = 102 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==L1Parser.ALL_CHARACTER):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





