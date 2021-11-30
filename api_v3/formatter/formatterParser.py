# Generated from formatter.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\n")
        buf.write("d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\5\2\16\n")
        buf.write("\2\3\2\3\2\5\2\22\n\2\3\2\3\2\3\3\6\3\27\n\3\r\3\16\3")
        buf.write("\30\3\4\6\4\34\n\4\r\4\16\4\35\3\5\5\5!\n\5\3\5\6\5$\n")
        buf.write("\5\r\5\16\5%\5\5(\n\5\3\5\3\5\6\5,\n\5\r\5\16\5-\3\5\3")
        buf.write("\5\6\5\62\n\5\r\5\16\5\63\3\5\3\5\6\58\n\5\r\5\16\59\3")
        buf.write("\5\3\5\6\5>\n\5\r\5\16\5?\6\5B\n\5\r\5\16\5C\5\5F\n\5")
        buf.write("\3\5\3\5\6\5J\n\5\r\5\16\5K\6\5N\n\5\r\5\16\5O\3\6\3\6")
        buf.write("\6\6T\n\6\r\6\16\6U\5\6X\n\6\3\6\3\6\6\6\\\n\6\r\6\16")
        buf.write("\6]\6\6`\n\6\r\6\16\6a\3\6\2\2\7\2\4\6\b\n\2\2\2t\2\r")
        buf.write("\3\2\2\2\4\26\3\2\2\2\6\33\3\2\2\2\b \3\2\2\2\nQ\3\2\2")
        buf.write("\2\f\16\5\4\3\2\r\f\3\2\2\2\r\16\3\2\2\2\16\17\3\2\2\2")
        buf.write("\17\21\5\6\4\2\20\22\5\n\6\2\21\20\3\2\2\2\21\22\3\2\2")
        buf.write("\2\22\23\3\2\2\2\23\24\7\2\2\3\24\3\3\2\2\2\25\27\7\n")
        buf.write("\2\2\26\25\3\2\2\2\27\30\3\2\2\2\30\26\3\2\2\2\30\31\3")
        buf.write("\2\2\2\31\5\3\2\2\2\32\34\5\b\5\2\33\32\3\2\2\2\34\35")
        buf.write("\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36\7\3\2\2\2\37!")
        buf.write("\7\t\2\2 \37\3\2\2\2 !\3\2\2\2!\'\3\2\2\2\"$\7\n\2\2#")
        buf.write("\"\3\2\2\2$%\3\2\2\2%#\3\2\2\2%&\3\2\2\2&(\3\2\2\2\'#")
        buf.write("\3\2\2\2\'(\3\2\2\2(M\3\2\2\2)+\7\5\2\2*,\7\n\2\2+*\3")
        buf.write("\2\2\2,-\3\2\2\2-+\3\2\2\2-.\3\2\2\2.B\3\2\2\2/\61\7\4")
        buf.write("\2\2\60\62\7\n\2\2\61\60\3\2\2\2\62\63\3\2\2\2\63\61\3")
        buf.write("\2\2\2\63\64\3\2\2\2\64B\3\2\2\2\65\67\7\6\2\2\668\7\n")
        buf.write("\2\2\67\66\3\2\2\289\3\2\2\29\67\3\2\2\29:\3\2\2\2:B\3")
        buf.write("\2\2\2;=\7\7\2\2<>\7\n\2\2=<\3\2\2\2>?\3\2\2\2?=\3\2\2")
        buf.write("\2?@\3\2\2\2@B\3\2\2\2A)\3\2\2\2A/\3\2\2\2A\65\3\2\2\2")
        buf.write("A;\3\2\2\2BC\3\2\2\2CA\3\2\2\2CD\3\2\2\2DF\3\2\2\2EA\3")
        buf.write("\2\2\2EF\3\2\2\2FG\3\2\2\2GI\7\3\2\2HJ\7\n\2\2IH\3\2\2")
        buf.write("\2JK\3\2\2\2KI\3\2\2\2KL\3\2\2\2LN\3\2\2\2ME\3\2\2\2N")
        buf.write("O\3\2\2\2OM\3\2\2\2OP\3\2\2\2P\t\3\2\2\2Q_\7\b\2\2RT\7")
        buf.write("\n\2\2SR\3\2\2\2TU\3\2\2\2US\3\2\2\2UV\3\2\2\2VX\3\2\2")
        buf.write("\2WS\3\2\2\2WX\3\2\2\2XY\3\2\2\2Y[\7\3\2\2Z\\\7\n\2\2")
        buf.write("[Z\3\2\2\2\\]\3\2\2\2][\3\2\2\2]^\3\2\2\2^`\3\2\2\2_W")
        buf.write("\3\2\2\2`a\3\2\2\2a_\3\2\2\2ab\3\2\2\2b\13\3\2\2\2\26")
        buf.write("\r\21\30\35 %\'-\639?ACEKOUW]a")
        return buf.getvalue()


