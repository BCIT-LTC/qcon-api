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
		START_OL=1, END_OL=2, LETTERLIST_PREFIX=3, FIB_START=4, FIB_END=5, CORRECT_ANSWER=6, 
		CORRECT_ANSWER_FOR_WR=7, ALL_CHARACTER=8;
	public static final int
		RULE_questionparser = 0, RULE_question_wrapper = 1, RULE_question = 2, 
		RULE_fib_question = 3, RULE_fib_part = 4, RULE_answers = 5, RULE_answer_part = 6, 
		RULE_correct_answer_part = 7, RULE_wr_answer = 8, RULE_content = 9, RULE_trailing_content = 10;
	private static String[] makeRuleNames() {
		return new String[] {
			"questionparser", "question_wrapper", "question", "fib_question", "fib_part", 
			"answers", "answer_part", "correct_answer_part", "wr_answer", "content", 
			"trailing_content"
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
			null, "START_OL", "END_OL", "LETTERLIST_PREFIX", "FIB_START", "FIB_END", 
			"CORRECT_ANSWER", "CORRECT_ANSWER_FOR_WR", "ALL_CHARACTER"
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
			setState(22);
			question_wrapper();
			setState(24);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << START_OL) | (1L << LETTERLIST_PREFIX) | (1L << CORRECT_ANSWER) | (1L << CORRECT_ANSWER_FOR_WR))) != 0)) {
				{
				setState(23);
				answers();
				}
			}

			setState(26);
			trailing_content();
			setState(27);
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
		public QuestionContext question() {
			return getRuleContext(QuestionContext.class,0);
		}
		public Fib_questionContext fib_question() {
			return getRuleContext(Fib_questionContext.class,0);
		}
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
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(31);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				setState(29);
				question();
				}
				break;
			case 2:
				{
				setState(30);
				fib_question();
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
		public ContentContext content() {
			return getRuleContext(ContentContext.class,0);
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
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(33);
			content();
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

	public static class Fib_questionContext extends ParserRuleContext {
		public List<Fib_partContext> fib_part() {
			return getRuleContexts(Fib_partContext.class);
		}
		public Fib_partContext fib_part(int i) {
			return getRuleContext(Fib_partContext.class,i);
		}
		public List<ContentContext> content() {
			return getRuleContexts(ContentContext.class);
		}
		public ContentContext content(int i) {
			return getRuleContext(ContentContext.class,i);
		}
		public Fib_questionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fib_question; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof questionparserVisitor ) return ((questionparserVisitor<? extends T>)visitor).visitFib_question(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Fib_questionContext fib_question() throws RecognitionException {
		Fib_questionContext _localctx = new Fib_questionContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_fib_question);
		int _la;
		try {
			int _alt;
			setState(57);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(40);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==FIB_START) {
					{
					{
					setState(35);
					fib_part();
					setState(36);
					content();
					}
					}
					setState(42);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(48);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(43);
						content();
						setState(44);
						fib_part();
						}
						} 
					}
					setState(50);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
				}
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(54);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==FIB_START) {
					{
					{
					setState(51);
					fib_part();
					}
					}
					setState(56);
					_errHandler.sync(this);
					_la = _input.LA(1);
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
		enterRule(_localctx, 8, RULE_fib_part);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			match(FIB_START);
			setState(63);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ALL_CHARACTER) {
				{
				{
				setState(60);
				match(ALL_CHARACTER);
				}
				}
				setState(65);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(66);
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
		public Wr_answerContext wr_answer() {
			return getRuleContext(Wr_answerContext.class,0);
		}
		public TerminalNode START_OL() { return getToken(questionparserParser.START_OL, 0); }
		public TerminalNode END_OL() { return getToken(questionparserParser.END_OL, 0); }
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
		enterRule(_localctx, 10, RULE_answers);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(69);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==START_OL) {
				{
				setState(68);
				match(START_OL);
				}
			}

			setState(78);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LETTERLIST_PREFIX:
			case CORRECT_ANSWER:
				{
				setState(73); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					setState(73);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case LETTERLIST_PREFIX:
						{
						setState(71);
						answer_part();
						}
						break;
					case CORRECT_ANSWER:
						{
						setState(72);
						correct_answer_part();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					}
					setState(75); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==LETTERLIST_PREFIX || _la==CORRECT_ANSWER );
				}
				break;
			case CORRECT_ANSWER_FOR_WR:
				{
				setState(77);
				wr_answer();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(81);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==END_OL) {
				{
				setState(80);
				match(END_OL);
				}
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
		public ContentContext content() {
			return getRuleContext(ContentContext.class,0);
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
		enterRule(_localctx, 12, RULE_answer_part);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			match(LETTERLIST_PREFIX);
			setState(84);
			content();
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
		public ContentContext content() {
			return getRuleContext(ContentContext.class,0);
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
		enterRule(_localctx, 14, RULE_correct_answer_part);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(86);
			match(CORRECT_ANSWER);
			setState(87);
			content();
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

	public static class Wr_answerContext extends ParserRuleContext {
		public TerminalNode CORRECT_ANSWER_FOR_WR() { return getToken(questionparserParser.CORRECT_ANSWER_FOR_WR, 0); }
		public ContentContext content() {
			return getRuleContext(ContentContext.class,0);
		}
		public Wr_answerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_wr_answer; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof questionparserVisitor ) return ((questionparserVisitor<? extends T>)visitor).visitWr_answer(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Wr_answerContext wr_answer() throws RecognitionException {
		Wr_answerContext _localctx = new Wr_answerContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_wr_answer);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(89);
			match(CORRECT_ANSWER_FOR_WR);
			setState(90);
			content();
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

	public static class ContentContext extends ParserRuleContext {
		public List<TerminalNode> ALL_CHARACTER() { return getTokens(questionparserParser.ALL_CHARACTER); }
		public TerminalNode ALL_CHARACTER(int i) {
			return getToken(questionparserParser.ALL_CHARACTER, i);
		}
		public ContentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_content; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof questionparserVisitor ) return ((questionparserVisitor<? extends T>)visitor).visitContent(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ContentContext content() throws RecognitionException {
		ContentContext _localctx = new ContentContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_content);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(92);
					match(ALL_CHARACTER);
					}
					} 
				}
				setState(97);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
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
		enterRule(_localctx, 20, RULE_trailing_content);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(101);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ALL_CHARACTER) {
				{
				{
				setState(98);
				match(ALL_CHARACTER);
				}
				}
				setState(103);
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\nk\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4"+
		"\f\t\f\3\2\3\2\5\2\33\n\2\3\2\3\2\3\2\3\3\3\3\5\3\"\n\3\3\4\3\4\3\5\3"+
		"\5\3\5\7\5)\n\5\f\5\16\5,\13\5\3\5\3\5\3\5\7\5\61\n\5\f\5\16\5\64\13\5"+
		"\3\5\7\5\67\n\5\f\5\16\5:\13\5\5\5<\n\5\3\6\3\6\7\6@\n\6\f\6\16\6C\13"+
		"\6\3\6\3\6\3\7\5\7H\n\7\3\7\3\7\6\7L\n\7\r\7\16\7M\3\7\5\7Q\n\7\3\7\5"+
		"\7T\n\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\7\13`\n\13\f\13\16\13"+
		"c\13\13\3\f\7\ff\n\f\f\f\16\fi\13\f\3\f\2\2\r\2\4\6\b\n\f\16\20\22\24"+
		"\26\2\2\2n\2\30\3\2\2\2\4!\3\2\2\2\6#\3\2\2\2\b;\3\2\2\2\n=\3\2\2\2\f"+
		"G\3\2\2\2\16U\3\2\2\2\20X\3\2\2\2\22[\3\2\2\2\24a\3\2\2\2\26g\3\2\2\2"+
		"\30\32\5\4\3\2\31\33\5\f\7\2\32\31\3\2\2\2\32\33\3\2\2\2\33\34\3\2\2\2"+
		"\34\35\5\26\f\2\35\36\7\2\2\3\36\3\3\2\2\2\37\"\5\6\4\2 \"\5\b\5\2!\37"+
		"\3\2\2\2! \3\2\2\2\"\5\3\2\2\2#$\5\24\13\2$\7\3\2\2\2%&\5\n\6\2&\'\5\24"+
		"\13\2\')\3\2\2\2(%\3\2\2\2),\3\2\2\2*(\3\2\2\2*+\3\2\2\2+<\3\2\2\2,*\3"+
		"\2\2\2-.\5\24\13\2./\5\n\6\2/\61\3\2\2\2\60-\3\2\2\2\61\64\3\2\2\2\62"+
		"\60\3\2\2\2\62\63\3\2\2\2\63<\3\2\2\2\64\62\3\2\2\2\65\67\5\n\6\2\66\65"+
		"\3\2\2\2\67:\3\2\2\28\66\3\2\2\289\3\2\2\29<\3\2\2\2:8\3\2\2\2;*\3\2\2"+
		"\2;\62\3\2\2\2;8\3\2\2\2<\t\3\2\2\2=A\7\6\2\2>@\7\n\2\2?>\3\2\2\2@C\3"+
		"\2\2\2A?\3\2\2\2AB\3\2\2\2BD\3\2\2\2CA\3\2\2\2DE\7\7\2\2E\13\3\2\2\2F"+
		"H\7\3\2\2GF\3\2\2\2GH\3\2\2\2HP\3\2\2\2IL\5\16\b\2JL\5\20\t\2KI\3\2\2"+
		"\2KJ\3\2\2\2LM\3\2\2\2MK\3\2\2\2MN\3\2\2\2NQ\3\2\2\2OQ\5\22\n\2PK\3\2"+
		"\2\2PO\3\2\2\2QS\3\2\2\2RT\7\4\2\2SR\3\2\2\2ST\3\2\2\2T\r\3\2\2\2UV\7"+
		"\5\2\2VW\5\24\13\2W\17\3\2\2\2XY\7\b\2\2YZ\5\24\13\2Z\21\3\2\2\2[\\\7"+
		"\t\2\2\\]\5\24\13\2]\23\3\2\2\2^`\7\n\2\2_^\3\2\2\2`c\3\2\2\2a_\3\2\2"+
		"\2ab\3\2\2\2b\25\3\2\2\2ca\3\2\2\2df\7\n\2\2ed\3\2\2\2fi\3\2\2\2ge\3\2"+
		"\2\2gh\3\2\2\2h\27\3\2\2\2ig\3\2\2\2\20\32!*\628;AGKMPSag";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}