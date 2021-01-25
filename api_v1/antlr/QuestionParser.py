# Generated from QuestionParser.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\35")
        buf.write("\u01ed\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\5\2,\n\2\3\2\7\2/\n\2\f\2\16")
        buf.write("\2\62\13\2\3\2\5\2\65\n\2\3\2\3\2\3\3\3\3\3\4\5\4<\n\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\5\4C\n\4\3\4\3\4\3\4\5\4H\n\4\3\5")
        buf.write("\3\5\3\6\3\6\5\6N\n\6\3\6\5\6Q\n\6\3\6\5\6T\n\6\3\6\5")
        buf.write("\6W\n\6\3\6\3\6\5\6[\n\6\3\6\5\6^\n\6\3\6\5\6a\n\6\3\6")
        buf.write("\5\6d\n\6\3\6\3\6\5\6h\n\6\3\6\5\6k\n\6\3\6\5\6n\n\6\3")
        buf.write("\6\5\6q\n\6\3\6\3\6\5\6u\n\6\3\6\5\6x\n\6\3\6\5\6{\n\6")
        buf.write("\3\6\5\6~\n\6\3\6\3\6\5\6\u0082\n\6\3\6\5\6\u0085\n\6")
        buf.write("\3\6\5\6\u0088\n\6\3\6\5\6\u008b\n\6\3\6\3\6\5\6\u008f")
        buf.write("\n\6\3\6\5\6\u0092\n\6\3\6\5\6\u0095\n\6\3\6\5\6\u0098")
        buf.write("\n\6\3\6\3\6\5\6\u009c\n\6\3\6\5\6\u009f\n\6\3\6\5\6\u00a2")
        buf.write("\n\6\3\6\5\6\u00a5\n\6\3\6\3\6\5\6\u00a9\n\6\3\6\5\6\u00ac")
        buf.write("\n\6\3\6\5\6\u00af\n\6\3\6\5\6\u00b2\n\6\3\6\3\6\5\6\u00b6")
        buf.write("\n\6\3\6\5\6\u00b9\n\6\3\6\5\6\u00bc\n\6\3\6\5\6\u00bf")
        buf.write("\n\6\3\6\3\6\5\6\u00c3\n\6\3\6\5\6\u00c6\n\6\3\6\5\6\u00c9")
        buf.write("\n\6\3\6\5\6\u00cc\n\6\3\6\3\6\5\6\u00d0\n\6\3\6\5\6\u00d3")
        buf.write("\n\6\3\6\5\6\u00d6\n\6\3\6\5\6\u00d9\n\6\3\6\3\6\5\6\u00dd")
        buf.write("\n\6\3\6\5\6\u00e0\n\6\3\6\5\6\u00e3\n\6\3\6\5\6\u00e6")
        buf.write("\n\6\3\6\3\6\5\6\u00ea\n\6\3\6\5\6\u00ed\n\6\3\6\5\6\u00f0")
        buf.write("\n\6\3\6\5\6\u00f3\n\6\3\6\3\6\5\6\u00f7\n\6\3\6\5\6\u00fa")
        buf.write("\n\6\3\6\5\6\u00fd\n\6\3\6\5\6\u0100\n\6\3\6\3\6\5\6\u0104")
        buf.write("\n\6\3\6\5\6\u0107\n\6\3\6\5\6\u010a\n\6\3\6\5\6\u010d")
        buf.write("\n\6\3\6\3\6\5\6\u0111\n\6\3\6\5\6\u0114\n\6\3\6\5\6\u0117")
        buf.write("\n\6\3\6\5\6\u011a\n\6\3\6\3\6\5\6\u011e\n\6\3\6\5\6\u0121")
        buf.write("\n\6\3\6\5\6\u0124\n\6\3\6\5\6\u0127\n\6\3\6\3\6\5\6\u012b")
        buf.write("\n\6\3\6\5\6\u012e\n\6\3\6\5\6\u0131\n\6\3\6\5\6\u0134")
        buf.write("\n\6\3\6\3\6\5\6\u0138\n\6\3\6\5\6\u013b\n\6\3\6\5\6\u013e")
        buf.write("\n\6\3\6\5\6\u0141\n\6\3\6\3\6\5\6\u0145\n\6\3\6\5\6\u0148")
        buf.write("\n\6\3\6\5\6\u014b\n\6\3\6\5\6\u014e\n\6\3\6\3\6\5\6\u0152")
        buf.write("\n\6\3\6\5\6\u0155\n\6\3\6\5\6\u0158\n\6\3\6\5\6\u015b")
        buf.write("\n\6\3\6\3\6\5\6\u015f\n\6\3\6\5\6\u0162\n\6\3\6\5\6\u0165")
        buf.write("\n\6\3\6\5\6\u0168\n\6\3\6\3\6\5\6\u016c\n\6\3\6\5\6\u016f")
        buf.write("\n\6\3\6\5\6\u0172\n\6\3\6\5\6\u0175\n\6\3\6\3\6\5\6\u0179")
        buf.write("\n\6\3\6\5\6\u017c\n\6\3\6\5\6\u017f\n\6\3\6\5\6\u0182")
        buf.write("\n\6\5\6\u0184\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7")
        buf.write("\u018e\n\7\3\b\3\b\3\t\3\t\3\n\3\n\5\n\u0196\n\n\3\13")
        buf.write("\3\13\6\13\u019a\n\13\r\13\16\13\u019b\3\13\5\13\u019f")
        buf.write("\n\13\3\f\3\f\3\r\3\r\3\r\3\r\6\r\u01a7\n\r\r\r\16\r\u01a8")
        buf.write("\3\r\3\r\6\r\u01ad\n\r\r\r\16\r\u01ae\5\r\u01b1\n\r\3")
        buf.write("\16\3\16\6\16\u01b5\n\16\r\16\16\16\u01b6\3\17\3\17\6")
        buf.write("\17\u01bb\n\17\r\17\16\17\u01bc\3\17\3\17\3\17\6\17\u01c2")
        buf.write("\n\17\r\17\16\17\u01c3\5\17\u01c6\n\17\3\20\3\20\6\20")
        buf.write("\u01ca\n\20\r\20\16\20\u01cb\3\20\5\20\u01cf\n\20\3\21")
        buf.write("\3\21\3\22\3\22\6\22\u01d5\n\22\r\22\16\22\u01d6\3\22")
        buf.write("\5\22\u01da\n\22\3\23\3\23\3\24\3\24\6\24\u01e0\n\24\r")
        buf.write("\24\16\24\u01e1\3\25\3\25\6\25\u01e6\n\25\r\25\16\25\u01e7")
        buf.write("\3\25\5\25\u01eb\n\25\3\25\2\2\26\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(\2\2\2\u0270\2+\3\2\2\2\48\3\2")
        buf.write("\2\2\6G\3\2\2\2\bI\3\2\2\2\n\u0183\3\2\2\2\f\u018d\3\2")
        buf.write("\2\2\16\u018f\3\2\2\2\20\u0191\3\2\2\2\22\u0195\3\2\2")
        buf.write("\2\24\u0197\3\2\2\2\26\u01a0\3\2\2\2\30\u01b0\3\2\2\2")
        buf.write("\32\u01b2\3\2\2\2\34\u01c5\3\2\2\2\36\u01c7\3\2\2\2 \u01d0")
        buf.write("\3\2\2\2\"\u01d2\3\2\2\2$\u01db\3\2\2\2&\u01dd\3\2\2\2")
        buf.write("(\u01e3\3\2\2\2*,\5\4\3\2+*\3\2\2\2+,\3\2\2\2,\60\3\2")
        buf.write("\2\2-/\5\6\4\2.-\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\60\61")
        buf.write("\3\2\2\2\61\64\3\2\2\2\62\60\3\2\2\2\63\65\5&\24\2\64")
        buf.write("\63\3\2\2\2\64\65\3\2\2\2\65\66\3\2\2\2\66\67\7\2\2\3")
        buf.write("\67\3\3\2\2\289\7\r\2\29\5\3\2\2\2:<\5\n\6\2;:\3\2\2\2")
        buf.write(";<\3\2\2\2<=\3\2\2\2=>\5\b\5\2>?\5\24\13\2?@\5\34\17\2")
        buf.write("@H\3\2\2\2AC\5\n\6\2BA\3\2\2\2BC\3\2\2\2CD\3\2\2\2DE\5")
        buf.write("\b\5\2EF\5\24\13\2FH\3\2\2\2G;\3\2\2\2GB\3\2\2\2H\7\3")
        buf.write("\2\2\2IJ\7\4\2\2J\t\3\2\2\2KM\7\3\2\2LN\5\f\7\2ML\3\2")
        buf.write("\2\2MN\3\2\2\2NP\3\2\2\2OQ\5\16\b\2PO\3\2\2\2PQ\3\2\2")
        buf.write("\2QS\3\2\2\2RT\5\20\t\2SR\3\2\2\2ST\3\2\2\2TV\3\2\2\2")
        buf.write("UW\5\22\n\2VU\3\2\2\2VW\3\2\2\2W\u0184\3\2\2\2XZ\7\3\2")
        buf.write("\2Y[\5\f\7\2ZY\3\2\2\2Z[\3\2\2\2[]\3\2\2\2\\^\5\16\b\2")
        buf.write("]\\\3\2\2\2]^\3\2\2\2^`\3\2\2\2_a\5\22\n\2`_\3\2\2\2`")
        buf.write("a\3\2\2\2ac\3\2\2\2bd\5\20\t\2cb\3\2\2\2cd\3\2\2\2d\u0184")
        buf.write("\3\2\2\2eg\7\3\2\2fh\5\f\7\2gf\3\2\2\2gh\3\2\2\2hj\3\2")
        buf.write("\2\2ik\5\20\t\2ji\3\2\2\2jk\3\2\2\2km\3\2\2\2ln\5\16\b")
        buf.write("\2ml\3\2\2\2mn\3\2\2\2np\3\2\2\2oq\5\22\n\2po\3\2\2\2")
        buf.write("pq\3\2\2\2q\u0184\3\2\2\2rt\7\3\2\2su\5\f\7\2ts\3\2\2")
        buf.write("\2tu\3\2\2\2uw\3\2\2\2vx\5\20\t\2wv\3\2\2\2wx\3\2\2\2")
        buf.write("xz\3\2\2\2y{\5\22\n\2zy\3\2\2\2z{\3\2\2\2{}\3\2\2\2|~")
        buf.write("\5\16\b\2}|\3\2\2\2}~\3\2\2\2~\u0184\3\2\2\2\177\u0081")
        buf.write("\7\3\2\2\u0080\u0082\5\f\7\2\u0081\u0080\3\2\2\2\u0081")
        buf.write("\u0082\3\2\2\2\u0082\u0084\3\2\2\2\u0083\u0085\5\22\n")
        buf.write("\2\u0084\u0083\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0087")
        buf.write("\3\2\2\2\u0086\u0088\5\16\b\2\u0087\u0086\3\2\2\2\u0087")
        buf.write("\u0088\3\2\2\2\u0088\u008a\3\2\2\2\u0089\u008b\5\20\t")
        buf.write("\2\u008a\u0089\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u0184")
        buf.write("\3\2\2\2\u008c\u008e\7\3\2\2\u008d\u008f\5\f\7\2\u008e")
        buf.write("\u008d\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0091\3\2\2\2")
        buf.write("\u0090\u0092\5\22\n\2\u0091\u0090\3\2\2\2\u0091\u0092")
        buf.write("\3\2\2\2\u0092\u0094\3\2\2\2\u0093\u0095\5\20\t\2\u0094")
        buf.write("\u0093\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0097\3\2\2\2")
        buf.write("\u0096\u0098\5\16\b\2\u0097\u0096\3\2\2\2\u0097\u0098")
        buf.write("\3\2\2\2\u0098\u0184\3\2\2\2\u0099\u009b\7\3\2\2\u009a")
        buf.write("\u009c\5\16\b\2\u009b\u009a\3\2\2\2\u009b\u009c\3\2\2")
        buf.write("\2\u009c\u009e\3\2\2\2\u009d\u009f\5\f\7\2\u009e\u009d")
        buf.write("\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a1\3\2\2\2\u00a0")
        buf.write("\u00a2\5\20\t\2\u00a1\u00a0\3\2\2\2\u00a1\u00a2\3\2\2")
        buf.write("\2\u00a2\u00a4\3\2\2\2\u00a3\u00a5\5\22\n\2\u00a4\u00a3")
        buf.write("\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u0184\3\2\2\2\u00a6")
        buf.write("\u00a8\7\3\2\2\u00a7\u00a9\5\16\b\2\u00a8\u00a7\3\2\2")
        buf.write("\2\u00a8\u00a9\3\2\2\2\u00a9\u00ab\3\2\2\2\u00aa\u00ac")
        buf.write("\5\f\7\2\u00ab\u00aa\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac")
        buf.write("\u00ae\3\2\2\2\u00ad\u00af\5\22\n\2\u00ae\u00ad\3\2\2")
        buf.write("\2\u00ae\u00af\3\2\2\2\u00af\u00b1\3\2\2\2\u00b0\u00b2")
        buf.write("\5\20\t\2\u00b1\u00b0\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2")
        buf.write("\u0184\3\2\2\2\u00b3\u00b5\7\3\2\2\u00b4\u00b6\5\16\b")
        buf.write("\2\u00b5\u00b4\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b8")
        buf.write("\3\2\2\2\u00b7\u00b9\5\20\t\2\u00b8\u00b7\3\2\2\2\u00b8")
        buf.write("\u00b9\3\2\2\2\u00b9\u00bb\3\2\2\2\u00ba\u00bc\5\f\7\2")
        buf.write("\u00bb\u00ba\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00be\3")
        buf.write("\2\2\2\u00bd\u00bf\5\22\n\2\u00be\u00bd\3\2\2\2\u00be")
        buf.write("\u00bf\3\2\2\2\u00bf\u0184\3\2\2\2\u00c0\u00c2\7\3\2\2")
        buf.write("\u00c1\u00c3\5\16\b\2\u00c2\u00c1\3\2\2\2\u00c2\u00c3")
        buf.write("\3\2\2\2\u00c3\u00c5\3\2\2\2\u00c4\u00c6\5\20\t\2\u00c5")
        buf.write("\u00c4\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c8\3\2\2\2")
        buf.write("\u00c7\u00c9\5\22\n\2\u00c8\u00c7\3\2\2\2\u00c8\u00c9")
        buf.write("\3\2\2\2\u00c9\u00cb\3\2\2\2\u00ca\u00cc\5\f\7\2\u00cb")
        buf.write("\u00ca\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u0184\3\2\2\2")
        buf.write("\u00cd\u00cf\7\3\2\2\u00ce\u00d0\5\16\b\2\u00cf\u00ce")
        buf.write("\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d2\3\2\2\2\u00d1")
        buf.write("\u00d3\5\22\n\2\u00d2\u00d1\3\2\2\2\u00d2\u00d3\3\2\2")
        buf.write("\2\u00d3\u00d5\3\2\2\2\u00d4\u00d6\5\f\7\2\u00d5\u00d4")
        buf.write("\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d8\3\2\2\2\u00d7")
        buf.write("\u00d9\5\20\t\2\u00d8\u00d7\3\2\2\2\u00d8\u00d9\3\2\2")
        buf.write("\2\u00d9\u0184\3\2\2\2\u00da\u00dc\7\3\2\2\u00db\u00dd")
        buf.write("\5\16\b\2\u00dc\u00db\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd")
        buf.write("\u00df\3\2\2\2\u00de\u00e0\5\22\n\2\u00df\u00de\3\2\2")
        buf.write("\2\u00df\u00e0\3\2\2\2\u00e0\u00e2\3\2\2\2\u00e1\u00e3")
        buf.write("\5\20\t\2\u00e2\u00e1\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3")
        buf.write("\u00e5\3\2\2\2\u00e4\u00e6\5\f\7\2\u00e5\u00e4\3\2\2\2")
        buf.write("\u00e5\u00e6\3\2\2\2\u00e6\u0184\3\2\2\2\u00e7\u00e9\7")
        buf.write("\3\2\2\u00e8\u00ea\5\20\t\2\u00e9\u00e8\3\2\2\2\u00e9")
        buf.write("\u00ea\3\2\2\2\u00ea\u00ec\3\2\2\2\u00eb\u00ed\5\f\7\2")
        buf.write("\u00ec\u00eb\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00ef\3")
        buf.write("\2\2\2\u00ee\u00f0\5\16\b\2\u00ef\u00ee\3\2\2\2\u00ef")
        buf.write("\u00f0\3\2\2\2\u00f0\u00f2\3\2\2\2\u00f1\u00f3\5\22\n")
        buf.write("\2\u00f2\u00f1\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u0184")
        buf.write("\3\2\2\2\u00f4\u00f6\7\3\2\2\u00f5\u00f7\5\20\t\2\u00f6")
        buf.write("\u00f5\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f9\3\2\2\2")
        buf.write("\u00f8\u00fa\5\f\7\2\u00f9\u00f8\3\2\2\2\u00f9\u00fa\3")
        buf.write("\2\2\2\u00fa\u00fc\3\2\2\2\u00fb\u00fd\5\22\n\2\u00fc")
        buf.write("\u00fb\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00ff\3\2\2\2")
        buf.write("\u00fe\u0100\5\16\b\2\u00ff\u00fe\3\2\2\2\u00ff\u0100")
        buf.write("\3\2\2\2\u0100\u0184\3\2\2\2\u0101\u0103\7\3\2\2\u0102")
        buf.write("\u0104\5\20\t\2\u0103\u0102\3\2\2\2\u0103\u0104\3\2\2")
        buf.write("\2\u0104\u0106\3\2\2\2\u0105\u0107\5\16\b\2\u0106\u0105")
        buf.write("\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0109\3\2\2\2\u0108")
        buf.write("\u010a\5\f\7\2\u0109\u0108\3\2\2\2\u0109\u010a\3\2\2\2")
        buf.write("\u010a\u010c\3\2\2\2\u010b\u010d\5\22\n\2\u010c\u010b")
        buf.write("\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u0184\3\2\2\2\u010e")
        buf.write("\u0110\7\3\2\2\u010f\u0111\5\20\t\2\u0110\u010f\3\2\2")
        buf.write("\2\u0110\u0111\3\2\2\2\u0111\u0113\3\2\2\2\u0112\u0114")
        buf.write("\5\16\b\2\u0113\u0112\3\2\2\2\u0113\u0114\3\2\2\2\u0114")
        buf.write("\u0116\3\2\2\2\u0115\u0117\5\22\n\2\u0116\u0115\3\2\2")
        buf.write("\2\u0116\u0117\3\2\2\2\u0117\u0119\3\2\2\2\u0118\u011a")
        buf.write("\5\f\7\2\u0119\u0118\3\2\2\2\u0119\u011a\3\2\2\2\u011a")
        buf.write("\u0184\3\2\2\2\u011b\u011d\7\3\2\2\u011c\u011e\5\20\t")
        buf.write("\2\u011d\u011c\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u0120")
        buf.write("\3\2\2\2\u011f\u0121\5\22\n\2\u0120\u011f\3\2\2\2\u0120")
        buf.write("\u0121\3\2\2\2\u0121\u0123\3\2\2\2\u0122\u0124\5\f\7\2")
        buf.write("\u0123\u0122\3\2\2\2\u0123\u0124\3\2\2\2\u0124\u0126\3")
        buf.write("\2\2\2\u0125\u0127\5\16\b\2\u0126\u0125\3\2\2\2\u0126")
        buf.write("\u0127\3\2\2\2\u0127\u0184\3\2\2\2\u0128\u012a\7\3\2\2")
        buf.write("\u0129\u012b\5\20\t\2\u012a\u0129\3\2\2\2\u012a\u012b")
        buf.write("\3\2\2\2\u012b\u012d\3\2\2\2\u012c\u012e\5\22\n\2\u012d")
        buf.write("\u012c\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u0130\3\2\2\2")
        buf.write("\u012f\u0131\5\16\b\2\u0130\u012f\3\2\2\2\u0130\u0131")
        buf.write("\3\2\2\2\u0131\u0133\3\2\2\2\u0132\u0134\5\f\7\2\u0133")
        buf.write("\u0132\3\2\2\2\u0133\u0134\3\2\2\2\u0134\u0184\3\2\2\2")
        buf.write("\u0135\u0137\7\3\2\2\u0136\u0138\5\22\n\2\u0137\u0136")
        buf.write("\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u013a\3\2\2\2\u0139")
        buf.write("\u013b\5\f\7\2\u013a\u0139\3\2\2\2\u013a\u013b\3\2\2\2")
        buf.write("\u013b\u013d\3\2\2\2\u013c\u013e\5\16\b\2\u013d\u013c")
        buf.write("\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u0140\3\2\2\2\u013f")
        buf.write("\u0141\5\20\t\2\u0140\u013f\3\2\2\2\u0140\u0141\3\2\2")
        buf.write("\2\u0141\u0184\3\2\2\2\u0142\u0144\7\3\2\2\u0143\u0145")
        buf.write("\5\22\n\2\u0144\u0143\3\2\2\2\u0144\u0145\3\2\2\2\u0145")
        buf.write("\u0147\3\2\2\2\u0146\u0148\5\f\7\2\u0147\u0146\3\2\2\2")
        buf.write("\u0147\u0148\3\2\2\2\u0148\u014a\3\2\2\2\u0149\u014b\5")
        buf.write("\20\t\2\u014a\u0149\3\2\2\2\u014a\u014b\3\2\2\2\u014b")
        buf.write("\u014d\3\2\2\2\u014c\u014e\5\16\b\2\u014d\u014c\3\2\2")
        buf.write("\2\u014d\u014e\3\2\2\2\u014e\u0184\3\2\2\2\u014f\u0151")
        buf.write("\7\3\2\2\u0150\u0152\5\22\n\2\u0151\u0150\3\2\2\2\u0151")
        buf.write("\u0152\3\2\2\2\u0152\u0154\3\2\2\2\u0153\u0155\5\16\b")
        buf.write("\2\u0154\u0153\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0157")
        buf.write("\3\2\2\2\u0156\u0158\5\f\7\2\u0157\u0156\3\2\2\2\u0157")
        buf.write("\u0158\3\2\2\2\u0158\u015a\3\2\2\2\u0159\u015b\5\20\t")
        buf.write("\2\u015a\u0159\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u0184")
        buf.write("\3\2\2\2\u015c\u015e\7\3\2\2\u015d\u015f\5\22\n\2\u015e")
        buf.write("\u015d\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u0161\3\2\2\2")
        buf.write("\u0160\u0162\5\16\b\2\u0161\u0160\3\2\2\2\u0161\u0162")
        buf.write("\3\2\2\2\u0162\u0164\3\2\2\2\u0163\u0165\5\20\t\2\u0164")
        buf.write("\u0163\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0167\3\2\2\2")
        buf.write("\u0166\u0168\5\f\7\2\u0167\u0166\3\2\2\2\u0167\u0168\3")
        buf.write("\2\2\2\u0168\u0184\3\2\2\2\u0169\u016b\7\3\2\2\u016a\u016c")
        buf.write("\5\22\n\2\u016b\u016a\3\2\2\2\u016b\u016c\3\2\2\2\u016c")
        buf.write("\u016e\3\2\2\2\u016d\u016f\5\20\t\2\u016e\u016d\3\2\2")
        buf.write("\2\u016e\u016f\3\2\2\2\u016f\u0171\3\2\2\2\u0170\u0172")
        buf.write("\5\f\7\2\u0171\u0170\3\2\2\2\u0171\u0172\3\2\2\2\u0172")
        buf.write("\u0174\3\2\2\2\u0173\u0175\5\16\b\2\u0174\u0173\3\2\2")
        buf.write("\2\u0174\u0175\3\2\2\2\u0175\u0184\3\2\2\2\u0176\u0178")
        buf.write("\7\3\2\2\u0177\u0179\5\22\n\2\u0178\u0177\3\2\2\2\u0178")
        buf.write("\u0179\3\2\2\2\u0179\u017b\3\2\2\2\u017a\u017c\5\20\t")
        buf.write("\2\u017b\u017a\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017e")
        buf.write("\3\2\2\2\u017d\u017f\5\16\b\2\u017e\u017d\3\2\2\2\u017e")
        buf.write("\u017f\3\2\2\2\u017f\u0181\3\2\2\2\u0180\u0182\5\f\7\2")
        buf.write("\u0181\u0180\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0184\3")
        buf.write("\2\2\2\u0183K\3\2\2\2\u0183X\3\2\2\2\u0183e\3\2\2\2\u0183")
        buf.write("r\3\2\2\2\u0183\177\3\2\2\2\u0183\u008c\3\2\2\2\u0183")
        buf.write("\u0099\3\2\2\2\u0183\u00a6\3\2\2\2\u0183\u00b3\3\2\2\2")
        buf.write("\u0183\u00c0\3\2\2\2\u0183\u00cd\3\2\2\2\u0183\u00da\3")
        buf.write("\2\2\2\u0183\u00e7\3\2\2\2\u0183\u00f4\3\2\2\2\u0183\u0101")
        buf.write("\3\2\2\2\u0183\u010e\3\2\2\2\u0183\u011b\3\2\2\2\u0183")
        buf.write("\u0128\3\2\2\2\u0183\u0135\3\2\2\2\u0183\u0142\3\2\2\2")
        buf.write("\u0183\u014f\3\2\2\2\u0183\u015c\3\2\2\2\u0183\u0169\3")
        buf.write("\2\2\2\u0183\u0176\3\2\2\2\u0184\13\3\2\2\2\u0185\u018e")
        buf.write("\7\22\2\2\u0186\u018e\7\23\2\2\u0187\u018e\7\24\2\2\u0188")
        buf.write("\u018e\7\25\2\2\u0189\u018e\7\26\2\2\u018a\u018e\7\27")
        buf.write("\2\2\u018b\u018e\7\30\2\2\u018c\u018e\7\31\2\2\u018d\u0185")
        buf.write("\3\2\2\2\u018d\u0186\3\2\2\2\u018d\u0187\3\2\2\2\u018d")
        buf.write("\u0188\3\2\2\2\u018d\u0189\3\2\2\2\u018d\u018a\3\2\2\2")
        buf.write("\u018d\u018b\3\2\2\2\u018d\u018c\3\2\2\2\u018e\r\3\2\2")
        buf.write("\2\u018f\u0190\7\16\2\2\u0190\17\3\2\2\2\u0191\u0192\7")
        buf.write("\17\2\2\u0192\21\3\2\2\2\u0193\u0196\7\20\2\2\u0194\u0196")
        buf.write("\7\21\2\2\u0195\u0193\3\2\2\2\u0195\u0194\3\2\2\2\u0196")
        buf.write("\23\3\2\2\2\u0197\u0199\5\26\f\2\u0198\u019a\5\30\r\2")
        buf.write("\u0199\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u0199\3")
        buf.write("\2\2\2\u019b\u019c\3\2\2\2\u019c\u019e\3\2\2\2\u019d\u019f")
        buf.write("\5\32\16\2\u019e\u019d\3\2\2\2\u019e\u019f\3\2\2\2\u019f")
        buf.write("\25\3\2\2\2\u01a0\u01a1\7\6\2\2\u01a1\27\3\2\2\2\u01a2")
        buf.write("\u01b1\7\b\2\2\u01a3\u01b1\7\t\2\2\u01a4\u01a6\7\13\2")
        buf.write("\2\u01a5\u01a7\7\n\2\2\u01a6\u01a5\3\2\2\2\u01a7\u01a8")
        buf.write("\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9")
        buf.write("\u01aa\3\2\2\2\u01aa\u01b1\7\f\2\2\u01ab\u01ad\7\n\2\2")
        buf.write("\u01ac\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01ac\3")
        buf.write("\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b1\3\2\2\2\u01b0\u01a2")
        buf.write("\3\2\2\2\u01b0\u01a3\3\2\2\2\u01b0\u01a4\3\2\2\2\u01b0")
        buf.write("\u01ac\3\2\2\2\u01b1\31\3\2\2\2\u01b2\u01b4\7\7\2\2\u01b3")
        buf.write("\u01b5\5\30\r\2\u01b4\u01b3\3\2\2\2\u01b5\u01b6\3\2\2")
        buf.write("\2\u01b6\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\33\3")
        buf.write("\2\2\2\u01b8\u01ba\7\32\2\2\u01b9\u01bb\5\36\20\2\u01ba")
        buf.write("\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01ba\3\2\2\2")
        buf.write("\u01bc\u01bd\3\2\2\2\u01bd\u01c6\3\2\2\2\u01be\u01c1\7")
        buf.write("\32\2\2\u01bf\u01c2\5\"\22\2\u01c0\u01c2\5\36\20\2\u01c1")
        buf.write("\u01bf\3\2\2\2\u01c1\u01c0\3\2\2\2\u01c2\u01c3\3\2\2\2")
        buf.write("\u01c3\u01c1\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c6\3")
        buf.write("\2\2\2\u01c5\u01b8\3\2\2\2\u01c5\u01be\3\2\2\2\u01c6\35")
        buf.write("\3\2\2\2\u01c7\u01c9\5 \21\2\u01c8\u01ca\5\30\r\2\u01c9")
        buf.write("\u01c8\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01c9\3\2\2\2")
        buf.write("\u01cb\u01cc\3\2\2\2\u01cc\u01ce\3\2\2\2\u01cd\u01cf\5")
        buf.write("\32\16\2\u01ce\u01cd\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf")
        buf.write("\37\3\2\2\2\u01d0\u01d1\7\34\2\2\u01d1!\3\2\2\2\u01d2")
        buf.write("\u01d4\5$\23\2\u01d3\u01d5\5\30\r\2\u01d4\u01d3\3\2\2")
        buf.write("\2\u01d5\u01d6\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d7")
        buf.write("\3\2\2\2\u01d7\u01d9\3\2\2\2\u01d8\u01da\5\32\16\2\u01d9")
        buf.write("\u01d8\3\2\2\2\u01d9\u01da\3\2\2\2\u01da#\3\2\2\2\u01db")
        buf.write("\u01dc\7\33\2\2\u01dc%\3\2\2\2\u01dd\u01df\7\5\2\2\u01de")
        buf.write("\u01e0\5(\25\2\u01df\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2")
        buf.write("\u01e1\u01df\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\'\3\2\2")
        buf.write("\2\u01e3\u01e5\5\26\f\2\u01e4\u01e6\5\30\r\2\u01e5\u01e4")
        buf.write("\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e7")
        buf.write("\u01e8\3\2\2\2\u01e8\u01ea\3\2\2\2\u01e9\u01eb\5\32\16")
        buf.write("\2\u01ea\u01e9\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb)\3\2")
        buf.write("\2\2|+\60\64;BGMPSVZ]`cgjmptwz}\u0081\u0084\u0087\u008a")
        buf.write("\u008e\u0091\u0094\u0097\u009b\u009e\u00a1\u00a4\u00a8")
        buf.write("\u00ab\u00ae\u00b1\u00b5\u00b8\u00bb\u00be\u00c2\u00c5")
        buf.write("\u00c8\u00cb\u00cf\u00d2\u00d5\u00d8\u00dc\u00df\u00e2")
        buf.write("\u00e5\u00e9\u00ec\u00ef\u00f2\u00f6\u00f9\u00fc\u00ff")
        buf.write("\u0103\u0106\u0109\u010c\u0110\u0113\u0116\u0119\u011d")
        buf.write("\u0120\u0123\u0126\u012a\u012d\u0130\u0133\u0137\u013a")
        buf.write("\u013d\u0140\u0144\u0147\u014a\u014d\u0151\u0154\u0157")
        buf.write("\u015a\u015e\u0161\u0164\u0167\u016b\u016e\u0171\u0174")
        buf.write("\u0178\u017b\u017e\u0181\u0183\u018d\u0195\u019b\u019e")
        buf.write("\u01a8\u01ae\u01b0\u01b6\u01bc\u01c1\u01c3\u01c5\u01cb")
        buf.write("\u01ce\u01d6\u01d9\u01e1\u01e7\u01ea")
        return buf.getvalue()


