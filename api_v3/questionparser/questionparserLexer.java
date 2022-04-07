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
		START_OF_QUESTION=1, TITLE=2, POINTS=3, TYPE=4, RANDOMIZE=5, ALL_CHARACTER=6;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"NEWLINE", "CLOSING_PARENTHESIS", "BACKSLASH", "ASTERISK", "DOUBLE_ASTERISK", 
			"DOT", "WHITESPACE", "DELIMITER", "GREATER_THAN", "COLON", "A", "B", 
			"C", "D", "E", "F", "I", "K", "L", "M", "N", "O", "P", "R", "S", "T", 
			"U", "W", "Y", "Z", "EXCLUDE_1", "INCLUDE_1", "ZERO", "EXCLUDE_ONE", 
			"NEWLINE_ADDED", "START_OL", "NUMLIST_EXCLUDE_1_PREFIX", "START_OF_QUESTION", 
			"TITLE", "POINTS", "TYPE", "RANDOMIZE", "ALL_CHARACTER"
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
			null, "START_OF_QUESTION", "TITLE", "POINTS", "TYPE", "RANDOMIZE", "ALL_CHARACTER"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b\u0193\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\3\2\5\2[\n\2\3\2\3\2\5\2_\n\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6"+
		"\3\7\3\7\3\b\3\b\3\t\5\to\n\t\3\t\3\t\5\ts\n\t\3\n\3\n\3\13\3\13\3\f\3"+
		"\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23"+
		"\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32"+
		"\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\""+
		"\3#\3#\3#\3#\3#\6#\u00ac\n#\r#\16#\u00ad\3#\3#\3#\3#\6#\u00b4\n#\r#\16"+
		"#\u00b5\5#\u00b8\n#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3"+
		"$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3&\3"+
		"&\7&\u00e2\n&\f&\16&\u00e5\13&\3&\5&\u00e8\n&\3&\7&\u00eb\n&\f&\16&\u00ee"+
		"\13&\3&\5&\u00f1\n&\3&\3&\7&\u00f5\n&\f&\16&\u00f8\13&\3&\3&\7&\u00fc"+
		"\n&\f&\16&\u00ff\13&\3\'\3\'\7\'\u0103\n\'\f\'\16\'\u0106\13\'\3\'\5\'"+
		"\u0109\n\'\3\'\7\'\u010c\n\'\f\'\16\'\u010f\13\'\3\'\3\'\3(\3(\7(\u0115"+
		"\n(\f(\16(\u0118\13(\3(\5(\u011b\n(\3(\7(\u011e\n(\f(\16(\u0121\13(\3"+
		"(\3(\3(\3(\3(\3(\5(\u0129\n(\3(\7(\u012c\n(\f(\16(\u012f\13(\3)\3)\7)"+
		"\u0133\n)\f)\16)\u0136\13)\3)\5)\u0139\n)\3)\7)\u013c\n)\f)\16)\u013f"+
		"\13)\3)\3)\3)\3)\3)\3)\5)\u0147\n)\3)\7)\u014a\n)\f)\16)\u014d\13)\3*"+
		"\3*\7*\u0151\n*\f*\16*\u0154\13*\3*\5*\u0157\n*\3*\7*\u015a\n*\f*\16*"+
		"\u015d\13*\3*\3*\3*\3*\3*\5*\u0164\n*\3*\7*\u0167\n*\f*\16*\u016a\13*"+
		"\3+\3+\7+\u016e\n+\f+\16+\u0171\13+\3+\5+\u0174\n+\3+\7+\u0177\n+\f+\16"+
		"+\u017a\13+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\5+\u0186\n+\3+\3+\5+\u018a\n"+
		"+\3+\7+\u018d\n+\f+\16+\u0190\13+\3,\3,\2\2-\3\2\5\2\7\2\t\2\13\2\r\2"+
		"\17\2\21\2\23\2\25\2\27\2\31\2\33\2\35\2\37\2!\2#\2%\2\'\2)\2+\2-\2/\2"+
		"\61\2\63\2\65\2\67\29\2;\2=\2?\2A\2C\2E\2G\2I\2K\2M\3O\4Q\5S\6U\7W\b\3"+
		"\2\30\4\2\13\13\"\"\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4"+
		"\2KKkk\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2TTtt\4\2UUu"+
		"u\4\2VVvv\4\2WWww\4\2YYyy\4\2[[{{\4\2\\\\||\3\2\64;\2\u0198\2M\3\2\2\2"+
		"\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\3^\3\2\2\2\5`"+
		"\3\2\2\2\7b\3\2\2\2\td\3\2\2\2\13f\3\2\2\2\ri\3\2\2\2\17k\3\2\2\2\21n"+
		"\3\2\2\2\23t\3\2\2\2\25v\3\2\2\2\27x\3\2\2\2\31z\3\2\2\2\33|\3\2\2\2\35"+
		"~\3\2\2\2\37\u0080\3\2\2\2!\u0082\3\2\2\2#\u0084\3\2\2\2%\u0086\3\2\2"+
		"\2\'\u0088\3\2\2\2)\u008a\3\2\2\2+\u008c\3\2\2\2-\u008e\3\2\2\2/\u0090"+
		"\3\2\2\2\61\u0092\3\2\2\2\63\u0094\3\2\2\2\65\u0096\3\2\2\2\67\u0098\3"+
		"\2\2\29\u009a\3\2\2\2;\u009c\3\2\2\2=\u009e\3\2\2\2?\u00a0\3\2\2\2A\u00a2"+
		"\3\2\2\2C\u00a4\3\2\2\2E\u00b7\3\2\2\2G\u00b9\3\2\2\2I\u00ca\3\2\2\2K"+
		"\u00df\3\2\2\2M\u0100\3\2\2\2O\u0112\3\2\2\2Q\u0130\3\2\2\2S\u014e\3\2"+
		"\2\2U\u016b\3\2\2\2W\u0191\3\2\2\2Y[\7\17\2\2ZY\3\2\2\2Z[\3\2\2\2[\\\3"+
		"\2\2\2\\_\7\f\2\2]_\7\17\2\2^Z\3\2\2\2^]\3\2\2\2_\4\3\2\2\2`a\7+\2\2a"+
		"\6\3\2\2\2bc\7^\2\2c\b\3\2\2\2de\7,\2\2e\n\3\2\2\2fg\7,\2\2gh\7,\2\2h"+
		"\f\3\2\2\2ij\7\60\2\2j\16\3\2\2\2kl\t\2\2\2l\20\3\2\2\2mo\5\7\4\2nm\3"+
		"\2\2\2no\3\2\2\2or\3\2\2\2ps\5\r\7\2qs\5\5\3\2rp\3\2\2\2rq\3\2\2\2s\22"+
		"\3\2\2\2tu\7@\2\2u\24\3\2\2\2vw\7<\2\2w\26\3\2\2\2xy\t\3\2\2y\30\3\2\2"+
		"\2z{\t\4\2\2{\32\3\2\2\2|}\t\5\2\2}\34\3\2\2\2~\177\t\6\2\2\177\36\3\2"+
		"\2\2\u0080\u0081\t\7\2\2\u0081 \3\2\2\2\u0082\u0083\t\b\2\2\u0083\"\3"+
		"\2\2\2\u0084\u0085\t\t\2\2\u0085$\3\2\2\2\u0086\u0087\t\n\2\2\u0087&\3"+
		"\2\2\2\u0088\u0089\t\13\2\2\u0089(\3\2\2\2\u008a\u008b\t\f\2\2\u008b*"+
		"\3\2\2\2\u008c\u008d\t\r\2\2\u008d,\3\2\2\2\u008e\u008f\t\16\2\2\u008f"+
		".\3\2\2\2\u0090\u0091\t\17\2\2\u0091\60\3\2\2\2\u0092\u0093\t\20\2\2\u0093"+
		"\62\3\2\2\2\u0094\u0095\t\21\2\2\u0095\64\3\2\2\2\u0096\u0097\t\22\2\2"+
		"\u0097\66\3\2\2\2\u0098\u0099\t\23\2\2\u00998\3\2\2\2\u009a\u009b\t\24"+
		"\2\2\u009b:\3\2\2\2\u009c\u009d\t\25\2\2\u009d<\3\2\2\2\u009e\u009f\t"+
		"\26\2\2\u009f>\3\2\2\2\u00a0\u00a1\t\27\2\2\u00a1@\3\2\2\2\u00a2\u00a3"+
		"\7\63\2\2\u00a3B\3\2\2\2\u00a4\u00a5\7\62\2\2\u00a5D\3\2\2\2\u00a6\u00b8"+
		"\5? \2\u00a7\u00ab\5A!\2\u00a8\u00ac\5C\"\2\u00a9\u00ac\5A!\2\u00aa\u00ac"+
		"\5? \2\u00ab\u00a8\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00aa\3\2\2\2\u00ac"+
		"\u00ad\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00b8\3\2"+
		"\2\2\u00af\u00b3\5? \2\u00b0\u00b4\5C\"\2\u00b1\u00b4\5A!\2\u00b2\u00b4"+
		"\5? \2\u00b3\u00b0\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b2\3\2\2\2\u00b4"+
		"\u00b5\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b8\3\2"+
		"\2\2\u00b7\u00a6\3\2\2\2\u00b7\u00a7\3\2\2\2\u00b7\u00af\3\2\2\2\u00b8"+
		"F\3\2\2\2\u00b9\u00ba\7>\2\2\u00ba\u00bb\7#\2\2\u00bb\u00bc\7/\2\2\u00bc"+
		"\u00bd\7/\2\2\u00bd\u00be\7\"\2\2\u00be\u00bf\7P\2\2\u00bf\u00c0\7g\2"+
		"\2\u00c0\u00c1\7y\2\2\u00c1\u00c2\7N\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4"+
		"\7p\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6\7\"\2\2\u00c6\u00c7\7/\2\2\u00c7"+
		"\u00c8\7/\2\2\u00c8\u00c9\7@\2\2\u00c9H\3\2\2\2\u00ca\u00cb\7>\2\2\u00cb"+
		"\u00cc\7#\2\2\u00cc\u00cd\7/\2\2\u00cd\u00ce\7/\2\2\u00ce\u00cf\7\"\2"+
		"\2\u00cf\u00d0\7U\2\2\u00d0\u00d1\7V\2\2\u00d1\u00d2\7C\2\2\u00d2\u00d3"+
		"\7T\2\2\u00d3\u00d4\7V\2\2\u00d4\u00d5\7\"\2\2\u00d5\u00d6\7Q\2\2\u00d6"+
		"\u00d7\7H\2\2\u00d7\u00d8\7\"\2\2\u00d8\u00d9\7Q\2\2\u00d9\u00da\7N\2"+
		"\2\u00da\u00db\7\"\2\2\u00db\u00dc\7/\2\2\u00dc\u00dd\7/\2\2\u00dd\u00de"+
		"\7@\2\2\u00deJ\3\2\2\2\u00df\u00e3\5\3\2\2\u00e0\u00e2\5\17\b\2\u00e1"+
		"\u00e0\3\2\2\2\u00e2\u00e5\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3\u00e4\3\2"+
		"\2\2\u00e4\u00e7\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e6\u00e8\5\23\n\2\u00e7"+
		"\u00e6\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00ec\3\2\2\2\u00e9\u00eb\5\17"+
		"\b\2\u00ea\u00e9\3\2\2\2\u00eb\u00ee\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec"+
		"\u00ed\3\2\2\2\u00ed\u00f0\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ef\u00f1\5\13"+
		"\6\2\u00f0\u00ef\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2"+
		"\u00f6\5E#\2\u00f3\u00f5\5\17\b\2\u00f4\u00f3\3\2\2\2\u00f5\u00f8\3\2"+
		"\2\2\u00f6\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f9\3\2\2\2\u00f8"+
		"\u00f6\3\2\2\2\u00f9\u00fd\5\21\t\2\u00fa\u00fc\5\17\b\2\u00fb\u00fa\3"+
		"\2\2\2\u00fc\u00ff\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe"+
		"L\3\2\2\2\u00ff\u00fd\3\2\2\2\u0100\u0104\5G$\2\u0101\u0103\5\3\2\2\u0102"+
		"\u0101\3\2\2\2\u0103\u0106\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0105\3\2"+
		"\2\2\u0105\u0108\3\2\2\2\u0106\u0104\3\2\2\2\u0107\u0109\5I%\2\u0108\u0107"+
		"\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u010d\3\2\2\2\u010a\u010c\5\3\2\2\u010b"+
		"\u010a\3\2\2\2\u010c\u010f\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010e\3\2"+
		"\2\2\u010e\u0110\3\2\2\2\u010f\u010d\3\2\2\2\u0110\u0111\5K&\2\u0111N"+
		"\3\2\2\2\u0112\u0116\5\3\2\2\u0113\u0115\5\17\b\2\u0114\u0113\3\2\2\2"+
		"\u0115\u0118\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u011a"+
		"\3\2\2\2\u0118\u0116\3\2\2\2\u0119\u011b\5\23\n\2\u011a\u0119\3\2\2\2"+
		"\u011a\u011b\3\2\2\2\u011b\u011f\3\2\2\2\u011c\u011e\5\17\b\2\u011d\u011c"+
		"\3\2\2\2\u011e\u0121\3\2\2\2\u011f\u011d\3\2\2\2\u011f\u0120\3\2\2\2\u0120"+
		"\u0122\3\2\2\2\u0121\u011f\3\2\2\2\u0122\u0123\5\65\33\2\u0123\u0124\5"+
		"#\22\2\u0124\u0125\5\65\33\2\u0125\u0126\5\'\24\2\u0126\u0128\5\37\20"+
		"\2\u0127\u0129\5\63\32\2\u0128\u0127\3\2\2\2\u0128\u0129\3\2\2\2\u0129"+
		"\u012d\3\2\2\2\u012a\u012c\5\17\b\2\u012b\u012a\3\2\2\2\u012c\u012f\3"+
		"\2\2\2\u012d\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012eP\3\2\2\2\u012f\u012d"+
		"\3\2\2\2\u0130\u0134\5\3\2\2\u0131\u0133\5\17\b\2\u0132\u0131\3\2\2\2"+
		"\u0133\u0136\3\2\2\2\u0134\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0138"+
		"\3\2\2\2\u0136\u0134\3\2\2\2\u0137\u0139\5\23\n\2\u0138\u0137\3\2\2\2"+
		"\u0138\u0139\3\2\2\2\u0139\u013d\3\2\2\2\u013a\u013c\5\17\b\2\u013b\u013a"+
		"\3\2\2\2\u013c\u013f\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013e\3\2\2\2\u013e"+
		"\u0140\3\2\2\2\u013f\u013d\3\2\2\2\u0140\u0141\5/\30\2\u0141\u0142\5-"+
		"\27\2\u0142\u0143\5#\22\2\u0143\u0144\5+\26\2\u0144\u0146\5\65\33\2\u0145"+
		"\u0147\5\63\32\2\u0146\u0145\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u014b\3"+
		"\2\2\2\u0148\u014a\5\17\b\2\u0149\u0148\3\2\2\2\u014a\u014d\3\2\2\2\u014b"+
		"\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014cR\3\2\2\2\u014d\u014b\3\2\2\2"+
		"\u014e\u0152\5\3\2\2\u014f\u0151\5\17\b\2\u0150\u014f\3\2\2\2\u0151\u0154"+
		"\3\2\2\2\u0152\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0156\3\2\2\2\u0154"+
		"\u0152\3\2\2\2\u0155\u0157\5\23\n\2\u0156\u0155\3\2\2\2\u0156\u0157\3"+
		"\2\2\2\u0157\u015b\3\2\2\2\u0158\u015a\5\17\b\2\u0159\u0158\3\2\2\2\u015a"+
		"\u015d\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015e\3\2"+
		"\2\2\u015d\u015b\3\2\2\2\u015e\u015f\5\65\33\2\u015f\u0160\5;\36\2\u0160"+
		"\u0161\5/\30\2\u0161\u0163\5\37\20\2\u0162\u0164\5\63\32\2\u0163\u0162"+
		"\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0168\3\2\2\2\u0165\u0167\5\17\b\2"+
		"\u0166\u0165\3\2\2\2\u0167\u016a\3\2\2\2\u0168\u0166\3\2\2\2\u0168\u0169"+
		"\3\2\2\2\u0169T\3\2\2\2\u016a\u0168\3\2\2\2\u016b\u016f\5\3\2\2\u016c"+
		"\u016e\5\17\b\2\u016d\u016c\3\2\2\2\u016e\u0171\3\2\2\2\u016f\u016d\3"+
		"\2\2\2\u016f\u0170\3\2\2\2\u0170\u0173\3\2\2\2\u0171\u016f\3\2\2\2\u0172"+
		"\u0174\5\23\n\2\u0173\u0172\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0178\3"+
		"\2\2\2\u0175\u0177\5\17\b\2\u0176\u0175\3\2\2\2\u0177\u017a\3\2\2\2\u0178"+
		"\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017b\3\2\2\2\u017a\u0178\3\2"+
		"\2\2\u017b\u017c\5\61\31\2\u017c\u017d\5\27\f\2\u017d\u017e\5+\26\2\u017e"+
		"\u017f\5\35\17\2\u017f\u0180\5-\27\2\u0180\u0185\5)\25\2\u0181\u0182\5"+
		"#\22\2\u0182\u0183\5=\37\2\u0183\u0184\5\37\20\2\u0184\u0186\3\2\2\2\u0185"+
		"\u0181\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0189\3\2\2\2\u0187\u018a\5\63"+
		"\32\2\u0188\u018a\5\35\17\2\u0189\u0187\3\2\2\2\u0189\u0188\3\2\2\2\u0189"+
		"\u018a\3\2\2\2\u018a\u018e\3\2\2\2\u018b\u018d\5\17\b\2\u018c\u018b\3"+
		"\2\2\2\u018d\u0190\3\2\2\2\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018f"+
		"V\3\2\2\2\u0190\u018e\3\2\2\2\u0191\u0192\13\2\2\2\u0192X\3\2\2\2*\2Z"+
		"^nr\u00ab\u00ad\u00b3\u00b5\u00b7\u00e3\u00e7\u00ec\u00f0\u00f6\u00fd"+
		"\u0104\u0108\u010d\u0116\u011a\u011f\u0128\u012d\u0134\u0138\u013d\u0146"+
		"\u014b\u0152\u0156\u015b\u0163\u0168\u016f\u0173\u0178\u0185\u0189\u018e"+
		"\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}