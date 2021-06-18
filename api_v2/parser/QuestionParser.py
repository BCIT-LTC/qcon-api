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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\36")
        buf.write("\u0200\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\3\2\5\2.\n\2\3\2\7\2\61")
        buf.write("\n\2\f\2\16\2\64\13\2\3\2\5\2\67\n\2\3\2\3\2\3\3\3\3\6")
        buf.write("\3=\n\3\r\3\16\3>\3\4\5\4B\n\4\3\4\3\4\3\4\3\4\3\4\5\4")
        buf.write("I\n\4\3\4\3\4\3\4\3\4\3\4\5\4P\n\4\3\4\3\4\3\4\5\4U\n")
        buf.write("\4\3\5\3\5\3\6\3\6\5\6[\n\6\3\6\5\6^\n\6\3\6\5\6a\n\6")
        buf.write("\3\6\5\6d\n\6\3\6\3\6\5\6h\n\6\3\6\5\6k\n\6\3\6\5\6n\n")
        buf.write("\6\3\6\5\6q\n\6\3\6\3\6\5\6u\n\6\3\6\5\6x\n\6\3\6\5\6")
        buf.write("{\n\6\3\6\5\6~\n\6\3\6\3\6\5\6\u0082\n\6\3\6\5\6\u0085")
        buf.write("\n\6\3\6\5\6\u0088\n\6\3\6\5\6\u008b\n\6\3\6\3\6\5\6\u008f")
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
        buf.write("\n\6\3\6\3\6\5\6\u0186\n\6\3\6\5\6\u0189\n\6\3\6\5\6\u018c")
        buf.write("\n\6\3\6\5\6\u018f\n\6\5\6\u0191\n\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\5\7\u019b\n\7\3\b\3\b\3\t\3\t\3\n\3\n\5")
        buf.write("\n\u01a3\n\n\3\13\6\13\u01a6\n\13\r\13\16\13\u01a7\3\13")
        buf.write("\5\13\u01ab\n\13\3\f\3\f\3\f\3\f\3\f\6\f\u01b2\n\f\r\f")
        buf.write("\16\f\u01b3\3\f\3\f\6\f\u01b8\n\f\r\f\16\f\u01b9\5\f\u01bc")
        buf.write("\n\f\3\r\3\r\6\r\u01c0\n\r\r\r\16\r\u01c1\3\16\3\16\6")
        buf.write("\16\u01c6\n\16\r\16\16\16\u01c7\3\16\3\16\3\16\6\16\u01cd")
        buf.write("\n\16\r\16\16\16\u01ce\5\16\u01d1\n\16\3\17\3\17\6\17")
        buf.write("\u01d5\n\17\r\17\16\17\u01d6\3\17\5\17\u01da\n\17\3\20")
        buf.write("\3\20\3\21\3\21\6\21\u01e0\n\21\r\21\16\21\u01e1\3\21")
        buf.write("\5\21\u01e5\n\21\3\22\3\22\3\23\3\23\6\23\u01eb\n\23\r")
        buf.write("\23\16\23\u01ec\3\24\3\24\6\24\u01f1\n\24\r\24\16\24\u01f2")
        buf.write("\3\25\3\25\6\25\u01f7\n\25\r\25\16\25\u01f8\3\25\5\25")
        buf.write("\u01fc\n\25\3\26\3\26\3\26\2\2\27\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*\2\2\2\u0287\2-\3\2\2\2\4:\3")
        buf.write("\2\2\2\6T\3\2\2\2\bV\3\2\2\2\n\u0190\3\2\2\2\f\u019a\3")
        buf.write("\2\2\2\16\u019c\3\2\2\2\20\u019e\3\2\2\2\22\u01a2\3\2")
        buf.write("\2\2\24\u01a5\3\2\2\2\26\u01bb\3\2\2\2\30\u01bd\3\2\2")
        buf.write("\2\32\u01d0\3\2\2\2\34\u01d2\3\2\2\2\36\u01db\3\2\2\2")
        buf.write(" \u01dd\3\2\2\2\"\u01e6\3\2\2\2$\u01e8\3\2\2\2&\u01ee")
        buf.write("\3\2\2\2(\u01f4\3\2\2\2*\u01fd\3\2\2\2,.\5\4\3\2-,\3\2")
        buf.write("\2\2-.\3\2\2\2.\62\3\2\2\2/\61\5\6\4\2\60/\3\2\2\2\61")
        buf.write("\64\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63\66\3\2\2\2")
        buf.write("\64\62\3\2\2\2\65\67\5&\24\2\66\65\3\2\2\2\66\67\3\2\2")
        buf.write("\2\678\3\2\2\289\7\2\2\39\3\3\2\2\2:<\7\r\2\2;=\7\n\2")
        buf.write("\2<;\3\2\2\2=>\3\2\2\2><\3\2\2\2>?\3\2\2\2?\5\3\2\2\2")
        buf.write("@B\5\n\6\2A@\3\2\2\2AB\3\2\2\2BC\3\2\2\2CD\5\b\5\2DE\5")
        buf.write("\24\13\2EF\5\32\16\2FU\3\2\2\2GI\5\n\6\2HG\3\2\2\2HI\3")
        buf.write("\2\2\2IJ\3\2\2\2JK\5\b\5\2KL\5\24\13\2LM\5$\23\2MU\3\2")
        buf.write("\2\2NP\5\n\6\2ON\3\2\2\2OP\3\2\2\2PQ\3\2\2\2QR\5\b\5\2")
        buf.write("RS\5\24\13\2SU\3\2\2\2TA\3\2\2\2TH\3\2\2\2TO\3\2\2\2U")
        buf.write("\7\3\2\2\2VW\7\4\2\2W\t\3\2\2\2XZ\7\3\2\2Y[\5\f\7\2ZY")
        buf.write("\3\2\2\2Z[\3\2\2\2[]\3\2\2\2\\^\5\16\b\2]\\\3\2\2\2]^")
        buf.write("\3\2\2\2^`\3\2\2\2_a\5\20\t\2`_\3\2\2\2`a\3\2\2\2ac\3")
        buf.write("\2\2\2bd\5\22\n\2cb\3\2\2\2cd\3\2\2\2d\u0191\3\2\2\2e")
        buf.write("g\7\3\2\2fh\5\f\7\2gf\3\2\2\2gh\3\2\2\2hj\3\2\2\2ik\5")
        buf.write("\16\b\2ji\3\2\2\2jk\3\2\2\2km\3\2\2\2ln\5\22\n\2ml\3\2")
        buf.write("\2\2mn\3\2\2\2np\3\2\2\2oq\5\20\t\2po\3\2\2\2pq\3\2\2")
        buf.write("\2q\u0191\3\2\2\2rt\7\3\2\2su\5\f\7\2ts\3\2\2\2tu\3\2")
        buf.write("\2\2uw\3\2\2\2vx\5\20\t\2wv\3\2\2\2wx\3\2\2\2xz\3\2\2")
        buf.write("\2y{\5\16\b\2zy\3\2\2\2z{\3\2\2\2{}\3\2\2\2|~\5\22\n\2")
        buf.write("}|\3\2\2\2}~\3\2\2\2~\u0191\3\2\2\2\177\u0081\7\3\2\2")
        buf.write("\u0080\u0082\5\f\7\2\u0081\u0080\3\2\2\2\u0081\u0082\3")
        buf.write("\2\2\2\u0082\u0084\3\2\2\2\u0083\u0085\5\20\t\2\u0084")
        buf.write("\u0083\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0087\3\2\2\2")
        buf.write("\u0086\u0088\5\22\n\2\u0087\u0086\3\2\2\2\u0087\u0088")
        buf.write("\3\2\2\2\u0088\u008a\3\2\2\2\u0089\u008b\5\16\b\2\u008a")
        buf.write("\u0089\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u0191\3\2\2\2")
        buf.write("\u008c\u008e\7\3\2\2\u008d\u008f\5\f\7\2\u008e\u008d\3")
        buf.write("\2\2\2\u008e\u008f\3\2\2\2\u008f\u0091\3\2\2\2\u0090\u0092")
        buf.write("\5\22\n\2\u0091\u0090\3\2\2\2\u0091\u0092\3\2\2\2\u0092")
        buf.write("\u0094\3\2\2\2\u0093\u0095\5\16\b\2\u0094\u0093\3\2\2")
        buf.write("\2\u0094\u0095\3\2\2\2\u0095\u0097\3\2\2\2\u0096\u0098")
        buf.write("\5\20\t\2\u0097\u0096\3\2\2\2\u0097\u0098\3\2\2\2\u0098")
        buf.write("\u0191\3\2\2\2\u0099\u009b\7\3\2\2\u009a\u009c\5\f\7\2")
        buf.write("\u009b\u009a\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009e\3")
        buf.write("\2\2\2\u009d\u009f\5\22\n\2\u009e\u009d\3\2\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009f\u00a1\3\2\2\2\u00a0\u00a2\5\20\t")
        buf.write("\2\u00a1\u00a0\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a4")
        buf.write("\3\2\2\2\u00a3\u00a5\5\16\b\2\u00a4\u00a3\3\2\2\2\u00a4")
        buf.write("\u00a5\3\2\2\2\u00a5\u0191\3\2\2\2\u00a6\u00a8\7\3\2\2")
        buf.write("\u00a7\u00a9\5\16\b\2\u00a8\u00a7\3\2\2\2\u00a8\u00a9")
        buf.write("\3\2\2\2\u00a9\u00ab\3\2\2\2\u00aa\u00ac\5\f\7\2\u00ab")
        buf.write("\u00aa\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ae\3\2\2\2")
        buf.write("\u00ad\u00af\5\20\t\2\u00ae\u00ad\3\2\2\2\u00ae\u00af")
        buf.write("\3\2\2\2\u00af\u00b1\3\2\2\2\u00b0\u00b2\5\22\n\2\u00b1")
        buf.write("\u00b0\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u0191\3\2\2\2")
        buf.write("\u00b3\u00b5\7\3\2\2\u00b4\u00b6\5\16\b\2\u00b5\u00b4")
        buf.write("\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b8\3\2\2\2\u00b7")
        buf.write("\u00b9\5\f\7\2\u00b8\u00b7\3\2\2\2\u00b8\u00b9\3\2\2\2")
        buf.write("\u00b9\u00bb\3\2\2\2\u00ba\u00bc\5\22\n\2\u00bb\u00ba")
        buf.write("\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00be\3\2\2\2\u00bd")
        buf.write("\u00bf\5\20\t\2\u00be\u00bd\3\2\2\2\u00be\u00bf\3\2\2")
        buf.write("\2\u00bf\u0191\3\2\2\2\u00c0\u00c2\7\3\2\2\u00c1\u00c3")
        buf.write("\5\16\b\2\u00c2\u00c1\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3")
        buf.write("\u00c5\3\2\2\2\u00c4\u00c6\5\20\t\2\u00c5\u00c4\3\2\2")
        buf.write("\2\u00c5\u00c6\3\2\2\2\u00c6\u00c8\3\2\2\2\u00c7\u00c9")
        buf.write("\5\f\7\2\u00c8\u00c7\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9")
        buf.write("\u00cb\3\2\2\2\u00ca\u00cc\5\22\n\2\u00cb\u00ca\3\2\2")
        buf.write("\2\u00cb\u00cc\3\2\2\2\u00cc\u0191\3\2\2\2\u00cd\u00cf")
        buf.write("\7\3\2\2\u00ce\u00d0\5\16\b\2\u00cf\u00ce\3\2\2\2\u00cf")
        buf.write("\u00d0\3\2\2\2\u00d0\u00d2\3\2\2\2\u00d1\u00d3\5\20\t")
        buf.write("\2\u00d2\u00d1\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d5")
        buf.write("\3\2\2\2\u00d4\u00d6\5\22\n\2\u00d5\u00d4\3\2\2\2\u00d5")
        buf.write("\u00d6\3\2\2\2\u00d6\u00d8\3\2\2\2\u00d7\u00d9\5\f\7\2")
        buf.write("\u00d8\u00d7\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u0191\3")
        buf.write("\2\2\2\u00da\u00dc\7\3\2\2\u00db\u00dd\5\16\b\2\u00dc")
        buf.write("\u00db\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00df\3\2\2\2")
        buf.write("\u00de\u00e0\5\22\n\2\u00df\u00de\3\2\2\2\u00df\u00e0")
        buf.write("\3\2\2\2\u00e0\u00e2\3\2\2\2\u00e1\u00e3\5\f\7\2\u00e2")
        buf.write("\u00e1\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e5\3\2\2\2")
        buf.write("\u00e4\u00e6\5\20\t\2\u00e5\u00e4\3\2\2\2\u00e5\u00e6")
        buf.write("\3\2\2\2\u00e6\u0191\3\2\2\2\u00e7\u00e9\7\3\2\2\u00e8")
        buf.write("\u00ea\5\16\b\2\u00e9\u00e8\3\2\2\2\u00e9\u00ea\3\2\2")
        buf.write("\2\u00ea\u00ec\3\2\2\2\u00eb\u00ed\5\22\n\2\u00ec\u00eb")
        buf.write("\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00ef\3\2\2\2\u00ee")
        buf.write("\u00f0\5\20\t\2\u00ef\u00ee\3\2\2\2\u00ef\u00f0\3\2\2")
        buf.write("\2\u00f0\u00f2\3\2\2\2\u00f1\u00f3\5\f\7\2\u00f2\u00f1")
        buf.write("\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u0191\3\2\2\2\u00f4")
        buf.write("\u00f6\7\3\2\2\u00f5\u00f7\5\20\t\2\u00f6\u00f5\3\2\2")
        buf.write("\2\u00f6\u00f7\3\2\2\2\u00f7\u00f9\3\2\2\2\u00f8\u00fa")
        buf.write("\5\f\7\2\u00f9\u00f8\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa")
        buf.write("\u00fc\3\2\2\2\u00fb\u00fd\5\16\b\2\u00fc\u00fb\3\2\2")
        buf.write("\2\u00fc\u00fd\3\2\2\2\u00fd\u00ff\3\2\2\2\u00fe\u0100")
        buf.write("\5\22\n\2\u00ff\u00fe\3\2\2\2\u00ff\u0100\3\2\2\2\u0100")
        buf.write("\u0191\3\2\2\2\u0101\u0103\7\3\2\2\u0102\u0104\5\20\t")
        buf.write("\2\u0103\u0102\3\2\2\2\u0103\u0104\3\2\2\2\u0104\u0106")
        buf.write("\3\2\2\2\u0105\u0107\5\f\7\2\u0106\u0105\3\2\2\2\u0106")
        buf.write("\u0107\3\2\2\2\u0107\u0109\3\2\2\2\u0108\u010a\5\22\n")
        buf.write("\2\u0109\u0108\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u010c")
        buf.write("\3\2\2\2\u010b\u010d\5\16\b\2\u010c\u010b\3\2\2\2\u010c")
        buf.write("\u010d\3\2\2\2\u010d\u0191\3\2\2\2\u010e\u0110\7\3\2\2")
        buf.write("\u010f\u0111\5\20\t\2\u0110\u010f\3\2\2\2\u0110\u0111")
        buf.write("\3\2\2\2\u0111\u0113\3\2\2\2\u0112\u0114\5\16\b\2\u0113")
        buf.write("\u0112\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0116\3\2\2\2")
        buf.write("\u0115\u0117\5\f\7\2\u0116\u0115\3\2\2\2\u0116\u0117\3")
        buf.write("\2\2\2\u0117\u0119\3\2\2\2\u0118\u011a\5\22\n\2\u0119")
        buf.write("\u0118\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u0191\3\2\2\2")
        buf.write("\u011b\u011d\7\3\2\2\u011c\u011e\5\20\t\2\u011d\u011c")
        buf.write("\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u0120\3\2\2\2\u011f")
        buf.write("\u0121\5\16\b\2\u0120\u011f\3\2\2\2\u0120\u0121\3\2\2")
        buf.write("\2\u0121\u0123\3\2\2\2\u0122\u0124\5\22\n\2\u0123\u0122")
        buf.write("\3\2\2\2\u0123\u0124\3\2\2\2\u0124\u0126\3\2\2\2\u0125")
        buf.write("\u0127\5\f\7\2\u0126\u0125\3\2\2\2\u0126\u0127\3\2\2\2")
        buf.write("\u0127\u0191\3\2\2\2\u0128\u012a\7\3\2\2\u0129\u012b\5")
        buf.write("\20\t\2\u012a\u0129\3\2\2\2\u012a\u012b\3\2\2\2\u012b")
        buf.write("\u012d\3\2\2\2\u012c\u012e\5\22\n\2\u012d\u012c\3\2\2")
        buf.write("\2\u012d\u012e\3\2\2\2\u012e\u0130\3\2\2\2\u012f\u0131")
        buf.write("\5\f\7\2\u0130\u012f\3\2\2\2\u0130\u0131\3\2\2\2\u0131")
        buf.write("\u0133\3\2\2\2\u0132\u0134\5\16\b\2\u0133\u0132\3\2\2")
        buf.write("\2\u0133\u0134\3\2\2\2\u0134\u0191\3\2\2\2\u0135\u0137")
        buf.write("\7\3\2\2\u0136\u0138\5\20\t\2\u0137\u0136\3\2\2\2\u0137")
        buf.write("\u0138\3\2\2\2\u0138\u013a\3\2\2\2\u0139\u013b\5\22\n")
        buf.write("\2\u013a\u0139\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013d")
        buf.write("\3\2\2\2\u013c\u013e\5\16\b\2\u013d\u013c\3\2\2\2\u013d")
        buf.write("\u013e\3\2\2\2\u013e\u0140\3\2\2\2\u013f\u0141\5\f\7\2")
        buf.write("\u0140\u013f\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0191\3")
        buf.write("\2\2\2\u0142\u0144\7\3\2\2\u0143\u0145\5\22\n\2\u0144")
        buf.write("\u0143\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0147\3\2\2\2")
        buf.write("\u0146\u0148\5\f\7\2\u0147\u0146\3\2\2\2\u0147\u0148\3")
        buf.write("\2\2\2\u0148\u014a\3\2\2\2\u0149\u014b\5\16\b\2\u014a")
        buf.write("\u0149\3\2\2\2\u014a\u014b\3\2\2\2\u014b\u014d\3\2\2\2")
        buf.write("\u014c\u014e\5\20\t\2\u014d\u014c\3\2\2\2\u014d\u014e")
        buf.write("\3\2\2\2\u014e\u0191\3\2\2\2\u014f\u0151\7\3\2\2\u0150")
        buf.write("\u0152\5\22\n\2\u0151\u0150\3\2\2\2\u0151\u0152\3\2\2")
        buf.write("\2\u0152\u0154\3\2\2\2\u0153\u0155\5\f\7\2\u0154\u0153")
        buf.write("\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0157\3\2\2\2\u0156")
        buf.write("\u0158\5\20\t\2\u0157\u0156\3\2\2\2\u0157\u0158\3\2\2")
        buf.write("\2\u0158\u015a\3\2\2\2\u0159\u015b\5\16\b\2\u015a\u0159")
        buf.write("\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u0191\3\2\2\2\u015c")
        buf.write("\u015e\7\3\2\2\u015d\u015f\5\22\n\2\u015e\u015d\3\2\2")
        buf.write("\2\u015e\u015f\3\2\2\2\u015f\u0161\3\2\2\2\u0160\u0162")
        buf.write("\5\16\b\2\u0161\u0160\3\2\2\2\u0161\u0162\3\2\2\2\u0162")
        buf.write("\u0164\3\2\2\2\u0163\u0165\5\f\7\2\u0164\u0163\3\2\2\2")
        buf.write("\u0164\u0165\3\2\2\2\u0165\u0167\3\2\2\2\u0166\u0168\5")
        buf.write("\20\t\2\u0167\u0166\3\2\2\2\u0167\u0168\3\2\2\2\u0168")
        buf.write("\u0191\3\2\2\2\u0169\u016b\7\3\2\2\u016a\u016c\5\22\n")
        buf.write("\2\u016b\u016a\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016e")
        buf.write("\3\2\2\2\u016d\u016f\5\16\b\2\u016e\u016d\3\2\2\2\u016e")
        buf.write("\u016f\3\2\2\2\u016f\u0171\3\2\2\2\u0170\u0172\5\20\t")
        buf.write("\2\u0171\u0170\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0174")
        buf.write("\3\2\2\2\u0173\u0175\5\f\7\2\u0174\u0173\3\2\2\2\u0174")
        buf.write("\u0175\3\2\2\2\u0175\u0191\3\2\2\2\u0176\u0178\7\3\2\2")
        buf.write("\u0177\u0179\5\22\n\2\u0178\u0177\3\2\2\2\u0178\u0179")
        buf.write("\3\2\2\2\u0179\u017b\3\2\2\2\u017a\u017c\5\20\t\2\u017b")
        buf.write("\u017a\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017e\3\2\2\2")
        buf.write("\u017d\u017f\5\f\7\2\u017e\u017d\3\2\2\2\u017e\u017f\3")
        buf.write("\2\2\2\u017f\u0181\3\2\2\2\u0180\u0182\5\16\b\2\u0181")
        buf.write("\u0180\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0191\3\2\2\2")
        buf.write("\u0183\u0185\7\3\2\2\u0184\u0186\5\22\n\2\u0185\u0184")
        buf.write("\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0188\3\2\2\2\u0187")
        buf.write("\u0189\5\20\t\2\u0188\u0187\3\2\2\2\u0188\u0189\3\2\2")
        buf.write("\2\u0189\u018b\3\2\2\2\u018a\u018c\5\16\b\2\u018b\u018a")
        buf.write("\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u018e\3\2\2\2\u018d")
        buf.write("\u018f\5\f\7\2\u018e\u018d\3\2\2\2\u018e\u018f\3\2\2\2")
        buf.write("\u018f\u0191\3\2\2\2\u0190X\3\2\2\2\u0190e\3\2\2\2\u0190")
        buf.write("r\3\2\2\2\u0190\177\3\2\2\2\u0190\u008c\3\2\2\2\u0190")
        buf.write("\u0099\3\2\2\2\u0190\u00a6\3\2\2\2\u0190\u00b3\3\2\2\2")
        buf.write("\u0190\u00c0\3\2\2\2\u0190\u00cd\3\2\2\2\u0190\u00da\3")
        buf.write("\2\2\2\u0190\u00e7\3\2\2\2\u0190\u00f4\3\2\2\2\u0190\u0101")
        buf.write("\3\2\2\2\u0190\u010e\3\2\2\2\u0190\u011b\3\2\2\2\u0190")
        buf.write("\u0128\3\2\2\2\u0190\u0135\3\2\2\2\u0190\u0142\3\2\2\2")
        buf.write("\u0190\u014f\3\2\2\2\u0190\u015c\3\2\2\2\u0190\u0169\3")
        buf.write("\2\2\2\u0190\u0176\3\2\2\2\u0190\u0183\3\2\2\2\u0191\13")
        buf.write("\3\2\2\2\u0192\u019b\7\22\2\2\u0193\u019b\7\23\2\2\u0194")
        buf.write("\u019b\7\24\2\2\u0195\u019b\7\25\2\2\u0196\u019b\7\26")
        buf.write("\2\2\u0197\u019b\7\27\2\2\u0198\u019b\7\30\2\2\u0199\u019b")
        buf.write("\7\31\2\2\u019a\u0192\3\2\2\2\u019a\u0193\3\2\2\2\u019a")
        buf.write("\u0194\3\2\2\2\u019a\u0195\3\2\2\2\u019a\u0196\3\2\2\2")
        buf.write("\u019a\u0197\3\2\2\2\u019a\u0198\3\2\2\2\u019a\u0199\3")
        buf.write("\2\2\2\u019b\r\3\2\2\2\u019c\u019d\7\16\2\2\u019d\17\3")
        buf.write("\2\2\2\u019e\u019f\7\17\2\2\u019f\21\3\2\2\2\u01a0\u01a3")
        buf.write("\7\20\2\2\u01a1\u01a3\7\21\2\2\u01a2\u01a0\3\2\2\2\u01a2")
        buf.write("\u01a1\3\2\2\2\u01a3\23\3\2\2\2\u01a4\u01a6\5\26\f\2\u01a5")
        buf.write("\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a5\3\2\2\2")
        buf.write("\u01a7\u01a8\3\2\2\2\u01a8\u01aa\3\2\2\2\u01a9\u01ab\5")
        buf.write("\30\r\2\u01aa\u01a9\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab")
        buf.write("\25\3\2\2\2\u01ac\u01bc\7\b\2\2\u01ad\u01bc\7\7\2\2\u01ae")
        buf.write("\u01bc\7\t\2\2\u01af\u01b1\7\13\2\2\u01b0\u01b2\7\n\2")
        buf.write("\2\u01b1\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b1")
        buf.write("\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5")
        buf.write("\u01bc\7\f\2\2\u01b6\u01b8\7\n\2\2\u01b7\u01b6\3\2\2\2")
        buf.write("\u01b8\u01b9\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9\u01ba\3")
        buf.write("\2\2\2\u01ba\u01bc\3\2\2\2\u01bb\u01ac\3\2\2\2\u01bb\u01ad")
        buf.write("\3\2\2\2\u01bb\u01ae\3\2\2\2\u01bb\u01af\3\2\2\2\u01bb")
        buf.write("\u01b7\3\2\2\2\u01bc\27\3\2\2\2\u01bd\u01bf\7\6\2\2\u01be")
        buf.write("\u01c0\5\26\f\2\u01bf\u01be\3\2\2\2\u01c0\u01c1\3\2\2")
        buf.write("\2\u01c1\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\31\3")
        buf.write("\2\2\2\u01c3\u01c5\7\32\2\2\u01c4\u01c6\5\34\17\2\u01c5")
        buf.write("\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c5\3\2\2\2")
        buf.write("\u01c7\u01c8\3\2\2\2\u01c8\u01d1\3\2\2\2\u01c9\u01cc\7")
        buf.write("\32\2\2\u01ca\u01cd\5 \21\2\u01cb\u01cd\5\34\17\2\u01cc")
        buf.write("\u01ca\3\2\2\2\u01cc\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2")
        buf.write("\u01ce\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d1\3")
        buf.write("\2\2\2\u01d0\u01c3\3\2\2\2\u01d0\u01c9\3\2\2\2\u01d1\33")
        buf.write("\3\2\2\2\u01d2\u01d4\5\36\20\2\u01d3\u01d5\5\26\f\2\u01d4")
        buf.write("\u01d3\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d4\3\2\2\2")
        buf.write("\u01d6\u01d7\3\2\2\2\u01d7\u01d9\3\2\2\2\u01d8\u01da\5")
        buf.write("\30\r\2\u01d9\u01d8\3\2\2\2\u01d9\u01da\3\2\2\2\u01da")
        buf.write("\35\3\2\2\2\u01db\u01dc\7\35\2\2\u01dc\37\3\2\2\2\u01dd")
        buf.write("\u01df\5\"\22\2\u01de\u01e0\5\26\f\2\u01df\u01de\3\2\2")
        buf.write("\2\u01e0\u01e1\3\2\2\2\u01e1\u01df\3\2\2\2\u01e1\u01e2")
        buf.write("\3\2\2\2\u01e2\u01e4\3\2\2\2\u01e3\u01e5\5\30\r\2\u01e4")
        buf.write("\u01e3\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5!\3\2\2\2\u01e6")
        buf.write("\u01e7\7\34\2\2\u01e7#\3\2\2\2\u01e8\u01ea\7\33\2\2\u01e9")
        buf.write("\u01eb\7\n\2\2\u01ea\u01e9\3\2\2\2\u01eb\u01ec\3\2\2\2")
        buf.write("\u01ec\u01ea\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed%\3\2\2")
        buf.write("\2\u01ee\u01f0\7\5\2\2\u01ef\u01f1\5(\25\2\u01f0\u01ef")
        buf.write("\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f2")
        buf.write("\u01f3\3\2\2\2\u01f3\'\3\2\2\2\u01f4\u01f6\5*\26\2\u01f5")
        buf.write("\u01f7\5\26\f\2\u01f6\u01f5\3\2\2\2\u01f7\u01f8\3\2\2")
        buf.write("\2\u01f8\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01fb")
        buf.write("\3\2\2\2\u01fa\u01fc\5\30\r\2\u01fb\u01fa\3\2\2\2\u01fb")
        buf.write("\u01fc\3\2\2\2\u01fc)\3\2\2\2\u01fd\u01fe\7\36\2\2\u01fe")
        buf.write("+\3\2\2\2\177-\62\66>AHOTZ]`cgjmptwz}\u0081\u0084\u0087")
        buf.write("\u008a\u008e\u0091\u0094\u0097\u009b\u009e\u00a1\u00a4")
        buf.write("\u00a8\u00ab\u00ae\u00b1\u00b5\u00b8\u00bb\u00be\u00c2")
        buf.write("\u00c5\u00c8\u00cb\u00cf\u00d2\u00d5\u00d8\u00dc\u00df")
        buf.write("\u00e2\u00e5\u00e9\u00ec\u00ef\u00f2\u00f6\u00f9\u00fc")
        buf.write("\u00ff\u0103\u0106\u0109\u010c\u0110\u0113\u0116\u0119")
        buf.write("\u011d\u0120\u0123\u0126\u012a\u012d\u0130\u0133\u0137")
        buf.write("\u013a\u013d\u0140\u0144\u0147\u014a\u014d\u0151\u0154")
        buf.write("\u0157\u015a\u015e\u0161\u0164\u0167\u016b\u016e\u0171")
        buf.write("\u0174\u0178\u017b\u017e\u0181\u0185\u0188\u018b\u018e")
        buf.write("\u0190\u019a\u01a2\u01a7\u01aa\u01b3\u01b9\u01bb\u01c1")
        buf.write("\u01c7\u01cc\u01ce\u01d0\u01d6\u01d9\u01e1\u01e4\u01ec")
        buf.write("\u01f2\u01f8\u01fb")
        return buf.getvalue()


