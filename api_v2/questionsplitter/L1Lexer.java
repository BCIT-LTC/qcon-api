// Generated from L1.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class L1Lexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ENDOFLIST=1, NUMLIST_PREFIX=2, LETTERLIST_PREFIX=3, STAR_AFTER_DOT=4, 
		STAR_BEFORE_DOT=5, STAR_BEFORE_LETTER=6, TITLE=7, POINTS=8, TYPE=9, RANDOMIZE=10, 
		END_ANSWER=11, ALL_CHARACTER=12;
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
			"GREATER_THAN", "COLON", "A", "B", "C", "D", "E", "F", "I", "L", "M", 
			"N", "O", "P", "R", "S", "T", "U", "W", "Y", "Z", "ENDOFLIST", "NUMLIST_PREFIX", 
			"LETTERLIST_PREFIX", "STAR_AFTER_DOT", "STAR_BEFORE_DOT", "STAR_BEFORE_LETTER", 
			"TITLE", "POINTS", "TYPE", "RANDOMIZE", "END_ANSWER", "ALL_CHARACTER"
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


	public L1Lexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "L1.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16\u0239\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t"+
		" \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t"+
		"+\4,\t,\4-\t-\4.\t.\3\2\3\2\3\3\5\3a\n\3\3\3\3\3\5\3e\n\3\3\4\3\4\3\5"+
		"\3\5\3\6\6\6l\n\6\r\6\16\6m\3\6\6\6q\n\6\r\6\16\6r\5\6u\n\6\3\7\3\7\3"+
		"\b\3\b\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\5\f\u0083\n\f\3\f\3\f\5\f\u0087"+
		"\n\f\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23"+
		"\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32"+
		"\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3"+
		"\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\7$\u00c3\n$\f$\16$\u00c6"+
		"\13$\3$\5$\u00c9\n$\3$\7$\u00cc\n$\f$\16$\u00cf\13$\3$\5$\u00d2\n$\3$"+
		"\3$\7$\u00d6\n$\f$\16$\u00d9\13$\3$\7$\u00dc\n$\f$\16$\u00df\13$\3$\3"+
		"$\7$\u00e3\n$\f$\16$\u00e6\13$\3%\3%\7%\u00ea\n%\f%\16%\u00ed\13%\3%\5"+
		"%\u00f0\n%\3%\7%\u00f3\n%\f%\16%\u00f6\13%\3%\5%\u00f9\n%\3%\3%\5%\u00fd"+
		"\n%\3%\7%\u0100\n%\f%\16%\u0103\13%\3%\7%\u0106\n%\f%\16%\u0109\13%\3"+
		"%\3%\7%\u010d\n%\f%\16%\u0110\13%\3&\3&\7&\u0114\n&\f&\16&\u0117\13&\3"+
		"&\5&\u011a\n&\3&\7&\u011d\n&\f&\16&\u0120\13&\3&\5&\u0123\n&\3&\3&\5&"+
		"\u0127\n&\3&\7&\u012a\n&\f&\16&\u012d\13&\3&\3&\7&\u0131\n&\f&\16&\u0134"+
		"\13&\3&\3&\7&\u0138\n&\f&\16&\u013b\13&\3\'\3\'\7\'\u013f\n\'\f\'\16\'"+
		"\u0142\13\'\3\'\5\'\u0145\n\'\3\'\7\'\u0148\n\'\f\'\16\'\u014b\13\'\3"+
		"\'\5\'\u014e\n\'\3\'\3\'\5\'\u0152\n\'\3\'\7\'\u0155\n\'\f\'\16\'\u0158"+
		"\13\'\3\'\3\'\7\'\u015c\n\'\f\'\16\'\u015f\13\'\3\'\3\'\7\'\u0163\n\'"+
		"\f\'\16\'\u0166\13\'\3(\3(\7(\u016a\n(\f(\16(\u016d\13(\3(\5(\u0170\n"+
		"(\3(\7(\u0173\n(\f(\16(\u0176\13(\3(\5(\u0179\n(\3(\3(\7(\u017d\n(\f("+
		"\16(\u0180\13(\3(\3(\5(\u0184\n(\3(\7(\u0187\n(\f(\16(\u018a\13(\3(\3"+
		"(\7(\u018e\n(\f(\16(\u0191\13(\3)\3)\7)\u0195\n)\f)\16)\u0198\13)\3)\5"+
		")\u019b\n)\3)\7)\u019e\n)\f)\16)\u01a1\13)\3)\3)\3)\3)\3)\3)\5)\u01a9"+
		"\n)\3)\7)\u01ac\n)\f)\16)\u01af\13)\3*\3*\7*\u01b3\n*\f*\16*\u01b6\13"+
		"*\3*\5*\u01b9\n*\3*\7*\u01bc\n*\f*\16*\u01bf\13*\3*\3*\3*\3*\3*\3*\5*"+
		"\u01c7\n*\3*\7*\u01ca\n*\f*\16*\u01cd\13*\3+\3+\7+\u01d1\n+\f+\16+\u01d4"+
		"\13+\3+\5+\u01d7\n+\3+\7+\u01da\n+\f+\16+\u01dd\13+\3+\3+\3+\3+\3+\5+"+
		"\u01e4\n+\3+\7+\u01e7\n+\f+\16+\u01ea\13+\3,\3,\7,\u01ee\n,\f,\16,\u01f1"+
		"\13,\3,\5,\u01f4\n,\3,\7,\u01f7\n,\f,\16,\u01fa\13,\3,\3,\3,\3,\3,\3,"+
		"\3,\3,\3,\3,\5,\u0206\n,\3,\3,\5,\u020a\n,\3,\7,\u020d\n,\f,\16,\u0210"+
		"\13,\3-\3-\7-\u0214\n-\f-\16-\u0217\13-\3-\5-\u021a\n-\3-\7-\u021d\n-"+
		"\f-\16-\u0220\13-\3-\3-\3-\3-\3-\3-\3-\5-\u0229\n-\3-\7-\u022c\n-\f-\16"+
		"-\u022f\13-\3-\3-\7-\u0233\n-\f-\16-\u0236\13-\3.\3.\2\2/\3\2\5\2\7\2"+
		"\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2\31\2\33\2\35\2\37\2!\2#\2%\2\'"+
		"\2)\2+\2-\2/\2\61\2\63\2\65\2\67\29\2;\2=\2?\2A\2C\2E\3G\4I\5K\6M\7O\b"+
		"Q\tS\nU\13W\fY\r[\16\3\2\30\3\2\62;\4\2C\\c|\4\2\13\13\"\"\4\2CCcc\4\2"+
		"DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2KKkk\4\2NNnn\4\2OOoo\4\2PPpp\4"+
		"\2QQqq\4\2RRrr\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2YYyy\4\2[[{{\4\2\\\\"+
		"||\2\u0261\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3"+
		"\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2"+
		"\2\3]\3\2\2\2\5d\3\2\2\2\7f\3\2\2\2\th\3\2\2\2\13k\3\2\2\2\rv\3\2\2\2"+
		"\17x\3\2\2\2\21z\3\2\2\2\23}\3\2\2\2\25\177\3\2\2\2\27\u0082\3\2\2\2\31"+
		"\u0088\3\2\2\2\33\u008b\3\2\2\2\35\u008d\3\2\2\2\37\u008f\3\2\2\2!\u0091"+
		"\3\2\2\2#\u0093\3\2\2\2%\u0095\3\2\2\2\'\u0097\3\2\2\2)\u0099\3\2\2\2"+
		"+\u009b\3\2\2\2-\u009d\3\2\2\2/\u009f\3\2\2\2\61\u00a1\3\2\2\2\63\u00a3"+
		"\3\2\2\2\65\u00a5\3\2\2\2\67\u00a7\3\2\2\29\u00a9\3\2\2\2;\u00ab\3\2\2"+
		"\2=\u00ad\3\2\2\2?\u00af\3\2\2\2A\u00b1\3\2\2\2C\u00b3\3\2\2\2E\u00b5"+
		"\3\2\2\2G\u00c0\3\2\2\2I\u00e7\3\2\2\2K\u0111\3\2\2\2M\u013c\3\2\2\2O"+
		"\u0167\3\2\2\2Q\u0192\3\2\2\2S\u01b0\3\2\2\2U\u01ce\3\2\2\2W\u01eb\3\2"+
		"\2\2Y\u0211\3\2\2\2[\u0237\3\2\2\2]^\t\2\2\2^\4\3\2\2\2_a\7\17\2\2`_\3"+
		"\2\2\2`a\3\2\2\2ab\3\2\2\2be\7\f\2\2ce\7\17\2\2d`\3\2\2\2dc\3\2\2\2e\6"+
		"\3\2\2\2fg\7+\2\2g\b\3\2\2\2hi\t\3\2\2i\n\3\2\2\2jl\5\3\2\2kj\3\2\2\2"+
		"lm\3\2\2\2mk\3\2\2\2mn\3\2\2\2nt\3\2\2\2oq\5\3\2\2po\3\2\2\2qr\3\2\2\2"+
		"rp\3\2\2\2rs\3\2\2\2su\3\2\2\2tp\3\2\2\2tu\3\2\2\2u\f\3\2\2\2vw\7^\2\2"+
		"w\16\3\2\2\2xy\7,\2\2y\20\3\2\2\2z{\7,\2\2{|\7,\2\2|\22\3\2\2\2}~\7\60"+
		"\2\2~\24\3\2\2\2\177\u0080\t\4\2\2\u0080\26\3\2\2\2\u0081\u0083\5\r\7"+
		"\2\u0082\u0081\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0086\3\2\2\2\u0084\u0087"+
		"\5\23\n\2\u0085\u0087\5\7\4\2\u0086\u0084\3\2\2\2\u0086\u0085\3\2\2\2"+
		"\u0087\30\3\2\2\2\u0088\u0089\5\r\7\2\u0089\u008a\5\17\b\2\u008a\32\3"+
		"\2\2\2\u008b\u008c\7@\2\2\u008c\34\3\2\2\2\u008d\u008e\7<\2\2\u008e\36"+
		"\3\2\2\2\u008f\u0090\t\5\2\2\u0090 \3\2\2\2\u0091\u0092\t\6\2\2\u0092"+
		"\"\3\2\2\2\u0093\u0094\t\7\2\2\u0094$\3\2\2\2\u0095\u0096\t\b\2\2\u0096"+
		"&\3\2\2\2\u0097\u0098\t\t\2\2\u0098(\3\2\2\2\u0099\u009a\t\n\2\2\u009a"+
		"*\3\2\2\2\u009b\u009c\t\13\2\2\u009c,\3\2\2\2\u009d\u009e\t\f\2\2\u009e"+
		".\3\2\2\2\u009f\u00a0\t\r\2\2\u00a0\60\3\2\2\2\u00a1\u00a2\t\16\2\2\u00a2"+
		"\62\3\2\2\2\u00a3\u00a4\t\17\2\2\u00a4\64\3\2\2\2\u00a5\u00a6\t\20\2\2"+
		"\u00a6\66\3\2\2\2\u00a7\u00a8\t\21\2\2\u00a88\3\2\2\2\u00a9\u00aa\t\22"+
		"\2\2\u00aa:\3\2\2\2\u00ab\u00ac\t\23\2\2\u00ac<\3\2\2\2\u00ad\u00ae\t"+
		"\24\2\2\u00ae>\3\2\2\2\u00af\u00b0\t\25\2\2\u00b0@\3\2\2\2\u00b1\u00b2"+
		"\t\26\2\2\u00b2B\3\2\2\2\u00b3\u00b4\t\27\2\2\u00b4D\3\2\2\2\u00b5\u00b6"+
		"\7>\2\2\u00b6\u00b7\7#\2\2\u00b7\u00b8\7/\2\2\u00b8\u00b9\7/\2\2\u00b9"+
		"\u00ba\7\"\2\2\u00ba\u00bb\7/\2\2\u00bb\u00bc\7/\2\2\u00bc\u00bd\7@\2"+
		"\2\u00bd\u00be\3\2\2\2\u00be\u00bf\5\5\3\2\u00bfF\3\2\2\2\u00c0\u00c4"+
		"\5\5\3\2\u00c1\u00c3\5\25\13\2\u00c2\u00c1\3\2\2\2\u00c3\u00c6\3\2\2\2"+
		"\u00c4\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6\u00c4"+
		"\3\2\2\2\u00c7\u00c9\5\33\16\2\u00c8\u00c7\3\2\2\2\u00c8\u00c9\3\2\2\2"+
		"\u00c9\u00cd\3\2\2\2\u00ca\u00cc\5\25\13\2\u00cb\u00ca\3\2\2\2\u00cc\u00cf"+
		"\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf"+
		"\u00cd\3\2\2\2\u00d0\u00d2\5\21\t\2\u00d1\u00d0\3\2\2\2\u00d1\u00d2\3"+
		"\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d7\5\13\6\2\u00d4\u00d6\5\25\13\2"+
		"\u00d5\u00d4\3\2\2\2\u00d6\u00d9\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8"+
		"\3\2\2\2\u00d8\u00dd\3\2\2\2\u00d9\u00d7\3\2\2\2\u00da\u00dc\5\25\13\2"+
		"\u00db\u00da\3\2\2\2\u00dc\u00df\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd\u00de"+
		"\3\2\2\2\u00de\u00e0\3\2\2\2\u00df\u00dd\3\2\2\2\u00e0\u00e4\5\27\f\2"+
		"\u00e1\u00e3\5\25\13\2\u00e2\u00e1\3\2\2\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2"+
		"\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5H\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e7"+
		"\u00eb\5\5\3\2\u00e8\u00ea\5\25\13\2\u00e9\u00e8\3\2\2\2\u00ea\u00ed\3"+
		"\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ef\3\2\2\2\u00ed"+
		"\u00eb\3\2\2\2\u00ee\u00f0\5\33\16\2\u00ef\u00ee\3\2\2\2\u00ef\u00f0\3"+
		"\2\2\2\u00f0\u00f4\3\2\2\2\u00f1\u00f3\5\25\13\2\u00f2\u00f1\3\2\2\2\u00f3"+
		"\u00f6\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f8\3\2"+
		"\2\2\u00f6\u00f4\3\2\2\2\u00f7\u00f9\5\21\t\2\u00f8\u00f7\3\2\2\2\u00f8"+
		"\u00f9\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fc\5\t\5\2\u00fb\u00fd\5\t"+
		"\5\2\u00fc\u00fb\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u0101\3\2\2\2\u00fe"+
		"\u0100\5\25\13\2\u00ff\u00fe\3\2\2\2\u0100\u0103\3\2\2\2\u0101\u00ff\3"+
		"\2\2\2\u0101\u0102\3\2\2\2\u0102\u0107\3\2\2\2\u0103\u0101\3\2\2\2\u0104"+
		"\u0106\5\25\13\2\u0105\u0104\3\2\2\2\u0106\u0109\3\2\2\2\u0107\u0105\3"+
		"\2\2\2\u0107\u0108\3\2\2\2\u0108\u010a\3\2\2\2\u0109\u0107\3\2\2\2\u010a"+
		"\u010e\5\27\f\2\u010b\u010d\5\25\13\2\u010c\u010b\3\2\2\2\u010d\u0110"+
		"\3\2\2\2\u010e\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010fJ\3\2\2\2\u0110"+
		"\u010e\3\2\2\2\u0111\u0115\5\5\3\2\u0112\u0114\5\25\13\2\u0113\u0112\3"+
		"\2\2\2\u0114\u0117\3\2\2\2\u0115\u0113\3\2\2\2\u0115\u0116\3\2\2\2\u0116"+
		"\u0119\3\2\2\2\u0117\u0115\3\2\2\2\u0118\u011a\5\33\16\2\u0119\u0118\3"+
		"\2\2\2\u0119\u011a\3\2\2\2\u011a\u011e\3\2\2\2\u011b\u011d\5\25\13\2\u011c"+
		"\u011b\3\2\2\2\u011d\u0120\3\2\2\2\u011e\u011c\3\2\2\2\u011e\u011f\3\2"+
		"\2\2\u011f\u0122\3\2\2\2\u0120\u011e\3\2\2\2\u0121\u0123\5\21\t\2\u0122"+
		"\u0121\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0124\3\2\2\2\u0124\u0126\5\t"+
		"\5\2\u0125\u0127\5\t\5\2\u0126\u0125\3\2\2\2\u0126\u0127\3\2\2\2\u0127"+
		"\u012b\3\2\2\2\u0128\u012a\5\25\13\2\u0129\u0128\3\2\2\2\u012a\u012d\3"+
		"\2\2\2\u012b\u0129\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012e\3\2\2\2\u012d"+
		"\u012b\3\2\2\2\u012e\u0132\5\27\f\2\u012f\u0131\5\25\13\2\u0130\u012f"+
		"\3\2\2\2\u0131\u0134\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133"+
		"\u0135\3\2\2\2\u0134\u0132\3\2\2\2\u0135\u0139\5\31\r\2\u0136\u0138\5"+
		"\25\13\2\u0137\u0136\3\2\2\2\u0138\u013b\3\2\2\2\u0139\u0137\3\2\2\2\u0139"+
		"\u013a\3\2\2\2\u013aL\3\2\2\2\u013b\u0139\3\2\2\2\u013c\u0140\5\5\3\2"+
		"\u013d\u013f\5\25\13\2\u013e\u013d\3\2\2\2\u013f\u0142\3\2\2\2\u0140\u013e"+
		"\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0144\3\2\2\2\u0142\u0140\3\2\2\2\u0143"+
		"\u0145\5\33\16\2\u0144\u0143\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0149\3"+
		"\2\2\2\u0146\u0148\5\25\13\2\u0147\u0146\3\2\2\2\u0148\u014b\3\2\2\2\u0149"+
		"\u0147\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014d\3\2\2\2\u014b\u0149\3\2"+
		"\2\2\u014c\u014e\5\21\t\2\u014d\u014c\3\2\2\2\u014d\u014e\3\2\2\2\u014e"+
		"\u014f\3\2\2\2\u014f\u0151\5\t\5\2\u0150\u0152\5\t\5\2\u0151\u0150\3\2"+
		"\2\2\u0151\u0152\3\2\2\2\u0152\u0156\3\2\2\2\u0153\u0155\5\25\13\2\u0154"+
		"\u0153\3\2\2\2\u0155\u0158\3\2\2\2\u0156\u0154\3\2\2\2\u0156\u0157\3\2"+
		"\2\2\u0157\u0159\3\2\2\2\u0158\u0156\3\2\2\2\u0159\u015d\5\31\r\2\u015a"+
		"\u015c\5\25\13\2\u015b\u015a\3\2\2\2\u015c\u015f\3\2\2\2\u015d\u015b\3"+
		"\2\2\2\u015d\u015e\3\2\2\2\u015e\u0160\3\2\2\2\u015f\u015d\3\2\2\2\u0160"+
		"\u0164\5\27\f\2\u0161\u0163\5\25\13\2\u0162\u0161\3\2\2\2\u0163\u0166"+
		"\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165N\3\2\2\2\u0166"+
		"\u0164\3\2\2\2\u0167\u016b\5\5\3\2\u0168\u016a\5\25\13\2\u0169\u0168\3"+
		"\2\2\2\u016a\u016d\3\2\2\2\u016b\u0169\3\2\2\2\u016b\u016c\3\2\2\2\u016c"+
		"\u016f\3\2\2\2\u016d\u016b\3\2\2\2\u016e\u0170\5\33\16\2\u016f\u016e\3"+
		"\2\2\2\u016f\u0170\3\2\2\2\u0170\u0174\3\2\2\2\u0171\u0173\5\25\13\2\u0172"+
		"\u0171\3\2\2\2\u0173\u0176\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175\3\2"+
		"\2\2\u0175\u0178\3\2\2\2\u0176\u0174\3\2\2\2\u0177\u0179\5\21\t\2\u0178"+
		"\u0177\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u017e\5\31"+
		"\r\2\u017b\u017d\5\25\13\2\u017c\u017b\3\2\2\2\u017d\u0180\3\2\2\2\u017e"+
		"\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0181\3\2\2\2\u0180\u017e\3\2"+
		"\2\2\u0181\u0183\5\t\5\2\u0182\u0184\5\t\5\2\u0183\u0182\3\2\2\2\u0183"+
		"\u0184\3\2\2\2\u0184\u0188\3\2\2\2\u0185\u0187\5\25\13\2\u0186\u0185\3"+
		"\2\2\2\u0187\u018a\3\2\2\2\u0188\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189"+
		"\u018b\3\2\2\2\u018a\u0188\3\2\2\2\u018b\u018f\5\27\f\2\u018c\u018e\5"+
		"\25\13\2\u018d\u018c\3\2\2\2\u018e\u0191\3\2\2\2\u018f\u018d\3\2\2\2\u018f"+
		"\u0190\3\2\2\2\u0190P\3\2\2\2\u0191\u018f\3\2\2\2\u0192\u0196\5\5\3\2"+
		"\u0193\u0195\5\25\13\2\u0194\u0193\3\2\2\2\u0195\u0198\3\2\2\2\u0196\u0194"+
		"\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u019a\3\2\2\2\u0198\u0196\3\2\2\2\u0199"+
		"\u019b\5\33\16\2\u019a\u0199\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u019f\3"+
		"\2\2\2\u019c\u019e\5\25\13\2\u019d\u019c\3\2\2\2\u019e\u01a1\3\2\2\2\u019f"+
		"\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a2\3\2\2\2\u01a1\u019f\3\2"+
		"\2\2\u01a2\u01a3\5;\36\2\u01a3\u01a4\5+\26\2\u01a4\u01a5\5;\36\2\u01a5"+
		"\u01a6\5-\27\2\u01a6\u01a8\5\'\24\2\u01a7\u01a9\59\35\2\u01a8\u01a7\3"+
		"\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01ad\3\2\2\2\u01aa\u01ac\5\25\13\2\u01ab"+
		"\u01aa\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2"+
		"\2\2\u01aeR\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b4\5\5\3\2\u01b1\u01b3"+
		"\5\25\13\2\u01b2\u01b1\3\2\2\2\u01b3\u01b6\3\2\2\2\u01b4\u01b2\3\2\2\2"+
		"\u01b4\u01b5\3\2\2\2\u01b5\u01b8\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b7\u01b9"+
		"\5\33\16\2\u01b8\u01b7\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01bd\3\2\2\2"+
		"\u01ba\u01bc\5\25\13\2\u01bb\u01ba\3\2\2\2\u01bc\u01bf\3\2\2\2\u01bd\u01bb"+
		"\3\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01c0\3\2\2\2\u01bf\u01bd\3\2\2\2\u01c0"+
		"\u01c1\5\65\33\2\u01c1\u01c2\5\63\32\2\u01c2\u01c3\5+\26\2\u01c3\u01c4"+
		"\5\61\31\2\u01c4\u01c6\5;\36\2\u01c5\u01c7\59\35\2\u01c6\u01c5\3\2\2\2"+
		"\u01c6\u01c7\3\2\2\2\u01c7\u01cb\3\2\2\2\u01c8\u01ca\5\25\13\2\u01c9\u01c8"+
		"\3\2\2\2\u01ca\u01cd\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc"+
		"T\3\2\2\2\u01cd\u01cb\3\2\2\2\u01ce\u01d2\5\5\3\2\u01cf\u01d1\5\25\13"+
		"\2\u01d0\u01cf\3\2\2\2\u01d1\u01d4\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d2\u01d3"+
		"\3\2\2\2\u01d3\u01d6\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d5\u01d7\5\33\16\2"+
		"\u01d6\u01d5\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01db\3\2\2\2\u01d8\u01da"+
		"\5\25\13\2\u01d9\u01d8\3\2\2\2\u01da\u01dd\3\2\2\2\u01db\u01d9\3\2\2\2"+
		"\u01db\u01dc\3\2\2\2\u01dc\u01de\3\2\2\2\u01dd\u01db\3\2\2\2\u01de\u01df"+
		"\5;\36\2\u01df\u01e0\5A!\2\u01e0\u01e1\5\65\33\2\u01e1\u01e3\5\'\24\2"+
		"\u01e2\u01e4\59\35\2\u01e3\u01e2\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e8"+
		"\3\2\2\2\u01e5\u01e7\5\25\13\2\u01e6\u01e5\3\2\2\2\u01e7\u01ea\3\2\2\2"+
		"\u01e8\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9V\3\2\2\2\u01ea\u01e8\3"+
		"\2\2\2\u01eb\u01ef\5\5\3\2\u01ec\u01ee\5\25\13\2\u01ed\u01ec\3\2\2\2\u01ee"+
		"\u01f1\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01f3\3\2"+
		"\2\2\u01f1\u01ef\3\2\2\2\u01f2\u01f4\5\33\16\2\u01f3\u01f2\3\2\2\2\u01f3"+
		"\u01f4\3\2\2\2\u01f4\u01f8\3\2\2\2\u01f5\u01f7\5\25\13\2\u01f6\u01f5\3"+
		"\2\2\2\u01f7\u01fa\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9"+
		"\u01fb\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fb\u01fc\5\67\34\2\u01fc\u01fd\5"+
		"\37\20\2\u01fd\u01fe\5\61\31\2\u01fe\u01ff\5%\23\2\u01ff\u0200\5\63\32"+
		"\2\u0200\u0205\5/\30\2\u0201\u0202\5+\26\2\u0202\u0203\5C\"\2\u0203\u0204"+
		"\5\'\24\2\u0204\u0206\3\2\2\2\u0205\u0201\3\2\2\2\u0205\u0206\3\2\2\2"+
		"\u0206\u0209\3\2\2\2\u0207\u020a\59\35\2\u0208\u020a\5%\23\2\u0209\u0207"+
		"\3\2\2\2\u0209\u0208\3\2\2\2\u0209\u020a\3\2\2\2\u020a\u020e\3\2\2\2\u020b"+
		"\u020d\5\25\13\2\u020c\u020b\3\2\2\2\u020d\u0210\3\2\2\2\u020e\u020c\3"+
		"\2\2\2\u020e\u020f\3\2\2\2\u020fX\3\2\2\2\u0210\u020e\3\2\2\2\u0211\u0215"+
		"\5\5\3\2\u0212\u0214\5\25\13\2\u0213\u0212\3\2\2\2\u0214\u0217\3\2\2\2"+
		"\u0215\u0213\3\2\2\2\u0215\u0216\3\2\2\2\u0216\u0219\3\2\2\2\u0217\u0215"+
		"\3\2\2\2\u0218\u021a\5\33\16\2\u0219\u0218\3\2\2\2\u0219\u021a\3\2\2\2"+
		"\u021a\u021e\3\2\2\2\u021b\u021d\5\25\13\2\u021c\u021b\3\2\2\2\u021d\u0220"+
		"\3\2\2\2\u021e\u021c\3\2\2\2\u021e\u021f\3\2\2\2\u021f\u0221\3\2\2\2\u0220"+
		"\u021e\3\2\2\2\u0221\u0222\5\37\20\2\u0222\u0223\5\61\31\2\u0223\u0224"+
		"\59\35\2\u0224\u0225\5? \2\u0225\u0226\5\'\24\2\u0226\u0228\5\67\34\2"+
		"\u0227\u0229\59\35\2\u0228\u0227\3\2\2\2\u0228\u0229\3\2\2\2\u0229\u022d"+
		"\3\2\2\2\u022a\u022c\5\25\13\2\u022b\u022a\3\2\2\2\u022c\u022f\3\2\2\2"+
		"\u022d\u022b\3\2\2\2\u022d\u022e\3\2\2\2\u022e\u0230\3\2\2\2\u022f\u022d"+
		"\3\2\2\2\u0230\u0234\5\35\17\2\u0231\u0233\5\5\3\2\u0232\u0231\3\2\2\2"+
		"\u0233\u0236\3\2\2\2\u0234\u0232\3\2\2\2\u0234\u0235\3\2\2\2\u0235Z\3"+
		"\2\2\2\u0236\u0234\3\2\2\2\u0237\u0238\13\2\2\2\u0238\\\3\2\2\2L\2`dm"+
		"rt\u0082\u0086\u00c4\u00c8\u00cd\u00d1\u00d7\u00dd\u00e4\u00eb\u00ef\u00f4"+
		"\u00f8\u00fc\u0101\u0107\u010e\u0115\u0119\u011e\u0122\u0126\u012b\u0132"+
		"\u0139\u0140\u0144\u0149\u014d\u0151\u0156\u015d\u0164\u016b\u016f\u0174"+
		"\u0178\u017e\u0183\u0188\u018f\u0196\u019a\u019f\u01a8\u01ad\u01b4\u01b8"+
		"\u01bd\u01c6\u01cb\u01d2\u01d6\u01db\u01e3\u01e8\u01ef\u01f3\u01f8\u0205"+
		"\u0209\u020e\u0215\u0219\u021e\u0228\u022d\u0234\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}