class QuestionParser ( Parser ):

    grammarFileName = "QuestionParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'##########_START_QUESTION_##########'" ]

    symbolicNames = [ "<INVALID>", "START_QUESTION_HEADER", "START_QUESTION", 
                      "END_ANSWERS", "QUESTION_PREFIX", "FEEDBACK_MARKER", 
                      "MEDIA", "HYPERLINK", "ALL_CHARACTER", "ESCAPED_OPEN_BRACKET", 
                      "ESCAPED_CLOSE_BRACKET", "SECTION_TITLE", "TITLE", 
                      "POINTS", "RANDOMIZE_TRUE", "RANDOMIZE_FALSE", "TYPE_MC", 
                      "TYPE_TF", "TYPE_MS", "TYPE_MT", "TYPE_ORD", "TYPE_FIB", 
                      "TYPE_WR", "TYPE_OTHER", "START_ANSWER", "RIGHT_ANSWER", 
                      "LIST_PREFIX", "DEFAULT_START_HEADER" ]

    RULE_parse_question = 0
    RULE_section_title = 1
    RULE_question = 2
    RULE_start_question = 3
    RULE_question_header = 4
    RULE_question_type = 5
    RULE_title = 6
    RULE_points = 7
    RULE_randomize = 8
    RULE_question_body = 9
    RULE_question_prefix = 10
    RULE_content = 11
    RULE_feedback = 12
    RULE_answer_list = 13
    RULE_list_item = 14
    RULE_list_prefix = 15
    RULE_list_answer_item = 16
    RULE_answer_prefix = 17
    RULE_end_answers = 18
    RULE_end_answers_item = 19

    ruleNames =  [ "parse_question", "section_title", "question", "start_question", 
                   "question_header", "question_type", "title", "points", 
                   "randomize", "question_body", "question_prefix", "content", 
                   "feedback", "answer_list", "list_item", "list_prefix", 
                   "list_answer_item", "answer_prefix", "end_answers", "end_answers_item" ]

    EOF = Token.EOF
    START_QUESTION_HEADER=1
    START_QUESTION=2
    END_ANSWERS=3
    QUESTION_PREFIX=4
    FEEDBACK_MARKER=5
    MEDIA=6
    HYPERLINK=7
    ALL_CHARACTER=8
    ESCAPED_OPEN_BRACKET=9
    ESCAPED_CLOSE_BRACKET=10
    SECTION_TITLE=11
    TITLE=12
    POINTS=13
    RANDOMIZE_TRUE=14
    RANDOMIZE_FALSE=15
    TYPE_MC=16
    TYPE_TF=17
    TYPE_MS=18
    TYPE_MT=19
    TYPE_ORD=20
    TYPE_FIB=21
    TYPE_WR=22
    TYPE_OTHER=23
    START_ANSWER=24
    RIGHT_ANSWER=25
    LIST_PREFIX=26
    DEFAULT_START_HEADER=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Parse_questionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(QuestionParser.EOF, 0)

        def section_title(self):
            return self.getTypedRuleContext(QuestionParser.Section_titleContext,0)


        def question(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuestionParser.QuestionContext)
            else:
                return self.getTypedRuleContext(QuestionParser.QuestionContext,i)


        def end_answers(self):
            return self.getTypedRuleContext(QuestionParser.End_answersContext,0)


        def getRuleIndex(self):
            return QuestionParser.RULE_parse_question

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParse_question" ):
                listener.enterParse_question(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParse_question" ):
                listener.exitParse_question(self)




    def parse_question(self):

        localctx = QuestionParser.Parse_questionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse_question)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.SECTION_TITLE:
                self.state = 40
                self.section_title()


            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==QuestionParser.START_QUESTION_HEADER or _la==QuestionParser.START_QUESTION:
                self.state = 43
                self.question()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.END_ANSWERS:
                self.state = 49
                self.end_answers()


            self.state = 52
            self.match(QuestionParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Section_titleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SECTION_TITLE(self):
            return self.getToken(QuestionParser.SECTION_TITLE, 0)

        def getRuleIndex(self):
            return QuestionParser.RULE_section_title

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSection_title" ):
                listener.enterSection_title(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSection_title" ):
                listener.exitSection_title(self)




    def section_title(self):

        localctx = QuestionParser.Section_titleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_section_title)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(QuestionParser.SECTION_TITLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuestionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def start_question(self):
            return self.getTypedRuleContext(QuestionParser.Start_questionContext,0)


        def question_body(self):
            return self.getTypedRuleContext(QuestionParser.Question_bodyContext,0)


        def answer_list(self):
            return self.getTypedRuleContext(QuestionParser.Answer_listContext,0)


        def question_header(self):
            return self.getTypedRuleContext(QuestionParser.Question_headerContext,0)


        def getRuleIndex(self):
            return QuestionParser.RULE_question

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuestion" ):
                listener.enterQuestion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuestion" ):
                listener.exitQuestion(self)




    def question(self):

        localctx = QuestionParser.QuestionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_question)
        self._la = 0 # Token type
        try:
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.START_QUESTION_HEADER:
                    self.state = 56
                    self.question_header()


                self.state = 59
                self.start_question()
                self.state = 60
                self.question_body()
                self.state = 61
                self.answer_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.START_QUESTION_HEADER:
                    self.state = 63
                    self.question_header()


                self.state = 66
                self.start_question()
                self.state = 67
                self.question_body()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Start_questionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def START_QUESTION(self):
            return self.getToken(QuestionParser.START_QUESTION, 0)

        def getRuleIndex(self):
            return QuestionParser.RULE_start_question

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart_question" ):
                listener.enterStart_question(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart_question" ):
                listener.exitStart_question(self)




    def start_question(self):

        localctx = QuestionParser.Start_questionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_start_question)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(QuestionParser.START_QUESTION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Question_headerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def START_QUESTION_HEADER(self):
            return self.getToken(QuestionParser.START_QUESTION_HEADER, 0)

        def question_type(self):
            return self.getTypedRuleContext(QuestionParser.Question_typeContext,0)


        def title(self):
            return self.getTypedRuleContext(QuestionParser.TitleContext,0)


        def points(self):
            return self.getTypedRuleContext(QuestionParser.PointsContext,0)


        def randomize(self):
            return self.getTypedRuleContext(QuestionParser.RandomizeContext,0)


        def getRuleIndex(self):
            return QuestionParser.RULE_question_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuestion_header" ):
                listener.enterQuestion_header(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuestion_header" ):
                listener.exitQuestion_header(self)




    def question_header(self):

        localctx = QuestionParser.Question_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_question_header)
        self._la = 0 # Token type
        try:
            self.state = 385
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,102,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 74
                    self.question_type()


                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 77
                    self.title()


                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 80
                    self.points()


                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 83
                    self.randomize()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 87
                    self.question_type()


                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 90
                    self.title()


                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 93
                    self.randomize()


                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 96
                    self.points()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 99
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 100
                    self.question_type()


                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 103
                    self.points()


                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 106
                    self.title()


                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 109
                    self.randomize()


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 112
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 113
                    self.question_type()


                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 116
                    self.points()


                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 119
                    self.randomize()


                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 122
                    self.title()


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 125
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 126
                    self.question_type()


                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 129
                    self.randomize()


                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 132
                    self.title()


                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 135
                    self.points()


                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 138
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 139
                    self.question_type()


                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 142
                    self.randomize()


                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 145
                    self.points()


                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 148
                    self.title()


                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 151
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 152
                    self.title()


                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 155
                    self.question_type()


                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 158
                    self.points()


                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 161
                    self.randomize()


                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 164
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 165
                    self.title()


                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 168
                    self.question_type()


                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 171
                    self.randomize()


                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 174
                    self.points()


                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 177
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 178
                    self.title()


                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 181
                    self.points()


                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 184
                    self.question_type()


                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 187
                    self.randomize()


                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 190
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 191
                    self.title()


                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 194
                    self.points()


                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 197
                    self.randomize()


                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 200
                    self.question_type()


                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 203
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 204
                    self.title()


                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 207
                    self.randomize()


                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 210
                    self.question_type()


                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 213
                    self.points()


                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 216
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 217
                    self.title()


                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 220
                    self.randomize()


                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 223
                    self.points()


                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 226
                    self.question_type()


                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 229
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 230
                    self.points()


                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 233
                    self.question_type()


                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 236
                    self.title()


                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 239
                    self.randomize()


                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 242
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 243
                    self.points()


                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 246
                    self.question_type()


                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 249
                    self.randomize()


                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 252
                    self.title()


                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 255
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 257
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 256
                    self.points()


                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 259
                    self.title()


                self.state = 263
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 262
                    self.question_type()


                self.state = 266
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 265
                    self.randomize()


                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 268
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 270
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 269
                    self.points()


                self.state = 273
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 272
                    self.title()


                self.state = 276
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 275
                    self.randomize()


                self.state = 279
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 278
                    self.question_type()


                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 281
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 283
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 282
                    self.points()


                self.state = 286
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 285
                    self.randomize()


                self.state = 289
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 288
                    self.question_type()


                self.state = 292
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 291
                    self.title()


                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 294
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 296
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 295
                    self.points()


                self.state = 299
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 298
                    self.randomize()


                self.state = 302
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 301
                    self.title()


                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 304
                    self.question_type()


                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 307
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 308
                    self.randomize()


                self.state = 312
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 311
                    self.question_type()


                self.state = 315
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 314
                    self.title()


                self.state = 318
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 317
                    self.points()


                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 320
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 322
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 321
                    self.randomize()


                self.state = 325
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 324
                    self.question_type()


                self.state = 328
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 327
                    self.points()


                self.state = 331
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 330
                    self.title()


                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)
                self.state = 333
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 335
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 334
                    self.randomize()


                self.state = 338
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 337
                    self.title()


                self.state = 341
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 340
                    self.question_type()


                self.state = 344
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 343
                    self.points()


                pass

            elif la_ == 22:
                self.enterOuterAlt(localctx, 22)
                self.state = 346
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 348
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 347
                    self.randomize()


                self.state = 351
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 350
                    self.title()


                self.state = 354
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 353
                    self.points()


                self.state = 357
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 356
                    self.question_type()


                pass

            elif la_ == 23:
                self.enterOuterAlt(localctx, 23)
                self.state = 359
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 361
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 360
                    self.randomize()


                self.state = 364
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 363
                    self.points()


                self.state = 367
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 366
                    self.question_type()


                self.state = 370
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 369
                    self.title()


                pass

            elif la_ == 24:
                self.enterOuterAlt(localctx, 24)
                self.state = 372
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 374
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 373
                    self.randomize()


                self.state = 377
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 376
                    self.points()


                self.state = 380
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 379
                    self.title()


                self.state = 383
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 382
                    self.question_type()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Question_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return QuestionParser.RULE_question_type

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TypeWrContext(Question_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuestionParser.Question_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TYPE_WR(self):
            return self.getToken(QuestionParser.TYPE_WR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeWr" ):
                listener.enterTypeWr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeWr" ):
                listener.exitTypeWr(self)


    class TypeOtherContext(Question_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuestionParser.Question_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TYPE_OTHER(self):
            return self.getToken(QuestionParser.TYPE_OTHER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeOther" ):
                listener.enterTypeOther(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeOther" ):
                listener.exitTypeOther(self)


    class TypeMcContext(Question_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuestionParser.Question_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TYPE_MC(self):
            return self.getToken(QuestionParser.TYPE_MC, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeMc" ):
                listener.enterTypeMc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeMc" ):
                listener.exitTypeMc(self)


    class TypeMsContext(Question_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuestionParser.Question_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TYPE_MS(self):
            return self.getToken(QuestionParser.TYPE_MS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeMs" ):
                listener.enterTypeMs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeMs" ):
                listener.exitTypeMs(self)


    class TypeMtContext(Question_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuestionParser.Question_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TYPE_MT(self):
            return self.getToken(QuestionParser.TYPE_MT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeMt" ):
                listener.enterTypeMt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeMt" ):
                listener.exitTypeMt(self)


    class TypeTfContext(Question_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuestionParser.Question_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TYPE_TF(self):
            return self.getToken(QuestionParser.TYPE_TF, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeTf" ):
                listener.enterTypeTf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeTf" ):
                listener.exitTypeTf(self)


    class TypeOrdContext(Question_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuestionParser.Question_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TYPE_ORD(self):
            return self.getToken(QuestionParser.TYPE_ORD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeOrd" ):
                listener.enterTypeOrd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeOrd" ):
                listener.exitTypeOrd(self)


    class TypeFibContext(Question_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuestionParser.Question_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TYPE_FIB(self):
            return self.getToken(QuestionParser.TYPE_FIB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeFib" ):
                listener.enterTypeFib(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeFib" ):
                listener.exitTypeFib(self)



    def question_type(self):

        localctx = QuestionParser.Question_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_question_type)
        try:
            self.state = 395
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuestionParser.TYPE_MC]:
                localctx = QuestionParser.TypeMcContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.match(QuestionParser.TYPE_MC)
                pass
            elif token in [QuestionParser.TYPE_TF]:
                localctx = QuestionParser.TypeTfContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self.match(QuestionParser.TYPE_TF)
                pass
            elif token in [QuestionParser.TYPE_MS]:
                localctx = QuestionParser.TypeMsContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 389
                self.match(QuestionParser.TYPE_MS)
                pass
            elif token in [QuestionParser.TYPE_MT]:
                localctx = QuestionParser.TypeMtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 390
                self.match(QuestionParser.TYPE_MT)
                pass
            elif token in [QuestionParser.TYPE_ORD]:
                localctx = QuestionParser.TypeOrdContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 391
                self.match(QuestionParser.TYPE_ORD)
                pass
            elif token in [QuestionParser.TYPE_FIB]:
                localctx = QuestionParser.TypeFibContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 392
                self.match(QuestionParser.TYPE_FIB)
                pass
            elif token in [QuestionParser.TYPE_WR]:
                localctx = QuestionParser.TypeWrContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 393
                self.match(QuestionParser.TYPE_WR)
                pass
            elif token in [QuestionParser.TYPE_OTHER]:
                localctx = QuestionParser.TypeOtherContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 394
                self.match(QuestionParser.TYPE_OTHER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TitleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TITLE(self):
            return self.getToken(QuestionParser.TITLE, 0)

        def getRuleIndex(self):
            return QuestionParser.RULE_title

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTitle" ):
                listener.enterTitle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTitle" ):
                listener.exitTitle(self)




    def title(self):

        localctx = QuestionParser.TitleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_title)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(QuestionParser.TITLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PointsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POINTS(self):
            return self.getToken(QuestionParser.POINTS, 0)

        def getRuleIndex(self):
            return QuestionParser.RULE_points

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPoints" ):
                listener.enterPoints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPoints" ):
                listener.exitPoints(self)




    def points(self):

        localctx = QuestionParser.PointsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_points)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(QuestionParser.POINTS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RandomizeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return QuestionParser.RULE_randomize

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RandomTrueContext(RandomizeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuestionParser.RandomizeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RANDOMIZE_TRUE(self):
            return self.getToken(QuestionParser.RANDOMIZE_TRUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRandomTrue" ):
                listener.enterRandomTrue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRandomTrue" ):
                listener.exitRandomTrue(self)


    class RandomFalseContext(RandomizeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuestionParser.RandomizeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RANDOMIZE_FALSE(self):
            return self.getToken(QuestionParser.RANDOMIZE_FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRandomFalse" ):
                listener.enterRandomFalse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRandomFalse" ):
                listener.exitRandomFalse(self)



    def randomize(self):

        localctx = QuestionParser.RandomizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_randomize)
        try:
            self.state = 403
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuestionParser.RANDOMIZE_TRUE]:
                localctx = QuestionParser.RandomTrueContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.match(QuestionParser.RANDOMIZE_TRUE)
                pass
            elif token in [QuestionParser.RANDOMIZE_FALSE]:
                localctx = QuestionParser.RandomFalseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 402
                self.match(QuestionParser.RANDOMIZE_FALSE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Question_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def question_prefix(self):
            return self.getTypedRuleContext(QuestionParser.Question_prefixContext,0)


        def content(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuestionParser.ContentContext)
            else:
                return self.getTypedRuleContext(QuestionParser.ContentContext,i)


        def feedback(self):
            return self.getTypedRuleContext(QuestionParser.FeedbackContext,0)


        def getRuleIndex(self):
            return QuestionParser.RULE_question_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuestion_body" ):
                listener.enterQuestion_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuestion_body" ):
                listener.exitQuestion_body(self)




    def question_body(self):

        localctx = QuestionParser.Question_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_question_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.question_prefix()
            self.state = 407 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 406
                self.content()
                self.state = 409 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.MEDIA) | (1 << QuestionParser.HYPERLINK) | (1 << QuestionParser.ALL_CHARACTER) | (1 << QuestionParser.ESCAPED_OPEN_BRACKET))) != 0)):
                    break

            self.state = 412
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.FEEDBACK_MARKER:
                self.state = 411
                self.feedback()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Question_prefixContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUESTION_PREFIX(self):
            return self.getToken(QuestionParser.QUESTION_PREFIX, 0)

        def getRuleIndex(self):
            return QuestionParser.RULE_question_prefix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuestion_prefix" ):
                listener.enterQuestion_prefix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuestion_prefix" ):
                listener.exitQuestion_prefix(self)




    def question_prefix(self):

        localctx = QuestionParser.Question_prefixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_question_prefix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(QuestionParser.QUESTION_PREFIX)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return QuestionParser.RULE_content

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ContentCharactersContext(ContentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuestionParser.ContentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ALL_CHARACTER(self, i:int=None):
            if i is None:
                return self.getTokens(QuestionParser.ALL_CHARACTER)
            else:
                return self.getToken(QuestionParser.ALL_CHARACTER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContentCharacters" ):
                listener.enterContentCharacters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContentCharacters" ):
                listener.exitContentCharacters(self)


    class MediaContext(ContentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuestionParser.ContentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MEDIA(self):
            return self.getToken(QuestionParser.MEDIA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMedia" ):
                listener.enterMedia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMedia" ):
                listener.exitMedia(self)


    class FibAnswerContext(ContentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuestionParser.ContentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ESCAPED_OPEN_BRACKET(self):
            return self.getToken(QuestionParser.ESCAPED_OPEN_BRACKET, 0)
        def ESCAPED_CLOSE_BRACKET(self):
            return self.getToken(QuestionParser.ESCAPED_CLOSE_BRACKET, 0)
        def ALL_CHARACTER(self, i:int=None):
            if i is None:
                return self.getTokens(QuestionParser.ALL_CHARACTER)
            else:
                return self.getToken(QuestionParser.ALL_CHARACTER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFibAnswer" ):
                listener.enterFibAnswer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFibAnswer" ):
                listener.exitFibAnswer(self)


    class HyperlinkContext(ContentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuestionParser.ContentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def HYPERLINK(self):
            return self.getToken(QuestionParser.HYPERLINK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHyperlink" ):
                listener.enterHyperlink(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHyperlink" ):
                listener.exitHyperlink(self)



    def content(self):

        localctx = QuestionParser.ContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_content)
        self._la = 0 # Token type
        try:
            self.state = 430
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuestionParser.MEDIA]:
                localctx = QuestionParser.MediaContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 416
                self.match(QuestionParser.MEDIA)
                pass
            elif token in [QuestionParser.HYPERLINK]:
                localctx = QuestionParser.HyperlinkContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 417
                self.match(QuestionParser.HYPERLINK)
                pass
            elif token in [QuestionParser.ESCAPED_OPEN_BRACKET]:
                localctx = QuestionParser.FibAnswerContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 418
                self.match(QuestionParser.ESCAPED_OPEN_BRACKET)
                self.state = 420 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 419
                    self.match(QuestionParser.ALL_CHARACTER)
                    self.state = 422 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==QuestionParser.ALL_CHARACTER):
                        break

                self.state = 424
                self.match(QuestionParser.ESCAPED_CLOSE_BRACKET)
                pass
            elif token in [QuestionParser.ALL_CHARACTER]:
                localctx = QuestionParser.ContentCharactersContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 426 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 425
                        self.match(QuestionParser.ALL_CHARACTER)

                    else:
                        raise NoViableAltException(self)
                    self.state = 428 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,108,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FeedbackContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FEEDBACK_MARKER(self):
            return self.getToken(QuestionParser.FEEDBACK_MARKER, 0)

        def content(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuestionParser.ContentContext)
            else:
                return self.getTypedRuleContext(QuestionParser.ContentContext,i)


        def getRuleIndex(self):
            return QuestionParser.RULE_feedback

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFeedback" ):
                listener.enterFeedback(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFeedback" ):
                listener.exitFeedback(self)




    def feedback(self):

        localctx = QuestionParser.FeedbackContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_feedback)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(QuestionParser.FEEDBACK_MARKER)
            self.state = 434 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 433
                self.content()
                self.state = 436 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.MEDIA) | (1 << QuestionParser.HYPERLINK) | (1 << QuestionParser.ALL_CHARACTER) | (1 << QuestionParser.ESCAPED_OPEN_BRACKET))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Answer_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return QuestionParser.RULE_answer_list

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ListNoAnswerContext(Answer_listContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuestionParser.Answer_listContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def START_ANSWER(self):
            return self.getToken(QuestionParser.START_ANSWER, 0)
        def list_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuestionParser.List_itemContext)
            else:
                return self.getTypedRuleContext(QuestionParser.List_itemContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListNoAnswer" ):
                listener.enterListNoAnswer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListNoAnswer" ):
                listener.exitListNoAnswer(self)


    class ListWithAnswerContext(Answer_listContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuestionParser.Answer_listContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def START_ANSWER(self):
            return self.getToken(QuestionParser.START_ANSWER, 0)
        def list_answer_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuestionParser.List_answer_itemContext)
            else:
                return self.getTypedRuleContext(QuestionParser.List_answer_itemContext,i)

        def list_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuestionParser.List_itemContext)
            else:
                return self.getTypedRuleContext(QuestionParser.List_itemContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListWithAnswer" ):
                listener.enterListWithAnswer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListWithAnswer" ):
                listener.exitListWithAnswer(self)



    def answer_list(self):

        localctx = QuestionParser.Answer_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_answer_list)
        self._la = 0 # Token type
        try:
            self.state = 451
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,114,self._ctx)
            if la_ == 1:
                localctx = QuestionParser.ListNoAnswerContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 438
                self.match(QuestionParser.START_ANSWER)
                self.state = 440 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 439
                    self.list_item()
                    self.state = 442 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==QuestionParser.LIST_PREFIX):
                        break

                pass

            elif la_ == 2:
                localctx = QuestionParser.ListWithAnswerContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 444
                self.match(QuestionParser.START_ANSWER)
                self.state = 447 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 447
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [QuestionParser.RIGHT_ANSWER]:
                        self.state = 445
                        self.list_answer_item()
                        pass
                    elif token in [QuestionParser.LIST_PREFIX]:
                        self.state = 446
                        self.list_item()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 449 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==QuestionParser.RIGHT_ANSWER or _la==QuestionParser.LIST_PREFIX):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_itemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_prefix(self):
            return self.getTypedRuleContext(QuestionParser.List_prefixContext,0)


        def content(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuestionParser.ContentContext)
            else:
                return self.getTypedRuleContext(QuestionParser.ContentContext,i)


        def feedback(self):
            return self.getTypedRuleContext(QuestionParser.FeedbackContext,0)


        def getRuleIndex(self):
            return QuestionParser.RULE_list_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_item" ):
                listener.enterList_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_item" ):
                listener.exitList_item(self)




    def list_item(self):

        localctx = QuestionParser.List_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_list_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self.list_prefix()
            self.state = 455 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 454
                self.content()
                self.state = 457 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.MEDIA) | (1 << QuestionParser.HYPERLINK) | (1 << QuestionParser.ALL_CHARACTER) | (1 << QuestionParser.ESCAPED_OPEN_BRACKET))) != 0)):
                    break

            self.state = 460
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.FEEDBACK_MARKER:
                self.state = 459
                self.feedback()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_prefixContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIST_PREFIX(self):
            return self.getToken(QuestionParser.LIST_PREFIX, 0)

        def getRuleIndex(self):
            return QuestionParser.RULE_list_prefix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_prefix" ):
                listener.enterList_prefix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_prefix" ):
                listener.exitList_prefix(self)




    def list_prefix(self):

        localctx = QuestionParser.List_prefixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_list_prefix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.match(QuestionParser.LIST_PREFIX)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_answer_itemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def answer_prefix(self):
            return self.getTypedRuleContext(QuestionParser.Answer_prefixContext,0)


        def content(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuestionParser.ContentContext)
            else:
                return self.getTypedRuleContext(QuestionParser.ContentContext,i)


        def feedback(self):
            return self.getTypedRuleContext(QuestionParser.FeedbackContext,0)


        def getRuleIndex(self):
            return QuestionParser.RULE_list_answer_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_answer_item" ):
                listener.enterList_answer_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_answer_item" ):
                listener.exitList_answer_item(self)




    def list_answer_item(self):

        localctx = QuestionParser.List_answer_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_list_answer_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self.answer_prefix()
            self.state = 466 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 465
                self.content()
                self.state = 468 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.MEDIA) | (1 << QuestionParser.HYPERLINK) | (1 << QuestionParser.ALL_CHARACTER) | (1 << QuestionParser.ESCAPED_OPEN_BRACKET))) != 0)):
                    break

            self.state = 471
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.FEEDBACK_MARKER:
                self.state = 470
                self.feedback()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Answer_prefixContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RIGHT_ANSWER(self):
            return self.getToken(QuestionParser.RIGHT_ANSWER, 0)

        def getRuleIndex(self):
            return QuestionParser.RULE_answer_prefix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnswer_prefix" ):
                listener.enterAnswer_prefix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnswer_prefix" ):
                listener.exitAnswer_prefix(self)




    def answer_prefix(self):

        localctx = QuestionParser.Answer_prefixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_answer_prefix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.match(QuestionParser.RIGHT_ANSWER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class End_answersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def END_ANSWERS(self):
            return self.getToken(QuestionParser.END_ANSWERS, 0)

        def end_answers_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuestionParser.End_answers_itemContext)
            else:
                return self.getTypedRuleContext(QuestionParser.End_answers_itemContext,i)


        def getRuleIndex(self):
            return QuestionParser.RULE_end_answers

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnd_answers" ):
                listener.enterEnd_answers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnd_answers" ):
                listener.exitEnd_answers(self)




    def end_answers(self):

        localctx = QuestionParser.End_answersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_end_answers)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.match(QuestionParser.END_ANSWERS)
            self.state = 477 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 476
                self.end_answers_item()
                self.state = 479 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==QuestionParser.QUESTION_PREFIX):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class End_answers_itemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def question_prefix(self):
            return self.getTypedRuleContext(QuestionParser.Question_prefixContext,0)


        def content(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuestionParser.ContentContext)
            else:
                return self.getTypedRuleContext(QuestionParser.ContentContext,i)


        def feedback(self):
            return self.getTypedRuleContext(QuestionParser.FeedbackContext,0)


        def getRuleIndex(self):
            return QuestionParser.RULE_end_answers_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnd_answers_item" ):
                listener.enterEnd_answers_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnd_answers_item" ):
                listener.exitEnd_answers_item(self)




    def end_answers_item(self):

        localctx = QuestionParser.End_answers_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_end_answers_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self.question_prefix()
            self.state = 483 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 482
                self.content()
                self.state = 485 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.MEDIA) | (1 << QuestionParser.HYPERLINK) | (1 << QuestionParser.ALL_CHARACTER) | (1 << QuestionParser.ESCAPED_OPEN_BRACKET))) != 0)):
                    break

            self.state = 488
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.FEEDBACK_MARKER:
                self.state = 487
                self.feedback()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





