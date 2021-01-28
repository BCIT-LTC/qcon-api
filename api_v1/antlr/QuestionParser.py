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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\34")
        buf.write("\u01f0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\5\2,\n\2\3\2\7\2/\n\2\f\2\16")
        buf.write("\2\62\13\2\3\2\5\2\65\n\2\3\2\3\2\3\3\3\3\6\3;\n\3\r\3")
        buf.write("\16\3<\3\4\5\4@\n\4\3\4\3\4\3\4\3\4\3\4\5\4G\n\4\3\4\3")
        buf.write("\4\3\4\5\4L\n\4\3\5\3\5\3\6\3\6\5\6R\n\6\3\6\5\6U\n\6")
        buf.write("\3\6\5\6X\n\6\3\6\5\6[\n\6\3\6\3\6\5\6_\n\6\3\6\5\6b\n")
        buf.write("\6\3\6\5\6e\n\6\3\6\5\6h\n\6\3\6\3\6\5\6l\n\6\3\6\5\6")
        buf.write("o\n\6\3\6\5\6r\n\6\3\6\5\6u\n\6\3\6\3\6\5\6y\n\6\3\6\5")
        buf.write("\6|\n\6\3\6\5\6\177\n\6\3\6\5\6\u0082\n\6\3\6\3\6\5\6")
        buf.write("\u0086\n\6\3\6\5\6\u0089\n\6\3\6\5\6\u008c\n\6\3\6\5\6")
        buf.write("\u008f\n\6\3\6\3\6\5\6\u0093\n\6\3\6\5\6\u0096\n\6\3\6")
        buf.write("\5\6\u0099\n\6\3\6\5\6\u009c\n\6\3\6\3\6\5\6\u00a0\n\6")
        buf.write("\3\6\5\6\u00a3\n\6\3\6\5\6\u00a6\n\6\3\6\5\6\u00a9\n\6")
        buf.write("\3\6\3\6\5\6\u00ad\n\6\3\6\5\6\u00b0\n\6\3\6\5\6\u00b3")
        buf.write("\n\6\3\6\5\6\u00b6\n\6\3\6\3\6\5\6\u00ba\n\6\3\6\5\6\u00bd")
        buf.write("\n\6\3\6\5\6\u00c0\n\6\3\6\5\6\u00c3\n\6\3\6\3\6\5\6\u00c7")
        buf.write("\n\6\3\6\5\6\u00ca\n\6\3\6\5\6\u00cd\n\6\3\6\5\6\u00d0")
        buf.write("\n\6\3\6\3\6\5\6\u00d4\n\6\3\6\5\6\u00d7\n\6\3\6\5\6\u00da")
        buf.write("\n\6\3\6\5\6\u00dd\n\6\3\6\3\6\5\6\u00e1\n\6\3\6\5\6\u00e4")
        buf.write("\n\6\3\6\5\6\u00e7\n\6\3\6\5\6\u00ea\n\6\3\6\3\6\5\6\u00ee")
        buf.write("\n\6\3\6\5\6\u00f1\n\6\3\6\5\6\u00f4\n\6\3\6\5\6\u00f7")
        buf.write("\n\6\3\6\3\6\5\6\u00fb\n\6\3\6\5\6\u00fe\n\6\3\6\5\6\u0101")
        buf.write("\n\6\3\6\5\6\u0104\n\6\3\6\3\6\5\6\u0108\n\6\3\6\5\6\u010b")
        buf.write("\n\6\3\6\5\6\u010e\n\6\3\6\5\6\u0111\n\6\3\6\3\6\5\6\u0115")
        buf.write("\n\6\3\6\5\6\u0118\n\6\3\6\5\6\u011b\n\6\3\6\5\6\u011e")
        buf.write("\n\6\3\6\3\6\5\6\u0122\n\6\3\6\5\6\u0125\n\6\3\6\5\6\u0128")
        buf.write("\n\6\3\6\5\6\u012b\n\6\3\6\3\6\5\6\u012f\n\6\3\6\5\6\u0132")
        buf.write("\n\6\3\6\5\6\u0135\n\6\3\6\5\6\u0138\n\6\3\6\3\6\5\6\u013c")
        buf.write("\n\6\3\6\5\6\u013f\n\6\3\6\5\6\u0142\n\6\3\6\5\6\u0145")
        buf.write("\n\6\3\6\3\6\5\6\u0149\n\6\3\6\5\6\u014c\n\6\3\6\5\6\u014f")
        buf.write("\n\6\3\6\5\6\u0152\n\6\3\6\3\6\5\6\u0156\n\6\3\6\5\6\u0159")
        buf.write("\n\6\3\6\5\6\u015c\n\6\3\6\5\6\u015f\n\6\3\6\3\6\5\6\u0163")
        buf.write("\n\6\3\6\5\6\u0166\n\6\3\6\5\6\u0169\n\6\3\6\5\6\u016c")
        buf.write("\n\6\3\6\3\6\5\6\u0170\n\6\3\6\5\6\u0173\n\6\3\6\5\6\u0176")
        buf.write("\n\6\3\6\5\6\u0179\n\6\3\6\3\6\5\6\u017d\n\6\3\6\5\6\u0180")
        buf.write("\n\6\3\6\5\6\u0183\n\6\3\6\5\6\u0186\n\6\5\6\u0188\n\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u0192\n\7\3\b\3\b")
        buf.write("\3\t\3\t\3\n\3\n\5\n\u019a\n\n\3\13\6\13\u019d\n\13\r")
        buf.write("\13\16\13\u019e\3\13\5\13\u01a2\n\13\3\f\3\f\3\f\3\f\6")
        buf.write("\f\u01a8\n\f\r\f\16\f\u01a9\3\f\3\f\6\f\u01ae\n\f\r\f")
        buf.write("\16\f\u01af\5\f\u01b2\n\f\3\r\3\r\6\r\u01b6\n\r\r\r\16")
        buf.write("\r\u01b7\3\16\3\16\6\16\u01bc\n\16\r\16\16\16\u01bd\3")
        buf.write("\16\3\16\3\16\6\16\u01c3\n\16\r\16\16\16\u01c4\5\16\u01c7")
        buf.write("\n\16\3\17\3\17\6\17\u01cb\n\17\r\17\16\17\u01cc\3\17")
        buf.write("\5\17\u01d0\n\17\3\20\3\20\3\21\3\21\6\21\u01d6\n\21\r")
        buf.write("\21\16\21\u01d7\3\21\5\21\u01db\n\21\3\22\3\22\3\23\3")
        buf.write("\23\6\23\u01e1\n\23\r\23\16\23\u01e2\3\24\3\24\6\24\u01e7")
        buf.write("\n\24\r\24\16\24\u01e8\3\24\5\24\u01ec\n\24\3\25\3\25")
        buf.write("\3\25\2\2\26\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(\2\2\2\u0274\2+\3\2\2\2\48\3\2\2\2\6K\3\2\2\2\bM\3")
        buf.write("\2\2\2\n\u0187\3\2\2\2\f\u0191\3\2\2\2\16\u0193\3\2\2")
        buf.write("\2\20\u0195\3\2\2\2\22\u0199\3\2\2\2\24\u019c\3\2\2\2")
        buf.write("\26\u01b1\3\2\2\2\30\u01b3\3\2\2\2\32\u01c6\3\2\2\2\34")
        buf.write("\u01c8\3\2\2\2\36\u01d1\3\2\2\2 \u01d3\3\2\2\2\"\u01dc")
        buf.write("\3\2\2\2$\u01de\3\2\2\2&\u01e4\3\2\2\2(\u01ed\3\2\2\2")
        buf.write("*,\5\4\3\2+*\3\2\2\2+,\3\2\2\2,\60\3\2\2\2-/\5\6\4\2.")
        buf.write("-\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61\64")
        buf.write("\3\2\2\2\62\60\3\2\2\2\63\65\5$\23\2\64\63\3\2\2\2\64")
        buf.write("\65\3\2\2\2\65\66\3\2\2\2\66\67\7\2\2\3\67\3\3\2\2\28")
        buf.write(":\7\f\2\29;\7\t\2\2:9\3\2\2\2;<\3\2\2\2<:\3\2\2\2<=\3")
        buf.write("\2\2\2=\5\3\2\2\2>@\5\n\6\2?>\3\2\2\2?@\3\2\2\2@A\3\2")
        buf.write("\2\2AB\5\b\5\2BC\5\24\13\2CD\5\32\16\2DL\3\2\2\2EG\5\n")
        buf.write("\6\2FE\3\2\2\2FG\3\2\2\2GH\3\2\2\2HI\5\b\5\2IJ\5\24\13")
        buf.write("\2JL\3\2\2\2K?\3\2\2\2KF\3\2\2\2L\7\3\2\2\2MN\7\4\2\2")
        buf.write("N\t\3\2\2\2OQ\7\3\2\2PR\5\f\7\2QP\3\2\2\2QR\3\2\2\2RT")
        buf.write("\3\2\2\2SU\5\16\b\2TS\3\2\2\2TU\3\2\2\2UW\3\2\2\2VX\5")
        buf.write("\20\t\2WV\3\2\2\2WX\3\2\2\2XZ\3\2\2\2Y[\5\22\n\2ZY\3\2")
        buf.write("\2\2Z[\3\2\2\2[\u0188\3\2\2\2\\^\7\3\2\2]_\5\f\7\2^]\3")
        buf.write("\2\2\2^_\3\2\2\2_a\3\2\2\2`b\5\16\b\2a`\3\2\2\2ab\3\2")
        buf.write("\2\2bd\3\2\2\2ce\5\22\n\2dc\3\2\2\2de\3\2\2\2eg\3\2\2")
        buf.write("\2fh\5\20\t\2gf\3\2\2\2gh\3\2\2\2h\u0188\3\2\2\2ik\7\3")
        buf.write("\2\2jl\5\f\7\2kj\3\2\2\2kl\3\2\2\2ln\3\2\2\2mo\5\20\t")
        buf.write("\2nm\3\2\2\2no\3\2\2\2oq\3\2\2\2pr\5\16\b\2qp\3\2\2\2")
        buf.write("qr\3\2\2\2rt\3\2\2\2su\5\22\n\2ts\3\2\2\2tu\3\2\2\2u\u0188")
        buf.write("\3\2\2\2vx\7\3\2\2wy\5\f\7\2xw\3\2\2\2xy\3\2\2\2y{\3\2")
        buf.write("\2\2z|\5\20\t\2{z\3\2\2\2{|\3\2\2\2|~\3\2\2\2}\177\5\22")
        buf.write("\n\2~}\3\2\2\2~\177\3\2\2\2\177\u0081\3\2\2\2\u0080\u0082")
        buf.write("\5\16\b\2\u0081\u0080\3\2\2\2\u0081\u0082\3\2\2\2\u0082")
        buf.write("\u0188\3\2\2\2\u0083\u0085\7\3\2\2\u0084\u0086\5\f\7\2")
        buf.write("\u0085\u0084\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0088\3")
        buf.write("\2\2\2\u0087\u0089\5\22\n\2\u0088\u0087\3\2\2\2\u0088")
        buf.write("\u0089\3\2\2\2\u0089\u008b\3\2\2\2\u008a\u008c\5\16\b")
        buf.write("\2\u008b\u008a\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008e")
        buf.write("\3\2\2\2\u008d\u008f\5\20\t\2\u008e\u008d\3\2\2\2\u008e")
        buf.write("\u008f\3\2\2\2\u008f\u0188\3\2\2\2\u0090\u0092\7\3\2\2")
        buf.write("\u0091\u0093\5\f\7\2\u0092\u0091\3\2\2\2\u0092\u0093\3")
        buf.write("\2\2\2\u0093\u0095\3\2\2\2\u0094\u0096\5\22\n\2\u0095")
        buf.write("\u0094\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0098\3\2\2\2")
        buf.write("\u0097\u0099\5\20\t\2\u0098\u0097\3\2\2\2\u0098\u0099")
        buf.write("\3\2\2\2\u0099\u009b\3\2\2\2\u009a\u009c\5\16\b\2\u009b")
        buf.write("\u009a\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u0188\3\2\2\2")
        buf.write("\u009d\u009f\7\3\2\2\u009e\u00a0\5\16\b\2\u009f\u009e")
        buf.write("\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a2\3\2\2\2\u00a1")
        buf.write("\u00a3\5\f\7\2\u00a2\u00a1\3\2\2\2\u00a2\u00a3\3\2\2\2")
        buf.write("\u00a3\u00a5\3\2\2\2\u00a4\u00a6\5\20\t\2\u00a5\u00a4")
        buf.write("\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a8\3\2\2\2\u00a7")
        buf.write("\u00a9\5\22\n\2\u00a8\u00a7\3\2\2\2\u00a8\u00a9\3\2\2")
        buf.write("\2\u00a9\u0188\3\2\2\2\u00aa\u00ac\7\3\2\2\u00ab\u00ad")
        buf.write("\5\16\b\2\u00ac\u00ab\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad")
        buf.write("\u00af\3\2\2\2\u00ae\u00b0\5\f\7\2\u00af\u00ae\3\2\2\2")
        buf.write("\u00af\u00b0\3\2\2\2\u00b0\u00b2\3\2\2\2\u00b1\u00b3\5")
        buf.write("\22\n\2\u00b2\u00b1\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3")
        buf.write("\u00b5\3\2\2\2\u00b4\u00b6\5\20\t\2\u00b5\u00b4\3\2\2")
        buf.write("\2\u00b5\u00b6\3\2\2\2\u00b6\u0188\3\2\2\2\u00b7\u00b9")
        buf.write("\7\3\2\2\u00b8\u00ba\5\16\b\2\u00b9\u00b8\3\2\2\2\u00b9")
        buf.write("\u00ba\3\2\2\2\u00ba\u00bc\3\2\2\2\u00bb\u00bd\5\20\t")
        buf.write("\2\u00bc\u00bb\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00bf")
        buf.write("\3\2\2\2\u00be\u00c0\5\f\7\2\u00bf\u00be\3\2\2\2\u00bf")
        buf.write("\u00c0\3\2\2\2\u00c0\u00c2\3\2\2\2\u00c1\u00c3\5\22\n")
        buf.write("\2\u00c2\u00c1\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u0188")
        buf.write("\3\2\2\2\u00c4\u00c6\7\3\2\2\u00c5\u00c7\5\16\b\2\u00c6")
        buf.write("\u00c5\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c9\3\2\2\2")
        buf.write("\u00c8\u00ca\5\20\t\2\u00c9\u00c8\3\2\2\2\u00c9\u00ca")
        buf.write("\3\2\2\2\u00ca\u00cc\3\2\2\2\u00cb\u00cd\5\22\n\2\u00cc")
        buf.write("\u00cb\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00cf\3\2\2\2")
        buf.write("\u00ce\u00d0\5\f\7\2\u00cf\u00ce\3\2\2\2\u00cf\u00d0\3")
        buf.write("\2\2\2\u00d0\u0188\3\2\2\2\u00d1\u00d3\7\3\2\2\u00d2\u00d4")
        buf.write("\5\16\b\2\u00d3\u00d2\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4")
        buf.write("\u00d6\3\2\2\2\u00d5\u00d7\5\22\n\2\u00d6\u00d5\3\2\2")
        buf.write("\2\u00d6\u00d7\3\2\2\2\u00d7\u00d9\3\2\2\2\u00d8\u00da")
        buf.write("\5\f\7\2\u00d9\u00d8\3\2\2\2\u00d9\u00da\3\2\2\2\u00da")
        buf.write("\u00dc\3\2\2\2\u00db\u00dd\5\20\t\2\u00dc\u00db\3\2\2")
        buf.write("\2\u00dc\u00dd\3\2\2\2\u00dd\u0188\3\2\2\2\u00de\u00e0")
        buf.write("\7\3\2\2\u00df\u00e1\5\16\b\2\u00e0\u00df\3\2\2\2\u00e0")
        buf.write("\u00e1\3\2\2\2\u00e1\u00e3\3\2\2\2\u00e2\u00e4\5\22\n")
        buf.write("\2\u00e3\u00e2\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e6")
        buf.write("\3\2\2\2\u00e5\u00e7\5\20\t\2\u00e6\u00e5\3\2\2\2\u00e6")
        buf.write("\u00e7\3\2\2\2\u00e7\u00e9\3\2\2\2\u00e8\u00ea\5\f\7\2")
        buf.write("\u00e9\u00e8\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u0188\3")
        buf.write("\2\2\2\u00eb\u00ed\7\3\2\2\u00ec\u00ee\5\20\t\2\u00ed")
        buf.write("\u00ec\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00f0\3\2\2\2")
        buf.write("\u00ef\u00f1\5\f\7\2\u00f0\u00ef\3\2\2\2\u00f0\u00f1\3")
        buf.write("\2\2\2\u00f1\u00f3\3\2\2\2\u00f2\u00f4\5\16\b\2\u00f3")
        buf.write("\u00f2\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f6\3\2\2\2")
        buf.write("\u00f5\u00f7\5\22\n\2\u00f6\u00f5\3\2\2\2\u00f6\u00f7")
        buf.write("\3\2\2\2\u00f7\u0188\3\2\2\2\u00f8\u00fa\7\3\2\2\u00f9")
        buf.write("\u00fb\5\20\t\2\u00fa\u00f9\3\2\2\2\u00fa\u00fb\3\2\2")
        buf.write("\2\u00fb\u00fd\3\2\2\2\u00fc\u00fe\5\f\7\2\u00fd\u00fc")
        buf.write("\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u0100\3\2\2\2\u00ff")
        buf.write("\u0101\5\22\n\2\u0100\u00ff\3\2\2\2\u0100\u0101\3\2\2")
        buf.write("\2\u0101\u0103\3\2\2\2\u0102\u0104\5\16\b\2\u0103\u0102")
        buf.write("\3\2\2\2\u0103\u0104\3\2\2\2\u0104\u0188\3\2\2\2\u0105")
        buf.write("\u0107\7\3\2\2\u0106\u0108\5\20\t\2\u0107\u0106\3\2\2")
        buf.write("\2\u0107\u0108\3\2\2\2\u0108\u010a\3\2\2\2\u0109\u010b")
        buf.write("\5\16\b\2\u010a\u0109\3\2\2\2\u010a\u010b\3\2\2\2\u010b")
        buf.write("\u010d\3\2\2\2\u010c\u010e\5\f\7\2\u010d\u010c\3\2\2\2")
        buf.write("\u010d\u010e\3\2\2\2\u010e\u0110\3\2\2\2\u010f\u0111\5")
        buf.write("\22\n\2\u0110\u010f\3\2\2\2\u0110\u0111\3\2\2\2\u0111")
        buf.write("\u0188\3\2\2\2\u0112\u0114\7\3\2\2\u0113\u0115\5\20\t")
        buf.write("\2\u0114\u0113\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0117")
        buf.write("\3\2\2\2\u0116\u0118\5\16\b\2\u0117\u0116\3\2\2\2\u0117")
        buf.write("\u0118\3\2\2\2\u0118\u011a\3\2\2\2\u0119\u011b\5\22\n")
        buf.write("\2\u011a\u0119\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011d")
        buf.write("\3\2\2\2\u011c\u011e\5\f\7\2\u011d\u011c\3\2\2\2\u011d")
        buf.write("\u011e\3\2\2\2\u011e\u0188\3\2\2\2\u011f\u0121\7\3\2\2")
        buf.write("\u0120\u0122\5\20\t\2\u0121\u0120\3\2\2\2\u0121\u0122")
        buf.write("\3\2\2\2\u0122\u0124\3\2\2\2\u0123\u0125\5\22\n\2\u0124")
        buf.write("\u0123\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0127\3\2\2\2")
        buf.write("\u0126\u0128\5\f\7\2\u0127\u0126\3\2\2\2\u0127\u0128\3")
        buf.write("\2\2\2\u0128\u012a\3\2\2\2\u0129\u012b\5\16\b\2\u012a")
        buf.write("\u0129\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u0188\3\2\2\2")
        buf.write("\u012c\u012e\7\3\2\2\u012d\u012f\5\20\t\2\u012e\u012d")
        buf.write("\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0131\3\2\2\2\u0130")
        buf.write("\u0132\5\22\n\2\u0131\u0130\3\2\2\2\u0131\u0132\3\2\2")
        buf.write("\2\u0132\u0134\3\2\2\2\u0133\u0135\5\16\b\2\u0134\u0133")
        buf.write("\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0137\3\2\2\2\u0136")
        buf.write("\u0138\5\f\7\2\u0137\u0136\3\2\2\2\u0137\u0138\3\2\2\2")
        buf.write("\u0138\u0188\3\2\2\2\u0139\u013b\7\3\2\2\u013a\u013c\5")
        buf.write("\22\n\2\u013b\u013a\3\2\2\2\u013b\u013c\3\2\2\2\u013c")
        buf.write("\u013e\3\2\2\2\u013d\u013f\5\f\7\2\u013e\u013d\3\2\2\2")
        buf.write("\u013e\u013f\3\2\2\2\u013f\u0141\3\2\2\2\u0140\u0142\5")
        buf.write("\16\b\2\u0141\u0140\3\2\2\2\u0141\u0142\3\2\2\2\u0142")
        buf.write("\u0144\3\2\2\2\u0143\u0145\5\20\t\2\u0144\u0143\3\2\2")
        buf.write("\2\u0144\u0145\3\2\2\2\u0145\u0188\3\2\2\2\u0146\u0148")
        buf.write("\7\3\2\2\u0147\u0149\5\22\n\2\u0148\u0147\3\2\2\2\u0148")
        buf.write("\u0149\3\2\2\2\u0149\u014b\3\2\2\2\u014a\u014c\5\f\7\2")
        buf.write("\u014b\u014a\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014e\3")
        buf.write("\2\2\2\u014d\u014f\5\20\t\2\u014e\u014d\3\2\2\2\u014e")
        buf.write("\u014f\3\2\2\2\u014f\u0151\3\2\2\2\u0150\u0152\5\16\b")
        buf.write("\2\u0151\u0150\3\2\2\2\u0151\u0152\3\2\2\2\u0152\u0188")
        buf.write("\3\2\2\2\u0153\u0155\7\3\2\2\u0154\u0156\5\22\n\2\u0155")
        buf.write("\u0154\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u0158\3\2\2\2")
        buf.write("\u0157\u0159\5\16\b\2\u0158\u0157\3\2\2\2\u0158\u0159")
        buf.write("\3\2\2\2\u0159\u015b\3\2\2\2\u015a\u015c\5\f\7\2\u015b")
        buf.write("\u015a\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015e\3\2\2\2")
        buf.write("\u015d\u015f\5\20\t\2\u015e\u015d\3\2\2\2\u015e\u015f")
        buf.write("\3\2\2\2\u015f\u0188\3\2\2\2\u0160\u0162\7\3\2\2\u0161")
        buf.write("\u0163\5\22\n\2\u0162\u0161\3\2\2\2\u0162\u0163\3\2\2")
        buf.write("\2\u0163\u0165\3\2\2\2\u0164\u0166\5\16\b\2\u0165\u0164")
        buf.write("\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0168\3\2\2\2\u0167")
        buf.write("\u0169\5\20\t\2\u0168\u0167\3\2\2\2\u0168\u0169\3\2\2")
        buf.write("\2\u0169\u016b\3\2\2\2\u016a\u016c\5\f\7\2\u016b\u016a")
        buf.write("\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u0188\3\2\2\2\u016d")
        buf.write("\u016f\7\3\2\2\u016e\u0170\5\22\n\2\u016f\u016e\3\2\2")
        buf.write("\2\u016f\u0170\3\2\2\2\u0170\u0172\3\2\2\2\u0171\u0173")
        buf.write("\5\20\t\2\u0172\u0171\3\2\2\2\u0172\u0173\3\2\2\2\u0173")
        buf.write("\u0175\3\2\2\2\u0174\u0176\5\f\7\2\u0175\u0174\3\2\2\2")
        buf.write("\u0175\u0176\3\2\2\2\u0176\u0178\3\2\2\2\u0177\u0179\5")
        buf.write("\16\b\2\u0178\u0177\3\2\2\2\u0178\u0179\3\2\2\2\u0179")
        buf.write("\u0188\3\2\2\2\u017a\u017c\7\3\2\2\u017b\u017d\5\22\n")
        buf.write("\2\u017c\u017b\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u017f")
        buf.write("\3\2\2\2\u017e\u0180\5\20\t\2\u017f\u017e\3\2\2\2\u017f")
        buf.write("\u0180\3\2\2\2\u0180\u0182\3\2\2\2\u0181\u0183\5\16\b")
        buf.write("\2\u0182\u0181\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0185")
        buf.write("\3\2\2\2\u0184\u0186\5\f\7\2\u0185\u0184\3\2\2\2\u0185")
        buf.write("\u0186\3\2\2\2\u0186\u0188\3\2\2\2\u0187O\3\2\2\2\u0187")
        buf.write("\\\3\2\2\2\u0187i\3\2\2\2\u0187v\3\2\2\2\u0187\u0083\3")
        buf.write("\2\2\2\u0187\u0090\3\2\2\2\u0187\u009d\3\2\2\2\u0187\u00aa")
        buf.write("\3\2\2\2\u0187\u00b7\3\2\2\2\u0187\u00c4\3\2\2\2\u0187")
        buf.write("\u00d1\3\2\2\2\u0187\u00de\3\2\2\2\u0187\u00eb\3\2\2\2")
        buf.write("\u0187\u00f8\3\2\2\2\u0187\u0105\3\2\2\2\u0187\u0112\3")
        buf.write("\2\2\2\u0187\u011f\3\2\2\2\u0187\u012c\3\2\2\2\u0187\u0139")
        buf.write("\3\2\2\2\u0187\u0146\3\2\2\2\u0187\u0153\3\2\2\2\u0187")
        buf.write("\u0160\3\2\2\2\u0187\u016d\3\2\2\2\u0187\u017a\3\2\2\2")
        buf.write("\u0188\13\3\2\2\2\u0189\u0192\7\21\2\2\u018a\u0192\7\22")
        buf.write("\2\2\u018b\u0192\7\23\2\2\u018c\u0192\7\24\2\2\u018d\u0192")
        buf.write("\7\25\2\2\u018e\u0192\7\26\2\2\u018f\u0192\7\27\2\2\u0190")
        buf.write("\u0192\7\30\2\2\u0191\u0189\3\2\2\2\u0191\u018a\3\2\2")
        buf.write("\2\u0191\u018b\3\2\2\2\u0191\u018c\3\2\2\2\u0191\u018d")
        buf.write("\3\2\2\2\u0191\u018e\3\2\2\2\u0191\u018f\3\2\2\2\u0191")
        buf.write("\u0190\3\2\2\2\u0192\r\3\2\2\2\u0193\u0194\7\r\2\2\u0194")
        buf.write("\17\3\2\2\2\u0195\u0196\7\16\2\2\u0196\21\3\2\2\2\u0197")
        buf.write("\u019a\7\17\2\2\u0198\u019a\7\20\2\2\u0199\u0197\3\2\2")
        buf.write("\2\u0199\u0198\3\2\2\2\u019a\23\3\2\2\2\u019b\u019d\5")
        buf.write("\26\f\2\u019c\u019b\3\2\2\2\u019d\u019e\3\2\2\2\u019e")
        buf.write("\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a1\3\2\2\2")
        buf.write("\u01a0\u01a2\5\30\r\2\u01a1\u01a0\3\2\2\2\u01a1\u01a2")
        buf.write("\3\2\2\2\u01a2\25\3\2\2\2\u01a3\u01b2\7\7\2\2\u01a4\u01b2")
        buf.write("\7\b\2\2\u01a5\u01a7\7\n\2\2\u01a6\u01a8\7\t\2\2\u01a7")
        buf.write("\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01a7\3\2\2\2")
        buf.write("\u01a9\u01aa\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01b2\7")
        buf.write("\13\2\2\u01ac\u01ae\7\t\2\2\u01ad\u01ac\3\2\2\2\u01ae")
        buf.write("\u01af\3\2\2\2\u01af\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2")
        buf.write("\u01b0\u01b2\3\2\2\2\u01b1\u01a3\3\2\2\2\u01b1\u01a4\3")
        buf.write("\2\2\2\u01b1\u01a5\3\2\2\2\u01b1\u01ad\3\2\2\2\u01b2\27")
        buf.write("\3\2\2\2\u01b3\u01b5\7\6\2\2\u01b4\u01b6\5\26\f\2\u01b5")
        buf.write("\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b5\3\2\2\2")
        buf.write("\u01b7\u01b8\3\2\2\2\u01b8\31\3\2\2\2\u01b9\u01bb\7\31")
        buf.write("\2\2\u01ba\u01bc\5\34\17\2\u01bb\u01ba\3\2\2\2\u01bc\u01bd")
        buf.write("\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2\u01be")
        buf.write("\u01c7\3\2\2\2\u01bf\u01c2\7\31\2\2\u01c0\u01c3\5 \21")
        buf.write("\2\u01c1\u01c3\5\34\17\2\u01c2\u01c0\3\2\2\2\u01c2\u01c1")
        buf.write("\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4")
        buf.write("\u01c5\3\2\2\2\u01c5\u01c7\3\2\2\2\u01c6\u01b9\3\2\2\2")
        buf.write("\u01c6\u01bf\3\2\2\2\u01c7\33\3\2\2\2\u01c8\u01ca\5\36")
        buf.write("\20\2\u01c9\u01cb\5\26\f\2\u01ca\u01c9\3\2\2\2\u01cb\u01cc")
        buf.write("\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd")
        buf.write("\u01cf\3\2\2\2\u01ce\u01d0\5\30\r\2\u01cf\u01ce\3\2\2")
        buf.write("\2\u01cf\u01d0\3\2\2\2\u01d0\35\3\2\2\2\u01d1\u01d2\7")
        buf.write("\33\2\2\u01d2\37\3\2\2\2\u01d3\u01d5\5\"\22\2\u01d4\u01d6")
        buf.write("\5\26\f\2\u01d5\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7")
        buf.write("\u01d5\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01da\3\2\2\2")
        buf.write("\u01d9\u01db\5\30\r\2\u01da\u01d9\3\2\2\2\u01da\u01db")
        buf.write("\3\2\2\2\u01db!\3\2\2\2\u01dc\u01dd\7\32\2\2\u01dd#\3")
        buf.write("\2\2\2\u01de\u01e0\7\5\2\2\u01df\u01e1\5&\24\2\u01e0\u01df")
        buf.write("\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2")
        buf.write("\u01e3\3\2\2\2\u01e3%\3\2\2\2\u01e4\u01e6\5(\25\2\u01e5")
        buf.write("\u01e7\5\26\f\2\u01e6\u01e5\3\2\2\2\u01e7\u01e8\3\2\2")
        buf.write("\2\u01e8\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01eb")
        buf.write("\3\2\2\2\u01ea\u01ec\5\30\r\2\u01eb\u01ea\3\2\2\2\u01eb")
        buf.write("\u01ec\3\2\2\2\u01ec\'\3\2\2\2\u01ed\u01ee\7\34\2\2\u01ee")
        buf.write(")\3\2\2\2}+\60\64<?FKQTWZ^adgknqtx{~\u0081\u0085\u0088")
        buf.write("\u008b\u008e\u0092\u0095\u0098\u009b\u009f\u00a2\u00a5")
        buf.write("\u00a8\u00ac\u00af\u00b2\u00b5\u00b9\u00bc\u00bf\u00c2")
        buf.write("\u00c6\u00c9\u00cc\u00cf\u00d3\u00d6\u00d9\u00dc\u00e0")
        buf.write("\u00e3\u00e6\u00e9\u00ed\u00f0\u00f3\u00f6\u00fa\u00fd")
        buf.write("\u0100\u0103\u0107\u010a\u010d\u0110\u0114\u0117\u011a")
        buf.write("\u011d\u0121\u0124\u0127\u012a\u012e\u0131\u0134\u0137")
        buf.write("\u013b\u013e\u0141\u0144\u0148\u014b\u014e\u0151\u0155")
        buf.write("\u0158\u015b\u015e\u0162\u0165\u0168\u016b\u016f\u0172")
        buf.write("\u0175\u0178\u017c\u017f\u0182\u0185\u0187\u0191\u0199")
        buf.write("\u019e\u01a1\u01a9\u01af\u01b1\u01b7\u01bd\u01c2\u01c4")
        buf.write("\u01c6\u01cc\u01cf\u01d7\u01da\u01e2\u01e8\u01eb")
        return buf.getvalue()


