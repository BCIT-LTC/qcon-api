// Generated from formatter.g4 by ANTLR 4.9.3
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class formatterParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.3", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		HEADING_1=1, HEADING_2=2, START_NUMBER_ONE=3, END_ANSWER_BLOCK=4, TITLE=5, 
		POINTS=6, TYPE=7, RANDOMIZE=8, ALL_CHARACTER=9;
	public static final int
		RULE_formatter = 0, RULE_unused_content = 1, RULE_sectioninfo = 2, RULE_body = 3, 
		RULE_question_header_parameter = 4, RULE_end_answers = 5;
	private static String[] makeRuleNames() {
		return new String[] {
			"formatter", "unused_content", "sectioninfo", "body", "question_header_parameter", 
			"end_answers"
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
			null, "HEADING_1", "HEADING_2", "START_NUMBER_ONE", "END_ANSWER_BLOCK", 
			"TITLE", "POINTS", "TYPE", "RANDOMIZE", "ALL_CHARACTER"
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
	public String getGrammarFileName() { return "formatter.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public formatterParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class FormatterContext extends ParserRuleContext {
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public TerminalNode EOF() { return getToken(formatterParser.EOF, 0); }
		public Unused_contentContext unused_content() {
			return getRuleContext(Unused_contentContext.class,0);
		}
		public SectioninfoContext sectioninfo() {
			return getRuleContext(SectioninfoContext.class,0);
		}
		public End_answersContext end_answers() {
			return getRuleContext(End_answersContext.class,0);
		}
		public FormatterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formatter; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof formatterVisitor ) return ((formatterVisitor<? extends T>)visitor).visitFormatter(this);
			else return visitor.visitChildren(this);
		}
	}

	public final FormatterContext formatter() throws RecognitionException {
		FormatterContext _localctx = new FormatterContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_formatter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(13);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ALL_CHARACTER) {
				{
				setState(12);
				unused_content();
				}
			}

			setState(16);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				setState(15);
				sectioninfo(0);
				}
				break;
			}
			setState(18);
			body(0);
			setState(20);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==END_ANSWER_BLOCK) {
				{
				setState(19);
				end_answers();
				}
			}

			setState(22);
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

	public static class Unused_contentContext extends ParserRuleContext {
		public List<TerminalNode> ALL_CHARACTER() { return getTokens(formatterParser.ALL_CHARACTER); }
		public TerminalNode ALL_CHARACTER(int i) {
			return getToken(formatterParser.ALL_CHARACTER, i);
		}
		public Unused_contentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unused_content; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof formatterVisitor ) return ((formatterVisitor<? extends T>)visitor).visitUnused_content(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Unused_contentContext unused_content() throws RecognitionException {
		Unused_contentContext _localctx = new Unused_contentContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_unused_content);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(25); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(24);
				match(ALL_CHARACTER);
				}
				}
				setState(27); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ALL_CHARACTER );
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

	public static class SectioninfoContext extends ParserRuleContext {
		public TerminalNode HEADING_1() { return getToken(formatterParser.HEADING_1, 0); }
		public TerminalNode HEADING_2() { return getToken(formatterParser.HEADING_2, 0); }
		public List<TerminalNode> ALL_CHARACTER() { return getTokens(formatterParser.ALL_CHARACTER); }
		public TerminalNode ALL_CHARACTER(int i) {
			return getToken(formatterParser.ALL_CHARACTER, i);
		}
		public SectioninfoContext sectioninfo() {
			return getRuleContext(SectioninfoContext.class,0);
		}
		public SectioninfoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sectioninfo; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof formatterVisitor ) return ((formatterVisitor<? extends T>)visitor).visitSectioninfo(this);
			else return visitor.visitChildren(this);
		}
	}

	public final SectioninfoContext sectioninfo() throws RecognitionException {
		return sectioninfo(0);
	}

	private SectioninfoContext sectioninfo(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		SectioninfoContext _localctx = new SectioninfoContext(_ctx, _parentState);
		SectioninfoContext _prevctx = _localctx;
		int _startState = 4;
		enterRecursionRule(_localctx, 4, RULE_sectioninfo, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(30);
			_la = _input.LA(1);
			if ( !(_la==HEADING_1 || _la==HEADING_2) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			{
			setState(32); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(31);
					match(ALL_CHARACTER);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(34); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
			}
			_ctx.stop = _input.LT(-1);
			setState(45);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new SectioninfoContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_sectioninfo);
					setState(36);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(37);
					_la = _input.LA(1);
					if ( !(_la==HEADING_1 || _la==HEADING_2) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					{
					setState(39); 
					_errHandler.sync(this);
					_alt = 1;
					do {
						switch (_alt) {
						case 1:
							{
							{
							setState(38);
							match(ALL_CHARACTER);
							}
							}
							break;
						default:
							throw new NoViableAltException(this);
						}
						setState(41); 
						_errHandler.sync(this);
						_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
					} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
					}
					}
					} 
				}
				setState(47);
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
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class BodyContext extends ParserRuleContext {
		public TerminalNode START_NUMBER_ONE() { return getToken(formatterParser.START_NUMBER_ONE, 0); }
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public List<Question_header_parameterContext> question_header_parameter() {
			return getRuleContexts(Question_header_parameterContext.class);
		}
		public Question_header_parameterContext question_header_parameter(int i) {
			return getRuleContext(Question_header_parameterContext.class,i);
		}
		public List<TerminalNode> ALL_CHARACTER() { return getTokens(formatterParser.ALL_CHARACTER); }
		public TerminalNode ALL_CHARACTER(int i) {
			return getToken(formatterParser.ALL_CHARACTER, i);
		}
		public TerminalNode HEADING_1() { return getToken(formatterParser.HEADING_1, 0); }
		public TerminalNode HEADING_2() { return getToken(formatterParser.HEADING_2, 0); }
		public BodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_body; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof formatterVisitor ) return ((formatterVisitor<? extends T>)visitor).visitBody(this);
			else return visitor.visitChildren(this);
		}
	}

	public final BodyContext body() throws RecognitionException {
		return body(0);
	}

	private BodyContext body(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		BodyContext _localctx = new BodyContext(_ctx, _parentState);
		BodyContext _prevctx = _localctx;
		int _startState = 6;
		enterRecursionRule(_localctx, 6, RULE_body, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				{
				setState(52);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TITLE) | (1L << POINTS) | (1L << TYPE) | (1L << RANDOMIZE))) != 0)) {
					{
					{
					setState(49);
					question_header_parameter();
					}
					}
					setState(54);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(55);
				match(START_NUMBER_ONE);
				{
				setState(57); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(56);
					match(ALL_CHARACTER);
					}
					}
					setState(59); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==ALL_CHARACTER );
				setState(64);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(61);
						question_header_parameter();
						}
						} 
					}
					setState(66);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
				}
				}
				setState(67);
				body(3);
				}
				break;
			case 2:
				{
				setState(71);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TITLE) | (1L << POINTS) | (1L << TYPE) | (1L << RANDOMIZE))) != 0)) {
					{
					{
					setState(68);
					question_header_parameter();
					}
					}
					setState(73);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(74);
				match(START_NUMBER_ONE);
				{
				setState(76); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(75);
						match(ALL_CHARACTER);
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(78); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				setState(83);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(80);
						question_header_parameter();
						}
						} 
					}
					setState(85);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
				}
				}
				}
				break;
			case 3:
				{
				setState(86);
				_la = _input.LA(1);
				if ( !(_la==HEADING_1 || _la==HEADING_2) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				{
				setState(88); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(87);
					match(ALL_CHARACTER);
					}
					}
					setState(90); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==ALL_CHARACTER );
				setState(95);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(92);
						question_header_parameter();
						}
						} 
					}
					setState(97);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
				}
				}
				setState(98);
				body(1);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(124);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new BodyContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_body);
					setState(101);
					if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
					setState(105);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TITLE) | (1L << POINTS) | (1L << TYPE) | (1L << RANDOMIZE))) != 0)) {
						{
						{
						setState(102);
						question_header_parameter();
						}
						}
						setState(107);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					setState(108);
					match(START_NUMBER_ONE);
					setState(120);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
					case 1:
						{
						setState(110); 
						_errHandler.sync(this);
						_alt = 1;
						do {
							switch (_alt) {
							case 1:
								{
								{
								setState(109);
								match(ALL_CHARACTER);
								}
								}
								break;
							default:
								throw new NoViableAltException(this);
							}
							setState(112); 
							_errHandler.sync(this);
							_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
						} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
						}
						break;
					case 2:
						{
						setState(117);
						_errHandler.sync(this);
						_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
						while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
							if ( _alt==1 ) {
								{
								{
								setState(114);
								question_header_parameter();
								}
								} 
							}
							setState(119);
							_errHandler.sync(this);
							_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
						}
						}
						break;
					}
					}
					} 
				}
				setState(126);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Question_header_parameterContext extends ParserRuleContext {
		public TerminalNode TITLE() { return getToken(formatterParser.TITLE, 0); }
		public List<TerminalNode> ALL_CHARACTER() { return getTokens(formatterParser.ALL_CHARACTER); }
		public TerminalNode ALL_CHARACTER(int i) {
			return getToken(formatterParser.ALL_CHARACTER, i);
		}
		public TerminalNode POINTS() { return getToken(formatterParser.POINTS, 0); }
		public TerminalNode TYPE() { return getToken(formatterParser.TYPE, 0); }
		public TerminalNode RANDOMIZE() { return getToken(formatterParser.RANDOMIZE, 0); }
		public Question_header_parameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_question_header_parameter; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof formatterVisitor ) return ((formatterVisitor<? extends T>)visitor).visitQuestion_header_parameter(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Question_header_parameterContext question_header_parameter() throws RecognitionException {
		Question_header_parameterContext _localctx = new Question_header_parameterContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_question_header_parameter);
		try {
			int _alt;
			setState(151);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TITLE:
				enterOuterAlt(_localctx, 1);
				{
				setState(127);
				match(TITLE);
				setState(129); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(128);
						match(ALL_CHARACTER);
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(131); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				}
				break;
			case POINTS:
				enterOuterAlt(_localctx, 2);
				{
				setState(133);
				match(POINTS);
				setState(135); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(134);
						match(ALL_CHARACTER);
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(137); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				}
				break;
			case TYPE:
				enterOuterAlt(_localctx, 3);
				{
				setState(139);
				match(TYPE);
				setState(141); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(140);
						match(ALL_CHARACTER);
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(143); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				}
				break;
			case RANDOMIZE:
				enterOuterAlt(_localctx, 4);
				{
				setState(145);
				match(RANDOMIZE);
				setState(147); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(146);
						match(ALL_CHARACTER);
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(149); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class End_answersContext extends ParserRuleContext {
		public TerminalNode END_ANSWER_BLOCK() { return getToken(formatterParser.END_ANSWER_BLOCK, 0); }
		public TerminalNode START_NUMBER_ONE() { return getToken(formatterParser.START_NUMBER_ONE, 0); }
		public List<TerminalNode> ALL_CHARACTER() { return getTokens(formatterParser.ALL_CHARACTER); }
		public TerminalNode ALL_CHARACTER(int i) {
			return getToken(formatterParser.ALL_CHARACTER, i);
		}
		public End_answersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_end_answers; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof formatterVisitor ) return ((formatterVisitor<? extends T>)visitor).visitEnd_answers(this);
			else return visitor.visitChildren(this);
		}
	}

	public final End_answersContext end_answers() throws RecognitionException {
		End_answersContext _localctx = new End_answersContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_end_answers);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(153);
			match(END_ANSWER_BLOCK);
			setState(155); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(154);
				match(ALL_CHARACTER);
				}
				}
				setState(157); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ALL_CHARACTER );
			setState(159);
			match(START_NUMBER_ONE);
			setState(161); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(160);
				match(ALL_CHARACTER);
				}
				}
				setState(163); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ALL_CHARACTER );
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 2:
			return sectioninfo_sempred((SectioninfoContext)_localctx, predIndex);
		case 3:
			return body_sempred((BodyContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean sectioninfo_sempred(SectioninfoContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean body_sempred(BodyContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 4);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13\u00a8\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2\5\2\20\n\2\3\2\5\2\23\n\2"+
		"\3\2\3\2\5\2\27\n\2\3\2\3\2\3\3\6\3\34\n\3\r\3\16\3\35\3\4\3\4\3\4\6\4"+
		"#\n\4\r\4\16\4$\3\4\3\4\3\4\6\4*\n\4\r\4\16\4+\7\4.\n\4\f\4\16\4\61\13"+
		"\4\3\5\3\5\7\5\65\n\5\f\5\16\58\13\5\3\5\3\5\6\5<\n\5\r\5\16\5=\3\5\7"+
		"\5A\n\5\f\5\16\5D\13\5\3\5\3\5\7\5H\n\5\f\5\16\5K\13\5\3\5\3\5\6\5O\n"+
		"\5\r\5\16\5P\3\5\7\5T\n\5\f\5\16\5W\13\5\3\5\3\5\6\5[\n\5\r\5\16\5\\\3"+
		"\5\7\5`\n\5\f\5\16\5c\13\5\3\5\5\5f\n\5\3\5\3\5\7\5j\n\5\f\5\16\5m\13"+
		"\5\3\5\3\5\6\5q\n\5\r\5\16\5r\3\5\7\5v\n\5\f\5\16\5y\13\5\5\5{\n\5\7\5"+
		"}\n\5\f\5\16\5\u0080\13\5\3\6\3\6\6\6\u0084\n\6\r\6\16\6\u0085\3\6\3\6"+
		"\6\6\u008a\n\6\r\6\16\6\u008b\3\6\3\6\6\6\u0090\n\6\r\6\16\6\u0091\3\6"+
		"\3\6\6\6\u0096\n\6\r\6\16\6\u0097\5\6\u009a\n\6\3\7\3\7\6\7\u009e\n\7"+
		"\r\7\16\7\u009f\3\7\3\7\6\7\u00a4\n\7\r\7\16\7\u00a5\3\7\2\4\6\b\b\2\4"+
		"\6\b\n\f\2\3\3\2\3\4\2\u00c0\2\17\3\2\2\2\4\33\3\2\2\2\6\37\3\2\2\2\b"+
		"e\3\2\2\2\n\u0099\3\2\2\2\f\u009b\3\2\2\2\16\20\5\4\3\2\17\16\3\2\2\2"+
		"\17\20\3\2\2\2\20\22\3\2\2\2\21\23\5\6\4\2\22\21\3\2\2\2\22\23\3\2\2\2"+
		"\23\24\3\2\2\2\24\26\5\b\5\2\25\27\5\f\7\2\26\25\3\2\2\2\26\27\3\2\2\2"+
		"\27\30\3\2\2\2\30\31\7\2\2\3\31\3\3\2\2\2\32\34\7\13\2\2\33\32\3\2\2\2"+
		"\34\35\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36\5\3\2\2\2\37 \b\4\1\2 \""+
		"\t\2\2\2!#\7\13\2\2\"!\3\2\2\2#$\3\2\2\2$\"\3\2\2\2$%\3\2\2\2%/\3\2\2"+
		"\2&\'\f\4\2\2\')\t\2\2\2(*\7\13\2\2)(\3\2\2\2*+\3\2\2\2+)\3\2\2\2+,\3"+
		"\2\2\2,.\3\2\2\2-&\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\7\3\2"+
		"\2\2\61/\3\2\2\2\62\66\b\5\1\2\63\65\5\n\6\2\64\63\3\2\2\2\658\3\2\2\2"+
		"\66\64\3\2\2\2\66\67\3\2\2\2\679\3\2\2\28\66\3\2\2\29;\7\5\2\2:<\7\13"+
		"\2\2;:\3\2\2\2<=\3\2\2\2=;\3\2\2\2=>\3\2\2\2>B\3\2\2\2?A\5\n\6\2@?\3\2"+
		"\2\2AD\3\2\2\2B@\3\2\2\2BC\3\2\2\2CE\3\2\2\2DB\3\2\2\2Ef\5\b\5\5FH\5\n"+
		"\6\2GF\3\2\2\2HK\3\2\2\2IG\3\2\2\2IJ\3\2\2\2JL\3\2\2\2KI\3\2\2\2LN\7\5"+
		"\2\2MO\7\13\2\2NM\3\2\2\2OP\3\2\2\2PN\3\2\2\2PQ\3\2\2\2QU\3\2\2\2RT\5"+
		"\n\6\2SR\3\2\2\2TW\3\2\2\2US\3\2\2\2UV\3\2\2\2Vf\3\2\2\2WU\3\2\2\2XZ\t"+
		"\2\2\2Y[\7\13\2\2ZY\3\2\2\2[\\\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]a\3\2\2\2"+
		"^`\5\n\6\2_^\3\2\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2bd\3\2\2\2ca\3\2\2\2"+
		"df\5\b\5\3e\62\3\2\2\2eI\3\2\2\2eX\3\2\2\2f~\3\2\2\2gk\f\6\2\2hj\5\n\6"+
		"\2ih\3\2\2\2jm\3\2\2\2ki\3\2\2\2kl\3\2\2\2ln\3\2\2\2mk\3\2\2\2nz\7\5\2"+
		"\2oq\7\13\2\2po\3\2\2\2qr\3\2\2\2rp\3\2\2\2rs\3\2\2\2s{\3\2\2\2tv\5\n"+
		"\6\2ut\3\2\2\2vy\3\2\2\2wu\3\2\2\2wx\3\2\2\2x{\3\2\2\2yw\3\2\2\2zp\3\2"+
		"\2\2zw\3\2\2\2{}\3\2\2\2|g\3\2\2\2}\u0080\3\2\2\2~|\3\2\2\2~\177\3\2\2"+
		"\2\177\t\3\2\2\2\u0080~\3\2\2\2\u0081\u0083\7\7\2\2\u0082\u0084\7\13\2"+
		"\2\u0083\u0082\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0083\3\2\2\2\u0085\u0086"+
		"\3\2\2\2\u0086\u009a\3\2\2\2\u0087\u0089\7\b\2\2\u0088\u008a\7\13\2\2"+
		"\u0089\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c"+
		"\3\2\2\2\u008c\u009a\3\2\2\2\u008d\u008f\7\t\2\2\u008e\u0090\7\13\2\2"+
		"\u008f\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0092"+
		"\3\2\2\2\u0092\u009a\3\2\2\2\u0093\u0095\7\n\2\2\u0094\u0096\7\13\2\2"+
		"\u0095\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0098"+
		"\3\2\2\2\u0098\u009a\3\2\2\2\u0099\u0081\3\2\2\2\u0099\u0087\3\2\2\2\u0099"+
		"\u008d\3\2\2\2\u0099\u0093\3\2\2\2\u009a\13\3\2\2\2\u009b\u009d\7\6\2"+
		"\2\u009c\u009e\7\13\2\2\u009d\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f"+
		"\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a3\7\5"+
		"\2\2\u00a2\u00a4\7\13\2\2\u00a3\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5"+
		"\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\r\3\2\2\2\36\17\22\26\35$+/\66"+
		"=BIPU\\aekrwz~\u0085\u008b\u0091\u0097\u0099\u009f\u00a5";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}