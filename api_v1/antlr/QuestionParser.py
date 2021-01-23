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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\33")
        buf.write("\u01d1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\5\2,\n\2\3\2\7\2/\n\2\f\2\16")
        buf.write("\2\62\13\2\3\2\5\2\65\n\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\5\4D\n\4\3\5\3\5\3\6\5\6I\n\6")
        buf.write("\3\6\5\6L\n\6\3\6\5\6O\n\6\3\6\5\6R\n\6\3\6\5\6U\n\6\3")
        buf.write("\6\5\6X\n\6\3\6\5\6[\n\6\3\6\5\6^\n\6\3\6\5\6a\n\6\3\6")
        buf.write("\5\6d\n\6\3\6\5\6g\n\6\3\6\5\6j\n\6\3\6\5\6m\n\6\3\6\5")
        buf.write("\6p\n\6\3\6\5\6s\n\6\3\6\5\6v\n\6\3\6\5\6y\n\6\3\6\5\6")
        buf.write("|\n\6\3\6\5\6\177\n\6\3\6\5\6\u0082\n\6\3\6\5\6\u0085")
        buf.write("\n\6\3\6\5\6\u0088\n\6\3\6\5\6\u008b\n\6\3\6\5\6\u008e")
        buf.write("\n\6\3\6\5\6\u0091\n\6\3\6\5\6\u0094\n\6\3\6\5\6\u0097")
        buf.write("\n\6\3\6\5\6\u009a\n\6\3\6\5\6\u009d\n\6\3\6\5\6\u00a0")
        buf.write("\n\6\3\6\5\6\u00a3\n\6\3\6\5\6\u00a6\n\6\3\6\5\6\u00a9")
        buf.write("\n\6\3\6\5\6\u00ac\n\6\3\6\5\6\u00af\n\6\3\6\5\6\u00b2")
        buf.write("\n\6\3\6\5\6\u00b5\n\6\3\6\5\6\u00b8\n\6\3\6\5\6\u00bb")
        buf.write("\n\6\3\6\5\6\u00be\n\6\3\6\5\6\u00c1\n\6\3\6\5\6\u00c4")
        buf.write("\n\6\3\6\5\6\u00c7\n\6\3\6\5\6\u00ca\n\6\3\6\5\6\u00cd")
        buf.write("\n\6\3\6\5\6\u00d0\n\6\3\6\5\6\u00d3\n\6\3\6\5\6\u00d6")
        buf.write("\n\6\3\6\5\6\u00d9\n\6\3\6\5\6\u00dc\n\6\3\6\5\6\u00df")
        buf.write("\n\6\3\6\5\6\u00e2\n\6\3\6\5\6\u00e5\n\6\3\6\5\6\u00e8")
        buf.write("\n\6\3\6\5\6\u00eb\n\6\3\6\5\6\u00ee\n\6\3\6\5\6\u00f1")
        buf.write("\n\6\3\6\5\6\u00f4\n\6\3\6\5\6\u00f7\n\6\3\6\5\6\u00fa")
        buf.write("\n\6\3\6\5\6\u00fd\n\6\3\6\5\6\u0100\n\6\3\6\5\6\u0103")
        buf.write("\n\6\3\6\5\6\u0106\n\6\3\6\5\6\u0109\n\6\3\6\5\6\u010c")
        buf.write("\n\6\3\6\5\6\u010f\n\6\3\6\5\6\u0112\n\6\3\6\5\6\u0115")
        buf.write("\n\6\3\6\5\6\u0118\n\6\3\6\5\6\u011b\n\6\3\6\5\6\u011e")
        buf.write("\n\6\3\6\5\6\u0121\n\6\3\6\5\6\u0124\n\6\3\6\5\6\u0127")
        buf.write("\n\6\3\6\5\6\u012a\n\6\3\6\5\6\u012d\n\6\3\6\5\6\u0130")
        buf.write("\n\6\3\6\5\6\u0133\n\6\3\6\5\6\u0136\n\6\3\6\5\6\u0139")
        buf.write("\n\6\3\6\5\6\u013c\n\6\3\6\5\6\u013f\n\6\3\6\5\6\u0142")
        buf.write("\n\6\3\6\5\6\u0145\n\6\3\6\5\6\u0148\n\6\3\6\5\6\u014b")
        buf.write("\n\6\3\6\5\6\u014e\n\6\3\6\5\6\u0151\n\6\3\6\5\6\u0154")
        buf.write("\n\6\3\6\5\6\u0157\n\6\3\6\5\6\u015a\n\6\3\6\5\6\u015d")
        buf.write("\n\6\3\6\5\6\u0160\n\6\3\6\5\6\u0163\n\6\3\6\5\6\u0166")
        buf.write("\n\6\5\6\u0168\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7")
        buf.write("\u0172\n\7\3\b\3\b\3\t\3\t\3\n\3\n\5\n\u017a\n\n\3\13")
        buf.write("\3\13\6\13\u017e\n\13\r\13\16\13\u017f\3\13\5\13\u0183")
        buf.write("\n\13\3\f\3\f\3\r\3\r\3\r\3\r\6\r\u018b\n\r\r\r\16\r\u018c")
        buf.write("\3\r\3\r\6\r\u0191\n\r\r\r\16\r\u0192\5\r\u0195\n\r\3")
        buf.write("\16\3\16\6\16\u0199\n\16\r\16\16\16\u019a\3\17\3\17\6")
        buf.write("\17\u019f\n\17\r\17\16\17\u01a0\3\17\3\17\3\17\6\17\u01a6")
        buf.write("\n\17\r\17\16\17\u01a7\5\17\u01aa\n\17\3\20\3\20\6\20")
        buf.write("\u01ae\n\20\r\20\16\20\u01af\3\20\5\20\u01b3\n\20\3\21")
        buf.write("\3\21\3\22\3\22\6\22\u01b9\n\22\r\22\16\22\u01ba\3\22")
        buf.write("\5\22\u01be\n\22\3\23\3\23\3\24\3\24\6\24\u01c4\n\24\r")
        buf.write("\24\16\24\u01c5\3\25\3\25\6\25\u01ca\n\25\r\25\16\25\u01cb")
        buf.write("\3\25\5\25\u01cf\n\25\3\25\2\2\26\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(\2\2\2\u0252\2+\3\2\2\2\48\3\2")
        buf.write("\2\2\6C\3\2\2\2\bE\3\2\2\2\n\u0167\3\2\2\2\f\u0171\3\2")
        buf.write("\2\2\16\u0173\3\2\2\2\20\u0175\3\2\2\2\22\u0179\3\2\2")
        buf.write("\2\24\u017b\3\2\2\2\26\u0184\3\2\2\2\30\u0194\3\2\2\2")
        buf.write("\32\u0196\3\2\2\2\34\u01a9\3\2\2\2\36\u01ab\3\2\2\2 \u01b4")
        buf.write("\3\2\2\2\"\u01b6\3\2\2\2$\u01bf\3\2\2\2&\u01c1\3\2\2\2")
        buf.write("(\u01c7\3\2\2\2*,\5\4\3\2+*\3\2\2\2+,\3\2\2\2,\60\3\2")
        buf.write("\2\2-/\5\6\4\2.-\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\60\61")
        buf.write("\3\2\2\2\61\64\3\2\2\2\62\60\3\2\2\2\63\65\5&\24\2\64")
        buf.write("\63\3\2\2\2\64\65\3\2\2\2\65\66\3\2\2\2\66\67\7\2\2\3")
        buf.write("\67\3\3\2\2\289\7\f\2\29\5\3\2\2\2:;\5\n\6\2;<\5\b\5\2")
        buf.write("<=\5\24\13\2=>\5\34\17\2>D\3\2\2\2?@\5\n\6\2@A\5\b\5\2")
        buf.write("AB\5\24\13\2BD\3\2\2\2C:\3\2\2\2C?\3\2\2\2D\7\3\2\2\2")
        buf.write("EF\7\3\2\2F\t\3\2\2\2GI\5\f\7\2HG\3\2\2\2HI\3\2\2\2IK")
        buf.write("\3\2\2\2JL\5\16\b\2KJ\3\2\2\2KL\3\2\2\2LN\3\2\2\2MO\5")
        buf.write("\20\t\2NM\3\2\2\2NO\3\2\2\2OQ\3\2\2\2PR\5\22\n\2QP\3\2")
        buf.write("\2\2QR\3\2\2\2R\u0168\3\2\2\2SU\5\f\7\2TS\3\2\2\2TU\3")
        buf.write("\2\2\2UW\3\2\2\2VX\5\16\b\2WV\3\2\2\2WX\3\2\2\2XZ\3\2")
        buf.write("\2\2Y[\5\22\n\2ZY\3\2\2\2Z[\3\2\2\2[]\3\2\2\2\\^\5\20")
        buf.write("\t\2]\\\3\2\2\2]^\3\2\2\2^\u0168\3\2\2\2_a\5\f\7\2`_\3")
        buf.write("\2\2\2`a\3\2\2\2ac\3\2\2\2bd\5\20\t\2cb\3\2\2\2cd\3\2")
        buf.write("\2\2df\3\2\2\2eg\5\16\b\2fe\3\2\2\2fg\3\2\2\2gi\3\2\2")
        buf.write("\2hj\5\22\n\2ih\3\2\2\2ij\3\2\2\2j\u0168\3\2\2\2km\5\f")
        buf.write("\7\2lk\3\2\2\2lm\3\2\2\2mo\3\2\2\2np\5\20\t\2on\3\2\2")
        buf.write("\2op\3\2\2\2pr\3\2\2\2qs\5\22\n\2rq\3\2\2\2rs\3\2\2\2")
        buf.write("su\3\2\2\2tv\5\16\b\2ut\3\2\2\2uv\3\2\2\2v\u0168\3\2\2")
        buf.write("\2wy\5\f\7\2xw\3\2\2\2xy\3\2\2\2y{\3\2\2\2z|\5\22\n\2")
        buf.write("{z\3\2\2\2{|\3\2\2\2|~\3\2\2\2}\177\5\16\b\2~}\3\2\2\2")
        buf.write("~\177\3\2\2\2\177\u0081\3\2\2\2\u0080\u0082\5\20\t\2\u0081")
        buf.write("\u0080\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0168\3\2\2\2")
        buf.write("\u0083\u0085\5\f\7\2\u0084\u0083\3\2\2\2\u0084\u0085\3")
        buf.write("\2\2\2\u0085\u0087\3\2\2\2\u0086\u0088\5\22\n\2\u0087")
        buf.write("\u0086\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u008a\3\2\2\2")
        buf.write("\u0089\u008b\5\20\t\2\u008a\u0089\3\2\2\2\u008a\u008b")
        buf.write("\3\2\2\2\u008b\u008d\3\2\2\2\u008c\u008e\5\16\b\2\u008d")
        buf.write("\u008c\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u0168\3\2\2\2")
        buf.write("\u008f\u0091\5\16\b\2\u0090\u008f\3\2\2\2\u0090\u0091")
        buf.write("\3\2\2\2\u0091\u0093\3\2\2\2\u0092\u0094\5\f\7\2\u0093")
        buf.write("\u0092\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0096\3\2\2\2")
        buf.write("\u0095\u0097\5\20\t\2\u0096\u0095\3\2\2\2\u0096\u0097")
        buf.write("\3\2\2\2\u0097\u0099\3\2\2\2\u0098\u009a\5\22\n\2\u0099")
        buf.write("\u0098\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u0168\3\2\2\2")
        buf.write("\u009b\u009d\5\16\b\2\u009c\u009b\3\2\2\2\u009c\u009d")
        buf.write("\3\2\2\2\u009d\u009f\3\2\2\2\u009e\u00a0\5\f\7\2\u009f")
        buf.write("\u009e\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a2\3\2\2\2")
        buf.write("\u00a1\u00a3\5\22\n\2\u00a2\u00a1\3\2\2\2\u00a2\u00a3")
        buf.write("\3\2\2\2\u00a3\u00a5\3\2\2\2\u00a4\u00a6\5\20\t\2\u00a5")
        buf.write("\u00a4\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u0168\3\2\2\2")
        buf.write("\u00a7\u00a9\5\16\b\2\u00a8\u00a7\3\2\2\2\u00a8\u00a9")
        buf.write("\3\2\2\2\u00a9\u00ab\3\2\2\2\u00aa\u00ac\5\20\t\2\u00ab")
        buf.write("\u00aa\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ae\3\2\2\2")
        buf.write("\u00ad\u00af\5\f\7\2\u00ae\u00ad\3\2\2\2\u00ae\u00af\3")
        buf.write("\2\2\2\u00af\u00b1\3\2\2\2\u00b0\u00b2\5\22\n\2\u00b1")
        buf.write("\u00b0\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u0168\3\2\2\2")
        buf.write("\u00b3\u00b5\5\16\b\2\u00b4\u00b3\3\2\2\2\u00b4\u00b5")
        buf.write("\3\2\2\2\u00b5\u00b7\3\2\2\2\u00b6\u00b8\5\20\t\2\u00b7")
        buf.write("\u00b6\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00ba\3\2\2\2")
        buf.write("\u00b9\u00bb\5\22\n\2\u00ba\u00b9\3\2\2\2\u00ba\u00bb")
        buf.write("\3\2\2\2\u00bb\u00bd\3\2\2\2\u00bc\u00be\5\f\7\2\u00bd")
        buf.write("\u00bc\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u0168\3\2\2\2")
        buf.write("\u00bf\u00c1\5\16\b\2\u00c0\u00bf\3\2\2\2\u00c0\u00c1")
        buf.write("\3\2\2\2\u00c1\u00c3\3\2\2\2\u00c2\u00c4\5\22\n\2\u00c3")
        buf.write("\u00c2\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c6\3\2\2\2")
        buf.write("\u00c5\u00c7\5\f\7\2\u00c6\u00c5\3\2\2\2\u00c6\u00c7\3")
        buf.write("\2\2\2\u00c7\u00c9\3\2\2\2\u00c8\u00ca\5\20\t\2\u00c9")
        buf.write("\u00c8\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u0168\3\2\2\2")
        buf.write("\u00cb\u00cd\5\16\b\2\u00cc\u00cb\3\2\2\2\u00cc\u00cd")
        buf.write("\3\2\2\2\u00cd\u00cf\3\2\2\2\u00ce\u00d0\5\22\n\2\u00cf")
        buf.write("\u00ce\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d2\3\2\2\2")
        buf.write("\u00d1\u00d3\5\20\t\2\u00d2\u00d1\3\2\2\2\u00d2\u00d3")
        buf.write("\3\2\2\2\u00d3\u00d5\3\2\2\2\u00d4\u00d6\5\f\7\2\u00d5")
        buf.write("\u00d4\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u0168\3\2\2\2")
        buf.write("\u00d7\u00d9\5\20\t\2\u00d8\u00d7\3\2\2\2\u00d8\u00d9")
        buf.write("\3\2\2\2\u00d9\u00db\3\2\2\2\u00da\u00dc\5\f\7\2\u00db")
        buf.write("\u00da\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc\u00de\3\2\2\2")
        buf.write("\u00dd\u00df\5\16\b\2\u00de\u00dd\3\2\2\2\u00de\u00df")
        buf.write("\3\2\2\2\u00df\u00e1\3\2\2\2\u00e0\u00e2\5\22\n\2\u00e1")
        buf.write("\u00e0\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u0168\3\2\2\2")
        buf.write("\u00e3\u00e5\5\20\t\2\u00e4\u00e3\3\2\2\2\u00e4\u00e5")
        buf.write("\3\2\2\2\u00e5\u00e7\3\2\2\2\u00e6\u00e8\5\f\7\2\u00e7")
        buf.write("\u00e6\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00ea\3\2\2\2")
        buf.write("\u00e9\u00eb\5\22\n\2\u00ea\u00e9\3\2\2\2\u00ea\u00eb")
        buf.write("\3\2\2\2\u00eb\u00ed\3\2\2\2\u00ec\u00ee\5\16\b\2\u00ed")
        buf.write("\u00ec\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u0168\3\2\2\2")
        buf.write("\u00ef\u00f1\5\20\t\2\u00f0\u00ef\3\2\2\2\u00f0\u00f1")
        buf.write("\3\2\2\2\u00f1\u00f3\3\2\2\2\u00f2\u00f4\5\16\b\2\u00f3")
        buf.write("\u00f2\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f6\3\2\2\2")
        buf.write("\u00f5\u00f7\5\f\7\2\u00f6\u00f5\3\2\2\2\u00f6\u00f7\3")
        buf.write("\2\2\2\u00f7\u00f9\3\2\2\2\u00f8\u00fa\5\22\n\2\u00f9")
        buf.write("\u00f8\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u0168\3\2\2\2")
        buf.write("\u00fb\u00fd\5\20\t\2\u00fc\u00fb\3\2\2\2\u00fc\u00fd")
        buf.write("\3\2\2\2\u00fd\u00ff\3\2\2\2\u00fe\u0100\5\16\b\2\u00ff")
        buf.write("\u00fe\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0102\3\2\2\2")
        buf.write("\u0101\u0103\5\22\n\2\u0102\u0101\3\2\2\2\u0102\u0103")
        buf.write("\3\2\2\2\u0103\u0105\3\2\2\2\u0104\u0106\5\f\7\2\u0105")
        buf.write("\u0104\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0168\3\2\2\2")
        buf.write("\u0107\u0109\5\20\t\2\u0108\u0107\3\2\2\2\u0108\u0109")
        buf.write("\3\2\2\2\u0109\u010b\3\2\2\2\u010a\u010c\5\22\n\2\u010b")
        buf.write("\u010a\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010e\3\2\2\2")
        buf.write("\u010d\u010f\5\f\7\2\u010e\u010d\3\2\2\2\u010e\u010f\3")
        buf.write("\2\2\2\u010f\u0111\3\2\2\2\u0110\u0112\5\16\b\2\u0111")
        buf.write("\u0110\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0168\3\2\2\2")
        buf.write("\u0113\u0115\5\20\t\2\u0114\u0113\3\2\2\2\u0114\u0115")
        buf.write("\3\2\2\2\u0115\u0117\3\2\2\2\u0116\u0118\5\22\n\2\u0117")
        buf.write("\u0116\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u011a\3\2\2\2")
        buf.write("\u0119\u011b\5\16\b\2\u011a\u0119\3\2\2\2\u011a\u011b")
        buf.write("\3\2\2\2\u011b\u011d\3\2\2\2\u011c\u011e\5\f\7\2\u011d")
        buf.write("\u011c\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u0168\3\2\2\2")
        buf.write("\u011f\u0121\5\22\n\2\u0120\u011f\3\2\2\2\u0120\u0121")
        buf.write("\3\2\2\2\u0121\u0123\3\2\2\2\u0122\u0124\5\f\7\2\u0123")
        buf.write("\u0122\3\2\2\2\u0123\u0124\3\2\2\2\u0124\u0126\3\2\2\2")
        buf.write("\u0125\u0127\5\16\b\2\u0126\u0125\3\2\2\2\u0126\u0127")
        buf.write("\3\2\2\2\u0127\u0129\3\2\2\2\u0128\u012a\5\20\t\2\u0129")
        buf.write("\u0128\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u0168\3\2\2\2")
        buf.write("\u012b\u012d\5\22\n\2\u012c\u012b\3\2\2\2\u012c\u012d")
        buf.write("\3\2\2\2\u012d\u012f\3\2\2\2\u012e\u0130\5\f\7\2\u012f")
        buf.write("\u012e\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u0132\3\2\2\2")
        buf.write("\u0131\u0133\5\20\t\2\u0132\u0131\3\2\2\2\u0132\u0133")
        buf.write("\3\2\2\2\u0133\u0135\3\2\2\2\u0134\u0136\5\16\b\2\u0135")
        buf.write("\u0134\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u0168\3\2\2\2")
        buf.write("\u0137\u0139\5\22\n\2\u0138\u0137\3\2\2\2\u0138\u0139")
        buf.write("\3\2\2\2\u0139\u013b\3\2\2\2\u013a\u013c\5\16\b\2\u013b")
        buf.write("\u013a\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013e\3\2\2\2")
        buf.write("\u013d\u013f\5\f\7\2\u013e\u013d\3\2\2\2\u013e\u013f\3")
        buf.write("\2\2\2\u013f\u0141\3\2\2\2\u0140\u0142\5\20\t\2\u0141")
        buf.write("\u0140\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0168\3\2\2\2")
        buf.write("\u0143\u0145\5\22\n\2\u0144\u0143\3\2\2\2\u0144\u0145")
        buf.write("\3\2\2\2\u0145\u0147\3\2\2\2\u0146\u0148\5\16\b\2\u0147")
        buf.write("\u0146\3\2\2\2\u0147\u0148\3\2\2\2\u0148\u014a\3\2\2\2")
        buf.write("\u0149\u014b\5\20\t\2\u014a\u0149\3\2\2\2\u014a\u014b")
        buf.write("\3\2\2\2\u014b\u014d\3\2\2\2\u014c\u014e\5\f\7\2\u014d")
        buf.write("\u014c\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u0168\3\2\2\2")
        buf.write("\u014f\u0151\5\22\n\2\u0150\u014f\3\2\2\2\u0150\u0151")
        buf.write("\3\2\2\2\u0151\u0153\3\2\2\2\u0152\u0154\5\20\t\2\u0153")
        buf.write("\u0152\3\2\2\2\u0153\u0154\3\2\2\2\u0154\u0156\3\2\2\2")
        buf.write("\u0155\u0157\5\f\7\2\u0156\u0155\3\2\2\2\u0156\u0157\3")
        buf.write("\2\2\2\u0157\u0159\3\2\2\2\u0158\u015a\5\16\b\2\u0159")
        buf.write("\u0158\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u0168\3\2\2\2")
        buf.write("\u015b\u015d\5\22\n\2\u015c\u015b\3\2\2\2\u015c\u015d")
        buf.write("\3\2\2\2\u015d\u015f\3\2\2\2\u015e\u0160\5\20\t\2\u015f")
        buf.write("\u015e\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0162\3\2\2\2")
        buf.write("\u0161\u0163\5\16\b\2\u0162\u0161\3\2\2\2\u0162\u0163")
        buf.write("\3\2\2\2\u0163\u0165\3\2\2\2\u0164\u0166\5\f\7\2\u0165")
        buf.write("\u0164\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0168\3\2\2\2")
        buf.write("\u0167H\3\2\2\2\u0167T\3\2\2\2\u0167`\3\2\2\2\u0167l\3")
        buf.write("\2\2\2\u0167x\3\2\2\2\u0167\u0084\3\2\2\2\u0167\u0090")
        buf.write("\3\2\2\2\u0167\u009c\3\2\2\2\u0167\u00a8\3\2\2\2\u0167")
        buf.write("\u00b4\3\2\2\2\u0167\u00c0\3\2\2\2\u0167\u00cc\3\2\2\2")
        buf.write("\u0167\u00d8\3\2\2\2\u0167\u00e4\3\2\2\2\u0167\u00f0\3")
        buf.write("\2\2\2\u0167\u00fc\3\2\2\2\u0167\u0108\3\2\2\2\u0167\u0114")
        buf.write("\3\2\2\2\u0167\u0120\3\2\2\2\u0167\u012c\3\2\2\2\u0167")
        buf.write("\u0138\3\2\2\2\u0167\u0144\3\2\2\2\u0167\u0150\3\2\2\2")
        buf.write("\u0167\u015c\3\2\2\2\u0168\13\3\2\2\2\u0169\u0172\7\21")
        buf.write("\2\2\u016a\u0172\7\22\2\2\u016b\u0172\7\23\2\2\u016c\u0172")
        buf.write("\7\24\2\2\u016d\u0172\7\25\2\2\u016e\u0172\7\26\2\2\u016f")
        buf.write("\u0172\7\27\2\2\u0170\u0172\7\30\2\2\u0171\u0169\3\2\2")
        buf.write("\2\u0171\u016a\3\2\2\2\u0171\u016b\3\2\2\2\u0171\u016c")
        buf.write("\3\2\2\2\u0171\u016d\3\2\2\2\u0171\u016e\3\2\2\2\u0171")
        buf.write("\u016f\3\2\2\2\u0171\u0170\3\2\2\2\u0172\r\3\2\2\2\u0173")
        buf.write("\u0174\7\r\2\2\u0174\17\3\2\2\2\u0175\u0176\7\16\2\2\u0176")
        buf.write("\21\3\2\2\2\u0177\u017a\7\17\2\2\u0178\u017a\7\20\2\2")
        buf.write("\u0179\u0177\3\2\2\2\u0179\u0178\3\2\2\2\u017a\23\3\2")
        buf.write("\2\2\u017b\u017d\5\26\f\2\u017c\u017e\5\30\r\2\u017d\u017c")
        buf.write("\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u017d\3\2\2\2\u017f")
        buf.write("\u0180\3\2\2\2\u0180\u0182\3\2\2\2\u0181\u0183\5\32\16")
        buf.write("\2\u0182\u0181\3\2\2\2\u0182\u0183\3\2\2\2\u0183\25\3")
        buf.write("\2\2\2\u0184\u0185\7\5\2\2\u0185\27\3\2\2\2\u0186\u0195")
        buf.write("\7\7\2\2\u0187\u0195\7\b\2\2\u0188\u018a\7\n\2\2\u0189")
        buf.write("\u018b\7\t\2\2\u018a\u0189\3\2\2\2\u018b\u018c\3\2\2\2")
        buf.write("\u018c\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018e\3")
        buf.write("\2\2\2\u018e\u0195\7\13\2\2\u018f\u0191\7\t\2\2\u0190")
        buf.write("\u018f\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0190\3\2\2\2")
        buf.write("\u0192\u0193\3\2\2\2\u0193\u0195\3\2\2\2\u0194\u0186\3")
        buf.write("\2\2\2\u0194\u0187\3\2\2\2\u0194\u0188\3\2\2\2\u0194\u0190")
        buf.write("\3\2\2\2\u0195\31\3\2\2\2\u0196\u0198\7\6\2\2\u0197\u0199")
        buf.write("\5\30\r\2\u0198\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019a")
        buf.write("\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019b\33\3\2\2\2\u019c")
        buf.write("\u019e\7\31\2\2\u019d\u019f\5\36\20\2\u019e\u019d\3\2")
        buf.write("\2\2\u019f\u01a0\3\2\2\2\u01a0\u019e\3\2\2\2\u01a0\u01a1")
        buf.write("\3\2\2\2\u01a1\u01aa\3\2\2\2\u01a2\u01a5\7\31\2\2\u01a3")
        buf.write("\u01a6\5\"\22\2\u01a4\u01a6\5\36\20\2\u01a5\u01a3\3\2")
        buf.write("\2\2\u01a5\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a5")
        buf.write("\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01aa\3\2\2\2\u01a9")
        buf.write("\u019c\3\2\2\2\u01a9\u01a2\3\2\2\2\u01aa\35\3\2\2\2\u01ab")
        buf.write("\u01ad\5 \21\2\u01ac\u01ae\5\30\r\2\u01ad\u01ac\3\2\2")
        buf.write("\2\u01ae\u01af\3\2\2\2\u01af\u01ad\3\2\2\2\u01af\u01b0")
        buf.write("\3\2\2\2\u01b0\u01b2\3\2\2\2\u01b1\u01b3\5\32\16\2\u01b2")
        buf.write("\u01b1\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\37\3\2\2\2\u01b4")
        buf.write("\u01b5\7\33\2\2\u01b5!\3\2\2\2\u01b6\u01b8\5$\23\2\u01b7")
        buf.write("\u01b9\5\30\r\2\u01b8\u01b7\3\2\2\2\u01b9\u01ba\3\2\2")
        buf.write("\2\u01ba\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bd")
        buf.write("\3\2\2\2\u01bc\u01be\5\32\16\2\u01bd\u01bc\3\2\2\2\u01bd")
        buf.write("\u01be\3\2\2\2\u01be#\3\2\2\2\u01bf\u01c0\7\32\2\2\u01c0")
        buf.write("%\3\2\2\2\u01c1\u01c3\7\4\2\2\u01c2\u01c4\5(\25\2\u01c3")
        buf.write("\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c3\3\2\2\2")
        buf.write("\u01c5\u01c6\3\2\2\2\u01c6\'\3\2\2\2\u01c7\u01c9\5\26")
        buf.write("\f\2\u01c8\u01ca\5\30\r\2\u01c9\u01c8\3\2\2\2\u01ca\u01cb")
        buf.write("\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc")
        buf.write("\u01ce\3\2\2\2\u01cd\u01cf\5\32\16\2\u01ce\u01cd\3\2\2")
        buf.write("\2\u01ce\u01cf\3\2\2\2\u01cf)\3\2\2\2z+\60\64CHKNQTWZ")
        buf.write("]`cfilorux{~\u0081\u0084\u0087\u008a\u008d\u0090\u0093")
        buf.write("\u0096\u0099\u009c\u009f\u00a2\u00a5\u00a8\u00ab\u00ae")
        buf.write("\u00b1\u00b4\u00b7\u00ba\u00bd\u00c0\u00c3\u00c6\u00c9")
        buf.write("\u00cc\u00cf\u00d2\u00d5\u00d8\u00db\u00de\u00e1\u00e4")
        buf.write("\u00e7\u00ea\u00ed\u00f0\u00f3\u00f6\u00f9\u00fc\u00ff")
        buf.write("\u0102\u0105\u0108\u010b\u010e\u0111\u0114\u0117\u011a")
        buf.write("\u011d\u0120\u0123\u0126\u0129\u012c\u012f\u0132\u0135")
        buf.write("\u0138\u013b\u013e\u0141\u0144\u0147\u014a\u014d\u0150")
        buf.write("\u0153\u0156\u0159\u015c\u015f\u0162\u0165\u0167\u0171")
        buf.write("\u0179\u017f\u0182\u018c\u0192\u0194\u019a\u01a0\u01a5")
        buf.write("\u01a7\u01a9\u01af\u01b2\u01ba\u01bd\u01c5\u01cb\u01ce")
        return buf.getvalue()