class QuestionParser ( Parser ):

    grammarFileName = "QuestionParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "START_QUESTION_HEADER", "START_QUESTION", 
                      "END_ANSWERS", "FEEDBACK_MARKER", "MEDIA", "HYPERLINK", 
                      "ALL_CHARACTER", "ESCAPED_OPEN_BRACKET", "ESCAPED_CLOSE_BRACKET", 
                      "SECTION_TITLE", "TITLE", "POINTS", "RANDOMIZE_TRUE", 
                      "RANDOMIZE_FALSE", "TYPE_MC", "TYPE_TF", "TYPE_MS", 
                      "TYPE_MT", "TYPE_ORD", "TYPE_FIB", "TYPE_WR", "TYPE_OTHER", 
                      "START_ANSWER", "RIGHT_ANSWER", "LIST_PREFIX", "QUESTION_PREFIX" ]

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
    RULE_end_answers = 17
    RULE_end_answers_item = 18
    RULE_question_prefix = 19

    ruleNames =  [ "parse_question", "section_title", "question", "start_question", 
                   "question_header", "question_type", "title", "points", 
                   "randomize", "question_body", "content", "feedback", 
                   "answer_list", "list_item", "list_prefix", "list_answer_item", 
                   "answer_prefix", "end_answers", "end_answers_item", "question_prefix" ]

    EOF = Token.EOF
    START_QUESTION_HEADER=1
    START_QUESTION=2
    END_ANSWERS=3
    FEEDBACK_MARKER=4
    MEDIA=5
    HYPERLINK=6
    ALL_CHARACTER=7
    ESCAPED_OPEN_BRACKET=8
    ESCAPED_CLOSE_BRACKET=9
    SECTION_TITLE=10
    TITLE=11
    POINTS=12
    RANDOMIZE_TRUE=13
    RANDOMIZE_FALSE=14
    TYPE_MC=15
    TYPE_TF=16
    TYPE_MS=17
    TYPE_MT=18
    TYPE_ORD=19
    TYPE_FIB=20
    TYPE_WR=21
    TYPE_OTHER=22
    START_ANSWER=23
    RIGHT_ANSWER=24
    LIST_PREFIX=25
    QUESTION_PREFIX=26

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
            self.state = 54
            self.match(QuestionParser.SECTION_TITLE)
            self.state = 56 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 55
                self.match(QuestionParser.ALL_CHARACTER)
                self.state = 58 
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
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.START_QUESTION_HEADER:
                    self.state = 60
                    self.question_header()


                self.state = 63
                self.start_question()
                self.state = 64
                self.question_body()
                self.state = 65
                self.answer_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.START_QUESTION_HEADER:
                    self.state = 67
                    self.question_header()


                self.state = 70
                self.start_question()
                self.state = 71
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
            self.state = 75
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
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,103,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 78
                    self.question_type()


                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 81
                    self.title()


                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 84
                    self.points()


                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 87
                    self.randomize()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 91
                    self.question_type()


                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 94
                    self.title()


                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 97
                    self.randomize()


                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 100
                    self.points()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 103
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 104
                    self.question_type()


                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 107
                    self.points()


                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 110
                    self.title()


                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 113
                    self.randomize()


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 116
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 117
                    self.question_type()


                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 120
                    self.points()


                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 123
                    self.randomize()


                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 126
                    self.title()


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 129
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 130
                    self.question_type()


                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 133
                    self.randomize()


                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 136
                    self.title()


                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 139
                    self.points()


                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 142
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 143
                    self.question_type()


                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 146
                    self.randomize()


                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 149
                    self.points()


                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 152
                    self.title()


                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 155
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 156
                    self.title()


                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 159
                    self.question_type()


                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 162
                    self.points()


                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 165
                    self.randomize()


                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 168
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 169
                    self.title()


                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 172
                    self.question_type()


                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 175
                    self.randomize()


                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 178
                    self.points()


                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 181
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 182
                    self.title()


                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 185
                    self.points()


                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 188
                    self.question_type()


                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 191
                    self.randomize()


                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 194
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 195
                    self.title()


                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 198
                    self.points()


                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 201
                    self.randomize()


                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 204
                    self.question_type()


                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 207
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 208
                    self.title()


                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 211
                    self.randomize()


                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 214
                    self.question_type()


                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 217
                    self.points()


                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 220
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 221
                    self.title()


                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 224
                    self.randomize()


                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 227
                    self.points()


                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 230
                    self.question_type()


                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 233
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 234
                    self.points()


                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 237
                    self.question_type()


                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 240
                    self.title()


                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 243
                    self.randomize()


                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 246
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 247
                    self.points()


                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 250
                    self.question_type()


                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 253
                    self.randomize()


                self.state = 257
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 256
                    self.title()


                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 259
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 261
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 260
                    self.points()


                self.state = 264
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 263
                    self.title()


                self.state = 267
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 266
                    self.question_type()


                self.state = 270
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 269
                    self.randomize()


                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 272
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 274
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 273
                    self.points()


                self.state = 277
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 276
                    self.title()


                self.state = 280
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 279
                    self.randomize()


                self.state = 283
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 282
                    self.question_type()


                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 285
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 287
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 286
                    self.points()


                self.state = 290
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 289
                    self.randomize()


                self.state = 293
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 292
                    self.question_type()


                self.state = 296
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 295
                    self.title()


                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 298
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 300
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 299
                    self.points()


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


                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 311
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 313
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 312
                    self.randomize()


                self.state = 316
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 315
                    self.question_type()


                self.state = 319
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 318
                    self.title()


                self.state = 322
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 321
                    self.points()


                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 324
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 326
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 325
                    self.randomize()


                self.state = 329
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 328
                    self.question_type()


                self.state = 332
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 331
                    self.points()


                self.state = 335
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 334
                    self.title()


                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)
                self.state = 337
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 339
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 338
                    self.randomize()


                self.state = 342
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 341
                    self.title()


                self.state = 345
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 344
                    self.question_type()


                self.state = 348
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 347
                    self.points()


                pass

            elif la_ == 22:
                self.enterOuterAlt(localctx, 22)
                self.state = 350
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 352
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 351
                    self.randomize()


                self.state = 355
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 354
                    self.title()


                self.state = 358
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 357
                    self.points()


                self.state = 361
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 360
                    self.question_type()


                pass

            elif la_ == 23:
                self.enterOuterAlt(localctx, 23)
                self.state = 363
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 365
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 364
                    self.randomize()


                self.state = 368
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 367
                    self.points()


                self.state = 371
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 370
                    self.question_type()


                self.state = 374
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 373
                    self.title()


                pass

            elif la_ == 24:
                self.enterOuterAlt(localctx, 24)
                self.state = 376
                self.match(QuestionParser.START_QUESTION_HEADER)
                self.state = 378
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 377
                    self.randomize()


                self.state = 381
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 380
                    self.points()


                self.state = 384
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 383
                    self.title()


                self.state = 387
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 386
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
            self.state = 399
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuestionParser.TYPE_MC]:
                localctx = QuestionParser.TypeMcContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                self.match(QuestionParser.TYPE_MC)
                pass
            elif token in [QuestionParser.TYPE_TF]:
                localctx = QuestionParser.TypeTfContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 392
                self.match(QuestionParser.TYPE_TF)
                pass
            elif token in [QuestionParser.TYPE_MS]:
                localctx = QuestionParser.TypeMsContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 393
                self.match(QuestionParser.TYPE_MS)
                pass
            elif token in [QuestionParser.TYPE_MT]:
                localctx = QuestionParser.TypeMtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 394
                self.match(QuestionParser.TYPE_MT)
                pass
            elif token in [QuestionParser.TYPE_ORD]:
                localctx = QuestionParser.TypeOrdContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 395
                self.match(QuestionParser.TYPE_ORD)
                pass
            elif token in [QuestionParser.TYPE_FIB]:
                localctx = QuestionParser.TypeFibContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 396
                self.match(QuestionParser.TYPE_FIB)
                pass
            elif token in [QuestionParser.TYPE_WR]:
                localctx = QuestionParser.TypeWrContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 397
                self.match(QuestionParser.TYPE_WR)
                pass
            elif token in [QuestionParser.TYPE_OTHER]:
                localctx = QuestionParser.TypeOtherContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 398
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
            self.state = 401
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
            self.state = 403
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
            self.state = 407
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuestionParser.RANDOMIZE_TRUE]:
                localctx = QuestionParser.RandomTrueContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 405
                self.match(QuestionParser.RANDOMIZE_TRUE)
                pass
            elif token in [QuestionParser.RANDOMIZE_FALSE]:
                localctx = QuestionParser.RandomFalseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 406
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
            self.state = 410 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 409
                self.content()
                self.state = 412 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.MEDIA) | (1 << QuestionParser.HYPERLINK) | (1 << QuestionParser.ALL_CHARACTER) | (1 << QuestionParser.ESCAPED_OPEN_BRACKET))) != 0)):
                    break

            self.state = 415
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.FEEDBACK_MARKER:
                self.state = 414
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
            self.state = 431
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuestionParser.MEDIA]:
                localctx = QuestionParser.MediaContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 417
                self.match(QuestionParser.MEDIA)
                pass
            elif token in [QuestionParser.HYPERLINK]:
                localctx = QuestionParser.HyperlinkContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 418
                self.match(QuestionParser.HYPERLINK)
                pass
            elif token in [QuestionParser.ESCAPED_OPEN_BRACKET]:
                localctx = QuestionParser.FibAnswerContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 419
                self.match(QuestionParser.ESCAPED_OPEN_BRACKET)
                self.state = 421 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 420
                    self.match(QuestionParser.ALL_CHARACTER)
                    self.state = 423 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==QuestionParser.ALL_CHARACTER):
                        break

                self.state = 425
                self.match(QuestionParser.ESCAPED_CLOSE_BRACKET)
                pass
            elif token in [QuestionParser.ALL_CHARACTER]:
                localctx = QuestionParser.ContentCharactersContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 427 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 426
                        self.match(QuestionParser.ALL_CHARACTER)

                    else:
                        raise NoViableAltException(self)
                    self.state = 429 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,109,self._ctx)

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
            self.state = 433
            self.match(QuestionParser.FEEDBACK_MARKER)
            self.state = 435 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 434
                self.content()
                self.state = 437 
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
            self.state = 452
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,115,self._ctx)
            if la_ == 1:
                localctx = QuestionParser.ListNoAnswerContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 439
                self.match(QuestionParser.START_ANSWER)
                self.state = 441 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 440
                    self.list_item()
                    self.state = 443 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==QuestionParser.LIST_PREFIX):
                        break

                pass

            elif la_ == 2:
                localctx = QuestionParser.ListWithAnswerContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 445
                self.match(QuestionParser.START_ANSWER)
                self.state = 448 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 448
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [QuestionParser.RIGHT_ANSWER]:
                        self.state = 446
                        self.list_answer_item()
                        pass
                    elif token in [QuestionParser.LIST_PREFIX]:
                        self.state = 447
                        self.list_item()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 450 
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
            self.state = 454
            self.list_prefix()
            self.state = 456 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 455
                self.content()
                self.state = 458 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.MEDIA) | (1 << QuestionParser.HYPERLINK) | (1 << QuestionParser.ALL_CHARACTER) | (1 << QuestionParser.ESCAPED_OPEN_BRACKET))) != 0)):
                    break

            self.state = 461
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.FEEDBACK_MARKER:
                self.state = 460
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
            self.state = 463
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
            self.state = 465
            self.answer_prefix()
            self.state = 467 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 466
                self.content()
                self.state = 469 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.MEDIA) | (1 << QuestionParser.HYPERLINK) | (1 << QuestionParser.ALL_CHARACTER) | (1 << QuestionParser.ESCAPED_OPEN_BRACKET))) != 0)):
                    break

            self.state = 472
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.FEEDBACK_MARKER:
                self.state = 471
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
            self.state = 474
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
            self.state = 476
            self.match(QuestionParser.END_ANSWERS)
            self.state = 478 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 477
                self.end_answers_item()
                self.state = 480 
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
            self.state = 482
            self.question_prefix()
            self.state = 484 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 483
                self.content()
                self.state = 486 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.MEDIA) | (1 << QuestionParser.HYPERLINK) | (1 << QuestionParser.ALL_CHARACTER) | (1 << QuestionParser.ESCAPED_OPEN_BRACKET))) != 0)):
                    break

            self.state = 489
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.FEEDBACK_MARKER:
                self.state = 488
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
        self.enterRule(localctx, 38, self.RULE_question_prefix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self.match(QuestionParser.QUESTION_PREFIX)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





