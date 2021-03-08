// Generated from L1.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class L1Parser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ENDOFLIST=1, NUMLIST_PREFIX=2, LETTERLIST_PREFIX=3, STAR_AFTER_DOT=4, 
		STAR_BEFORE_DOT=5, STAR_BEFORE_LETTER=6, TITLE=7, POINTS=8, TYPE=9, RANDOMIZE=10, 
		END_ANSWER=11, ALL_CHARACTER=12;
	public static final int
		RULE_l1 = 0, RULE_sectionheading = 1, RULE_rootlist = 2, RULE_numlist = 3, 
		RULE_letterlist = 4, RULE_question_header = 5, RULE_numlist_prefix = 6, 
		RULE_letterlist_prefix_regular = 7, RULE_letterlist_prefix_correct = 8, 
		RULE_endoflist = 9, RULE_question_header_parameter = 10, RULE_end_answers = 11, 
		RULE_end_answers_item = 12, RULE_title = 13, RULE_points = 14, RULE_questiontype = 15, 
		RULE_randomize = 16, RULE_content = 17;
	private static String[] makeRuleNames() {
		return new String[] {
			"l1", "sectionheading", "rootlist", "numlist", "letterlist", "question_header", 
			"numlist_prefix", "letterlist_prefix_regular", "letterlist_prefix_correct", 
			"endoflist", "question_header_parameter", "end_answers", "end_answers_item", 
			"title", "points", "questiontype", "randomize", "content"
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
			null, "ENDOFLIST", "NUMLIST_PREFIX", "LETTERLIST_PREFIX", "STAR_AFTER_DOT", 
			"STAR_BEFORE_DOT", "STAR_BEFORE_LETTER", "TITLE", "POINTS", "TYPE", "RANDOMIZE", 
			"END_ANSWER", "ALL_CHARACTER"
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
	public String getGrammarFileName() { return "L1.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public L1Parser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class L1Context extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(L1Parser.EOF, 0); }
		public SectionheadingContext sectionheading() {
			return getRuleContext(SectionheadingContext.class,0);
		}
		public List<RootlistContext> rootlist() {
			return getRuleContexts(RootlistContext.class);
		}
		public RootlistContext rootlist(int i) {
			return getRuleContext(RootlistContext.class,i);
		}
		public End_answersContext end_answers() {
			return getRuleContext(End_answersContext.class,0);
		}
		public L1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_l1; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).enterL1(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).exitL1(this);
		}
	}

	public final L1Context l1() throws RecognitionException {
		L1Context _localctx = new L1Context(_ctx, getState());
		enterRule(_localctx, 0, RULE_l1);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(37);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ALL_CHARACTER) {
				{
				setState(36);
				sectionheading();
				}
			}

			setState(42);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NUMLIST_PREFIX) | (1L << LETTERLIST_PREFIX) | (1L << STAR_AFTER_DOT) | (1L << STAR_BEFORE_DOT) | (1L << STAR_BEFORE_LETTER) | (1L << TITLE) | (1L << POINTS) | (1L << TYPE) | (1L << RANDOMIZE))) != 0)) {
				{
				{
				setState(39);
				rootlist();
				}
				}
				setState(44);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(46);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==END_ANSWER) {
				{
				setState(45);
				end_answers();
				}
			}

			setState(48);
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

	public static class SectionheadingContext extends ParserRuleContext {
		public ContentContext content() {
			return getRuleContext(ContentContext.class,0);
		}
		public SectionheadingContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sectionheading; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).enterSectionheading(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).exitSectionheading(this);
		}
	}

	public final SectionheadingContext sectionheading() throws RecognitionException {
		SectionheadingContext _localctx = new SectionheadingContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_sectionheading);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
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

	public static class RootlistContext extends ParserRuleContext {
		public NumlistContext numlist() {
			return getRuleContext(NumlistContext.class,0);
		}
		public LetterlistContext letterlist() {
			return getRuleContext(LetterlistContext.class,0);
		}
		public Question_headerContext question_header() {
			return getRuleContext(Question_headerContext.class,0);
		}
		public EndoflistContext endoflist() {
			return getRuleContext(EndoflistContext.class,0);
		}
		public RootlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rootlist; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).enterRootlist(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).exitRootlist(this);
		}
	}

	public final RootlistContext rootlist() throws RecognitionException {
		RootlistContext _localctx = new RootlistContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_rootlist);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TITLE) | (1L << POINTS) | (1L << TYPE) | (1L << RANDOMIZE))) != 0)) {
				{
				setState(52);
				question_header();
				}
			}

			setState(57);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMLIST_PREFIX:
				{
				setState(55);
				numlist();
				}
				break;
			case LETTERLIST_PREFIX:
			case STAR_AFTER_DOT:
			case STAR_BEFORE_DOT:
			case STAR_BEFORE_LETTER:
				{
				setState(56);
				letterlist();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(60);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ENDOFLIST) {
				{
				setState(59);
				endoflist();
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

	public static class NumlistContext extends ParserRuleContext {
		public Numlist_prefixContext numlist_prefix() {
			return getRuleContext(Numlist_prefixContext.class,0);
		}
		public ContentContext content() {
			return getRuleContext(ContentContext.class,0);
		}
		public NumlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_numlist; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).enterNumlist(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).exitNumlist(this);
		}
	}

	public final NumlistContext numlist() throws RecognitionException {
		NumlistContext _localctx = new NumlistContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_numlist);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(62);
			numlist_prefix();
			setState(63);
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

	public static class LetterlistContext extends ParserRuleContext {
		public ContentContext content() {
			return getRuleContext(ContentContext.class,0);
		}
		public Letterlist_prefix_regularContext letterlist_prefix_regular() {
			return getRuleContext(Letterlist_prefix_regularContext.class,0);
		}
		public Letterlist_prefix_correctContext letterlist_prefix_correct() {
			return getRuleContext(Letterlist_prefix_correctContext.class,0);
		}
		public LetterlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_letterlist; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).enterLetterlist(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).exitLetterlist(this);
		}
	}

	public final LetterlistContext letterlist() throws RecognitionException {
		LetterlistContext _localctx = new LetterlistContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_letterlist);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LETTERLIST_PREFIX:
				{
				setState(65);
				letterlist_prefix_regular();
				}
				break;
			case STAR_AFTER_DOT:
			case STAR_BEFORE_DOT:
			case STAR_BEFORE_LETTER:
				{
				setState(66);
				letterlist_prefix_correct();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(69);
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

	public static class Question_headerContext extends ParserRuleContext {
		public List<Question_header_parameterContext> question_header_parameter() {
			return getRuleContexts(Question_header_parameterContext.class);
		}
		public Question_header_parameterContext question_header_parameter(int i) {
			return getRuleContext(Question_header_parameterContext.class,i);
		}
		public Question_headerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_question_header; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).enterQuestion_header(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).exitQuestion_header(this);
		}
	}

	public final Question_headerContext question_header() throws RecognitionException {
		Question_headerContext _localctx = new Question_headerContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_question_header);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(72); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(71);
				question_header_parameter();
				}
				}
				setState(74); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TITLE) | (1L << POINTS) | (1L << TYPE) | (1L << RANDOMIZE))) != 0) );
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

	public static class Numlist_prefixContext extends ParserRuleContext {
		public TerminalNode NUMLIST_PREFIX() { return getToken(L1Parser.NUMLIST_PREFIX, 0); }
		public Numlist_prefixContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_numlist_prefix; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).enterNumlist_prefix(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).exitNumlist_prefix(this);
		}
	}

	public final Numlist_prefixContext numlist_prefix() throws RecognitionException {
		Numlist_prefixContext _localctx = new Numlist_prefixContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_numlist_prefix);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(76);
			match(NUMLIST_PREFIX);
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

	public static class Letterlist_prefix_regularContext extends ParserRuleContext {
		public TerminalNode LETTERLIST_PREFIX() { return getToken(L1Parser.LETTERLIST_PREFIX, 0); }
		public Letterlist_prefix_regularContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_letterlist_prefix_regular; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).enterLetterlist_prefix_regular(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).exitLetterlist_prefix_regular(this);
		}
	}

	public final Letterlist_prefix_regularContext letterlist_prefix_regular() throws RecognitionException {
		Letterlist_prefix_regularContext _localctx = new Letterlist_prefix_regularContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_letterlist_prefix_regular);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
			match(LETTERLIST_PREFIX);
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

	public static class Letterlist_prefix_correctContext extends ParserRuleContext {
		public TerminalNode STAR_AFTER_DOT() { return getToken(L1Parser.STAR_AFTER_DOT, 0); }
		public TerminalNode STAR_BEFORE_DOT() { return getToken(L1Parser.STAR_BEFORE_DOT, 0); }
		public TerminalNode STAR_BEFORE_LETTER() { return getToken(L1Parser.STAR_BEFORE_LETTER, 0); }
		public Letterlist_prefix_correctContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_letterlist_prefix_correct; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).enterLetterlist_prefix_correct(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).exitLetterlist_prefix_correct(this);
		}
	}

	public final Letterlist_prefix_correctContext letterlist_prefix_correct() throws RecognitionException {
		Letterlist_prefix_correctContext _localctx = new Letterlist_prefix_correctContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_letterlist_prefix_correct);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(80);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << STAR_AFTER_DOT) | (1L << STAR_BEFORE_DOT) | (1L << STAR_BEFORE_LETTER))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
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

	public static class EndoflistContext extends ParserRuleContext {
		public TerminalNode ENDOFLIST() { return getToken(L1Parser.ENDOFLIST, 0); }
		public EndoflistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_endoflist; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).enterEndoflist(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).exitEndoflist(this);
		}
	}

	public final EndoflistContext endoflist() throws RecognitionException {
		EndoflistContext _localctx = new EndoflistContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_endoflist);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			match(ENDOFLIST);
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

	public static class Question_header_parameterContext extends ParserRuleContext {
		public PointsContext points() {
			return getRuleContext(PointsContext.class,0);
		}
		public ContentContext content() {
			return getRuleContext(ContentContext.class,0);
		}
		public TitleContext title() {
			return getRuleContext(TitleContext.class,0);
		}
		public QuestiontypeContext questiontype() {
			return getRuleContext(QuestiontypeContext.class,0);
		}
		public RandomizeContext randomize() {
			return getRuleContext(RandomizeContext.class,0);
		}
		public Question_header_parameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_question_header_parameter; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).enterQuestion_header_parameter(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).exitQuestion_header_parameter(this);
		}
	}

	public final Question_header_parameterContext question_header_parameter() throws RecognitionException {
		Question_header_parameterContext _localctx = new Question_header_parameterContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_question_header_parameter);
		try {
			setState(96);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case POINTS:
				enterOuterAlt(_localctx, 1);
				{
				setState(84);
				points();
				setState(85);
				content();
				}
				break;
			case TITLE:
				enterOuterAlt(_localctx, 2);
				{
				setState(87);
				title();
				setState(88);
				content();
				}
				break;
			case TYPE:
				enterOuterAlt(_localctx, 3);
				{
				setState(90);
				questiontype();
				setState(91);
				content();
				}
				break;
			case RANDOMIZE:
				enterOuterAlt(_localctx, 4);
				{
				setState(93);
				randomize();
				setState(94);
				content();
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
		public TerminalNode END_ANSWER() { return getToken(L1Parser.END_ANSWER, 0); }
		public List<End_answers_itemContext> end_answers_item() {
			return getRuleContexts(End_answers_itemContext.class);
		}
		public End_answers_itemContext end_answers_item(int i) {
			return getRuleContext(End_answers_itemContext.class,i);
		}
		public End_answersContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_end_answers; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).enterEnd_answers(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).exitEnd_answers(this);
		}
	}

	public final End_answersContext end_answers() throws RecognitionException {
		End_answersContext _localctx = new End_answersContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_end_answers);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(98);
			match(END_ANSWER);
			setState(100); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(99);
				end_answers_item();
				}
				}
				setState(102); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==NUMLIST_PREFIX );
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

	public static class End_answers_itemContext extends ParserRuleContext {
		public NumlistContext numlist() {
			return getRuleContext(NumlistContext.class,0);
		}
		public List<ContentContext> content() {
			return getRuleContexts(ContentContext.class);
		}
		public ContentContext content(int i) {
			return getRuleContext(ContentContext.class,i);
		}
		public End_answers_itemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_end_answers_item; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).enterEnd_answers_item(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).exitEnd_answers_item(this);
		}
	}

	public final End_answers_itemContext end_answers_item() throws RecognitionException {
		End_answers_itemContext _localctx = new End_answers_itemContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_end_answers_item);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(104);
			numlist();
			setState(106); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(105);
				content();
				}
				}
				setState(108); 
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

	public static class TitleContext extends ParserRuleContext {
		public TerminalNode TITLE() { return getToken(L1Parser.TITLE, 0); }
		public TitleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_title; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).enterTitle(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).exitTitle(this);
		}
	}

	public final TitleContext title() throws RecognitionException {
		TitleContext _localctx = new TitleContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_title);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(110);
			match(TITLE);
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

	public static class PointsContext extends ParserRuleContext {
		public TerminalNode POINTS() { return getToken(L1Parser.POINTS, 0); }
		public PointsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_points; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).enterPoints(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).exitPoints(this);
		}
	}

	public final PointsContext points() throws RecognitionException {
		PointsContext _localctx = new PointsContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_points);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(112);
			match(POINTS);
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

	public static class QuestiontypeContext extends ParserRuleContext {
		public TerminalNode TYPE() { return getToken(L1Parser.TYPE, 0); }
		public QuestiontypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_questiontype; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).enterQuestiontype(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).exitQuestiontype(this);
		}
	}

	public final QuestiontypeContext questiontype() throws RecognitionException {
		QuestiontypeContext _localctx = new QuestiontypeContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_questiontype);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(114);
			match(TYPE);
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

	public static class RandomizeContext extends ParserRuleContext {
		public TerminalNode RANDOMIZE() { return getToken(L1Parser.RANDOMIZE, 0); }
		public RandomizeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_randomize; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).enterRandomize(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).exitRandomize(this);
		}
	}

	public final RandomizeContext randomize() throws RecognitionException {
		RandomizeContext _localctx = new RandomizeContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_randomize);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(116);
			match(RANDOMIZE);
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
		public List<TerminalNode> ALL_CHARACTER() { return getTokens(L1Parser.ALL_CHARACTER); }
		public TerminalNode ALL_CHARACTER(int i) {
			return getToken(L1Parser.ALL_CHARACTER, i);
		}
		public ContentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_content; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).enterContent(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof L1Listener ) ((L1Listener)listener).exitContent(this);
		}
	}

	public final ContentContext content() throws RecognitionException {
		ContentContext _localctx = new ContentContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_content);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(119); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(118);
					match(ALL_CHARACTER);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(121); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16~\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4"+
		"\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23"+
		"\t\23\3\2\5\2(\n\2\3\2\7\2+\n\2\f\2\16\2.\13\2\3\2\5\2\61\n\2\3\2\3\2"+
		"\3\3\3\3\3\4\5\48\n\4\3\4\3\4\5\4<\n\4\3\4\5\4?\n\4\3\5\3\5\3\5\3\6\3"+
		"\6\5\6F\n\6\3\6\3\6\3\7\6\7K\n\7\r\7\16\7L\3\b\3\b\3\t\3\t\3\n\3\n\3\13"+
		"\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\fc\n\f\3\r\3\r"+
		"\6\rg\n\r\r\r\16\rh\3\16\3\16\6\16m\n\16\r\16\16\16n\3\17\3\17\3\20\3"+
		"\20\3\21\3\21\3\22\3\22\3\23\6\23z\n\23\r\23\16\23{\3\23\2\2\24\2\4\6"+
		"\b\n\f\16\20\22\24\26\30\32\34\36 \"$\2\3\3\2\6\b\2y\2\'\3\2\2\2\4\64"+
		"\3\2\2\2\6\67\3\2\2\2\b@\3\2\2\2\nE\3\2\2\2\fJ\3\2\2\2\16N\3\2\2\2\20"+
		"P\3\2\2\2\22R\3\2\2\2\24T\3\2\2\2\26b\3\2\2\2\30d\3\2\2\2\32j\3\2\2\2"+
		"\34p\3\2\2\2\36r\3\2\2\2 t\3\2\2\2\"v\3\2\2\2$y\3\2\2\2&(\5\4\3\2\'&\3"+
		"\2\2\2\'(\3\2\2\2(,\3\2\2\2)+\5\6\4\2*)\3\2\2\2+.\3\2\2\2,*\3\2\2\2,-"+
		"\3\2\2\2-\60\3\2\2\2.,\3\2\2\2/\61\5\30\r\2\60/\3\2\2\2\60\61\3\2\2\2"+
		"\61\62\3\2\2\2\62\63\7\2\2\3\63\3\3\2\2\2\64\65\5$\23\2\65\5\3\2\2\2\66"+
		"8\5\f\7\2\67\66\3\2\2\2\678\3\2\2\28;\3\2\2\29<\5\b\5\2:<\5\n\6\2;9\3"+
		"\2\2\2;:\3\2\2\2<>\3\2\2\2=?\5\24\13\2>=\3\2\2\2>?\3\2\2\2?\7\3\2\2\2"+
		"@A\5\16\b\2AB\5$\23\2B\t\3\2\2\2CF\5\20\t\2DF\5\22\n\2EC\3\2\2\2ED\3\2"+
		"\2\2FG\3\2\2\2GH\5$\23\2H\13\3\2\2\2IK\5\26\f\2JI\3\2\2\2KL\3\2\2\2LJ"+
		"\3\2\2\2LM\3\2\2\2M\r\3\2\2\2NO\7\4\2\2O\17\3\2\2\2PQ\7\5\2\2Q\21\3\2"+
		"\2\2RS\t\2\2\2S\23\3\2\2\2TU\7\3\2\2U\25\3\2\2\2VW\5\36\20\2WX\5$\23\2"+
		"Xc\3\2\2\2YZ\5\34\17\2Z[\5$\23\2[c\3\2\2\2\\]\5 \21\2]^\5$\23\2^c\3\2"+
		"\2\2_`\5\"\22\2`a\5$\23\2ac\3\2\2\2bV\3\2\2\2bY\3\2\2\2b\\\3\2\2\2b_\3"+
		"\2\2\2c\27\3\2\2\2df\7\r\2\2eg\5\32\16\2fe\3\2\2\2gh\3\2\2\2hf\3\2\2\2"+
		"hi\3\2\2\2i\31\3\2\2\2jl\5\b\5\2km\5$\23\2lk\3\2\2\2mn\3\2\2\2nl\3\2\2"+
		"\2no\3\2\2\2o\33\3\2\2\2pq\7\t\2\2q\35\3\2\2\2rs\7\n\2\2s\37\3\2\2\2t"+
		"u\7\13\2\2u!\3\2\2\2vw\7\f\2\2w#\3\2\2\2xz\7\16\2\2yx\3\2\2\2z{\3\2\2"+
		"\2{y\3\2\2\2{|\3\2\2\2|%\3\2\2\2\16\',\60\67;>ELbhn{";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}