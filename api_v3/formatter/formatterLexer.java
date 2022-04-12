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
		HEADING_1=1, HEADING_2=2, START_NUMBER_ONE=3, END_ANSWER_BLOCK=4, TITLE=5, 
		POINTS=6, TYPE=7, RANDOMIZE=8, ALL_CHARACTER=9;
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
			"ANSWER", "HASH", "DOUBLE_HASH", "HEADING_1", "HEADING_2", "START_NUMBER_ONE", 
			"END_ANSWER_BLOCK", "TITLE", "POINTS", "TYPE", "RANDOMIZE", "ALL_CHARACTER"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13\u0146\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t"+
		" \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2"+
		"\5\2W\n\2\3\2\3\2\5\2[\n\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\7\3\7"+
		"\3\b\3\b\3\t\3\t\3\n\5\nm\n\n\3\n\3\n\5\nq\n\n\3\13\3\13\3\f\3\f\3\r\3"+
		"\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3"+
		"\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3"+
		"\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5"+
		"\37\u00a2\n\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$"+
		"\3$\7$\u00b6\n$\f$\16$\u00b9\13$\3$\3$\3%\3%\7%\u00bf\n%\f%\16%\u00c2"+
		"\13%\3%\3%\7%\u00c6\n%\f%\16%\u00c9\13%\3%\3%\7%\u00cd\n%\f%\16%\u00d0"+
		"\13%\3&\3&\7&\u00d4\n&\f&\16&\u00d7\13&\3&\7&\u00da\n&\f&\16&\u00dd\13"+
		"&\3&\3&\3&\3&\3&\3&\5&\u00e5\n&\3&\7&\u00e8\n&\f&\16&\u00eb\13&\3\'\3"+
		"\'\7\'\u00ef\n\'\f\'\16\'\u00f2\13\'\3\'\7\'\u00f5\n\'\f\'\16\'\u00f8"+
		"\13\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u0100\n\'\3\'\7\'\u0103\n\'\f\'\16\'"+
		"\u0106\13\'\3(\3(\7(\u010a\n(\f(\16(\u010d\13(\3(\7(\u0110\n(\f(\16(\u0113"+
		"\13(\3(\3(\3(\3(\3(\5(\u011a\n(\3(\7(\u011d\n(\f(\16(\u0120\13(\3)\3)"+
		"\7)\u0124\n)\f)\16)\u0127\13)\3)\7)\u012a\n)\f)\16)\u012d\13)\3)\3)\3"+
		")\3)\3)\3)\3)\3)\3)\3)\5)\u0139\n)\3)\3)\5)\u013d\n)\3)\7)\u0140\n)\f"+
		")\16)\u0143\13)\3*\3*\2\2+\3\2\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25"+
		"\2\27\2\31\2\33\2\35\2\37\2!\2#\2%\2\'\2)\2+\2-\2/\2\61\2\63\2\65\2\67"+
		"\29\2;\2=\2?\2A\2C\3E\4G\5I\6K\7M\bO\tQ\nS\13\3\2\27\4\2\13\13\"\"\4\2"+
		"CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2KKkk\4\2MMmm\4\2NNnn\4"+
		"\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2YYy"+
		"y\4\2[[{{\4\2\\\\||\2\u0140\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2"+
		"\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\3Z\3\2\2\2\5"+
		"\\\3\2\2\2\7^\3\2\2\2\t`\3\2\2\2\13b\3\2\2\2\re\3\2\2\2\17g\3\2\2\2\21"+
		"i\3\2\2\2\23l\3\2\2\2\25r\3\2\2\2\27t\3\2\2\2\31v\3\2\2\2\33x\3\2\2\2"+
		"\35z\3\2\2\2\37|\3\2\2\2!~\3\2\2\2#\u0080\3\2\2\2%\u0082\3\2\2\2\'\u0084"+
		"\3\2\2\2)\u0086\3\2\2\2+\u0088\3\2\2\2-\u008a\3\2\2\2/\u008c\3\2\2\2\61"+
		"\u008e\3\2\2\2\63\u0090\3\2\2\2\65\u0092\3\2\2\2\67\u0094\3\2\2\29\u0096"+
		"\3\2\2\2;\u0098\3\2\2\2=\u009a\3\2\2\2?\u00a3\3\2\2\2A\u00a5\3\2\2\2C"+
		"\u00a8\3\2\2\2E\u00ac\3\2\2\2G\u00b2\3\2\2\2I\u00bc\3\2\2\2K\u00d1\3\2"+
		"\2\2M\u00ec\3\2\2\2O\u0107\3\2\2\2Q\u0121\3\2\2\2S\u0144\3\2\2\2UW\7\17"+
		"\2\2VU\3\2\2\2VW\3\2\2\2WX\3\2\2\2X[\7\f\2\2Y[\7\17\2\2ZV\3\2\2\2ZY\3"+
		"\2\2\2[\4\3\2\2\2\\]\7+\2\2]\6\3\2\2\2^_\7^\2\2_\b\3\2\2\2`a\7,\2\2a\n"+
		"\3\2\2\2bc\7,\2\2cd\7,\2\2d\f\3\2\2\2ef\7\60\2\2f\16\3\2\2\2gh\7<\2\2"+
		"h\20\3\2\2\2ij\t\2\2\2j\22\3\2\2\2km\5\7\4\2lk\3\2\2\2lm\3\2\2\2mp\3\2"+
		"\2\2nq\5\r\7\2oq\5\5\3\2pn\3\2\2\2po\3\2\2\2q\24\3\2\2\2rs\t\3\2\2s\26"+
		"\3\2\2\2tu\t\4\2\2u\30\3\2\2\2vw\t\5\2\2w\32\3\2\2\2xy\t\6\2\2y\34\3\2"+
		"\2\2z{\t\7\2\2{\36\3\2\2\2|}\t\b\2\2} \3\2\2\2~\177\t\t\2\2\177\"\3\2"+
		"\2\2\u0080\u0081\t\n\2\2\u0081$\3\2\2\2\u0082\u0083\t\13\2\2\u0083&\3"+
		"\2\2\2\u0084\u0085\t\f\2\2\u0085(\3\2\2\2\u0086\u0087\t\r\2\2\u0087*\3"+
		"\2\2\2\u0088\u0089\t\16\2\2\u0089,\3\2\2\2\u008a\u008b\t\17\2\2\u008b"+
		".\3\2\2\2\u008c\u008d\t\20\2\2\u008d\60\3\2\2\2\u008e\u008f\t\21\2\2\u008f"+
		"\62\3\2\2\2\u0090\u0091\t\22\2\2\u0091\64\3\2\2\2\u0092\u0093\t\23\2\2"+
		"\u0093\66\3\2\2\2\u0094\u0095\t\24\2\2\u00958\3\2\2\2\u0096\u0097\t\25"+
		"\2\2\u0097:\3\2\2\2\u0098\u0099\t\26\2\2\u0099<\3\2\2\2\u009a\u009b\5"+
		"\25\13\2\u009b\u009c\5)\25\2\u009c\u009d\5\61\31\2\u009d\u009e\5\67\34"+
		"\2\u009e\u009f\5\35\17\2\u009f\u00a1\5/\30\2\u00a0\u00a2\5\61\31\2\u00a1"+
		"\u00a0\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2>\3\2\2\2\u00a3\u00a4\7%\2\2\u00a4"+
		"@\3\2\2\2\u00a5\u00a6\7%\2\2\u00a6\u00a7\7%\2\2\u00a7B\3\2\2\2\u00a8\u00a9"+
		"\5\3\2\2\u00a9\u00aa\7%\2\2\u00aa\u00ab\5\21\t\2\u00abD\3\2\2\2\u00ac"+
		"\u00ad\5\3\2\2\u00ad\u00ae\7%\2\2\u00ae\u00af\7%\2\2\u00af\u00b0\3\2\2"+
		"\2\u00b0\u00b1\5\21\t\2\u00b1F\3\2\2\2\u00b2\u00b3\5\3\2\2\u00b3\u00b7"+
		"\7\63\2\2\u00b4\u00b6\5\21\t\2\u00b5\u00b4\3\2\2\2\u00b6\u00b9\3\2\2\2"+
		"\u00b7\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00ba\3\2\2\2\u00b9\u00b7"+
		"\3\2\2\2\u00ba\u00bb\5\23\n\2\u00bbH\3\2\2\2\u00bc\u00c0\5\3\2\2\u00bd"+
		"\u00bf\5\21\t\2\u00be\u00bd\3\2\2\2\u00bf\u00c2\3\2\2\2\u00c0\u00be\3"+
		"\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c3\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c3"+
		"\u00c7\5=\37\2\u00c4\u00c6\5\21\t\2\u00c5\u00c4\3\2\2\2\u00c6\u00c9\3"+
		"\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00ca\3\2\2\2\u00c9"+
		"\u00c7\3\2\2\2\u00ca\u00ce\5\17\b\2\u00cb\u00cd\5\21\t\2\u00cc\u00cb\3"+
		"\2\2\2\u00cd\u00d0\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf"+
		"J\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d1\u00d5\5\3\2\2\u00d2\u00d4\5\21\t\2"+
		"\u00d3\u00d2\3\2\2\2\u00d4\u00d7\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6"+
		"\3\2\2\2\u00d6\u00db\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d8\u00da\5\21\t\2"+
		"\u00d9\u00d8\3\2\2\2\u00da\u00dd\3\2\2\2\u00db\u00d9\3\2\2\2\u00db\u00dc"+
		"\3\2\2\2\u00dc\u00de\3\2\2\2\u00dd\u00db\3\2\2\2\u00de\u00df\5\63\32\2"+
		"\u00df\u00e0\5!\21\2\u00e0\u00e1\5\63\32\2\u00e1\u00e2\5%\23\2\u00e2\u00e4"+
		"\5\35\17\2\u00e3\u00e5\5\61\31\2\u00e4\u00e3\3\2\2\2\u00e4\u00e5\3\2\2"+
		"\2\u00e5\u00e9\3\2\2\2\u00e6\u00e8\5\21\t\2\u00e7\u00e6\3\2\2\2\u00e8"+
		"\u00eb\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00eaL\3\2\2\2"+
		"\u00eb\u00e9\3\2\2\2\u00ec\u00f0\5\3\2\2\u00ed\u00ef\5\21\t\2\u00ee\u00ed"+
		"\3\2\2\2\u00ef\u00f2\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1"+
		"\u00f6\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f3\u00f5\5\21\t\2\u00f4\u00f3\3"+
		"\2\2\2\u00f5\u00f8\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7"+
		"\u00f9\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f9\u00fa\5-\27\2\u00fa\u00fb\5+"+
		"\26\2\u00fb\u00fc\5!\21\2\u00fc\u00fd\5)\25\2\u00fd\u00ff\5\63\32\2\u00fe"+
		"\u0100\5\61\31\2\u00ff\u00fe\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0104\3"+
		"\2\2\2\u0101\u0103\5\21\t\2\u0102\u0101\3\2\2\2\u0103\u0106\3\2\2\2\u0104"+
		"\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105N\3\2\2\2\u0106\u0104\3\2\2\2"+
		"\u0107\u010b\5\3\2\2\u0108\u010a\5\21\t\2\u0109\u0108\3\2\2\2\u010a\u010d"+
		"\3\2\2\2\u010b\u0109\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u0111\3\2\2\2\u010d"+
		"\u010b\3\2\2\2\u010e\u0110\5\21\t\2\u010f\u010e\3\2\2\2\u0110\u0113\3"+
		"\2\2\2\u0111\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0114\3\2\2\2\u0113"+
		"\u0111\3\2\2\2\u0114\u0115\5\63\32\2\u0115\u0116\59\35\2\u0116\u0117\5"+
		"-\27\2\u0117\u0119\5\35\17\2\u0118\u011a\5\61\31\2\u0119\u0118\3\2\2\2"+
		"\u0119\u011a\3\2\2\2\u011a\u011e\3\2\2\2\u011b\u011d\5\21\t\2\u011c\u011b"+
		"\3\2\2\2\u011d\u0120\3\2\2\2\u011e\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011f"+
		"P\3\2\2\2\u0120\u011e\3\2\2\2\u0121\u0125\5\3\2\2\u0122\u0124\5\21\t\2"+
		"\u0123\u0122\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0123\3\2\2\2\u0125\u0126"+
		"\3\2\2\2\u0126\u012b\3\2\2\2\u0127\u0125\3\2\2\2\u0128\u012a\5\21\t\2"+
		"\u0129\u0128\3\2\2\2\u012a\u012d\3\2\2\2\u012b\u0129\3\2\2\2\u012b\u012c"+
		"\3\2\2\2\u012c\u012e\3\2\2\2\u012d\u012b\3\2\2\2\u012e\u012f\5/\30\2\u012f"+
		"\u0130\5\25\13\2\u0130\u0131\5)\25\2\u0131\u0132\5\33\16\2\u0132\u0133"+
		"\5+\26\2\u0133\u0138\5\'\24\2\u0134\u0135\5!\21\2\u0135\u0136\5;\36\2"+
		"\u0136\u0137\5\35\17\2\u0137\u0139\3\2\2\2\u0138\u0134\3\2\2\2\u0138\u0139"+
		"\3\2\2\2\u0139\u013c\3\2\2\2\u013a\u013d\5\61\31\2\u013b\u013d\5\33\16"+
		"\2\u013c\u013a\3\2\2\2\u013c\u013b\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u0141"+
		"\3\2\2\2\u013e\u0140\5\21\t\2\u013f\u013e\3\2\2\2\u0140\u0143\3\2\2\2"+
		"\u0141\u013f\3\2\2\2\u0141\u0142\3\2\2\2\u0142R\3\2\2\2\u0143\u0141\3"+
		"\2\2\2\u0144\u0145\13\2\2\2\u0145T\3\2\2\2\35\2VZlp\u00a1\u00b7\u00c0"+
		"\u00c7\u00ce\u00d5\u00db\u00e4\u00e9\u00f0\u00f6\u00ff\u0104\u010b\u0111"+
		"\u0119\u011e\u0125\u012b\u0138\u013c\u0141\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}