class QuestionParser ( Parser ):

    grammarFileName = "QuestionParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "START_QUESTION_HEADER", "START_QUESTION", 
                      "END_ANSWERS", "FEEDBACK_MARKER", "MEDIA", "IMAGE_TAG", 
                      "HYPERLINK", "ALL_CHARACTER", "ESCAPED_OPEN_BRACKET", 
                      "ESCAPED_CLOSE_BRACKET", "SECTION_TITLE", "TITLE", 
                      "POINTS", "RANDOMIZE_TRUE", "RANDOMIZE_FALSE", "TYPE_MC", 
                      "TYPE_TF", "TYPE_MS", "TYPE_MT", "TYPE_ORD", "TYPE_FIB", 
                      "TYPE_WR", "TYPE_OTHER", "START_ANSWER", "WR_ANSWER", 
                      "RIGHT_ANSWER", "LIST_PREFIX", "QUESTION_PREFIX" ]

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
    RULE_content = 10
    RULE_feedback = 11
    RULE_answer_list = 12
    RULE_list_item = 13
    RULE_list_prefix = 14
    RULE_list_answer_item = 15
    RULE_answer_prefix = 16
    RULE_wr_answer = 17
    RULE_end_answers = 18
    RULE_end_answers_item = 19
    RULE_question_prefix = 20

    ruleNames =  [ "parse_question", "section_title", "question", "start_question", 
                   "question_header", "question_type", "title", "points", 
                   "randomize", "question_body", "content", "feedback", 
                   "answer_list", "list_item", "list_prefix", "list_answer_item", 
                   "answer_prefix", "wr_answer", "end_answers", "end_answers_item", 
                   "question_prefix" ]

    EOF = Token.EOF
    START_QUESTION_HEADER=1
    START_QUESTION=2
    END_ANSWERS=3
    FEEDBACK_MARKER=4
    MEDIA=5
    IMAGE_TAG=6
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
    WR_ANSWER=25
    RIGHT_ANSWER=26
    LIST_PREFIX=27
    QUESTION_PREFIX=28

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
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.SECTION_TITLE:
                self.state = 42
                self.section_title()


            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==QuestionParser.START_QUESTION_HEADER or _la==QuestionParser.START_QUESTION:
                self.state = 45
                self.question()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.END_ANSWERS:
                self.state = 51
                self.end_answers()


            self.state = 54
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

        def ALL_CHARACTER(self, i:int=None):
            if i is None:
                return self.getTokens(QuestionParser.ALL_CHARACTER)
            else:
                return self.getToken(QuestionParser.ALL_CHARACTER, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(QuestionParser.SECTION_TITLE)
            self.state = 58 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 57
                self.match(QuestionParser.ALL_CHARACTER)
                self.state = 60 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==QuestionParser.ALL_CHARACTER):
                    break

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


        def wr_answer(self):
            return self.getTypedRuleContext(QuestionParser.Wr_answerContext,0)


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
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.START_QUESTION_HEADER:
                    self.state = 62
                    self.question_header()


                self.state = 65
                self.start_question()
                self.state = 66
                self.question_body()
                self.state = 67
                self.answer_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.START_QUESTION_HEADER:
                    self.state = 69
                    self.question_header()


                self.state = 72
                self.start_question()
                self.state = 73
                self.question_body()
                self.state = 74
                self.wr_answer()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.START_QUESTION_HEADER:
                    self.state = 76
                    self.question_header()


                self.state = 79
                self.start_question()
                self.state = 80
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
            self.state = 84
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
            self.state = 398
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,104,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
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
                if _la==QuestionParser.POINTS:
                    self.state = 93
                    self.points()


                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 96
                    self.randomize()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
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
                if _la==QuestionParser.TITLE:
                    self.state = 103
                    self.title()


                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 106
                    self.randomize()


                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 109
                    self.points()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
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
                if _la==QuestionParser.TITLE:
                    self.state = 119
                    self.title()


                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 122
                    self.randomize()


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
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
                if _la==QuestionParser.POINTS:
                    self.state = 129
                    self.points()


                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 132
                    self.randomize()


                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 135
                    self.title()


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
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
                if _la==QuestionParser.TITLE:
                    self.state = 145
                    self.title()


                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 148
                    self.points()


                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 151
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 152
                    self.question_type()


                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 155
                    self.randomize()


                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 158
                    self.points()


                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 161
                    self.title()


                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
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
                if _la==QuestionParser.POINTS:
                    self.state = 171
                    self.points()


                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 174
                    self.randomize()


                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
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
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 181
                    self.question_type()


                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 184
                    self.randomize()


                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 187
                    self.points()


                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
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
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 197
                    self.question_type()


                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 200
                    self.randomize()


                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
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
                if _la==QuestionParser.POINTS:
                    self.state = 207
                    self.points()


                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 210
                    self.randomize()


                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 213
                    self.question_type()


                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
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
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 223
                    self.question_type()


                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 226
                    self.points()


                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 229
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 230
                    self.title()


                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 233
                    self.randomize()


                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 236
                    self.points()


                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 239
                    self.question_type()


                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
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
                if _la==QuestionParser.TITLE:
                    self.state = 249
                    self.title()


                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 252
                    self.randomize()


                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
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
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 259
                    self.question_type()


                self.state = 263
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 262
                    self.randomize()


                self.state = 266
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 265
                    self.title()


                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
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
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 275
                    self.question_type()


                self.state = 279
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 278
                    self.randomize()


                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
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
                if _la==QuestionParser.TITLE:
                    self.state = 285
                    self.title()


                self.state = 289
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 288
                    self.randomize()


                self.state = 292
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 291
                    self.question_type()


                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
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
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 301
                    self.question_type()


                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 304
                    self.title()


                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 307
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 308
                    self.points()


                self.state = 312
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 311
                    self.randomize()


                self.state = 315
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 314
                    self.title()


                self.state = 318
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 317
                    self.question_type()


                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
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
                if _la==QuestionParser.TITLE:
                    self.state = 327
                    self.title()


                self.state = 331
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 330
                    self.points()


                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
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
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 337
                    self.question_type()


                self.state = 341
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 340
                    self.points()


                self.state = 344
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 343
                    self.title()


                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)
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
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 353
                    self.question_type()


                self.state = 357
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 356
                    self.points()


                pass

            elif la_ == 22:
                self.enterOuterAlt(localctx, 22)
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
                if _la==QuestionParser.TITLE:
                    self.state = 363
                    self.title()


                self.state = 367
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 366
                    self.points()


                self.state = 370
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 369
                    self.question_type()


                pass

            elif la_ == 23:
                self.enterOuterAlt(localctx, 23)
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
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 379
                    self.question_type()


                self.state = 383
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 382
                    self.title()


                pass

            elif la_ == 24:
                self.enterOuterAlt(localctx, 24)
                self.state = 385
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 387
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 386
                    self.randomize()


                self.state = 390
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 389
                    self.points()


                self.state = 393
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 392
                    self.title()


                self.state = 396
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 395
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
            self.state = 408
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuestionParser.TYPE_MC]:
                localctx = QuestionParser.TypeMcContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                self.match(QuestionParser.TYPE_MC)
                pass
            elif token in [QuestionParser.TYPE_TF]:
                localctx = QuestionParser.TypeTfContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 401
                self.match(QuestionParser.TYPE_TF)
                pass
            elif token in [QuestionParser.TYPE_MS]:
                localctx = QuestionParser.TypeMsContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 402
                self.match(QuestionParser.TYPE_MS)
                pass
            elif token in [QuestionParser.TYPE_MT]:
                localctx = QuestionParser.TypeMtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 403
                self.match(QuestionParser.TYPE_MT)
                pass
            elif token in [QuestionParser.TYPE_ORD]:
                localctx = QuestionParser.TypeOrdContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 404
                self.match(QuestionParser.TYPE_ORD)
                pass
            elif token in [QuestionParser.TYPE_FIB]:
                localctx = QuestionParser.TypeFibContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 405
                self.match(QuestionParser.TYPE_FIB)
                pass
            elif token in [QuestionParser.TYPE_WR]:
                localctx = QuestionParser.TypeWrContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 406
                self.match(QuestionParser.TYPE_WR)
                pass
            elif token in [QuestionParser.TYPE_OTHER]:
                localctx = QuestionParser.TypeOtherContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 407
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
            self.state = 410
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
            self.state = 412
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
            self.state = 416
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuestionParser.RANDOMIZE_TRUE]:
                localctx = QuestionParser.RandomTrueContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 414
                self.match(QuestionParser.RANDOMIZE_TRUE)
                pass
            elif token in [QuestionParser.RANDOMIZE_FALSE]:
                localctx = QuestionParser.RandomFalseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 415
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
            self.state = 419 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 418
                self.content()
                self.state = 421 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.MEDIA) | (1 << QuestionParser.IMAGE_TAG) | (1 << QuestionParser.HYPERLINK) | (1 << QuestionParser.ALL_CHARACTER) | (1 << QuestionParser.ESCAPED_OPEN_BRACKET))) != 0)):
                    break

            self.state = 424
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.FEEDBACK_MARKER:
                self.state = 423
                self.feedback()


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



    class ImageTagContext(ContentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuestionParser.ContentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IMAGE_TAG(self):
            return self.getToken(QuestionParser.IMAGE_TAG, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImageTag" ):
                listener.enterImageTag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImageTag" ):
                listener.exitImageTag(self)


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
        self.enterRule(localctx, 20, self.RULE_content)
        self._la = 0 # Token type
        try:
            self.state = 441
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuestionParser.IMAGE_TAG]:
                localctx = QuestionParser.ImageTagContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.match(QuestionParser.IMAGE_TAG)
                pass
            elif token in [QuestionParser.MEDIA]:
                localctx = QuestionParser.MediaContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 427
                self.match(QuestionParser.MEDIA)
                pass
            elif token in [QuestionParser.HYPERLINK]:
                localctx = QuestionParser.HyperlinkContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 428
                self.match(QuestionParser.HYPERLINK)
                pass
            elif token in [QuestionParser.ESCAPED_OPEN_BRACKET]:
                localctx = QuestionParser.FibAnswerContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 429
                self.match(QuestionParser.ESCAPED_OPEN_BRACKET)
                self.state = 431 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 430
                    self.match(QuestionParser.ALL_CHARACTER)
                    self.state = 433 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==QuestionParser.ALL_CHARACTER):
                        break

                self.state = 435
                self.match(QuestionParser.ESCAPED_CLOSE_BRACKET)
                pass
            elif token in [QuestionParser.ALL_CHARACTER]:
                localctx = QuestionParser.ContentCharactersContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 437 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 436
                        self.match(QuestionParser.ALL_CHARACTER)

                    else:
                        raise NoViableAltException(self)
                    self.state = 439 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,110,self._ctx)

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
        self.enterRule(localctx, 22, self.RULE_feedback)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.match(QuestionParser.FEEDBACK_MARKER)
            self.state = 445 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 444
                self.content()
                self.state = 447 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.MEDIA) | (1 << QuestionParser.IMAGE_TAG) | (1 << QuestionParser.HYPERLINK) | (1 << QuestionParser.ALL_CHARACTER) | (1 << QuestionParser.ESCAPED_OPEN_BRACKET))) != 0)):
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
        self.enterRule(localctx, 24, self.RULE_answer_list)
        self._la = 0 # Token type
        try:
            self.state = 462
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,116,self._ctx)
            if la_ == 1:
                localctx = QuestionParser.ListNoAnswerContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 449
                self.match(QuestionParser.START_ANSWER)
                self.state = 451 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 450
                    self.list_item()
                    self.state = 453 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==QuestionParser.LIST_PREFIX):
                        break

                pass

            elif la_ == 2:
                localctx = QuestionParser.ListWithAnswerContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 455
                self.match(QuestionParser.START_ANSWER)
                self.state = 458 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 458
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [QuestionParser.RIGHT_ANSWER]:
                        self.state = 456
                        self.list_answer_item()
                        pass
                    elif token in [QuestionParser.LIST_PREFIX]:
                        self.state = 457
                        self.list_item()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 460 
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
        self.enterRule(localctx, 26, self.RULE_list_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self.list_prefix()
            self.state = 466 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 465
                self.content()
                self.state = 468 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.MEDIA) | (1 << QuestionParser.IMAGE_TAG) | (1 << QuestionParser.HYPERLINK) | (1 << QuestionParser.ALL_CHARACTER) | (1 << QuestionParser.ESCAPED_OPEN_BRACKET))) != 0)):
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
        self.enterRule(localctx, 28, self.RULE_list_prefix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
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
        self.enterRule(localctx, 30, self.RULE_list_answer_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.answer_prefix()
            self.state = 477 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 476
                self.content()
                self.state = 479 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.MEDIA) | (1 << QuestionParser.IMAGE_TAG) | (1 << QuestionParser.HYPERLINK) | (1 << QuestionParser.ALL_CHARACTER) | (1 << QuestionParser.ESCAPED_OPEN_BRACKET))) != 0)):
                    break

            self.state = 482
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.FEEDBACK_MARKER:
                self.state = 481
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
        self.enterRule(localctx, 32, self.RULE_answer_prefix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self.match(QuestionParser.RIGHT_ANSWER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Wr_answerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WR_ANSWER(self):
            return self.getToken(QuestionParser.WR_ANSWER, 0)

        def ALL_CHARACTER(self, i:int=None):
            if i is None:
                return self.getTokens(QuestionParser.ALL_CHARACTER)
            else:
                return self.getToken(QuestionParser.ALL_CHARACTER, i)

        def getRuleIndex(self):
            return QuestionParser.RULE_wr_answer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWr_answer" ):
                listener.enterWr_answer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWr_answer" ):
                listener.exitWr_answer(self)




    def wr_answer(self):

        localctx = QuestionParser.Wr_answerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_wr_answer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.match(QuestionParser.WR_ANSWER)
            self.state = 488 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 487
                self.match(QuestionParser.ALL_CHARACTER)
                self.state = 490 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==QuestionParser.ALL_CHARACTER):
                    break

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
            self.state = 492
            self.match(QuestionParser.END_ANSWERS)
            self.state = 494 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 493
                self.end_answers_item()
                self.state = 496 
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
            self.state = 498
            self.question_prefix()
            self.state = 500 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 499
                self.content()
                self.state = 502 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.MEDIA) | (1 << QuestionParser.IMAGE_TAG) | (1 << QuestionParser.HYPERLINK) | (1 << QuestionParser.ALL_CHARACTER) | (1 << QuestionParser.ESCAPED_OPEN_BRACKET))) != 0)):
                    break

            self.state = 505
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.FEEDBACK_MARKER:
                self.state = 504
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
        self.enterRule(localctx, 40, self.RULE_question_prefix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.match(QuestionParser.QUESTION_PREFIX)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





