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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\32")
        buf.write("\u01ca\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\7\2*\n\2\f\2\16\2-\13\2\3\2\5\2\60\n\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3=\n\3")
        buf.write("\3\4\3\4\3\5\5\5B\n\5\3\5\5\5E\n\5\3\5\5\5H\n\5\3\5\5")
        buf.write("\5K\n\5\3\5\5\5N\n\5\3\5\5\5Q\n\5\3\5\5\5T\n\5\3\5\5\5")
        buf.write("W\n\5\3\5\5\5Z\n\5\3\5\5\5]\n\5\3\5\5\5`\n\5\3\5\5\5c")
        buf.write("\n\5\3\5\5\5f\n\5\3\5\5\5i\n\5\3\5\5\5l\n\5\3\5\5\5o\n")
        buf.write("\5\3\5\5\5r\n\5\3\5\5\5u\n\5\3\5\5\5x\n\5\3\5\5\5{\n\5")
        buf.write("\3\5\5\5~\n\5\3\5\5\5\u0081\n\5\3\5\5\5\u0084\n\5\3\5")
        buf.write("\5\5\u0087\n\5\3\5\5\5\u008a\n\5\3\5\5\5\u008d\n\5\3\5")
        buf.write("\5\5\u0090\n\5\3\5\5\5\u0093\n\5\3\5\5\5\u0096\n\5\3\5")
        buf.write("\5\5\u0099\n\5\3\5\5\5\u009c\n\5\3\5\5\5\u009f\n\5\3\5")
        buf.write("\5\5\u00a2\n\5\3\5\5\5\u00a5\n\5\3\5\5\5\u00a8\n\5\3\5")
        buf.write("\5\5\u00ab\n\5\3\5\5\5\u00ae\n\5\3\5\5\5\u00b1\n\5\3\5")
        buf.write("\5\5\u00b4\n\5\3\5\5\5\u00b7\n\5\3\5\5\5\u00ba\n\5\3\5")
        buf.write("\5\5\u00bd\n\5\3\5\5\5\u00c0\n\5\3\5\5\5\u00c3\n\5\3\5")
        buf.write("\5\5\u00c6\n\5\3\5\5\5\u00c9\n\5\3\5\5\5\u00cc\n\5\3\5")
        buf.write("\5\5\u00cf\n\5\3\5\5\5\u00d2\n\5\3\5\5\5\u00d5\n\5\3\5")
        buf.write("\5\5\u00d8\n\5\3\5\5\5\u00db\n\5\3\5\5\5\u00de\n\5\3\5")
        buf.write("\5\5\u00e1\n\5\3\5\5\5\u00e4\n\5\3\5\5\5\u00e7\n\5\3\5")
        buf.write("\5\5\u00ea\n\5\3\5\5\5\u00ed\n\5\3\5\5\5\u00f0\n\5\3\5")
        buf.write("\5\5\u00f3\n\5\3\5\5\5\u00f6\n\5\3\5\5\5\u00f9\n\5\3\5")
        buf.write("\5\5\u00fc\n\5\3\5\5\5\u00ff\n\5\3\5\5\5\u0102\n\5\3\5")
        buf.write("\5\5\u0105\n\5\3\5\5\5\u0108\n\5\3\5\5\5\u010b\n\5\3\5")
        buf.write("\5\5\u010e\n\5\3\5\5\5\u0111\n\5\3\5\5\5\u0114\n\5\3\5")
        buf.write("\5\5\u0117\n\5\3\5\5\5\u011a\n\5\3\5\5\5\u011d\n\5\3\5")
        buf.write("\5\5\u0120\n\5\3\5\5\5\u0123\n\5\3\5\5\5\u0126\n\5\3\5")
        buf.write("\5\5\u0129\n\5\3\5\5\5\u012c\n\5\3\5\5\5\u012f\n\5\3\5")
        buf.write("\5\5\u0132\n\5\3\5\5\5\u0135\n\5\3\5\5\5\u0138\n\5\3\5")
        buf.write("\5\5\u013b\n\5\3\5\5\5\u013e\n\5\3\5\5\5\u0141\n\5\3\5")
        buf.write("\5\5\u0144\n\5\3\5\5\5\u0147\n\5\3\5\5\5\u014a\n\5\3\5")
        buf.write("\5\5\u014d\n\5\3\5\5\5\u0150\n\5\3\5\5\5\u0153\n\5\3\5")
        buf.write("\5\5\u0156\n\5\3\5\5\5\u0159\n\5\3\5\5\5\u015c\n\5\3\5")
        buf.write("\5\5\u015f\n\5\5\5\u0161\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\5\6\u016b\n\6\3\7\3\7\3\b\3\b\3\t\3\t\5\t\u0173")
        buf.write("\n\t\3\n\3\n\6\n\u0177\n\n\r\n\16\n\u0178\3\n\5\n\u017c")
        buf.write("\n\n\3\13\3\13\3\f\3\f\3\f\3\f\6\f\u0184\n\f\r\f\16\f")
        buf.write("\u0185\3\f\3\f\6\f\u018a\n\f\r\f\16\f\u018b\5\f\u018e")
        buf.write("\n\f\3\r\3\r\6\r\u0192\n\r\r\r\16\r\u0193\3\16\3\16\6")
        buf.write("\16\u0198\n\16\r\16\16\16\u0199\3\16\3\16\3\16\6\16\u019f")
        buf.write("\n\16\r\16\16\16\u01a0\5\16\u01a3\n\16\3\17\3\17\6\17")
        buf.write("\u01a7\n\17\r\17\16\17\u01a8\3\17\5\17\u01ac\n\17\3\20")
        buf.write("\3\20\3\21\3\21\6\21\u01b2\n\21\r\21\16\21\u01b3\3\21")
        buf.write("\5\21\u01b7\n\21\3\22\3\22\3\23\3\23\6\23\u01bd\n\23\r")
        buf.write("\23\16\23\u01be\3\24\3\24\6\24\u01c3\n\24\r\24\16\24\u01c4")
        buf.write("\3\24\5\24\u01c8\n\24\3\24\2\2\25\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&\2\2\2\u024b\2+\3\2\2\2\4<\3\2")
        buf.write("\2\2\6>\3\2\2\2\b\u0160\3\2\2\2\n\u016a\3\2\2\2\f\u016c")
        buf.write("\3\2\2\2\16\u016e\3\2\2\2\20\u0172\3\2\2\2\22\u0174\3")
        buf.write("\2\2\2\24\u017d\3\2\2\2\26\u018d\3\2\2\2\30\u018f\3\2")
        buf.write("\2\2\32\u01a2\3\2\2\2\34\u01a4\3\2\2\2\36\u01ad\3\2\2")
        buf.write("\2 \u01af\3\2\2\2\"\u01b8\3\2\2\2$\u01ba\3\2\2\2&\u01c0")
        buf.write("\3\2\2\2(*\5\4\3\2)(\3\2\2\2*-\3\2\2\2+)\3\2\2\2+,\3\2")
        buf.write("\2\2,/\3\2\2\2-+\3\2\2\2.\60\5$\23\2/.\3\2\2\2/\60\3\2")
        buf.write("\2\2\60\61\3\2\2\2\61\62\7\2\2\3\62\3\3\2\2\2\63\64\5")
        buf.write("\6\4\2\64\65\5\b\5\2\65\66\5\22\n\2\66\67\5\32\16\2\67")
        buf.write("=\3\2\2\289\5\6\4\29:\5\b\5\2:;\5\22\n\2;=\3\2\2\2<\63")
        buf.write("\3\2\2\2<8\3\2\2\2=\5\3\2\2\2>?\7\3\2\2?\7\3\2\2\2@B\5")
        buf.write("\n\6\2A@\3\2\2\2AB\3\2\2\2BD\3\2\2\2CE\5\f\7\2DC\3\2\2")
        buf.write("\2DE\3\2\2\2EG\3\2\2\2FH\5\16\b\2GF\3\2\2\2GH\3\2\2\2")
        buf.write("HJ\3\2\2\2IK\5\20\t\2JI\3\2\2\2JK\3\2\2\2K\u0161\3\2\2")
        buf.write("\2LN\5\n\6\2ML\3\2\2\2MN\3\2\2\2NP\3\2\2\2OQ\5\f\7\2P")
        buf.write("O\3\2\2\2PQ\3\2\2\2QS\3\2\2\2RT\5\20\t\2SR\3\2\2\2ST\3")
        buf.write("\2\2\2TV\3\2\2\2UW\5\16\b\2VU\3\2\2\2VW\3\2\2\2W\u0161")
        buf.write("\3\2\2\2XZ\5\n\6\2YX\3\2\2\2YZ\3\2\2\2Z\\\3\2\2\2[]\5")
        buf.write("\16\b\2\\[\3\2\2\2\\]\3\2\2\2]_\3\2\2\2^`\5\f\7\2_^\3")
        buf.write("\2\2\2_`\3\2\2\2`b\3\2\2\2ac\5\20\t\2ba\3\2\2\2bc\3\2")
        buf.write("\2\2c\u0161\3\2\2\2df\5\n\6\2ed\3\2\2\2ef\3\2\2\2fh\3")
        buf.write("\2\2\2gi\5\16\b\2hg\3\2\2\2hi\3\2\2\2ik\3\2\2\2jl\5\20")
        buf.write("\t\2kj\3\2\2\2kl\3\2\2\2ln\3\2\2\2mo\5\f\7\2nm\3\2\2\2")
        buf.write("no\3\2\2\2o\u0161\3\2\2\2pr\5\n\6\2qp\3\2\2\2qr\3\2\2")
        buf.write("\2rt\3\2\2\2su\5\20\t\2ts\3\2\2\2tu\3\2\2\2uw\3\2\2\2")
        buf.write("vx\5\f\7\2wv\3\2\2\2wx\3\2\2\2xz\3\2\2\2y{\5\16\b\2zy")
        buf.write("\3\2\2\2z{\3\2\2\2{\u0161\3\2\2\2|~\5\n\6\2}|\3\2\2\2")
        buf.write("}~\3\2\2\2~\u0080\3\2\2\2\177\u0081\5\20\t\2\u0080\177")
        buf.write("\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0083\3\2\2\2\u0082")
        buf.write("\u0084\5\16\b\2\u0083\u0082\3\2\2\2\u0083\u0084\3\2\2")
        buf.write("\2\u0084\u0086\3\2\2\2\u0085\u0087\5\f\7\2\u0086\u0085")
        buf.write("\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0161\3\2\2\2\u0088")
        buf.write("\u008a\5\f\7\2\u0089\u0088\3\2\2\2\u0089\u008a\3\2\2\2")
        buf.write("\u008a\u008c\3\2\2\2\u008b\u008d\5\n\6\2\u008c\u008b\3")
        buf.write("\2\2\2\u008c\u008d\3\2\2\2\u008d\u008f\3\2\2\2\u008e\u0090")
        buf.write("\5\16\b\2\u008f\u008e\3\2\2\2\u008f\u0090\3\2\2\2\u0090")
        buf.write("\u0092\3\2\2\2\u0091\u0093\5\20\t\2\u0092\u0091\3\2\2")
        buf.write("\2\u0092\u0093\3\2\2\2\u0093\u0161\3\2\2\2\u0094\u0096")
        buf.write("\5\f\7\2\u0095\u0094\3\2\2\2\u0095\u0096\3\2\2\2\u0096")
        buf.write("\u0098\3\2\2\2\u0097\u0099\5\n\6\2\u0098\u0097\3\2\2\2")
        buf.write("\u0098\u0099\3\2\2\2\u0099\u009b\3\2\2\2\u009a\u009c\5")
        buf.write("\20\t\2\u009b\u009a\3\2\2\2\u009b\u009c\3\2\2\2\u009c")
        buf.write("\u009e\3\2\2\2\u009d\u009f\5\16\b\2\u009e\u009d\3\2\2")
        buf.write("\2\u009e\u009f\3\2\2\2\u009f\u0161\3\2\2\2\u00a0\u00a2")
        buf.write("\5\f\7\2\u00a1\u00a0\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2")
        buf.write("\u00a4\3\2\2\2\u00a3\u00a5\5\16\b\2\u00a4\u00a3\3\2\2")
        buf.write("\2\u00a4\u00a5\3\2\2\2\u00a5\u00a7\3\2\2\2\u00a6\u00a8")
        buf.write("\5\n\6\2\u00a7\u00a6\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8")
        buf.write("\u00aa\3\2\2\2\u00a9\u00ab\5\20\t\2\u00aa\u00a9\3\2\2")
        buf.write("\2\u00aa\u00ab\3\2\2\2\u00ab\u0161\3\2\2\2\u00ac\u00ae")
        buf.write("\5\f\7\2\u00ad\u00ac\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae")
        buf.write("\u00b0\3\2\2\2\u00af\u00b1\5\16\b\2\u00b0\u00af\3\2\2")
        buf.write("\2\u00b0\u00b1\3\2\2\2\u00b1\u00b3\3\2\2\2\u00b2\u00b4")
        buf.write("\5\20\t\2\u00b3\u00b2\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4")
        buf.write("\u00b6\3\2\2\2\u00b5\u00b7\5\n\6\2\u00b6\u00b5\3\2\2\2")
        buf.write("\u00b6\u00b7\3\2\2\2\u00b7\u0161\3\2\2\2\u00b8\u00ba\5")
        buf.write("\f\7\2\u00b9\u00b8\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bc")
        buf.write("\3\2\2\2\u00bb\u00bd\5\20\t\2\u00bc\u00bb\3\2\2\2\u00bc")
        buf.write("\u00bd\3\2\2\2\u00bd\u00bf\3\2\2\2\u00be\u00c0\5\n\6\2")
        buf.write("\u00bf\u00be\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c2\3")
        buf.write("\2\2\2\u00c1\u00c3\5\16\b\2\u00c2\u00c1\3\2\2\2\u00c2")
        buf.write("\u00c3\3\2\2\2\u00c3\u0161\3\2\2\2\u00c4\u00c6\5\f\7\2")
        buf.write("\u00c5\u00c4\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c8\3")
        buf.write("\2\2\2\u00c7\u00c9\5\20\t\2\u00c8\u00c7\3\2\2\2\u00c8")
        buf.write("\u00c9\3\2\2\2\u00c9\u00cb\3\2\2\2\u00ca\u00cc\5\16\b")
        buf.write("\2\u00cb\u00ca\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00ce")
        buf.write("\3\2\2\2\u00cd\u00cf\5\n\6\2\u00ce\u00cd\3\2\2\2\u00ce")
        buf.write("\u00cf\3\2\2\2\u00cf\u0161\3\2\2\2\u00d0\u00d2\5\16\b")
        buf.write("\2\u00d1\u00d0\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d4")
        buf.write("\3\2\2\2\u00d3\u00d5\5\n\6\2\u00d4\u00d3\3\2\2\2\u00d4")
        buf.write("\u00d5\3\2\2\2\u00d5\u00d7\3\2\2\2\u00d6\u00d8\5\f\7\2")
        buf.write("\u00d7\u00d6\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00da\3")
        buf.write("\2\2\2\u00d9\u00db\5\20\t\2\u00da\u00d9\3\2\2\2\u00da")
        buf.write("\u00db\3\2\2\2\u00db\u0161\3\2\2\2\u00dc\u00de\5\16\b")
        buf.write("\2\u00dd\u00dc\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00e0")
        buf.write("\3\2\2\2\u00df\u00e1\5\n\6\2\u00e0\u00df\3\2\2\2\u00e0")
        buf.write("\u00e1\3\2\2\2\u00e1\u00e3\3\2\2\2\u00e2\u00e4\5\20\t")
        buf.write("\2\u00e3\u00e2\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e6")
        buf.write("\3\2\2\2\u00e5\u00e7\5\f\7\2\u00e6\u00e5\3\2\2\2\u00e6")
        buf.write("\u00e7\3\2\2\2\u00e7\u0161\3\2\2\2\u00e8\u00ea\5\16\b")
        buf.write("\2\u00e9\u00e8\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00ec")
        buf.write("\3\2\2\2\u00eb\u00ed\5\f\7\2\u00ec\u00eb\3\2\2\2\u00ec")
        buf.write("\u00ed\3\2\2\2\u00ed\u00ef\3\2\2\2\u00ee\u00f0\5\n\6\2")
        buf.write("\u00ef\u00ee\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00f2\3")
        buf.write("\2\2\2\u00f1\u00f3\5\20\t\2\u00f2\u00f1\3\2\2\2\u00f2")
        buf.write("\u00f3\3\2\2\2\u00f3\u0161\3\2\2\2\u00f4\u00f6\5\16\b")
        buf.write("\2\u00f5\u00f4\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f8")
        buf.write("\3\2\2\2\u00f7\u00f9\5\f\7\2\u00f8\u00f7\3\2\2\2\u00f8")
        buf.write("\u00f9\3\2\2\2\u00f9\u00fb\3\2\2\2\u00fa\u00fc\5\20\t")
        buf.write("\2\u00fb\u00fa\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fe")
        buf.write("\3\2\2\2\u00fd\u00ff\5\n\6\2\u00fe\u00fd\3\2\2\2\u00fe")
        buf.write("\u00ff\3\2\2\2\u00ff\u0161\3\2\2\2\u0100\u0102\5\16\b")
        buf.write("\2\u0101\u0100\3\2\2\2\u0101\u0102\3\2\2\2\u0102\u0104")
        buf.write("\3\2\2\2\u0103\u0105\5\20\t\2\u0104\u0103\3\2\2\2\u0104")
        buf.write("\u0105\3\2\2\2\u0105\u0107\3\2\2\2\u0106\u0108\5\n\6\2")
        buf.write("\u0107\u0106\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u010a\3")
        buf.write("\2\2\2\u0109\u010b\5\f\7\2\u010a\u0109\3\2\2\2\u010a\u010b")
        buf.write("\3\2\2\2\u010b\u0161\3\2\2\2\u010c\u010e\5\16\b\2\u010d")
        buf.write("\u010c\3\2\2\2\u010d\u010e\3\2\2\2\u010e\u0110\3\2\2\2")
        buf.write("\u010f\u0111\5\20\t\2\u0110\u010f\3\2\2\2\u0110\u0111")
        buf.write("\3\2\2\2\u0111\u0113\3\2\2\2\u0112\u0114\5\f\7\2\u0113")
        buf.write("\u0112\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0116\3\2\2\2")
        buf.write("\u0115\u0117\5\n\6\2\u0116\u0115\3\2\2\2\u0116\u0117\3")
        buf.write("\2\2\2\u0117\u0161\3\2\2\2\u0118\u011a\5\20\t\2\u0119")
        buf.write("\u0118\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u011c\3\2\2\2")
        buf.write("\u011b\u011d\5\n\6\2\u011c\u011b\3\2\2\2\u011c\u011d\3")
        buf.write("\2\2\2\u011d\u011f\3\2\2\2\u011e\u0120\5\f\7\2\u011f\u011e")
        buf.write("\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u0122\3\2\2\2\u0121")
        buf.write("\u0123\5\16\b\2\u0122\u0121\3\2\2\2\u0122\u0123\3\2\2")
        buf.write("\2\u0123\u0161\3\2\2\2\u0124\u0126\5\20\t\2\u0125\u0124")
        buf.write("\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0128\3\2\2\2\u0127")
        buf.write("\u0129\5\n\6\2\u0128\u0127\3\2\2\2\u0128\u0129\3\2\2\2")
        buf.write("\u0129\u012b\3\2\2\2\u012a\u012c\5\16\b\2\u012b\u012a")
        buf.write("\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012e\3\2\2\2\u012d")
        buf.write("\u012f\5\f\7\2\u012e\u012d\3\2\2\2\u012e\u012f\3\2\2\2")
        buf.write("\u012f\u0161\3\2\2\2\u0130\u0132\5\20\t\2\u0131\u0130")
        buf.write("\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0134\3\2\2\2\u0133")
        buf.write("\u0135\5\f\7\2\u0134\u0133\3\2\2\2\u0134\u0135\3\2\2\2")
        buf.write("\u0135\u0137\3\2\2\2\u0136\u0138\5\n\6\2\u0137\u0136\3")
        buf.write("\2\2\2\u0137\u0138\3\2\2\2\u0138\u013a\3\2\2\2\u0139\u013b")
        buf.write("\5\16\b\2\u013a\u0139\3\2\2\2\u013a\u013b\3\2\2\2\u013b")
        buf.write("\u0161\3\2\2\2\u013c\u013e\5\20\t\2\u013d\u013c\3\2\2")
        buf.write("\2\u013d\u013e\3\2\2\2\u013e\u0140\3\2\2\2\u013f\u0141")
        buf.write("\5\f\7\2\u0140\u013f\3\2\2\2\u0140\u0141\3\2\2\2\u0141")
        buf.write("\u0143\3\2\2\2\u0142\u0144\5\16\b\2\u0143\u0142\3\2\2")
        buf.write("\2\u0143\u0144\3\2\2\2\u0144\u0146\3\2\2\2\u0145\u0147")
        buf.write("\5\n\6\2\u0146\u0145\3\2\2\2\u0146\u0147\3\2\2\2\u0147")
        buf.write("\u0161\3\2\2\2\u0148\u014a\5\20\t\2\u0149\u0148\3\2\2")
        buf.write("\2\u0149\u014a\3\2\2\2\u014a\u014c\3\2\2\2\u014b\u014d")
        buf.write("\5\16\b\2\u014c\u014b\3\2\2\2\u014c\u014d\3\2\2\2\u014d")
        buf.write("\u014f\3\2\2\2\u014e\u0150\5\n\6\2\u014f\u014e\3\2\2\2")
        buf.write("\u014f\u0150\3\2\2\2\u0150\u0152\3\2\2\2\u0151\u0153\5")
        buf.write("\f\7\2\u0152\u0151\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0161")
        buf.write("\3\2\2\2\u0154\u0156\5\20\t\2\u0155\u0154\3\2\2\2\u0155")
        buf.write("\u0156\3\2\2\2\u0156\u0158\3\2\2\2\u0157\u0159\5\16\b")
        buf.write("\2\u0158\u0157\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u015b")
        buf.write("\3\2\2\2\u015a\u015c\5\f\7\2\u015b\u015a\3\2\2\2\u015b")
        buf.write("\u015c\3\2\2\2\u015c\u015e\3\2\2\2\u015d\u015f\5\n\6\2")
        buf.write("\u015e\u015d\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u0161\3")
        buf.write("\2\2\2\u0160A\3\2\2\2\u0160M\3\2\2\2\u0160Y\3\2\2\2\u0160")
        buf.write("e\3\2\2\2\u0160q\3\2\2\2\u0160}\3\2\2\2\u0160\u0089\3")
        buf.write("\2\2\2\u0160\u0095\3\2\2\2\u0160\u00a1\3\2\2\2\u0160\u00ad")
        buf.write("\3\2\2\2\u0160\u00b9\3\2\2\2\u0160\u00c5\3\2\2\2\u0160")
        buf.write("\u00d1\3\2\2\2\u0160\u00dd\3\2\2\2\u0160\u00e9\3\2\2\2")
        buf.write("\u0160\u00f5\3\2\2\2\u0160\u0101\3\2\2\2\u0160\u010d\3")
        buf.write("\2\2\2\u0160\u0119\3\2\2\2\u0160\u0125\3\2\2\2\u0160\u0131")
        buf.write("\3\2\2\2\u0160\u013d\3\2\2\2\u0160\u0149\3\2\2\2\u0160")
        buf.write("\u0155\3\2\2\2\u0161\t\3\2\2\2\u0162\u016b\7\20\2\2\u0163")
        buf.write("\u016b\7\21\2\2\u0164\u016b\7\22\2\2\u0165\u016b\7\23")
        buf.write("\2\2\u0166\u016b\7\24\2\2\u0167\u016b\7\25\2\2\u0168\u016b")
        buf.write("\7\26\2\2\u0169\u016b\7\27\2\2\u016a\u0162\3\2\2\2\u016a")
        buf.write("\u0163\3\2\2\2\u016a\u0164\3\2\2\2\u016a\u0165\3\2\2\2")
        buf.write("\u016a\u0166\3\2\2\2\u016a\u0167\3\2\2\2\u016a\u0168\3")
        buf.write("\2\2\2\u016a\u0169\3\2\2\2\u016b\13\3\2\2\2\u016c\u016d")
        buf.write("\7\f\2\2\u016d\r\3\2\2\2\u016e\u016f\7\r\2\2\u016f\17")
        buf.write("\3\2\2\2\u0170\u0173\7\16\2\2\u0171\u0173\7\17\2\2\u0172")
        buf.write("\u0170\3\2\2\2\u0172\u0171\3\2\2\2\u0173\21\3\2\2\2\u0174")
        buf.write("\u0176\5\24\13\2\u0175\u0177\5\26\f\2\u0176\u0175\3\2")
        buf.write("\2\2\u0177\u0178\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0179")
        buf.write("\3\2\2\2\u0179\u017b\3\2\2\2\u017a\u017c\5\30\r\2\u017b")
        buf.write("\u017a\3\2\2\2\u017b\u017c\3\2\2\2\u017c\23\3\2\2\2\u017d")
        buf.write("\u017e\7\5\2\2\u017e\25\3\2\2\2\u017f\u018e\7\7\2\2\u0180")
        buf.write("\u018e\7\b\2\2\u0181\u0183\7\n\2\2\u0182\u0184\7\t\2\2")
        buf.write("\u0183\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0183\3")
        buf.write("\2\2\2\u0185\u0186\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u018e")
        buf.write("\7\13\2\2\u0188\u018a\7\t\2\2\u0189\u0188\3\2\2\2\u018a")
        buf.write("\u018b\3\2\2\2\u018b\u0189\3\2\2\2\u018b\u018c\3\2\2\2")
        buf.write("\u018c\u018e\3\2\2\2\u018d\u017f\3\2\2\2\u018d\u0180\3")
        buf.write("\2\2\2\u018d\u0181\3\2\2\2\u018d\u0189\3\2\2\2\u018e\27")
        buf.write("\3\2\2\2\u018f\u0191\7\6\2\2\u0190\u0192\5\26\f\2\u0191")
        buf.write("\u0190\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0191\3\2\2\2")
        buf.write("\u0193\u0194\3\2\2\2\u0194\31\3\2\2\2\u0195\u0197\7\30")
        buf.write("\2\2\u0196\u0198\5\34\17\2\u0197\u0196\3\2\2\2\u0198\u0199")
        buf.write("\3\2\2\2\u0199\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019a")
        buf.write("\u01a3\3\2\2\2\u019b\u019e\7\30\2\2\u019c\u019f\5 \21")
        buf.write("\2\u019d\u019f\5\34\17\2\u019e\u019c\3\2\2\2\u019e\u019d")
        buf.write("\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u019e\3\2\2\2\u01a0")
        buf.write("\u01a1\3\2\2\2\u01a1\u01a3\3\2\2\2\u01a2\u0195\3\2\2\2")
        buf.write("\u01a2\u019b\3\2\2\2\u01a3\33\3\2\2\2\u01a4\u01a6\5\36")
        buf.write("\20\2\u01a5\u01a7\5\26\f\2\u01a6\u01a5\3\2\2\2\u01a7\u01a8")
        buf.write("\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9")
        buf.write("\u01ab\3\2\2\2\u01aa\u01ac\5\30\r\2\u01ab\u01aa\3\2\2")
        buf.write("\2\u01ab\u01ac\3\2\2\2\u01ac\35\3\2\2\2\u01ad\u01ae\7")
        buf.write("\32\2\2\u01ae\37\3\2\2\2\u01af\u01b1\5\"\22\2\u01b0\u01b2")
        buf.write("\5\26\f\2\u01b1\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3")
        buf.write("\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b6\3\2\2\2")
        buf.write("\u01b5\u01b7\5\30\r\2\u01b6\u01b5\3\2\2\2\u01b6\u01b7")
        buf.write("\3\2\2\2\u01b7!\3\2\2\2\u01b8\u01b9\7\31\2\2\u01b9#\3")
        buf.write("\2\2\2\u01ba\u01bc\7\4\2\2\u01bb\u01bd\5&\24\2\u01bc\u01bb")
        buf.write("\3\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01bc\3\2\2\2\u01be")
        buf.write("\u01bf\3\2\2\2\u01bf%\3\2\2\2\u01c0\u01c2\5\24\13\2\u01c1")
        buf.write("\u01c3\5\26\f\2\u01c2\u01c1\3\2\2\2\u01c3\u01c4\3\2\2")
        buf.write("\2\u01c4\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c7")
        buf.write("\3\2\2\2\u01c6\u01c8\5\30\r\2\u01c7\u01c6\3\2\2\2\u01c7")
        buf.write("\u01c8\3\2\2\2\u01c8\'\3\2\2\2y+/<ADGJMPSVY\\_behknqt")
        buf.write("wz}\u0080\u0083\u0086\u0089\u008c\u008f\u0092\u0095\u0098")
        buf.write("\u009b\u009e\u00a1\u00a4\u00a7\u00aa\u00ad\u00b0\u00b3")
        buf.write("\u00b6\u00b9\u00bc\u00bf\u00c2\u00c5\u00c8\u00cb\u00ce")
        buf.write("\u00d1\u00d4\u00d7\u00da\u00dd\u00e0\u00e3\u00e6\u00e9")
        buf.write("\u00ec\u00ef\u00f2\u00f5\u00f8\u00fb\u00fe\u0101\u0104")
        buf.write("\u0107\u010a\u010d\u0110\u0113\u0116\u0119\u011c\u011f")
        buf.write("\u0122\u0125\u0128\u012b\u012e\u0131\u0134\u0137\u013a")
        buf.write("\u013d\u0140\u0143\u0146\u0149\u014c\u014f\u0152\u0155")
        buf.write("\u0158\u015b\u015e\u0160\u016a\u0172\u0178\u017b\u0185")
        buf.write("\u018b\u018d\u0193\u0199\u019e\u01a0\u01a2\u01a8\u01ab")
        buf.write("\u01b3\u01b6\u01be\u01c4\u01c7")
        return buf.getvalue()