class QuestionParser ( Parser ):

    grammarFileName = "QuestionParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "START_QUESTION", "END_ANSWERS", "QUESTION_PREFIX", 
                      "FEEDBACK_MARKER", "MEDIA", "HYPERLINK", "ALL_CHARACTER", 
                      "ESCAPED_OPEN_BRACKET", "ESCAPED_CLOSE_BRACKET", "SECTION_HEADER", 
                      "TITLE", "POINTS", "RANDOMIZE_TRUE", "RANDOMIZE_FALSE", 
                      "TYPE_MC", "TYPE_TF", "TYPE_MS", "TYPE_MT", "TYPE_ORD", 
                      "TYPE_FIB", "TYPE_WR", "TYPE_OTHER", "START_ANSWER", 
                      "RIGHT_ANSWER", "LIST_PREFIX" ]

    RULE_parse_question = 0
    RULE_section_header = 1
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

    ruleNames =  [ "parse_question", "section_header", "question", "start_question", 
                   "question_header", "question_type", "title", "points", 
                   "randomize", "question_body", "question_prefix", "content", 
                   "feedback", "answer_list", "list_item", "list_prefix", 
                   "list_answer_item", "answer_prefix", "end_answers", "end_answers_item" ]

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
    SECTION_HEADER=10
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

        def section_header(self):
            return self.getTypedRuleContext(QuestionParser.Section_headerContext,0)


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
            if _la==QuestionParser.SECTION_HEADER:
                self.state = 40
                self.section_header()


            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.START_QUESTION) | (1 << QuestionParser.TITLE) | (1 << QuestionParser.POINTS) | (1 << QuestionParser.RANDOMIZE_TRUE) | (1 << QuestionParser.RANDOMIZE_FALSE) | (1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
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


    class Section_headerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SECTION_HEADER(self):
            return self.getToken(QuestionParser.SECTION_HEADER, 0)

        def getRuleIndex(self):
            return QuestionParser.RULE_section_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSection_header" ):
                listener.enterSection_header(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSection_header" ):
                listener.exitSection_header(self)




    def section_header(self):

        localctx = QuestionParser.Section_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_section_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(QuestionParser.SECTION_HEADER)
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

        def question_header(self):
            return self.getTypedRuleContext(QuestionParser.Question_headerContext,0)


        def start_question(self):
            return self.getTypedRuleContext(QuestionParser.Start_questionContext,0)


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
        self.enterRule(localctx, 4, self.RULE_question)
        try:
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.question_header()
                self.state = 57
                self.start_question()
                self.state = 58
                self.question_body()
                self.state = 59
                self.answer_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.question_header()
                self.state = 62
                self.start_question()
                self.state = 63
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
            self.state = 67
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
        self.enterRule(localctx, 8, self.RULE_question_header)
        self._la = 0 # Token type
        try:
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,100,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 69
                    self.question_type()


                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 72
                    self.title()


                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 75
                    self.points()


                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 78
                    self.randomize()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 81
                    self.question_type()


                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 84
                    self.title()


                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 87
                    self.randomize()


                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 90
                    self.points()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 93
                    self.question_type()


                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 96
                    self.points()


                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 99
                    self.title()


                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 102
                    self.randomize()


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 105
                    self.question_type()


                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 108
                    self.points()


                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 111
                    self.randomize()


                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 114
                    self.title()


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 117
                    self.question_type()


                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 120
                    self.randomize()


                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 123
                    self.title()


                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 126
                    self.points()


                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 129
                    self.question_type()


                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 132
                    self.randomize()


                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 135
                    self.points()


                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 138
                    self.title()


                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 141
                    self.title()


                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 144
                    self.question_type()


                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 147
                    self.points()


                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 150
                    self.randomize()


                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 153
                    self.title()


                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 156
                    self.question_type()


                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 159
                    self.randomize()


                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 162
                    self.points()


                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 165
                    self.title()


                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 168
                    self.points()


                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 171
                    self.question_type()


                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 174
                    self.randomize()


                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 177
                    self.title()


                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 180
                    self.points()


                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 183
                    self.randomize()


                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 186
                    self.question_type()


                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 189
                    self.title()


                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 192
                    self.randomize()


                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 195
                    self.question_type()


                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 198
                    self.points()


                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 201
                    self.title()


                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 204
                    self.randomize()


                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 207
                    self.points()


                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 210
                    self.question_type()


                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 213
                    self.points()


                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 216
                    self.question_type()


                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 219
                    self.title()


                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 222
                    self.randomize()


                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 225
                    self.points()


                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 228
                    self.question_type()


                self.state = 232
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 231
                    self.randomize()


                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 234
                    self.title()


                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 237
                    self.points()


                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 240
                    self.title()


                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 243
                    self.question_type()


                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 246
                    self.randomize()


                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 249
                    self.points()


                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 252
                    self.title()


                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 255
                    self.randomize()


                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 258
                    self.question_type()


                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 261
                    self.points()


                self.state = 265
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 264
                    self.randomize()


                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 267
                    self.question_type()


                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 270
                    self.title()


                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 274
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 273
                    self.points()


                self.state = 277
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 276
                    self.randomize()


                self.state = 280
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 279
                    self.title()


                self.state = 283
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 282
                    self.question_type()


                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
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


                self.state = 295
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 294
                    self.points()


                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 298
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 297
                    self.randomize()


                self.state = 301
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 300
                    self.question_type()


                self.state = 304
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 303
                    self.points()


                self.state = 307
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 306
                    self.title()


                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)
                self.state = 310
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 309
                    self.randomize()


                self.state = 313
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 312
                    self.title()


                self.state = 316
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 315
                    self.question_type()


                self.state = 319
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 318
                    self.points()


                pass

            elif la_ == 22:
                self.enterOuterAlt(localctx, 22)
                self.state = 322
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 321
                    self.randomize()


                self.state = 325
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 324
                    self.title()


                self.state = 328
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 327
                    self.points()


                self.state = 331
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 330
                    self.question_type()


                pass

            elif la_ == 23:
                self.enterOuterAlt(localctx, 23)
                self.state = 334
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 333
                    self.randomize()


                self.state = 337
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 336
                    self.points()


                self.state = 340
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 339
                    self.question_type()


                self.state = 343
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 342
                    self.title()


                pass

            elif la_ == 24:
                self.enterOuterAlt(localctx, 24)
                self.state = 346
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 345
                    self.randomize()


                self.state = 349
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 348
                    self.points()


                self.state = 352
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 351
                    self.title()


                self.state = 355
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 354
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
            self.state = 367
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuestionParser.TYPE_MC]:
                localctx = QuestionParser.TypeMcContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.match(QuestionParser.TYPE_MC)
                pass
            elif token in [QuestionParser.TYPE_TF]:
                localctx = QuestionParser.TypeTfContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 360
                self.match(QuestionParser.TYPE_TF)
                pass
            elif token in [QuestionParser.TYPE_MS]:
                localctx = QuestionParser.TypeMsContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 361
                self.match(QuestionParser.TYPE_MS)
                pass
            elif token in [QuestionParser.TYPE_MT]:
                localctx = QuestionParser.TypeMtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 362
                self.match(QuestionParser.TYPE_MT)
                pass
            elif token in [QuestionParser.TYPE_ORD]:
                localctx = QuestionParser.TypeOrdContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 363
                self.match(QuestionParser.TYPE_ORD)
                pass
            elif token in [QuestionParser.TYPE_FIB]:
                localctx = QuestionParser.TypeFibContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 364
                self.match(QuestionParser.TYPE_FIB)
                pass
            elif token in [QuestionParser.TYPE_WR]:
                localctx = QuestionParser.TypeWrContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 365
                self.match(QuestionParser.TYPE_WR)
                pass
            elif token in [QuestionParser.TYPE_OTHER]:
                localctx = QuestionParser.TypeOtherContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 366
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
            self.state = 369
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
            self.state = 371
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
            self.state = 375
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuestionParser.RANDOMIZE_TRUE]:
                localctx = QuestionParser.RandomTrueContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.match(QuestionParser.RANDOMIZE_TRUE)
                pass
            elif token in [QuestionParser.RANDOMIZE_FALSE]:
                localctx = QuestionParser.RandomFalseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 374
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
            self.state = 377
            self.question_prefix()
            self.state = 379 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 378
                self.content()
                self.state = 381 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.MEDIA) | (1 << QuestionParser.HYPERLINK) | (1 << QuestionParser.ALL_CHARACTER) | (1 << QuestionParser.ESCAPED_OPEN_BRACKET))) != 0)):
                    break

            self.state = 384
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.FEEDBACK_MARKER:
                self.state = 383
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
            self.state = 386
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
            self.state = 402
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuestionParser.MEDIA]:
                localctx = QuestionParser.MediaContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.match(QuestionParser.MEDIA)
                pass
            elif token in [QuestionParser.HYPERLINK]:
                localctx = QuestionParser.HyperlinkContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 389
                self.match(QuestionParser.HYPERLINK)
                pass
            elif token in [QuestionParser.ESCAPED_OPEN_BRACKET]:
                localctx = QuestionParser.FibAnswerContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 390
                self.match(QuestionParser.ESCAPED_OPEN_BRACKET)
                self.state = 392 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 391
                    self.match(QuestionParser.ALL_CHARACTER)
                    self.state = 394 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==QuestionParser.ALL_CHARACTER):
                        break

                self.state = 396
                self.match(QuestionParser.ESCAPED_CLOSE_BRACKET)
                pass
            elif token in [QuestionParser.ALL_CHARACTER]:
                localctx = QuestionParser.ContentCharactersContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 398 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 397
                        self.match(QuestionParser.ALL_CHARACTER)

                    else:
                        raise NoViableAltException(self)
                    self.state = 400 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,106,self._ctx)

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
            self.state = 404
            self.match(QuestionParser.FEEDBACK_MARKER)
            self.state = 406 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 405
                self.content()
                self.state = 408 
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
            self.state = 423
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,112,self._ctx)
            if la_ == 1:
                localctx = QuestionParser.ListNoAnswerContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 410
                self.match(QuestionParser.START_ANSWER)
                self.state = 412 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 411
                    self.list_item()
                    self.state = 414 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==QuestionParser.LIST_PREFIX):
                        break

                pass

            elif la_ == 2:
                localctx = QuestionParser.ListWithAnswerContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 416
                self.match(QuestionParser.START_ANSWER)
                self.state = 419 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 419
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [QuestionParser.RIGHT_ANSWER]:
                        self.state = 417
                        self.list_answer_item()
                        pass
                    elif token in [QuestionParser.LIST_PREFIX]:
                        self.state = 418
                        self.list_item()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 421 
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
            self.state = 425
            self.list_prefix()
            self.state = 427 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 426
                self.content()
                self.state = 429 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.MEDIA) | (1 << QuestionParser.HYPERLINK) | (1 << QuestionParser.ALL_CHARACTER) | (1 << QuestionParser.ESCAPED_OPEN_BRACKET))) != 0)):
                    break

            self.state = 432
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.FEEDBACK_MARKER:
                self.state = 431
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
            self.state = 434
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
            self.state = 436
            self.answer_prefix()
            self.state = 438 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 437
                self.content()
                self.state = 440 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.MEDIA) | (1 << QuestionParser.HYPERLINK) | (1 << QuestionParser.ALL_CHARACTER) | (1 << QuestionParser.ESCAPED_OPEN_BRACKET))) != 0)):
                    break

            self.state = 443
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.FEEDBACK_MARKER:
                self.state = 442
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
            self.state = 445
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
            self.state = 447
            self.match(QuestionParser.END_ANSWERS)
            self.state = 449 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 448
                self.end_answers_item()
                self.state = 451 
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
            self.state = 453
            self.question_prefix()
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





