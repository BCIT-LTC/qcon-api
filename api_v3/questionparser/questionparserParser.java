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
		RULE_questionparser = 0, RULE_question_wrapper = 1, RULE_fib_question = 2, 
		RULE_question = 3, RULE_fib_part = 4, RULE_answers = 5, RULE_answer_part = 6, 
		RULE_correct_answer_part = 7, RULE_trailing_content = 8;
	private static String[] makeRuleNames() {
		return new String[] {
			"questionparser", "question_wrapper", "fib_question", "question", "fib_part", 
			"answers", "answer_part", "correct_answer_part", "trailing_content"
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
			setState(18);
			question_wrapper();
			setState(20);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << START_OL) | (1L << LETTERLIST_PREFIX) | (1L << CORRECT_ANSWER))) != 0)) {
				{
				setState(19);
				answers();
				}
			}

			setState(22);
			trailing_content();
			setState(23);
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
		public Fib_questionContext fib_question() {
			return getRuleContext(Fib_questionContext.class,0);
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
			setState(26);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==START_OL) {
				{
				setState(25);
				match(START_OL);
				}
			}

			setState(28);
			match(NUMLIST_PREFIX);
			setState(31);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
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
			setState(34);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(33);
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

	public static class Fib_questionContext extends ParserRuleContext {
		public List<Fib_partContext> fib_part() {
			return getRuleContexts(Fib_partContext.class);
		}
		public Fib_partContext fib_part(int i) {
			return getRuleContext(Fib_partContext.class,i);
		}
		public List<TerminalNode> ALL_CHARACTER() { return getTokens(questionparserParser.ALL_CHARACTER); }
		public TerminalNode ALL_CHARACTER(int i) {
			return getToken(questionparserParser.ALL_CHARACTER, i);
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
		enterRule(_localctx, 4, RULE_fib_question);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(40);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					setState(38);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case FIB_START:
						{
						setState(36);
						fib_part();
						}
						break;
					case ALL_CHARACTER:
						{
						setState(37);
						match(ALL_CHARACTER);
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					} 
				}
				setState(42);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
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
		enterRule(_localctx, 6, RULE_question);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(46);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(43);
					match(ALL_CHARACTER);
					}
					} 
				}
				setState(48);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
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
			setState(49);
			match(FIB_START);
			setState(53);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ALL_CHARACTER) {
				{
				{
				setState(50);
				match(ALL_CHARACTER);
				}
				}
				setState(55);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(56);
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
		enterRule(_localctx, 10, RULE_answers);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==START_OL) {
				{
				setState(58);
				match(START_OL);
				}
			}

			setState(63); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(63);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case LETTERLIST_PREFIX:
					{
					setState(61);
					answer_part();
					}
					break;
				case CORRECT_ANSWER:
					{
					setState(62);
					correct_answer_part();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(65); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LETTERLIST_PREFIX || _la==CORRECT_ANSWER );
			setState(68);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(67);
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
		enterRule(_localctx, 12, RULE_answer_part);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(70);
			match(LETTERLIST_PREFIX);
			setState(74);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(71);
					match(ALL_CHARACTER);
					}
					} 
				}
				setState(76);
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

	public static class Correct_answer_partContext extends ParserRuleContext {
		public TerminalNode CORRECT_ANSWER() { return getToken(questionparserParser.CORRECT_ANSWER, 0); }
		public List<TerminalNode> ALL_CHARACTER() { return getTokens(questionparserParser.ALL_CHARACTER); }
		public TerminalNode ALL_CHARACTER(int i) {
			return getToken(questionparserParser.ALL_CHARACTER, i);
		}
		public TerminalNode END_OL() { return getToken(questionparserParser.END_OL, 0); }
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
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			match(CORRECT_ANSWER);
			setState(81);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(78);
					match(ALL_CHARACTER);
					}
					} 
				}
				setState(83);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			}
			setState(85);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				{
				setState(84);
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
		enterRule(_localctx, 16, RULE_trailing_content);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==END_OL || _la==ALL_CHARACTER) {
				{
				{
				setState(87);
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
				setState(92);
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\n`\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\5\2"+
		"\27\n\2\3\2\3\2\3\2\3\3\5\3\35\n\3\3\3\3\3\3\3\5\3\"\n\3\3\3\5\3%\n\3"+
		"\3\4\3\4\7\4)\n\4\f\4\16\4,\13\4\3\5\7\5/\n\5\f\5\16\5\62\13\5\3\6\3\6"+
		"\7\6\66\n\6\f\6\16\69\13\6\3\6\3\6\3\7\5\7>\n\7\3\7\3\7\6\7B\n\7\r\7\16"+
		"\7C\3\7\5\7G\n\7\3\b\3\b\7\bK\n\b\f\b\16\bN\13\b\3\t\3\t\7\tR\n\t\f\t"+
		"\16\tU\13\t\3\t\5\tX\n\t\3\n\7\n[\n\n\f\n\16\n^\13\n\3\n\2\2\13\2\4\6"+
		"\b\n\f\16\20\22\2\3\4\2\4\4\n\n\2f\2\24\3\2\2\2\4\34\3\2\2\2\6*\3\2\2"+
		"\2\b\60\3\2\2\2\n\63\3\2\2\2\f=\3\2\2\2\16H\3\2\2\2\20O\3\2\2\2\22\\\3"+
		"\2\2\2\24\26\5\4\3\2\25\27\5\f\7\2\26\25\3\2\2\2\26\27\3\2\2\2\27\30\3"+
		"\2\2\2\30\31\5\22\n\2\31\32\7\2\2\3\32\3\3\2\2\2\33\35\7\3\2\2\34\33\3"+
		"\2\2\2\34\35\3\2\2\2\35\36\3\2\2\2\36!\7\5\2\2\37\"\5\b\5\2 \"\5\6\4\2"+
		"!\37\3\2\2\2! \3\2\2\2\"$\3\2\2\2#%\7\4\2\2$#\3\2\2\2$%\3\2\2\2%\5\3\2"+
		"\2\2&)\5\n\6\2\')\7\n\2\2(&\3\2\2\2(\'\3\2\2\2),\3\2\2\2*(\3\2\2\2*+\3"+
		"\2\2\2+\7\3\2\2\2,*\3\2\2\2-/\7\n\2\2.-\3\2\2\2/\62\3\2\2\2\60.\3\2\2"+
		"\2\60\61\3\2\2\2\61\t\3\2\2\2\62\60\3\2\2\2\63\67\7\7\2\2\64\66\7\n\2"+
		"\2\65\64\3\2\2\2\669\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28:\3\2\2\29\67\3"+
		"\2\2\2:;\7\b\2\2;\13\3\2\2\2<>\7\3\2\2=<\3\2\2\2=>\3\2\2\2>A\3\2\2\2?"+
		"B\5\16\b\2@B\5\20\t\2A?\3\2\2\2A@\3\2\2\2BC\3\2\2\2CA\3\2\2\2CD\3\2\2"+
		"\2DF\3\2\2\2EG\7\4\2\2FE\3\2\2\2FG\3\2\2\2G\r\3\2\2\2HL\7\6\2\2IK\7\n"+
		"\2\2JI\3\2\2\2KN\3\2\2\2LJ\3\2\2\2LM\3\2\2\2M\17\3\2\2\2NL\3\2\2\2OS\7"+
		"\t\2\2PR\7\n\2\2QP\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2TW\3\2\2\2US\3"+
		"\2\2\2VX\7\4\2\2WV\3\2\2\2WX\3\2\2\2X\21\3\2\2\2Y[\t\2\2\2ZY\3\2\2\2["+
		"^\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]\23\3\2\2\2^\\\3\2\2\2\22\26\34!$(*\60"+
		"\67=ACFLSW\\";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}