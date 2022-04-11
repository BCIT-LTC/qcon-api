// Generated from questionparser.g4 by ANTLR 4.9.3
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class questionparserParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.3", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		START_OL=1, END_OL=2, NUMLIST_PREFIX=3, LETTERLIST_PREFIX=4, FIB_START=5, 
		FIB_END=6, CORRECT_ANSWER=7, ALL_CHARACTER=8;
	public static final int
		RULE_questionparser = 0, RULE_question_wrapper = 1, RULE_question = 2, 
		RULE_fib_part = 3, RULE_answers = 4, RULE_answer_part = 5, RULE_correct_answer_part = 6, 
		RULE_trailing_content = 7;
	private static String[] makeRuleNames() {
		return new String[] {
			"questionparser", "question_wrapper", "question", "fib_part", "answers", 
			"answer_part", "correct_answer_part", "trailing_content"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "START_OL", "END_OL", "NUMLIST_PREFIX", "LETTERLIST_PREFIX", "FIB_START", 
			"FIB_END", "CORRECT_ANSWER", "ALL_CHARACTER"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "questionparser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public questionparserParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class QuestionparserContext extends ParserRuleContext {
		public Question_wrapperContext question_wrapper() {
			return getRuleContext(Question_wrapperContext.class,0);
		}
		public Trailing_contentContext trailing_content() {
			return getRuleContext(Trailing_contentContext.class,0);
		}
		public TerminalNode EOF() { return getToken(questionparserParser.EOF, 0); }
		public AnswersContext answers() {
			return getRuleContext(AnswersContext.class,0);
		}
		public QuestionparserContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_questionparser; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof questionparserVisitor ) return ((questionparserVisitor<? extends T>)visitor).visitQuestionparser(this);
			else return visitor.visitChildren(this);
		}
	}

	public final QuestionparserContext questionparser() throws RecognitionException {
		QuestionparserContext _localctx = new QuestionparserContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_questionparser);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(16);
			question_wrapper();
			setState(18);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << START_OL) | (1L << LETTERLIST_PREFIX) | (1L << CORRECT_ANSWER))) != 0)) {
				{
				setState(17);
				answers();
				}
			}

			setState(20);
			trailing_content();
			setState(21);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Question_wrapperContext extends ParserRuleContext {
		public TerminalNode NUMLIST_PREFIX() { return getToken(questionparserParser.NUMLIST_PREFIX, 0); }
		public QuestionContext question() {
			return getRuleContext(QuestionContext.class,0);
		}
		public TerminalNode START_OL() { return getToken(questionparserParser.START_OL, 0); }
		public TerminalNode END_OL() { return getToken(questionparserParser.END_OL, 0); }
		public Question_wrapperContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_question_wrapper; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof questionparserVisitor ) return ((questionparserVisitor<? extends T>)visitor).visitQuestion_wrapper(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Question_wrapperContext question_wrapper() throws RecognitionException {
		Question_wrapperContext _localctx = new Question_wrapperContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_question_wrapper);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(24);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==START_OL) {
				{
				setState(23);
				match(START_OL);
				}
			}

			setState(26);
			match(NUMLIST_PREFIX);
			setState(27);
			question();
			setState(29);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				setState(28);
				match(END_OL);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class QuestionContext extends ParserRuleContext {
		public Fib_partContext fib_part() {
			return getRuleContext(Fib_partContext.class,0);
		}
		public QuestionContext question() {
			return getRuleContext(QuestionContext.class,0);
		}
		public List<TerminalNode> ALL_CHARACTER() { return getTokens(questionparserParser.ALL_CHARACTER); }
		public TerminalNode ALL_CHARACTER(int i) {
			return getToken(questionparserParser.ALL_CHARACTER, i);
		}
		public QuestionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_question; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof questionparserVisitor ) return ((questionparserVisitor<? extends T>)visitor).visitQuestion(this);
			else return visitor.visitChildren(this);
		}
	}

	public final QuestionContext question() throws RecognitionException {
		QuestionContext _localctx = new QuestionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_question);
		int _la;
		try {
			int _alt;
			setState(69);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(31);
				fib_part();
				setState(35);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(32);
						match(ALL_CHARACTER);
						}
						} 
					}
					setState(37);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
				}
				setState(38);
				question();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(43);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==ALL_CHARACTER) {
					{
					{
					setState(40);
					match(ALL_CHARACTER);
					}
					}
					setState(45);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(46);
				fib_part();
				setState(47);
				question();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(52);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==ALL_CHARACTER) {
					{
					{
					setState(49);
					match(ALL_CHARACTER);
					}
					}
					setState(54);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(55);
				fib_part();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(56);
				fib_part();
				setState(60);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(57);
						match(ALL_CHARACTER);
						}
						} 
					}
					setState(62);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
				}
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(66);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(63);
						match(ALL_CHARACTER);
						}
						} 
					}
					setState(68);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Fib_partContext extends ParserRuleContext {
		public TerminalNode FIB_START() { return getToken(questionparserParser.FIB_START, 0); }
		public TerminalNode FIB_END() { return getToken(questionparserParser.FIB_END, 0); }
		public List<TerminalNode> ALL_CHARACTER() { return getTokens(questionparserParser.ALL_CHARACTER); }
		public TerminalNode ALL_CHARACTER(int i) {
			return getToken(questionparserParser.ALL_CHARACTER, i);
		}
		public Fib_partContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fib_part; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof questionparserVisitor ) return ((questionparserVisitor<? extends T>)visitor).visitFib_part(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Fib_partContext fib_part() throws RecognitionException {
		Fib_partContext _localctx = new Fib_partContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_fib_part);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			match(FIB_START);
			setState(75);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ALL_CHARACTER) {
				{
				{
				setState(72);
				match(ALL_CHARACTER);
				}
				}
				setState(77);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(78);
			match(FIB_END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AnswersContext extends ParserRuleContext {
		public TerminalNode START_OL() { return getToken(questionparserParser.START_OL, 0); }
		public List<Answer_partContext> answer_part() {
			return getRuleContexts(Answer_partContext.class);
		}
		public Answer_partContext answer_part(int i) {
			return getRuleContext(Answer_partContext.class,i);
		}
		public List<Correct_answer_partContext> correct_answer_part() {
			return getRuleContexts(Correct_answer_partContext.class);
		}
		public Correct_answer_partContext correct_answer_part(int i) {
			return getRuleContext(Correct_answer_partContext.class,i);
		}
		public TerminalNode END_OL() { return getToken(questionparserParser.END_OL, 0); }
		public AnswersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_answers; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof questionparserVisitor ) return ((questionparserVisitor<? extends T>)visitor).visitAnswers(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AnswersContext answers() throws RecognitionException {
		AnswersContext _localctx = new AnswersContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_answers);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(81);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==START_OL) {
				{
				setState(80);
				match(START_OL);
				}
			}

			setState(85); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(85);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case LETTERLIST_PREFIX:
					{
					setState(83);
					answer_part();
					}
					break;
				case CORRECT_ANSWER:
					{
					setState(84);
					correct_answer_part();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(87); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LETTERLIST_PREFIX || _la==CORRECT_ANSWER );
			setState(90);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				{
				setState(89);
				match(END_OL);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Answer_partContext extends ParserRuleContext {
		public TerminalNode LETTERLIST_PREFIX() { return getToken(questionparserParser.LETTERLIST_PREFIX, 0); }
		public List<TerminalNode> ALL_CHARACTER() { return getTokens(questionparserParser.ALL_CHARACTER); }
		public TerminalNode ALL_CHARACTER(int i) {
			return getToken(questionparserParser.ALL_CHARACTER, i);
		}
		public Answer_partContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_answer_part; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof questionparserVisitor ) return ((questionparserVisitor<? extends T>)visitor).visitAnswer_part(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Answer_partContext answer_part() throws RecognitionException {
		Answer_partContext _localctx = new Answer_partContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_answer_part);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(92);
			match(LETTERLIST_PREFIX);
			setState(96);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(93);
					match(ALL_CHARACTER);
					}
					} 
				}
				setState(98);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Correct_answer_partContext extends ParserRuleContext {
		public TerminalNode CORRECT_ANSWER() { return getToken(questionparserParser.CORRECT_ANSWER, 0); }
		public List<TerminalNode> ALL_CHARACTER() { return getTokens(questionparserParser.ALL_CHARACTER); }
		public TerminalNode ALL_CHARACTER(int i) {
			return getToken(questionparserParser.ALL_CHARACTER, i);
		}
		public Correct_answer_partContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_correct_answer_part; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof questionparserVisitor ) return ((questionparserVisitor<? extends T>)visitor).visitCorrect_answer_part(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Correct_answer_partContext correct_answer_part() throws RecognitionException {
		Correct_answer_partContext _localctx = new Correct_answer_partContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_correct_answer_part);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			match(CORRECT_ANSWER);
			setState(103);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(100);
					match(ALL_CHARACTER);
					}
					} 
				}
				setState(105);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Trailing_contentContext extends ParserRuleContext {
		public List<TerminalNode> ALL_CHARACTER() { return getTokens(questionparserParser.ALL_CHARACTER); }
		public TerminalNode ALL_CHARACTER(int i) {
			return getToken(questionparserParser.ALL_CHARACTER, i);
		}
		public List<TerminalNode> END_OL() { return getTokens(questionparserParser.END_OL); }
		public TerminalNode END_OL(int i) {
			return getToken(questionparserParser.END_OL, i);
		}
		public Trailing_contentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_trailing_content; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof questionparserVisitor ) return ((questionparserVisitor<? extends T>)visitor).visitTrailing_content(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Trailing_contentContext trailing_content() throws RecognitionException {
		Trailing_contentContext _localctx = new Trailing_contentContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_trailing_content);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(109);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==END_OL || _la==ALL_CHARACTER) {
				{
				{
				setState(106);
				_la = _input.LA(1);
				if ( !(_la==END_OL || _la==ALL_CHARACTER) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(111);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\ns\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\3\2\3\2\5\2\25\n\2"+
		"\3\2\3\2\3\2\3\3\5\3\33\n\3\3\3\3\3\3\3\5\3 \n\3\3\4\3\4\7\4$\n\4\f\4"+
		"\16\4\'\13\4\3\4\3\4\3\4\7\4,\n\4\f\4\16\4/\13\4\3\4\3\4\3\4\3\4\7\4\65"+
		"\n\4\f\4\16\48\13\4\3\4\3\4\3\4\7\4=\n\4\f\4\16\4@\13\4\3\4\7\4C\n\4\f"+
		"\4\16\4F\13\4\5\4H\n\4\3\5\3\5\7\5L\n\5\f\5\16\5O\13\5\3\5\3\5\3\6\5\6"+
		"T\n\6\3\6\3\6\6\6X\n\6\r\6\16\6Y\3\6\5\6]\n\6\3\7\3\7\7\7a\n\7\f\7\16"+
		"\7d\13\7\3\b\3\b\7\bh\n\b\f\b\16\bk\13\b\3\t\7\tn\n\t\f\t\16\tq\13\t\3"+
		"\t\2\2\n\2\4\6\b\n\f\16\20\2\3\4\2\4\4\n\n\2~\2\22\3\2\2\2\4\32\3\2\2"+
		"\2\6G\3\2\2\2\bI\3\2\2\2\nS\3\2\2\2\f^\3\2\2\2\16e\3\2\2\2\20o\3\2\2\2"+
		"\22\24\5\4\3\2\23\25\5\n\6\2\24\23\3\2\2\2\24\25\3\2\2\2\25\26\3\2\2\2"+
		"\26\27\5\20\t\2\27\30\7\2\2\3\30\3\3\2\2\2\31\33\7\3\2\2\32\31\3\2\2\2"+
		"\32\33\3\2\2\2\33\34\3\2\2\2\34\35\7\5\2\2\35\37\5\6\4\2\36 \7\4\2\2\37"+
		"\36\3\2\2\2\37 \3\2\2\2 \5\3\2\2\2!%\5\b\5\2\"$\7\n\2\2#\"\3\2\2\2$\'"+
		"\3\2\2\2%#\3\2\2\2%&\3\2\2\2&(\3\2\2\2\'%\3\2\2\2()\5\6\4\2)H\3\2\2\2"+
		"*,\7\n\2\2+*\3\2\2\2,/\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\60\3\2\2\2/-\3\2\2"+
		"\2\60\61\5\b\5\2\61\62\5\6\4\2\62H\3\2\2\2\63\65\7\n\2\2\64\63\3\2\2\2"+
		"\658\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2\679\3\2\2\28\66\3\2\2\29H\5\b"+
		"\5\2:>\5\b\5\2;=\7\n\2\2<;\3\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2?H\3\2"+
		"\2\2@>\3\2\2\2AC\7\n\2\2BA\3\2\2\2CF\3\2\2\2DB\3\2\2\2DE\3\2\2\2EH\3\2"+
		"\2\2FD\3\2\2\2G!\3\2\2\2G-\3\2\2\2G\66\3\2\2\2G:\3\2\2\2GD\3\2\2\2H\7"+
		"\3\2\2\2IM\7\7\2\2JL\7\n\2\2KJ\3\2\2\2LO\3\2\2\2MK\3\2\2\2MN\3\2\2\2N"+
		"P\3\2\2\2OM\3\2\2\2PQ\7\b\2\2Q\t\3\2\2\2RT\7\3\2\2SR\3\2\2\2ST\3\2\2\2"+
		"TW\3\2\2\2UX\5\f\7\2VX\5\16\b\2WU\3\2\2\2WV\3\2\2\2XY\3\2\2\2YW\3\2\2"+
		"\2YZ\3\2\2\2Z\\\3\2\2\2[]\7\4\2\2\\[\3\2\2\2\\]\3\2\2\2]\13\3\2\2\2^b"+
		"\7\6\2\2_a\7\n\2\2`_\3\2\2\2ad\3\2\2\2b`\3\2\2\2bc\3\2\2\2c\r\3\2\2\2"+
		"db\3\2\2\2ei\7\t\2\2fh\7\n\2\2gf\3\2\2\2hk\3\2\2\2ig\3\2\2\2ij\3\2\2\2"+
		"j\17\3\2\2\2ki\3\2\2\2ln\t\2\2\2ml\3\2\2\2nq\3\2\2\2om\3\2\2\2op\3\2\2"+
		"\2p\21\3\2\2\2qo\3\2\2\2\23\24\32\37%-\66>DGMSWY\\bio";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}