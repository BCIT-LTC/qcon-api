// Generated from formatter.g4 by ANTLR 4.9.3
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class formatterLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.3", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		START_OL=1, END_OL=2, HEADING_1=3, HEADING_2=4, START_NUMBER_ONE=5, END_ANSWER_BLOCK=6, 
		TITLE=7, POINTS=8, TYPE=9, RANDOMIZE=10, ALL_CHARACTER=11;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"NEWLINE", "CLOSING_PARENTHESIS", "BACKSLASH", "ASTERISK", "DOUBLE_ASTERISK", 
			"DOT", "COLON", "WHITESPACE", "DELIMITER", "A", "B", "C", "D", "E", "F", 
			"I", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "W", "Y", "Z", 
			"ANSWER", "HASH", "DOUBLE_HASH", "START_OL", "END_OL", "HEADING_1", "HEADING_2", 
			"START_NUMBER_ONE", "END_ANSWER_BLOCK", "TITLE", "POINTS", "TYPE", "RANDOMIZE", 
			"ALL_CHARACTER"
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
			null, "START_OL", "END_OL", "HEADING_1", "HEADING_2", "START_NUMBER_ONE", 
			"END_ANSWER_BLOCK", "TITLE", "POINTS", "TYPE", "RANDOMIZE", "ALL_CHARACTER"
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


	public formatterLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "formatter.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r\u0184\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\3\2\5\2[\n\2\3\2\3\2\5\2_\n\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6"+
		"\3\7\3\7\3\b\3\b\3\t\3\t\3\n\5\nq\n\n\3\n\3\n\5\nu\n\n\3\13\3\13\3\f\3"+
		"\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23"+
		"\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32"+
		"\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37"+
		"\3\37\5\37\u00a6\n\37\3 \3 \3!\3!\3!\3\"\3\"\7\"\u00af\n\"\f\"\16\"\u00b2"+
		"\13\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\""+
		"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\7#\u00cd\n#\f#\16#\u00d0\13#\3#\3#"+
		"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$"+
		"\3%\3%\3%\3%\3%\3%\3&\3&\3&\7&\u00f4\n&\f&\16&\u00f7\13&\3&\3&\3\'\3\'"+
		"\7\'\u00fd\n\'\f\'\16\'\u0100\13\'\3\'\3\'\7\'\u0104\n\'\f\'\16\'\u0107"+
		"\13\'\3\'\3\'\7\'\u010b\n\'\f\'\16\'\u010e\13\'\3(\3(\7(\u0112\n(\f(\16"+
		"(\u0115\13(\3(\7(\u0118\n(\f(\16(\u011b\13(\3(\3(\3(\3(\3(\3(\5(\u0123"+
		"\n(\3(\7(\u0126\n(\f(\16(\u0129\13(\3)\3)\7)\u012d\n)\f)\16)\u0130\13"+
		")\3)\7)\u0133\n)\f)\16)\u0136\13)\3)\3)\3)\3)\3)\3)\5)\u013e\n)\3)\7)"+
		"\u0141\n)\f)\16)\u0144\13)\3*\3*\7*\u0148\n*\f*\16*\u014b\13*\3*\7*\u014e"+
		"\n*\f*\16*\u0151\13*\3*\3*\3*\3*\3*\5*\u0158\n*\3*\7*\u015b\n*\f*\16*"+
		"\u015e\13*\3+\3+\7+\u0162\n+\f+\16+\u0165\13+\3+\7+\u0168\n+\f+\16+\u016b"+
		"\13+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\5+\u0177\n+\3+\3+\5+\u017b\n+\3+\7"+
		"+\u017e\n+\f+\16+\u0181\13+\3,\3,\2\2-\3\2\5\2\7\2\t\2\13\2\r\2\17\2\21"+
		"\2\23\2\25\2\27\2\31\2\33\2\35\2\37\2!\2#\2%\2\'\2)\2+\2-\2/\2\61\2\63"+
		"\2\65\2\67\29\2;\2=\2?\2A\2C\3E\4G\5I\6K\7M\bO\tQ\nS\13U\fW\r\3\2\27\4"+
		"\2\13\13\"\"\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2KKkk\4"+
		"\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2TTtt\4\2UUuu\4\2VVv"+
		"v\4\2WWww\4\2YYyy\4\2[[{{\4\2\\\\||\2\u0180\2C\3\2\2\2\2E\3\2\2\2\2G\3"+
		"\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2"+
		"\2\2U\3\2\2\2\2W\3\2\2\2\3^\3\2\2\2\5`\3\2\2\2\7b\3\2\2\2\td\3\2\2\2\13"+
		"f\3\2\2\2\ri\3\2\2\2\17k\3\2\2\2\21m\3\2\2\2\23p\3\2\2\2\25v\3\2\2\2\27"+
		"x\3\2\2\2\31z\3\2\2\2\33|\3\2\2\2\35~\3\2\2\2\37\u0080\3\2\2\2!\u0082"+
		"\3\2\2\2#\u0084\3\2\2\2%\u0086\3\2\2\2\'\u0088\3\2\2\2)\u008a\3\2\2\2"+
		"+\u008c\3\2\2\2-\u008e\3\2\2\2/\u0090\3\2\2\2\61\u0092\3\2\2\2\63\u0094"+
		"\3\2\2\2\65\u0096\3\2\2\2\67\u0098\3\2\2\29\u009a\3\2\2\2;\u009c\3\2\2"+
		"\2=\u009e\3\2\2\2?\u00a7\3\2\2\2A\u00a9\3\2\2\2C\u00ac\3\2\2\2E\u00ca"+
		"\3\2\2\2G\u00e6\3\2\2\2I\u00ea\3\2\2\2K\u00f0\3\2\2\2M\u00fa\3\2\2\2O"+
		"\u010f\3\2\2\2Q\u012a\3\2\2\2S\u0145\3\2\2\2U\u015f\3\2\2\2W\u0182\3\2"+
		"\2\2Y[\7\17\2\2ZY\3\2\2\2Z[\3\2\2\2[\\\3\2\2\2\\_\7\f\2\2]_\7\17\2\2^"+
		"Z\3\2\2\2^]\3\2\2\2_\4\3\2\2\2`a\7+\2\2a\6\3\2\2\2bc\7^\2\2c\b\3\2\2\2"+
		"de\7,\2\2e\n\3\2\2\2fg\7,\2\2gh\7,\2\2h\f\3\2\2\2ij\7\60\2\2j\16\3\2\2"+
		"\2kl\7<\2\2l\20\3\2\2\2mn\t\2\2\2n\22\3\2\2\2oq\5\7\4\2po\3\2\2\2pq\3"+
		"\2\2\2qt\3\2\2\2ru\5\r\7\2su\5\5\3\2tr\3\2\2\2ts\3\2\2\2u\24\3\2\2\2v"+
		"w\t\3\2\2w\26\3\2\2\2xy\t\4\2\2y\30\3\2\2\2z{\t\5\2\2{\32\3\2\2\2|}\t"+
		"\6\2\2}\34\3\2\2\2~\177\t\7\2\2\177\36\3\2\2\2\u0080\u0081\t\b\2\2\u0081"+
		" \3\2\2\2\u0082\u0083\t\t\2\2\u0083\"\3\2\2\2\u0084\u0085\t\n\2\2\u0085"+
		"$\3\2\2\2\u0086\u0087\t\13\2\2\u0087&\3\2\2\2\u0088\u0089\t\f\2\2\u0089"+
		"(\3\2\2\2\u008a\u008b\t\r\2\2\u008b*\3\2\2\2\u008c\u008d\t\16\2\2\u008d"+
		",\3\2\2\2\u008e\u008f\t\17\2\2\u008f.\3\2\2\2\u0090\u0091\t\20\2\2\u0091"+
		"\60\3\2\2\2\u0092\u0093\t\21\2\2\u0093\62\3\2\2\2\u0094\u0095\t\22\2\2"+
		"\u0095\64\3\2\2\2\u0096\u0097\t\23\2\2\u0097\66\3\2\2\2\u0098\u0099\t"+
		"\24\2\2\u00998\3\2\2\2\u009a\u009b\t\25\2\2\u009b:\3\2\2\2\u009c\u009d"+
		"\t\26\2\2\u009d<\3\2\2\2\u009e\u009f\5\25\13\2\u009f\u00a0\5)\25\2\u00a0"+
		"\u00a1\5\61\31\2\u00a1\u00a2\5\67\34\2\u00a2\u00a3\5\35\17\2\u00a3\u00a5"+
		"\5/\30\2\u00a4\u00a6\5\61\31\2\u00a5\u00a4\3\2\2\2\u00a5\u00a6\3\2\2\2"+
		"\u00a6>\3\2\2\2\u00a7\u00a8\7%\2\2\u00a8@\3\2\2\2\u00a9\u00aa\7%\2\2\u00aa"+
		"\u00ab\7%\2\2\u00abB\3\2\2\2\u00ac\u00b0\5\3\2\2\u00ad\u00af\5\21\t\2"+
		"\u00ae\u00ad\3\2\2\2\u00af\u00b2\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1"+
		"\3\2\2\2\u00b1\u00b3\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3\u00b4\7>\2\2\u00b4"+
		"\u00b5\7#\2\2\u00b5\u00b6\7/\2\2\u00b6\u00b7\7/\2\2\u00b7\u00b8\7\"\2"+
		"\2\u00b8\u00b9\7U\2\2\u00b9\u00ba\7V\2\2\u00ba\u00bb\7C\2\2\u00bb\u00bc"+
		"\7T\2\2\u00bc\u00bd\7V\2\2\u00bd\u00be\7\"\2\2\u00be\u00bf\7Q\2\2\u00bf"+
		"\u00c0\7H\2\2\u00c0\u00c1\7\"\2\2\u00c1\u00c2\7Q\2\2\u00c2\u00c3\7N\2"+
		"\2\u00c3\u00c4\7\"\2\2\u00c4\u00c5\7/\2\2\u00c5\u00c6\7/\2\2\u00c6\u00c7"+
		"\7@\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00c9\b\"\2\2\u00c9D\3\2\2\2\u00ca\u00ce"+
		"\5\3\2\2\u00cb\u00cd\5\21\t\2\u00cc\u00cb\3\2\2\2\u00cd\u00d0\3\2\2\2"+
		"\u00ce\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d1\3\2\2\2\u00d0\u00ce"+
		"\3\2\2\2\u00d1\u00d2\7>\2\2\u00d2\u00d3\7#\2\2\u00d3\u00d4\7/\2\2\u00d4"+
		"\u00d5\7/\2\2\u00d5\u00d6\7\"\2\2\u00d6\u00d7\7G\2\2\u00d7\u00d8\7P\2"+
		"\2\u00d8\u00d9\7F\2\2\u00d9\u00da\7\"\2\2\u00da\u00db\7Q\2\2\u00db\u00dc"+
		"\7H\2\2\u00dc\u00dd\7\"\2\2\u00dd\u00de\7Q\2\2\u00de\u00df\7N\2\2\u00df"+
		"\u00e0\7\"\2\2\u00e0\u00e1\7/\2\2\u00e1\u00e2\7/\2\2\u00e2\u00e3\7@\2"+
		"\2\u00e3\u00e4\3\2\2\2\u00e4\u00e5\b#\2\2\u00e5F\3\2\2\2\u00e6\u00e7\5"+
		"\3\2\2\u00e7\u00e8\7%\2\2\u00e8\u00e9\5\21\t\2\u00e9H\3\2\2\2\u00ea\u00eb"+
		"\5\3\2\2\u00eb\u00ec\7%\2\2\u00ec\u00ed\7%\2\2\u00ed\u00ee\3\2\2\2\u00ee"+
		"\u00ef\5\21\t\2\u00efJ\3\2\2\2\u00f0\u00f1\5\3\2\2\u00f1\u00f5\7\63\2"+
		"\2\u00f2\u00f4\5\21\t\2\u00f3\u00f2\3\2\2\2\u00f4\u00f7\3\2\2\2\u00f5"+
		"\u00f3\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f8\3\2\2\2\u00f7\u00f5\3\2"+
		"\2\2\u00f8\u00f9\5\23\n\2\u00f9L\3\2\2\2\u00fa\u00fe\5\3\2\2\u00fb\u00fd"+
		"\5\21\t\2\u00fc\u00fb\3\2\2\2\u00fd\u0100\3\2\2\2\u00fe\u00fc\3\2\2\2"+
		"\u00fe\u00ff\3\2\2\2\u00ff\u0101\3\2\2\2\u0100\u00fe\3\2\2\2\u0101\u0105"+
		"\5=\37\2\u0102\u0104\5\21\t\2\u0103\u0102\3\2\2\2\u0104\u0107\3\2\2\2"+
		"\u0105\u0103\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0108\3\2\2\2\u0107\u0105"+
		"\3\2\2\2\u0108\u010c\5\17\b\2\u0109\u010b\5\21\t\2\u010a\u0109\3\2\2\2"+
		"\u010b\u010e\3\2\2\2\u010c\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010dN\3"+
		"\2\2\2\u010e\u010c\3\2\2\2\u010f\u0113\5\3\2\2\u0110\u0112\5\21\t\2\u0111"+
		"\u0110\3\2\2\2\u0112\u0115\3\2\2\2\u0113\u0111\3\2\2\2\u0113\u0114\3\2"+
		"\2\2\u0114\u0119\3\2\2\2\u0115\u0113\3\2\2\2\u0116\u0118\5\21\t\2\u0117"+
		"\u0116\3\2\2\2\u0118\u011b\3\2\2\2\u0119\u0117\3\2\2\2\u0119\u011a\3\2"+
		"\2\2\u011a\u011c\3\2\2\2\u011b\u0119\3\2\2\2\u011c\u011d\5\63\32\2\u011d"+
		"\u011e\5!\21\2\u011e\u011f\5\63\32\2\u011f\u0120\5%\23\2\u0120\u0122\5"+
		"\35\17\2\u0121\u0123\5\61\31\2\u0122\u0121\3\2\2\2\u0122\u0123\3\2\2\2"+
		"\u0123\u0127\3\2\2\2\u0124\u0126\5\21\t\2\u0125\u0124\3\2\2\2\u0126\u0129"+
		"\3\2\2\2\u0127\u0125\3\2\2\2\u0127\u0128\3\2\2\2\u0128P\3\2\2\2\u0129"+
		"\u0127\3\2\2\2\u012a\u012e\5\3\2\2\u012b\u012d\5\21\t\2\u012c\u012b\3"+
		"\2\2\2\u012d\u0130\3\2\2\2\u012e\u012c\3\2\2\2\u012e\u012f\3\2\2\2\u012f"+
		"\u0134\3\2\2\2\u0130\u012e\3\2\2\2\u0131\u0133\5\21\t\2\u0132\u0131\3"+
		"\2\2\2\u0133\u0136\3\2\2\2\u0134\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135"+
		"\u0137\3\2\2\2\u0136\u0134\3\2\2\2\u0137\u0138\5-\27\2\u0138\u0139\5+"+
		"\26\2\u0139\u013a\5!\21\2\u013a\u013b\5)\25\2\u013b\u013d\5\63\32\2\u013c"+
		"\u013e\5\61\31\2\u013d\u013c\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u0142\3"+
		"\2\2\2\u013f\u0141\5\21\t\2\u0140\u013f\3\2\2\2\u0141\u0144\3\2\2\2\u0142"+
		"\u0140\3\2\2\2\u0142\u0143\3\2\2\2\u0143R\3\2\2\2\u0144\u0142\3\2\2\2"+
		"\u0145\u0149\5\3\2\2\u0146\u0148\5\21\t\2\u0147\u0146\3\2\2\2\u0148\u014b"+
		"\3\2\2\2\u0149\u0147\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014f\3\2\2\2\u014b"+
		"\u0149\3\2\2\2\u014c\u014e\5\21\t\2\u014d\u014c\3\2\2\2\u014e\u0151\3"+
		"\2\2\2\u014f\u014d\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0152\3\2\2\2\u0151"+
		"\u014f\3\2\2\2\u0152\u0153\5\63\32\2\u0153\u0154\59\35\2\u0154\u0155\5"+
		"-\27\2\u0155\u0157\5\35\17\2\u0156\u0158\5\61\31\2\u0157\u0156\3\2\2\2"+
		"\u0157\u0158\3\2\2\2\u0158\u015c\3\2\2\2\u0159\u015b\5\21\t\2\u015a\u0159"+
		"\3\2\2\2\u015b\u015e\3\2\2\2\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d"+
		"T\3\2\2\2\u015e\u015c\3\2\2\2\u015f\u0163\5\3\2\2\u0160\u0162\5\21\t\2"+
		"\u0161\u0160\3\2\2\2\u0162\u0165\3\2\2\2\u0163\u0161\3\2\2\2\u0163\u0164"+
		"\3\2\2\2\u0164\u0169\3\2\2\2\u0165\u0163\3\2\2\2\u0166\u0168\5\21\t\2"+
		"\u0167\u0166\3\2\2\2\u0168\u016b\3\2\2\2\u0169\u0167\3\2\2\2\u0169\u016a"+
		"\3\2\2\2\u016a\u016c\3\2\2\2\u016b\u0169\3\2\2\2\u016c\u016d\5/\30\2\u016d"+
		"\u016e\5\25\13\2\u016e\u016f\5)\25\2\u016f\u0170\5\33\16\2\u0170\u0171"+
		"\5+\26\2\u0171\u0176\5\'\24\2\u0172\u0173\5!\21\2\u0173\u0174\5;\36\2"+
		"\u0174\u0175\5\35\17\2\u0175\u0177\3\2\2\2\u0176\u0172\3\2\2\2\u0176\u0177"+
		"\3\2\2\2\u0177\u017a\3\2\2\2\u0178\u017b\5\61\31\2\u0179\u017b\5\33\16"+
		"\2\u017a\u0178\3\2\2\2\u017a\u0179\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017f"+
		"\3\2\2\2\u017c\u017e\5\21\t\2\u017d\u017c\3\2\2\2\u017e\u0181\3\2\2\2"+
		"\u017f\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180V\3\2\2\2\u0181\u017f\3"+
		"\2\2\2\u0182\u0183\13\2\2\2\u0183X\3\2\2\2\37\2Z^pt\u00a5\u00b0\u00ce"+
		"\u00f5\u00fe\u0105\u010c\u0113\u0119\u0122\u0127\u012e\u0134\u013d\u0142"+
		"\u0149\u014f\u0157\u015c\u0163\u0169\u0176\u017a\u017f\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}