class QuestionParser ( Parser ):

    grammarFileName = "QuestionParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "START_QUESTION", "END_ANSWERS", "QUESTION_PREFIX", 
                      "FEEDBACK_MARKER", "MEDIA", "HYPERLINK", "ALL_CHARACTER", 
                      "ESCAPED_OPEN_BRACKET", "ESCAPED_CLOSE_BRACKET", "TITLE", 
                      "POINTS", "RANDOMIZE_TRUE", "RANDOMIZE_FALSE", "TYPE_MC", 
                      "TYPE_TF", "TYPE_MS", "TYPE_MT", "TYPE_ORD", "TYPE_FIB", 
                      "TYPE_WR", "TYPE_OTHER", "START_ANSWER", "RIGHT_ANSWER", 
                      "LIST_PREFIX" ]

    RULE_parse_question = 0
    RULE_question = 1
    RULE_start_question = 2
    RULE_question_header = 3
    RULE_question_type = 4
    RULE_title = 5
    RULE_points = 6
    RULE_randomize = 7
    RULE_question_body = 8
    RULE_question_prefix = 9
    RULE_content = 10
    RULE_feedback = 11
    RULE_answer_list = 12
    RULE_list_item = 13
    RULE_list_prefix = 14
    RULE_list_answer_item = 15
    RULE_answer_prefix = 16
    RULE_end_answers = 17
    RULE_end_answers_item = 18

    ruleNames =  [ "parse_question", "question", "start_question", "question_header", 
                   "question_type", "title", "points", "randomize", "question_body", 
                   "question_prefix", "content", "feedback", "answer_list", 
                   "list_item", "list_prefix", "list_answer_item", "answer_prefix", 
                   "end_answers", "end_answers_item" ]

    EOF = Token.EOF
    START_QUESTION=1
    END_ANSWERS=2
    QUESTION_PREFIX=3
    FEEDBACK_MARKER=4
    MEDIA=5
    HYPERLINK=6
    ALL_CHARACTER=7
    ESCAPED_OPEN_BRACKET=8
    ESCAPED_CLOSE_BRACKET=9
    TITLE=10
    POINTS=11
    RANDOMIZE_TRUE=12
    RANDOMIZE_FALSE=13
    TYPE_MC=14
    TYPE_TF=15
    TYPE_MS=16
    TYPE_MT=17
    TYPE_ORD=18
    TYPE_FIB=19
    TYPE_WR=20
    TYPE_OTHER=21
    START_ANSWER=22
    RIGHT_ANSWER=23
    LIST_PREFIX=24

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
            while _la==QuestionParser.START_QUESTION:
                self.state = 38
                self.question()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.END_ANSWERS:
                self.state = 44
                self.end_answers()


            self.state = 47
            self.match(QuestionParser.EOF)
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


        def question_header(self):
            return self.getTypedRuleContext(QuestionParser.Question_headerContext,0)


        def question_body(self):
            return self.getTypedRuleContext(QuestionParser.Question_bodyContext,0)


        def answer_list(self):
            return self.getTypedRuleContext(QuestionParser.Answer_listContext,0)


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
        self.enterRule(localctx, 2, self.RULE_question)
        try:
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.start_question()
                self.state = 50
                self.question_header()
                self.state = 51
                self.question_body()
                self.state = 52
                self.answer_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.start_question()
                self.state = 55
                self.question_header()
                self.state = 56
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
        self.enterRule(localctx, 4, self.RULE_start_question)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
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
        self.enterRule(localctx, 6, self.RULE_question_header)
        self._la = 0 # Token type
        try:
            self.state = 350
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,99,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 62
                    self.question_type()


                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 65
                    self.title()


                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 68
                    self.points()


                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 71
                    self.randomize()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
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
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 80
                    self.randomize()


                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 83
                    self.points()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 86
                    self.question_type()


                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 89
                    self.points()


                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 92
                    self.title()


                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 95
                    self.randomize()


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 98
                    self.question_type()


                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 101
                    self.points()


                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 104
                    self.randomize()


                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 107
                    self.title()


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 110
                    self.question_type()


                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 113
                    self.randomize()


                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 116
                    self.title()


                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 119
                    self.points()


                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 122
                    self.question_type()


                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 125
                    self.randomize()


                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 128
                    self.points()


                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 131
                    self.title()


                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 134
                    self.title()


                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 137
                    self.question_type()


                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 140
                    self.points()


                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 143
                    self.randomize()


                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 146
                    self.title()


                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 149
                    self.question_type()


                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 152
                    self.randomize()


                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 155
                    self.points()


                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 158
                    self.title()


                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 161
                    self.points()


                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 164
                    self.question_type()


                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 167
                    self.randomize()


                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 170
                    self.title()


                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 173
                    self.points()


                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 176
                    self.randomize()


                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 179
                    self.question_type()


                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 182
                    self.title()


                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 185
                    self.randomize()


                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 188
                    self.question_type()


                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 191
                    self.points()


                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 194
                    self.title()


                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 197
                    self.randomize()


                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 200
                    self.points()


                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 203
                    self.question_type()


                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 206
                    self.points()


                self.state = 210
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 209
                    self.question_type()


                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 212
                    self.title()


                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 215
                    self.randomize()


                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 218
                    self.points()


                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 221
                    self.question_type()


                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 224
                    self.randomize()


                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 227
                    self.title()


                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 230
                    self.points()


                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 233
                    self.title()


                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 236
                    self.question_type()


                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 239
                    self.randomize()


                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 242
                    self.points()


                self.state = 246
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 245
                    self.title()


                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 248
                    self.randomize()


                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 251
                    self.question_type()


                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 254
                    self.points()


                self.state = 258
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 257
                    self.randomize()


                self.state = 261
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 260
                    self.question_type()


                self.state = 264
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 263
                    self.title()


                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 267
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 266
                    self.points()


                self.state = 270
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 269
                    self.randomize()


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


                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 279
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 278
                    self.randomize()


                self.state = 282
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 281
                    self.question_type()


                self.state = 285
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 284
                    self.title()


                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 287
                    self.points()


                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 291
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 290
                    self.randomize()


                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 293
                    self.question_type()


                self.state = 297
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 296
                    self.points()


                self.state = 300
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 299
                    self.title()


                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)
                self.state = 303
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 302
                    self.randomize()


                self.state = 306
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 305
                    self.title()


                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 308
                    self.question_type()


                self.state = 312
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 311
                    self.points()


                pass

            elif la_ == 22:
                self.enterOuterAlt(localctx, 22)
                self.state = 315
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 314
                    self.randomize()


                self.state = 318
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 317
                    self.title()


                self.state = 321
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 320
                    self.points()


                self.state = 324
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 323
                    self.question_type()


                pass

            elif la_ == 23:
                self.enterOuterAlt(localctx, 23)
                self.state = 327
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 326
                    self.randomize()


                self.state = 330
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 329
                    self.points()


                self.state = 333
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 332
                    self.question_type()


                self.state = 336
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 335
                    self.title()


                pass

            elif la_ == 24:
                self.enterOuterAlt(localctx, 24)
                self.state = 339
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 338
                    self.randomize()


                self.state = 342
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 341
                    self.points()


                self.state = 345
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 344
                    self.title()


                self.state = 348
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 347
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
        self.enterRule(localctx, 8, self.RULE_question_type)
        try:
            self.state = 360
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuestionParser.TYPE_MC]:
                localctx = QuestionParser.TypeMcContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.match(QuestionParser.TYPE_MC)
                pass
            elif token in [QuestionParser.TYPE_TF]:
                localctx = QuestionParser.TypeTfContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.match(QuestionParser.TYPE_TF)
                pass
            elif token in [QuestionParser.TYPE_MS]:
                localctx = QuestionParser.TypeMsContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 354
                self.match(QuestionParser.TYPE_MS)
                pass
            elif token in [QuestionParser.TYPE_MT]:
                localctx = QuestionParser.TypeMtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 355
                self.match(QuestionParser.TYPE_MT)
                pass
            elif token in [QuestionParser.TYPE_ORD]:
                localctx = QuestionParser.TypeOrdContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 356
                self.match(QuestionParser.TYPE_ORD)
                pass
            elif token in [QuestionParser.TYPE_FIB]:
                localctx = QuestionParser.TypeFibContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 357
                self.match(QuestionParser.TYPE_FIB)
                pass
            elif token in [QuestionParser.TYPE_WR]:
                localctx = QuestionParser.TypeWrContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 358
                self.match(QuestionParser.TYPE_WR)
                pass
            elif token in [QuestionParser.TYPE_OTHER]:
                localctx = QuestionParser.TypeOtherContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 359
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
        self.enterRule(localctx, 10, self.RULE_title)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
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
        self.enterRule(localctx, 12, self.RULE_points)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
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
        self.enterRule(localctx, 14, self.RULE_randomize)
        try:
            self.state = 368
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuestionParser.RANDOMIZE_TRUE]:
                localctx = QuestionParser.RandomTrueContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.match(QuestionParser.RANDOMIZE_TRUE)
                pass
            elif token in [QuestionParser.RANDOMIZE_FALSE]:
                localctx = QuestionParser.RandomFalseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 367
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
        self.enterRule(localctx, 16, self.RULE_question_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.question_prefix()
            self.state = 372 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 371
                self.content()
                self.state = 374 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.MEDIA) | (1 << QuestionParser.HYPERLINK) | (1 << QuestionParser.ALL_CHARACTER) | (1 << QuestionParser.ESCAPED_OPEN_BRACKET))) != 0)):
                    break

            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.FEEDBACK_MARKER:
                self.state = 376
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
        self.enterRule(localctx, 18, self.RULE_question_prefix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
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
        self.enterRule(localctx, 20, self.RULE_content)
        self._la = 0 # Token type
        try:
            self.state = 395
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuestionParser.MEDIA]:
                localctx = QuestionParser.MediaContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.match(QuestionParser.MEDIA)
                pass
            elif token in [QuestionParser.HYPERLINK]:
                localctx = QuestionParser.HyperlinkContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 382
                self.match(QuestionParser.HYPERLINK)
                pass
            elif token in [QuestionParser.ESCAPED_OPEN_BRACKET]:
                localctx = QuestionParser.FibAnswerContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 383
                self.match(QuestionParser.ESCAPED_OPEN_BRACKET)
                self.state = 385 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 384
                    self.match(QuestionParser.ALL_CHARACTER)
                    self.state = 387 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==QuestionParser.ALL_CHARACTER):
                        break

                self.state = 389
                self.match(QuestionParser.ESCAPED_CLOSE_BRACKET)
                pass
            elif token in [QuestionParser.ALL_CHARACTER]:
                localctx = QuestionParser.ContentCharactersContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 391 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 390
                        self.match(QuestionParser.ALL_CHARACTER)

                    else:
                        raise NoViableAltException(self)
                    self.state = 393 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,105,self._ctx)

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
            self.state = 397
            self.match(QuestionParser.FEEDBACK_MARKER)
            self.state = 399 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 398
                self.content()
                self.state = 401 
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
        self.enterRule(localctx, 24, self.RULE_answer_list)
        self._la = 0 # Token type
        try:
            self.state = 416
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,111,self._ctx)
            if la_ == 1:
                localctx = QuestionParser.ListNoAnswerContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 403
                self.match(QuestionParser.START_ANSWER)
                self.state = 405 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 404
                    self.list_item()
                    self.state = 407 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==QuestionParser.LIST_PREFIX):
                        break

                pass

            elif la_ == 2:
                localctx = QuestionParser.ListWithAnswerContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 409
                self.match(QuestionParser.START_ANSWER)
                self.state = 412 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 412
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [QuestionParser.RIGHT_ANSWER]:
                        self.state = 410
                        self.list_answer_item()
                        pass
                    elif token in [QuestionParser.LIST_PREFIX]:
                        self.state = 411
                        self.list_item()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 414 
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
            self.state = 418
            self.list_prefix()
            self.state = 420 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 419
                self.content()
                self.state = 422 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.MEDIA) | (1 << QuestionParser.HYPERLINK) | (1 << QuestionParser.ALL_CHARACTER) | (1 << QuestionParser.ESCAPED_OPEN_BRACKET))) != 0)):
                    break

            self.state = 425
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.FEEDBACK_MARKER:
                self.state = 424
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
            self.state = 427
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
            self.state = 429
            self.answer_prefix()
            self.state = 431 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 430
                self.content()
                self.state = 433 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.MEDIA) | (1 << QuestionParser.HYPERLINK) | (1 << QuestionParser.ALL_CHARACTER) | (1 << QuestionParser.ESCAPED_OPEN_BRACKET))) != 0)):
                    break

            self.state = 436
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.FEEDBACK_MARKER:
                self.state = 435
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
            self.state = 438
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
        self.enterRule(localctx, 34, self.RULE_end_answers)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.match(QuestionParser.END_ANSWERS)
            self.state = 442 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 441
                self.end_answers_item()
                self.state = 444 
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
        self.enterRule(localctx, 36, self.RULE_end_answers_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.question_prefix()
            self.state = 448 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 447
                self.content()
                self.state = 450 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.MEDIA) | (1 << QuestionParser.HYPERLINK) | (1 << QuestionParser.ALL_CHARACTER) | (1 << QuestionParser.ESCAPED_OPEN_BRACKET))) != 0)):
                    break

            self.state = 453
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.FEEDBACK_MARKER:
                self.state = 452
                self.feedback()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





