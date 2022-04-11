// Generated from questionparser.g4 by ANTLR 4.9.3
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class questionparserLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.3", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		START_OL=1, END_OL=2, NUMLIST_PREFIX=3, LETTERLIST_PREFIX=4, FIB_START=5, 
		FIB_END=6, CORRECT_ANSWER=7, ALL_CHARACTER=8;
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
			"COLON", "A", "B", "C", "D", "E", "F", "I", "K", "L", "M", "N", "O", 
			"P", "R", "S", "T", "U", "W", "Y", "Z", "OPEN_BRACKET", "CLOSE_BRACKET", 
			"STAR_AFTER_DOT", "STAR_BEFORE_DOT", "STAR_BEFORE_LETTER", "START_OL", 
			"END_OL", "NUMLIST_PREFIX", "LETTERLIST_PREFIX", "FIB_START", "FIB_END", 
			"CORRECT_ANSWER", "ALL_CHARACTER"
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


	public questionparserLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "questionparser.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\n\u017f\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\3\2\3\2\3\3\5\3c\n\3\3\3\3\3\5\3g\n\3\3\4\3\4\3"+
		"\5\3\5\3\6\6\6n\n\6\r\6\16\6o\3\6\6\6s\n\6\r\6\16\6t\5\6w\n\6\3\7\3\7"+
		"\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\5\f\u0085\n\f\3\f\3\f\5\f\u0089"+
		"\n\f\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23"+
		"\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32"+
		"\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3"+
		"\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\7%\u00c0\n%\f%\16%\u00c3\13%\3%\3%\7%\u00c7"+
		"\n%\f%\16%\u00ca\13%\3%\3%\7%\u00ce\n%\f%\16%\u00d1\13%\3%\3%\7%\u00d5"+
		"\n%\f%\16%\u00d8\13%\3&\3&\7&\u00dc\n&\f&\16&\u00df\13&\3&\3&\7&\u00e3"+
		"\n&\f&\16&\u00e6\13&\3&\3&\7&\u00ea\n&\f&\16&\u00ed\13&\3&\3&\7&\u00f1"+
		"\n&\f&\16&\u00f4\13&\3\'\3\'\7\'\u00f8\n\'\f\'\16\'\u00fb\13\'\3\'\3\'"+
		"\7\'\u00ff\n\'\f\'\16\'\u0102\13\'\3\'\3\'\7\'\u0106\n\'\f\'\16\'\u0109"+
		"\13\'\3\'\3\'\7\'\u010d\n\'\f\'\16\'\u0110\13\'\3(\3(\3(\3(\3(\3(\3(\3"+
		"(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3"+
		")\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\7*\u0142\n*\f*\16"+
		"*\u0145\13*\3*\3*\7*\u0149\n*\f*\16*\u014c\13*\3*\3*\7*\u0150\n*\f*\16"+
		"*\u0153\13*\3+\3+\7+\u0157\n+\f+\16+\u015a\13+\3+\3+\7+\u015e\n+\f+\16"+
		"+\u0161\13+\3+\3+\7+\u0165\n+\f+\16+\u0168\13+\3,\3,\7,\u016c\n,\f,\16"+
		",\u016f\13,\3-\7-\u0172\n-\f-\16-\u0175\13-\3-\3-\3.\3.\3.\5.\u017c\n"+
		".\3/\3/\2\2\60\3\2\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2\31\2"+
		"\33\2\35\2\37\2!\2#\2%\2\'\2)\2+\2-\2/\2\61\2\63\2\65\2\67\29\2;\2=\2"+
		"?\2A\2C\2E\2G\2I\2K\2M\2O\3Q\4S\5U\6W\7Y\b[\t]\n\3\2\31\3\2\62;\4\2C\\"+
		"c|\4\2\13\13\"\"\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2K"+
		"Kkk\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2TTtt\4\2UUuu\4"+
		"\2VVvv\4\2WWww\4\2YYyy\4\2[[{{\4\2\\\\||\2\u0175\2O\3\2\2\2\2Q\3\2\2\2"+
		"\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\3_"+
		"\3\2\2\2\5f\3\2\2\2\7h\3\2\2\2\tj\3\2\2\2\13m\3\2\2\2\rx\3\2\2\2\17z\3"+
		"\2\2\2\21|\3\2\2\2\23\177\3\2\2\2\25\u0081\3\2\2\2\27\u0084\3\2\2\2\31"+
		"\u008a\3\2\2\2\33\u008d\3\2\2\2\35\u008f\3\2\2\2\37\u0091\3\2\2\2!\u0093"+
		"\3\2\2\2#\u0095\3\2\2\2%\u0097\3\2\2\2\'\u0099\3\2\2\2)\u009b\3\2\2\2"+
		"+\u009d\3\2\2\2-\u009f\3\2\2\2/\u00a1\3\2\2\2\61\u00a3\3\2\2\2\63\u00a5"+
		"\3\2\2\2\65\u00a7\3\2\2\2\67\u00a9\3\2\2\29\u00ab\3\2\2\2;\u00ad\3\2\2"+
		"\2=\u00af\3\2\2\2?\u00b1\3\2\2\2A\u00b3\3\2\2\2C\u00b5\3\2\2\2E\u00b7"+
		"\3\2\2\2G\u00ba\3\2\2\2I\u00bd\3\2\2\2K\u00d9\3\2\2\2M\u00f5\3\2\2\2O"+
		"\u0111\3\2\2\2Q\u0129\3\2\2\2S\u013f\3\2\2\2U\u0154\3\2\2\2W\u0169\3\2"+
		"\2\2Y\u0173\3\2\2\2[\u017b\3\2\2\2]\u017d\3\2\2\2_`\t\2\2\2`\4\3\2\2\2"+
		"ac\7\17\2\2ba\3\2\2\2bc\3\2\2\2cd\3\2\2\2dg\7\f\2\2eg\7\17\2\2fb\3\2\2"+
		"\2fe\3\2\2\2g\6\3\2\2\2hi\7+\2\2i\b\3\2\2\2jk\t\3\2\2k\n\3\2\2\2ln\5\3"+
		"\2\2ml\3\2\2\2no\3\2\2\2om\3\2\2\2op\3\2\2\2pv\3\2\2\2qs\5\3\2\2rq\3\2"+
		"\2\2st\3\2\2\2tr\3\2\2\2tu\3\2\2\2uw\3\2\2\2vr\3\2\2\2vw\3\2\2\2w\f\3"+
		"\2\2\2xy\7^\2\2y\16\3\2\2\2z{\7,\2\2{\20\3\2\2\2|}\7,\2\2}~\7,\2\2~\22"+
		"\3\2\2\2\177\u0080\7\60\2\2\u0080\24\3\2\2\2\u0081\u0082\t\4\2\2\u0082"+
		"\26\3\2\2\2\u0083\u0085\5\r\7\2\u0084\u0083\3\2\2\2\u0084\u0085\3\2\2"+
		"\2\u0085\u0088\3\2\2\2\u0086\u0089\5\23\n\2\u0087\u0089\5\7\4\2\u0088"+
		"\u0086\3\2\2\2\u0088\u0087\3\2\2\2\u0089\30\3\2\2\2\u008a\u008b\5\r\7"+
		"\2\u008b\u008c\5\17\b\2\u008c\32\3\2\2\2\u008d\u008e\7<\2\2\u008e\34\3"+
		"\2\2\2\u008f\u0090\t\5\2\2\u0090\36\3\2\2\2\u0091\u0092\t\6\2\2\u0092"+
		" \3\2\2\2\u0093\u0094\t\7\2\2\u0094\"\3\2\2\2\u0095\u0096\t\b\2\2\u0096"+
		"$\3\2\2\2\u0097\u0098\t\t\2\2\u0098&\3\2\2\2\u0099\u009a\t\n\2\2\u009a"+
		"(\3\2\2\2\u009b\u009c\t\13\2\2\u009c*\3\2\2\2\u009d\u009e\t\f\2\2\u009e"+
		",\3\2\2\2\u009f\u00a0\t\r\2\2\u00a0.\3\2\2\2\u00a1\u00a2\t\16\2\2\u00a2"+
		"\60\3\2\2\2\u00a3\u00a4\t\17\2\2\u00a4\62\3\2\2\2\u00a5\u00a6\t\20\2\2"+
		"\u00a6\64\3\2\2\2\u00a7\u00a8\t\21\2\2\u00a8\66\3\2\2\2\u00a9\u00aa\t"+
		"\22\2\2\u00aa8\3\2\2\2\u00ab\u00ac\t\23\2\2\u00ac:\3\2\2\2\u00ad\u00ae"+
		"\t\24\2\2\u00ae<\3\2\2\2\u00af\u00b0\t\25\2\2\u00b0>\3\2\2\2\u00b1\u00b2"+
		"\t\26\2\2\u00b2@\3\2\2\2\u00b3\u00b4\t\27\2\2\u00b4B\3\2\2\2\u00b5\u00b6"+
		"\t\30\2\2\u00b6D\3\2\2\2\u00b7\u00b8\7^\2\2\u00b8\u00b9\7]\2\2\u00b9F"+
		"\3\2\2\2\u00ba\u00bb\7^\2\2\u00bb\u00bc\7_\2\2\u00bcH\3\2\2\2\u00bd\u00c1"+
		"\5\5\3\2\u00be\u00c0\5\25\13\2\u00bf\u00be\3\2\2\2\u00c0\u00c3\3\2\2\2"+
		"\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c4\3\2\2\2\u00c3\u00c1"+
		"\3\2\2\2\u00c4\u00c8\5\t\5\2\u00c5\u00c7\5\25\13\2\u00c6\u00c5\3\2\2\2"+
		"\u00c7\u00ca\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00cb"+
		"\3\2\2\2\u00ca\u00c8\3\2\2\2\u00cb\u00cf\5\27\f\2\u00cc\u00ce\5\25\13"+
		"\2\u00cd\u00cc\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0"+
		"\3\2\2\2\u00d0\u00d2\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d2\u00d6\5\31\r\2"+
		"\u00d3\u00d5\5\25\13\2\u00d4\u00d3\3\2\2\2\u00d5\u00d8\3\2\2\2\u00d6\u00d4"+
		"\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7J\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d9"+
		"\u00dd\5\5\3\2\u00da\u00dc\5\25\13\2\u00db\u00da\3\2\2\2\u00dc\u00df\3"+
		"\2\2\2\u00dd\u00db\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00e0\3\2\2\2\u00df"+
		"\u00dd\3\2\2\2\u00e0\u00e4\5\t\5\2\u00e1\u00e3\5\25\13\2\u00e2\u00e1\3"+
		"\2\2\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5"+
		"\u00e7\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e7\u00eb\5\31\r\2\u00e8\u00ea\5"+
		"\25\13\2\u00e9\u00e8\3\2\2\2\u00ea\u00ed\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb"+
		"\u00ec\3\2\2\2\u00ec\u00ee\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00f2\5\27"+
		"\f\2\u00ef\u00f1\5\25\13\2\u00f0\u00ef\3\2\2\2\u00f1\u00f4\3\2\2\2\u00f2"+
		"\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3L\3\2\2\2\u00f4\u00f2\3\2\2\2"+
		"\u00f5\u00f9\5\5\3\2\u00f6\u00f8\5\25\13\2\u00f7\u00f6\3\2\2\2\u00f8\u00fb"+
		"\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fc\3\2\2\2\u00fb"+
		"\u00f9\3\2\2\2\u00fc\u0100\5\31\r\2\u00fd\u00ff\5\25\13\2\u00fe\u00fd"+
		"\3\2\2\2\u00ff\u0102\3\2\2\2\u0100\u00fe\3\2\2\2\u0100\u0101\3\2\2\2\u0101"+
		"\u0103\3\2\2\2\u0102\u0100\3\2\2\2\u0103\u0107\5\t\5\2\u0104\u0106\5\25"+
		"\13\2\u0105\u0104\3\2\2\2\u0106\u0109\3\2\2\2\u0107\u0105\3\2\2\2\u0107"+
		"\u0108\3\2\2\2\u0108\u010a\3\2\2\2\u0109\u0107\3\2\2\2\u010a\u010e\5\27"+
		"\f\2\u010b\u010d\5\25\13\2\u010c\u010b\3\2\2\2\u010d\u0110\3\2\2\2\u010e"+
		"\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010fN\3\2\2\2\u0110\u010e\3\2\2\2"+
		"\u0111\u0112\5\5\3\2\u0112\u0113\7>\2\2\u0113\u0114\7#\2\2\u0114\u0115"+
		"\7/\2\2\u0115\u0116\7/\2\2\u0116\u0117\7\"\2\2\u0117\u0118\7U\2\2\u0118"+
		"\u0119\7V\2\2\u0119\u011a\7C\2\2\u011a\u011b\7T\2\2\u011b\u011c\7V\2\2"+
		"\u011c\u011d\7\"\2\2\u011d\u011e\7Q\2\2\u011e\u011f\7H\2\2\u011f\u0120"+
		"\7\"\2\2\u0120\u0121\7Q\2\2\u0121\u0122\7N\2\2\u0122\u0123\7\"\2\2\u0123"+
		"\u0124\7/\2\2\u0124\u0125\7/\2\2\u0125\u0126\7@\2\2\u0126\u0127\3\2\2"+
		"\2\u0127\u0128\5\5\3\2\u0128P\3\2\2\2\u0129\u012a\5\5\3\2\u012a\u012b"+
		"\7>\2\2\u012b\u012c\7#\2\2\u012c\u012d\7/\2\2\u012d\u012e\7/\2\2\u012e"+
		"\u012f\7\"\2\2\u012f\u0130\7G\2\2\u0130\u0131\7P\2\2\u0131\u0132\7F\2"+
		"\2\u0132\u0133\7\"\2\2\u0133\u0134\7Q\2\2\u0134\u0135\7H\2\2\u0135\u0136"+
		"\7\"\2\2\u0136\u0137\7Q\2\2\u0137\u0138\7N\2\2\u0138\u0139\7\"\2\2\u0139"+
		"\u013a\7/\2\2\u013a\u013b\7/\2\2\u013b\u013c\7@\2\2\u013c\u013d\3\2\2"+
		"\2\u013d\u013e\5\5\3\2\u013eR\3\2\2\2\u013f\u0143\5\5\3\2\u0140\u0142"+
		"\5\25\13\2\u0141\u0140\3\2\2\2\u0142\u0145\3\2\2\2\u0143\u0141\3\2\2\2"+
		"\u0143\u0144\3\2\2\2\u0144\u0146\3\2\2\2\u0145\u0143\3\2\2\2\u0146\u014a"+
		"\5\13\6\2\u0147\u0149\5\25\13\2\u0148\u0147\3\2\2\2\u0149\u014c\3\2\2"+
		"\2\u014a\u0148\3\2\2\2\u014a\u014b\3\2\2\2\u014b\u014d\3\2\2\2\u014c\u014a"+
		"\3\2\2\2\u014d\u0151\5\27\f\2\u014e\u0150\5\25\13\2\u014f\u014e\3\2\2"+
		"\2\u0150\u0153\3\2\2\2\u0151\u014f\3\2\2\2\u0151\u0152\3\2\2\2\u0152T"+
		"\3\2\2\2\u0153\u0151\3\2\2\2\u0154\u0158\5\5\3\2\u0155\u0157\5\25\13\2"+
		"\u0156\u0155\3\2\2\2\u0157\u015a\3\2\2\2\u0158\u0156\3\2\2\2\u0158\u0159"+
		"\3\2\2\2\u0159\u015b\3\2\2\2\u015a\u0158\3\2\2\2\u015b\u015f\5\t\5\2\u015c"+
		"\u015e\5\25\13\2\u015d\u015c\3\2\2\2\u015e\u0161\3\2\2\2\u015f\u015d\3"+
		"\2\2\2\u015f\u0160\3\2\2\2\u0160\u0162\3\2\2\2\u0161\u015f\3\2\2\2\u0162"+
		"\u0166\5\27\f\2\u0163\u0165\5\25\13\2\u0164\u0163\3\2\2\2\u0165\u0168"+
		"\3\2\2\2\u0166\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167V\3\2\2\2\u0168"+
		"\u0166\3\2\2\2\u0169\u016d\5E#\2\u016a\u016c\5\25\13\2\u016b\u016a\3\2"+
		"\2\2\u016c\u016f\3\2\2\2\u016d\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e"+
		"X\3\2\2\2\u016f\u016d\3\2\2\2\u0170\u0172\5\25\13\2\u0171\u0170\3\2\2"+
		"\2\u0172\u0175\3\2\2\2\u0173\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0176"+
		"\3\2\2\2\u0175\u0173\3\2\2\2\u0176\u0177\5G$\2\u0177Z\3\2\2\2\u0178\u017c"+
		"\5I%\2\u0179\u017c\5K&\2\u017a\u017c\5M\'\2\u017b\u0178\3\2\2\2\u017b"+
		"\u0179\3\2\2\2\u017b\u017a\3\2\2\2\u017c\\\3\2\2\2\u017d\u017e\13\2\2"+
		"\2\u017e^\3\2\2\2\37\2bfotv\u0084\u0088\u00c1\u00c8\u00cf\u00d6\u00dd"+
		"\u00e4\u00eb\u00f2\u00f9\u0100\u0107\u010e\u0143\u014a\u0151\u0158\u015f"+
		"\u0166\u016d\u0173\u017b\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}