class formatterParser ( Parser ):

    grammarFileName = "formatter.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "NUMLIST_PREFIX", "TITLE", "POINTS", 
                      "TYPE", "RANDOMIZE", "END_ANSWER", "SECTION", "ALL_CHARACTER" ]

    RULE_formatter = 0
    RULE_rootheading = 1
    RULE_rootbody = 2
    RULE_section = 3
    RULE_end_answers_block = 4

    ruleNames =  [ "formatter", "rootheading", "rootbody", "section", "end_answers_block" ]

    EOF = Token.EOF
    NUMLIST_PREFIX=1
    TITLE=2
    POINTS=3
    TYPE=4
    RANDOMIZE=5
    END_ANSWER=6
    SECTION=7
    ALL_CHARACTER=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FormatterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rootbody(self):
            return self.getTypedRuleContext(formatterParser.RootbodyContext,0)


        def EOF(self):
            return self.getToken(formatterParser.EOF, 0)

        def rootheading(self):
            return self.getTypedRuleContext(formatterParser.RootheadingContext,0)


        def end_answers_block(self):
            return self.getTypedRuleContext(formatterParser.End_answers_blockContext,0)


        def getRuleIndex(self):
            return formatterParser.RULE_formatter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormatter" ):
                listener.enterFormatter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormatter" ):
                listener.exitFormatter(self)




    def formatter(self):

        localctx = formatterParser.FormatterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_formatter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 10
                self.rootheading()


            self.state = 13
            self.rootbody()
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==formatterParser.END_ANSWER:
                self.state = 14
                self.end_answers_block()


            self.state = 17
            self.match(formatterParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RootheadingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALL_CHARACTER(self, i:int=None):
            if i is None:
                return self.getTokens(formatterParser.ALL_CHARACTER)
            else:
                return self.getToken(formatterParser.ALL_CHARACTER, i)

        def getRuleIndex(self):
            return formatterParser.RULE_rootheading

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRootheading" ):
                listener.enterRootheading(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRootheading" ):
                listener.exitRootheading(self)




    def rootheading(self):

        localctx = formatterParser.RootheadingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_rootheading)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 19
                    self.match(formatterParser.ALL_CHARACTER)

                else:
                    raise NoViableAltException(self)
                self.state = 22 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RootbodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(formatterParser.SectionContext)
            else:
                return self.getTypedRuleContext(formatterParser.SectionContext,i)


        def getRuleIndex(self):
            return formatterParser.RULE_rootbody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRootbody" ):
                listener.enterRootbody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRootbody" ):
                listener.exitRootbody(self)




    def rootbody(self):

        localctx = formatterParser.RootbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_rootbody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.section()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << formatterParser.NUMLIST_PREFIX) | (1 << formatterParser.TITLE) | (1 << formatterParser.POINTS) | (1 << formatterParser.TYPE) | (1 << formatterParser.RANDOMIZE) | (1 << formatterParser.SECTION) | (1 << formatterParser.ALL_CHARACTER))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SectionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SECTION(self):
            return self.getToken(formatterParser.SECTION, 0)

        def NUMLIST_PREFIX(self, i:int=None):
            if i is None:
                return self.getTokens(formatterParser.NUMLIST_PREFIX)
            else:
                return self.getToken(formatterParser.NUMLIST_PREFIX, i)

        def ALL_CHARACTER(self, i:int=None):
            if i is None:
                return self.getTokens(formatterParser.ALL_CHARACTER)
            else:
                return self.getToken(formatterParser.ALL_CHARACTER, i)

        def POINTS(self, i:int=None):
            if i is None:
                return self.getTokens(formatterParser.POINTS)
            else:
                return self.getToken(formatterParser.POINTS, i)

        def TITLE(self, i:int=None):
            if i is None:
                return self.getTokens(formatterParser.TITLE)
            else:
                return self.getToken(formatterParser.TITLE, i)

        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(formatterParser.TYPE)
            else:
                return self.getToken(formatterParser.TYPE, i)

        def RANDOMIZE(self, i:int=None):
            if i is None:
                return self.getTokens(formatterParser.RANDOMIZE)
            else:
                return self.getToken(formatterParser.RANDOMIZE, i)

        def getRuleIndex(self):
            return formatterParser.RULE_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSection" ):
                listener.enterSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSection" ):
                listener.exitSection(self)




    def section(self):

        localctx = formatterParser.SectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==formatterParser.SECTION:
                self.state = 29
                self.match(formatterParser.SECTION)


            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==formatterParser.ALL_CHARACTER:
                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 32
                    self.match(formatterParser.ALL_CHARACTER)
                    self.state = 35 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==formatterParser.ALL_CHARACTER):
                        break



            self.state = 75 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 67
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << formatterParser.TITLE) | (1 << formatterParser.POINTS) | (1 << formatterParser.TYPE) | (1 << formatterParser.RANDOMIZE))) != 0):
                        self.state = 63 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 63
                            self._errHandler.sync(self)
                            token = self._input.LA(1)
                            if token in [formatterParser.POINTS]:
                                self.state = 39
                                self.match(formatterParser.POINTS)

                                self.state = 41 
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)
                                while True:
                                    self.state = 40
                                    self.match(formatterParser.ALL_CHARACTER)
                                    self.state = 43 
                                    self._errHandler.sync(self)
                                    _la = self._input.LA(1)
                                    if not (_la==formatterParser.ALL_CHARACTER):
                                        break

                                pass
                            elif token in [formatterParser.TITLE]:
                                self.state = 45
                                self.match(formatterParser.TITLE)

                                self.state = 47 
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)
                                while True:
                                    self.state = 46
                                    self.match(formatterParser.ALL_CHARACTER)
                                    self.state = 49 
                                    self._errHandler.sync(self)
                                    _la = self._input.LA(1)
                                    if not (_la==formatterParser.ALL_CHARACTER):
                                        break

                                pass
                            elif token in [formatterParser.TYPE]:
                                self.state = 51
                                self.match(formatterParser.TYPE)

                                self.state = 53 
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)
                                while True:
                                    self.state = 52
                                    self.match(formatterParser.ALL_CHARACTER)
                                    self.state = 55 
                                    self._errHandler.sync(self)
                                    _la = self._input.LA(1)
                                    if not (_la==formatterParser.ALL_CHARACTER):
                                        break

                                pass
                            elif token in [formatterParser.RANDOMIZE]:
                                self.state = 57
                                self.match(formatterParser.RANDOMIZE)

                                self.state = 59 
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)
                                while True:
                                    self.state = 58
                                    self.match(formatterParser.ALL_CHARACTER)
                                    self.state = 61 
                                    self._errHandler.sync(self)
                                    _la = self._input.LA(1)
                                    if not (_la==formatterParser.ALL_CHARACTER):
                                        break

                                pass
                            else:
                                raise NoViableAltException(self)

                            self.state = 65 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << formatterParser.TITLE) | (1 << formatterParser.POINTS) | (1 << formatterParser.TYPE) | (1 << formatterParser.RANDOMIZE))) != 0)):
                                break



                    self.state = 69
                    self.match(formatterParser.NUMLIST_PREFIX)

                    self.state = 71 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 70
                            self.match(formatterParser.ALL_CHARACTER)

                        else:
                            raise NoViableAltException(self)
                        self.state = 73 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,14,self._ctx)


                else:
                    raise NoViableAltException(self)
                self.state = 77 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class End_answers_blockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def END_ANSWER(self):
            return self.getToken(formatterParser.END_ANSWER, 0)

        def NUMLIST_PREFIX(self, i:int=None):
            if i is None:
                return self.getTokens(formatterParser.NUMLIST_PREFIX)
            else:
                return self.getToken(formatterParser.NUMLIST_PREFIX, i)

        def ALL_CHARACTER(self, i:int=None):
            if i is None:
                return self.getTokens(formatterParser.ALL_CHARACTER)
            else:
                return self.getToken(formatterParser.ALL_CHARACTER, i)

        def getRuleIndex(self):
            return formatterParser.RULE_end_answers_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnd_answers_block" ):
                listener.enterEnd_answers_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnd_answers_block" ):
                listener.exitEnd_answers_block(self)




    def end_answers_block(self):

        localctx = formatterParser.End_answers_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_end_answers_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(formatterParser.END_ANSWER)
            self.state = 93 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==formatterParser.ALL_CHARACTER:
                    self.state = 81 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 80
                        self.match(formatterParser.ALL_CHARACTER)
                        self.state = 83 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==formatterParser.ALL_CHARACTER):
                            break



                self.state = 87
                self.match(formatterParser.NUMLIST_PREFIX)

                self.state = 89 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 88
                        self.match(formatterParser.ALL_CHARACTER)

                    else:
                        raise NoViableAltException(self)
                    self.state = 91 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

                self.state = 95 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==formatterParser.NUMLIST_PREFIX or _la==formatterParser.ALL_CHARACTER):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





