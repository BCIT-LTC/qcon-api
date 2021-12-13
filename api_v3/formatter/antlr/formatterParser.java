// Generated from /Users/viresh/Documents/qcon_sept_2021/qcon-api/api_v3/formatter/formatter.g4 by ANTLR 4.8
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
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		NUMLIST_PREFIX=1, TITLE=2, POINTS=3, TYPE=4, RANDOMIZE=5, END_ANSWER=6, 
		SECTION=7, ALL_CHARACTER=8;
	public static final int
		RULE_formatter = 0, RULE_rootheading = 1, RULE_rootbody = 2, RULE_section = 3, 
		RULE_end_answers_block = 4;
	private static String[] makeRuleNames() {
		return new String[] {
			"formatter", "rootheading", "rootbody", "section", "end_answers_block"
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
			null, "NUMLIST_PREFIX", "TITLE", "POINTS", "TYPE", "RANDOMIZE", "END_ANSWER", 
			"SECTION", "ALL_CHARACTER"
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
		public RootbodyContext rootbody() {
			return getRuleContext(RootbodyContext.class,0);
		}
		public TerminalNode EOF() { return getToken(formatterParser.EOF, 0); }
		public RootheadingContext rootheading() {
			return getRuleContext(RootheadingContext.class,0);
		}
		public End_answers_blockContext end_answers_block() {
			return getRuleContext(End_answers_blockContext.class,0);
		}
		public FormatterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formatter; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof formatterListener ) ((formatterListener)listener).enterFormatter(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof formatterListener ) ((formatterListener)listener).exitFormatter(this);
		}
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
			setState(11);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				{
				setState(10);
				rootheading();
				}
				break;
			}
			setState(13);
			rootbody();
			setState(15);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==END_ANSWER) {
				{
				setState(14);
				end_answers_block();
				}
			}

			setState(17);
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

	public static class RootheadingContext extends ParserRuleContext {
		public List<TerminalNode> ALL_CHARACTER() { return getTokens(formatterParser.ALL_CHARACTER); }
		public TerminalNode ALL_CHARACTER(int i) {
			return getToken(formatterParser.ALL_CHARACTER, i);
		}
		public RootheadingContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rootheading; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof formatterListener ) ((formatterListener)listener).enterRootheading(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof formatterListener ) ((formatterListener)listener).exitRootheading(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof formatterVisitor ) return ((formatterVisitor<? extends T>)visitor).visitRootheading(this);
			else return visitor.visitChildren(this);
		}
	}

	public final RootheadingContext rootheading() throws RecognitionException {
		RootheadingContext _localctx = new RootheadingContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_rootheading);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(20); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(19);
					match(ALL_CHARACTER);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(22); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
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

	public static class RootbodyContext extends ParserRuleContext {
		public List<SectionContext> section() {
			return getRuleContexts(SectionContext.class);
		}
		public SectionContext section(int i) {
			return getRuleContext(SectionContext.class,i);
		}
		public RootbodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rootbody; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof formatterListener ) ((formatterListener)listener).enterRootbody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof formatterListener ) ((formatterListener)listener).exitRootbody(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof formatterVisitor ) return ((formatterVisitor<? extends T>)visitor).visitRootbody(this);
			else return visitor.visitChildren(this);
		}
	}

	public final RootbodyContext rootbody() throws RecognitionException {
		RootbodyContext _localctx = new RootbodyContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_rootbody);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(25); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(24);
				section();
				}
				}
				setState(27); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NUMLIST_PREFIX) | (1L << TITLE) | (1L << POINTS) | (1L << TYPE) | (1L << RANDOMIZE) | (1L << SECTION) | (1L << ALL_CHARACTER))) != 0) );
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

	public static class SectionContext extends ParserRuleContext {
		public TerminalNode SECTION() { return getToken(formatterParser.SECTION, 0); }
		public List<TerminalNode> NUMLIST_PREFIX() { return getTokens(formatterParser.NUMLIST_PREFIX); }
		public TerminalNode NUMLIST_PREFIX(int i) {
			return getToken(formatterParser.NUMLIST_PREFIX, i);
		}
		public List<TerminalNode> ALL_CHARACTER() { return getTokens(formatterParser.ALL_CHARACTER); }
		public TerminalNode ALL_CHARACTER(int i) {
			return getToken(formatterParser.ALL_CHARACTER, i);
		}
		public List<TerminalNode> POINTS() { return getTokens(formatterParser.POINTS); }
		public TerminalNode POINTS(int i) {
			return getToken(formatterParser.POINTS, i);
		}
		public List<TerminalNode> TITLE() { return getTokens(formatterParser.TITLE); }
		public TerminalNode TITLE(int i) {
			return getToken(formatterParser.TITLE, i);
		}
		public List<TerminalNode> TYPE() { return getTokens(formatterParser.TYPE); }
		public TerminalNode TYPE(int i) {
			return getToken(formatterParser.TYPE, i);
		}
		public List<TerminalNode> RANDOMIZE() { return getTokens(formatterParser.RANDOMIZE); }
		public TerminalNode RANDOMIZE(int i) {
			return getToken(formatterParser.RANDOMIZE, i);
		}
		public SectionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_section; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof formatterListener ) ((formatterListener)listener).enterSection(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof formatterListener ) ((formatterListener)listener).exitSection(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof formatterVisitor ) return ((formatterVisitor<? extends T>)visitor).visitSection(this);
			else return visitor.visitChildren(this);
		}
	}

	public final SectionContext section() throws RecognitionException {
		SectionContext _localctx = new SectionContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_section);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(30);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SECTION) {
				{
				setState(29);
				match(SECTION);
				}
			}

			setState(37);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ALL_CHARACTER) {
				{
				setState(33); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(32);
					match(ALL_CHARACTER);
					}
					}
					setState(35); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==ALL_CHARACTER );
				}
			}

			{
			setState(75); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(67);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TITLE) | (1L << POINTS) | (1L << TYPE) | (1L << RANDOMIZE))) != 0)) {
						{
						setState(63); 
						_errHandler.sync(this);
						_la = _input.LA(1);
						do {
							{
							setState(63);
							_errHandler.sync(this);
							switch (_input.LA(1)) {
							case POINTS:
								{
								setState(39);
								match(POINTS);
								{
								setState(41); 
								_errHandler.sync(this);
								_la = _input.LA(1);
								do {
									{
									{
									setState(40);
									match(ALL_CHARACTER);
									}
									}
									setState(43); 
									_errHandler.sync(this);
									_la = _input.LA(1);
								} while ( _la==ALL_CHARACTER );
								}
								}
								break;
							case TITLE:
								{
								setState(45);
								match(TITLE);
								{
								setState(47); 
								_errHandler.sync(this);
								_la = _input.LA(1);
								do {
									{
									{
									setState(46);
									match(ALL_CHARACTER);
									}
									}
									setState(49); 
									_errHandler.sync(this);
									_la = _input.LA(1);
								} while ( _la==ALL_CHARACTER );
								}
								}
								break;
							case TYPE:
								{
								setState(51);
								match(TYPE);
								{
								setState(53); 
								_errHandler.sync(this);
								_la = _input.LA(1);
								do {
									{
									{
									setState(52);
									match(ALL_CHARACTER);
									}
									}
									setState(55); 
									_errHandler.sync(this);
									_la = _input.LA(1);
								} while ( _la==ALL_CHARACTER );
								}
								}
								break;
							case RANDOMIZE:
								{
								setState(57);
								match(RANDOMIZE);
								{
								setState(59); 
								_errHandler.sync(this);
								_la = _input.LA(1);
								do {
									{
									{
									setState(58);
									match(ALL_CHARACTER);
									}
									}
									setState(61); 
									_errHandler.sync(this);
									_la = _input.LA(1);
								} while ( _la==ALL_CHARACTER );
								}
								}
								break;
							default:
								throw new NoViableAltException(this);
							}
							}
							setState(65); 
							_errHandler.sync(this);
							_la = _input.LA(1);
						} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TITLE) | (1L << POINTS) | (1L << TYPE) | (1L << RANDOMIZE))) != 0) );
						}
					}

					setState(69);
					match(NUMLIST_PREFIX);
					{
					setState(71); 
					_errHandler.sync(this);
					_alt = 1;
					do {
						switch (_alt) {
						case 1:
							{
							{
							setState(70);
							match(ALL_CHARACTER);
							}
							}
							break;
						default:
							throw new NoViableAltException(this);
						}
						setState(73); 
						_errHandler.sync(this);
						_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
					} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
					}
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(77); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
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

	public static class End_answers_blockContext extends ParserRuleContext {
		public TerminalNode END_ANSWER() { return getToken(formatterParser.END_ANSWER, 0); }
		public List<TerminalNode> NUMLIST_PREFIX() { return getTokens(formatterParser.NUMLIST_PREFIX); }
		public TerminalNode NUMLIST_PREFIX(int i) {
			return getToken(formatterParser.NUMLIST_PREFIX, i);
		}
		public List<TerminalNode> ALL_CHARACTER() { return getTokens(formatterParser.ALL_CHARACTER); }
		public TerminalNode ALL_CHARACTER(int i) {
			return getToken(formatterParser.ALL_CHARACTER, i);
		}
		public End_answers_blockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_end_answers_block; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof formatterListener ) ((formatterListener)listener).enterEnd_answers_block(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof formatterListener ) ((formatterListener)listener).exitEnd_answers_block(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof formatterVisitor ) return ((formatterVisitor<? extends T>)visitor).visitEnd_answers_block(this);
			else return visitor.visitChildren(this);
		}
	}

	public final End_answers_blockContext end_answers_block() throws RecognitionException {
		End_answers_blockContext _localctx = new End_answers_blockContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_end_answers_block);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(79);
			match(END_ANSWER);
			setState(93); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(85);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ALL_CHARACTER) {
					{
					setState(81); 
					_errHandler.sync(this);
					_la = _input.LA(1);
					do {
						{
						{
						setState(80);
						match(ALL_CHARACTER);
						}
						}
						setState(83); 
						_errHandler.sync(this);
						_la = _input.LA(1);
					} while ( _la==ALL_CHARACTER );
					}
				}

				setState(87);
				match(NUMLIST_PREFIX);
				{
				setState(89); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(88);
						match(ALL_CHARACTER);
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(91); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				}
				}
				}
				setState(95); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==NUMLIST_PREFIX || _la==ALL_CHARACTER );
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\nd\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\5\2\16\n\2\3\2\3\2\5\2\22\n\2\3\2\3\2\3"+
		"\3\6\3\27\n\3\r\3\16\3\30\3\4\6\4\34\n\4\r\4\16\4\35\3\5\5\5!\n\5\3\5"+
		"\6\5$\n\5\r\5\16\5%\5\5(\n\5\3\5\3\5\6\5,\n\5\r\5\16\5-\3\5\3\5\6\5\62"+
		"\n\5\r\5\16\5\63\3\5\3\5\6\58\n\5\r\5\16\59\3\5\3\5\6\5>\n\5\r\5\16\5"+
		"?\6\5B\n\5\r\5\16\5C\5\5F\n\5\3\5\3\5\6\5J\n\5\r\5\16\5K\6\5N\n\5\r\5"+
		"\16\5O\3\6\3\6\6\6T\n\6\r\6\16\6U\5\6X\n\6\3\6\3\6\6\6\\\n\6\r\6\16\6"+
		"]\6\6`\n\6\r\6\16\6a\3\6\2\2\7\2\4\6\b\n\2\2\2t\2\r\3\2\2\2\4\26\3\2\2"+
		"\2\6\33\3\2\2\2\b \3\2\2\2\nQ\3\2\2\2\f\16\5\4\3\2\r\f\3\2\2\2\r\16\3"+
		"\2\2\2\16\17\3\2\2\2\17\21\5\6\4\2\20\22\5\n\6\2\21\20\3\2\2\2\21\22\3"+
		"\2\2\2\22\23\3\2\2\2\23\24\7\2\2\3\24\3\3\2\2\2\25\27\7\n\2\2\26\25\3"+
		"\2\2\2\27\30\3\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2\31\5\3\2\2\2\32\34\5"+
		"\b\5\2\33\32\3\2\2\2\34\35\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36\7\3"+
		"\2\2\2\37!\7\t\2\2 \37\3\2\2\2 !\3\2\2\2!\'\3\2\2\2\"$\7\n\2\2#\"\3\2"+
		"\2\2$%\3\2\2\2%#\3\2\2\2%&\3\2\2\2&(\3\2\2\2\'#\3\2\2\2\'(\3\2\2\2(M\3"+
		"\2\2\2)+\7\5\2\2*,\7\n\2\2+*\3\2\2\2,-\3\2\2\2-+\3\2\2\2-.\3\2\2\2.B\3"+
		"\2\2\2/\61\7\4\2\2\60\62\7\n\2\2\61\60\3\2\2\2\62\63\3\2\2\2\63\61\3\2"+
		"\2\2\63\64\3\2\2\2\64B\3\2\2\2\65\67\7\6\2\2\668\7\n\2\2\67\66\3\2\2\2"+
		"89\3\2\2\29\67\3\2\2\29:\3\2\2\2:B\3\2\2\2;=\7\7\2\2<>\7\n\2\2=<\3\2\2"+
		"\2>?\3\2\2\2?=\3\2\2\2?@\3\2\2\2@B\3\2\2\2A)\3\2\2\2A/\3\2\2\2A\65\3\2"+
		"\2\2A;\3\2\2\2BC\3\2\2\2CA\3\2\2\2CD\3\2\2\2DF\3\2\2\2EA\3\2\2\2EF\3\2"+
		"\2\2FG\3\2\2\2GI\7\3\2\2HJ\7\n\2\2IH\3\2\2\2JK\3\2\2\2KI\3\2\2\2KL\3\2"+
		"\2\2LN\3\2\2\2ME\3\2\2\2NO\3\2\2\2OM\3\2\2\2OP\3\2\2\2P\t\3\2\2\2Q_\7"+
		"\b\2\2RT\7\n\2\2SR\3\2\2\2TU\3\2\2\2US\3\2\2\2UV\3\2\2\2VX\3\2\2\2WS\3"+
		"\2\2\2WX\3\2\2\2XY\3\2\2\2Y[\7\3\2\2Z\\\7\n\2\2[Z\3\2\2\2\\]\3\2\2\2]"+
		"[\3\2\2\2]^\3\2\2\2^`\3\2\2\2_W\3\2\2\2`a\3\2\2\2a_\3\2\2\2ab\3\2\2\2"+
		"b\13\3\2\2\2\26\r\21\30\35 %\'-\639?ACEKOUW]a";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}