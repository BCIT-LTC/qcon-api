// Generated from /Users/viresh/Documents/qcon_sept_2021/qcon-api/api_v3/splitter/splitter.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class splitterLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		NUMLIST_PREFIX=1, END_ANSWER=2, ALL_CHARACTER=3;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"DIGIT", "NEWLINE", "CLOSING_PARENTHESIS", "LETTER", "NUMBER", "BACKSLASH", 
			"ASTERISK", "DOUBLE_ASTERISK", "DOT", "WHITESPACE", "DELIMITER", "ANSWER_MARKER", 
			"GREATER_THAN", "COLON", "A", "B", "C", "D", "E", "F", "I", "K", "L", 
			"M", "N", "O", "P", "R", "S", "T", "U", "W", "Y", "Z", "NUMLIST_PREFIX", 
			"END_ANSWER", "ALL_CHARACTER"
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
			null, "NUMLIST_PREFIX", "END_ANSWER", "ALL_CHARACTER"
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


	public splitterLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "splitter.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\5\u00f6\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\3\2\3\2\3\3\5\3Q\n\3\3\3\3\3\5\3U"+
		"\n\3\3\4\3\4\3\5\3\5\3\6\6\6\\\n\6\r\6\16\6]\3\6\6\6a\n\6\r\6\16\6b\5"+
		"\6e\n\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\5\fs\n\f\3\f"+
		"\3\f\5\fw\n\f\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22"+
		"\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31"+
		"\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3"+
		" \3!\3!\3\"\3\"\3#\3#\3$\3$\7$\u00aa\n$\f$\16$\u00ad\13$\3$\5$\u00b0\n"+
		"$\3$\7$\u00b3\n$\f$\16$\u00b6\13$\3$\5$\u00b9\n$\3$\3$\7$\u00bd\n$\f$"+
		"\16$\u00c0\13$\3$\7$\u00c3\n$\f$\16$\u00c6\13$\3$\3$\7$\u00ca\n$\f$\16"+
		"$\u00cd\13$\3%\3%\7%\u00d1\n%\f%\16%\u00d4\13%\3%\5%\u00d7\n%\3%\7%\u00da"+
		"\n%\f%\16%\u00dd\13%\3%\3%\3%\3%\3%\3%\3%\5%\u00e6\n%\3%\7%\u00e9\n%\f"+
		"%\16%\u00ec\13%\3%\3%\7%\u00f0\n%\f%\16%\u00f3\13%\3&\3&\2\2\'\3\2\5\2"+
		"\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2\31\2\33\2\35\2\37\2!\2#\2%"+
		"\2\'\2)\2+\2-\2/\2\61\2\63\2\65\2\67\29\2;\2=\2?\2A\2C\2E\2G\3I\4K\5\3"+
		"\2\31\3\2\62;\4\2C\\c|\4\2\13\13\"\"\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4"+
		"\2GGgg\4\2HHhh\4\2KKkk\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRr"+
		"r\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2YYyy\4\2[[{{\4\2\\\\||\2\u00e7\2"+
		"G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\3M\3\2\2\2\5T\3\2\2\2\7V\3\2\2\2\tX\3"+
		"\2\2\2\13[\3\2\2\2\rf\3\2\2\2\17h\3\2\2\2\21j\3\2\2\2\23m\3\2\2\2\25o"+
		"\3\2\2\2\27r\3\2\2\2\31x\3\2\2\2\33{\3\2\2\2\35}\3\2\2\2\37\177\3\2\2"+
		"\2!\u0081\3\2\2\2#\u0083\3\2\2\2%\u0085\3\2\2\2\'\u0087\3\2\2\2)\u0089"+
		"\3\2\2\2+\u008b\3\2\2\2-\u008d\3\2\2\2/\u008f\3\2\2\2\61\u0091\3\2\2\2"+
		"\63\u0093\3\2\2\2\65\u0095\3\2\2\2\67\u0097\3\2\2\29\u0099\3\2\2\2;\u009b"+
		"\3\2\2\2=\u009d\3\2\2\2?\u009f\3\2\2\2A\u00a1\3\2\2\2C\u00a3\3\2\2\2E"+
		"\u00a5\3\2\2\2G\u00a7\3\2\2\2I\u00ce\3\2\2\2K\u00f4\3\2\2\2MN\t\2\2\2"+
		"N\4\3\2\2\2OQ\7\17\2\2PO\3\2\2\2PQ\3\2\2\2QR\3\2\2\2RU\7\f\2\2SU\7\17"+
		"\2\2TP\3\2\2\2TS\3\2\2\2U\6\3\2\2\2VW\7+\2\2W\b\3\2\2\2XY\t\3\2\2Y\n\3"+
		"\2\2\2Z\\\5\3\2\2[Z\3\2\2\2\\]\3\2\2\2][\3\2\2\2]^\3\2\2\2^d\3\2\2\2_"+
		"a\5\3\2\2`_\3\2\2\2ab\3\2\2\2b`\3\2\2\2bc\3\2\2\2ce\3\2\2\2d`\3\2\2\2"+
		"de\3\2\2\2e\f\3\2\2\2fg\7^\2\2g\16\3\2\2\2hi\7,\2\2i\20\3\2\2\2jk\7,\2"+
		"\2kl\7,\2\2l\22\3\2\2\2mn\7\60\2\2n\24\3\2\2\2op\t\4\2\2p\26\3\2\2\2q"+
		"s\5\r\7\2rq\3\2\2\2rs\3\2\2\2sv\3\2\2\2tw\5\23\n\2uw\5\7\4\2vt\3\2\2\2"+
		"vu\3\2\2\2w\30\3\2\2\2xy\5\r\7\2yz\5\17\b\2z\32\3\2\2\2{|\7@\2\2|\34\3"+
		"\2\2\2}~\7<\2\2~\36\3\2\2\2\177\u0080\t\5\2\2\u0080 \3\2\2\2\u0081\u0082"+
		"\t\6\2\2\u0082\"\3\2\2\2\u0083\u0084\t\7\2\2\u0084$\3\2\2\2\u0085\u0086"+
		"\t\b\2\2\u0086&\3\2\2\2\u0087\u0088\t\t\2\2\u0088(\3\2\2\2\u0089\u008a"+
		"\t\n\2\2\u008a*\3\2\2\2\u008b\u008c\t\13\2\2\u008c,\3\2\2\2\u008d\u008e"+
		"\t\f\2\2\u008e.\3\2\2\2\u008f\u0090\t\r\2\2\u0090\60\3\2\2\2\u0091\u0092"+
		"\t\16\2\2\u0092\62\3\2\2\2\u0093\u0094\t\17\2\2\u0094\64\3\2\2\2\u0095"+
		"\u0096\t\20\2\2\u0096\66\3\2\2\2\u0097\u0098\t\21\2\2\u00988\3\2\2\2\u0099"+
		"\u009a\t\22\2\2\u009a:\3\2\2\2\u009b\u009c\t\23\2\2\u009c<\3\2\2\2\u009d"+
		"\u009e\t\24\2\2\u009e>\3\2\2\2\u009f\u00a0\t\25\2\2\u00a0@\3\2\2\2\u00a1"+
		"\u00a2\t\26\2\2\u00a2B\3\2\2\2\u00a3\u00a4\t\27\2\2\u00a4D\3\2\2\2\u00a5"+
		"\u00a6\t\30\2\2\u00a6F\3\2\2\2\u00a7\u00ab\5\5\3\2\u00a8\u00aa\5\25\13"+
		"\2\u00a9\u00a8\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00ac"+
		"\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae\u00b0\5\33\16\2"+
		"\u00af\u00ae\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b4\3\2\2\2\u00b1\u00b3"+
		"\5\25\13\2\u00b2\u00b1\3\2\2\2\u00b3\u00b6\3\2\2\2\u00b4\u00b2\3\2\2\2"+
		"\u00b4\u00b5\3\2\2\2\u00b5\u00b8\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b7\u00b9"+
		"\5\21\t\2\u00b8\u00b7\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\3\2\2\2"+
		"\u00ba\u00be\5\13\6\2\u00bb\u00bd\5\25\13\2\u00bc\u00bb\3\2\2\2\u00bd"+
		"\u00c0\3\2\2\2\u00be\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c4\3\2"+
		"\2\2\u00c0\u00be\3\2\2\2\u00c1\u00c3\5\25\13\2\u00c2\u00c1\3\2\2\2\u00c3"+
		"\u00c6\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c7\3\2"+
		"\2\2\u00c6\u00c4\3\2\2\2\u00c7\u00cb\5\27\f\2\u00c8\u00ca\5\25\13\2\u00c9"+
		"\u00c8\3\2\2\2\u00ca\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00cc\3\2"+
		"\2\2\u00ccH\3\2\2\2\u00cd\u00cb\3\2\2\2\u00ce\u00d2\5\5\3\2\u00cf\u00d1"+
		"\5\25\13\2\u00d0\u00cf\3\2\2\2\u00d1\u00d4\3\2\2\2\u00d2\u00d0\3\2\2\2"+
		"\u00d2\u00d3\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d5\u00d7"+
		"\5\33\16\2\u00d6\u00d5\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00db\3\2\2\2"+
		"\u00d8\u00da\5\25\13\2\u00d9\u00d8\3\2\2\2\u00da\u00dd\3\2\2\2\u00db\u00d9"+
		"\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc\u00de\3\2\2\2\u00dd\u00db\3\2\2\2\u00de"+
		"\u00df\5\37\20\2\u00df\u00e0\5\63\32\2\u00e0\u00e1\5;\36\2\u00e1\u00e2"+
		"\5A!\2\u00e2\u00e3\5\'\24\2\u00e3\u00e5\59\35\2\u00e4\u00e6\5;\36\2\u00e5"+
		"\u00e4\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00ea\3\2\2\2\u00e7\u00e9\5\25"+
		"\13\2\u00e8\u00e7\3\2\2\2\u00e9\u00ec\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea"+
		"\u00eb\3\2\2\2\u00eb\u00ed\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ed\u00f1\5\35"+
		"\17\2\u00ee\u00f0\5\25\13\2\u00ef\u00ee\3\2\2\2\u00f0\u00f3\3\2\2\2\u00f1"+
		"\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2J\3\2\2\2\u00f3\u00f1\3\2\2\2"+
		"\u00f4\u00f5\13\2\2\2\u00f5L\3\2\2\2\27\2PT]bdrv\u00ab\u00af\u00b4\u00b8"+
		"\u00be\u00c4\u00cb\u00d2\u00d6\u00db\u00e5\u00ea\u00f1\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}