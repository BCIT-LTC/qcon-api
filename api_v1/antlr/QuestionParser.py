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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("\u01b4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\7\2")
        buf.write("&\n\2\f\2\16\2)\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\5\3\66\n\3\3\4\3\4\3\5\5\5;\n\5\3\5\5\5>\n")
        buf.write("\5\3\5\5\5A\n\5\3\5\5\5D\n\5\3\5\5\5G\n\5\3\5\5\5J\n\5")
        buf.write("\3\5\5\5M\n\5\3\5\5\5P\n\5\3\5\5\5S\n\5\3\5\5\5V\n\5\3")
        buf.write("\5\5\5Y\n\5\3\5\5\5\\\n\5\3\5\5\5_\n\5\3\5\5\5b\n\5\3")
        buf.write("\5\5\5e\n\5\3\5\5\5h\n\5\3\5\5\5k\n\5\3\5\5\5n\n\5\3\5")
        buf.write("\5\5q\n\5\3\5\5\5t\n\5\3\5\5\5w\n\5\3\5\5\5z\n\5\3\5\5")
        buf.write("\5}\n\5\3\5\5\5\u0080\n\5\3\5\5\5\u0083\n\5\3\5\5\5\u0086")
        buf.write("\n\5\3\5\5\5\u0089\n\5\3\5\5\5\u008c\n\5\3\5\5\5\u008f")
        buf.write("\n\5\3\5\5\5\u0092\n\5\3\5\5\5\u0095\n\5\3\5\5\5\u0098")
        buf.write("\n\5\3\5\5\5\u009b\n\5\3\5\5\5\u009e\n\5\3\5\5\5\u00a1")
        buf.write("\n\5\3\5\5\5\u00a4\n\5\3\5\5\5\u00a7\n\5\3\5\5\5\u00aa")
        buf.write("\n\5\3\5\5\5\u00ad\n\5\3\5\5\5\u00b0\n\5\3\5\5\5\u00b3")
        buf.write("\n\5\3\5\5\5\u00b6\n\5\3\5\5\5\u00b9\n\5\3\5\5\5\u00bc")
        buf.write("\n\5\3\5\5\5\u00bf\n\5\3\5\5\5\u00c2\n\5\3\5\5\5\u00c5")
        buf.write("\n\5\3\5\5\5\u00c8\n\5\3\5\5\5\u00cb\n\5\3\5\5\5\u00ce")
        buf.write("\n\5\3\5\5\5\u00d1\n\5\3\5\5\5\u00d4\n\5\3\5\5\5\u00d7")
        buf.write("\n\5\3\5\5\5\u00da\n\5\3\5\5\5\u00dd\n\5\3\5\5\5\u00e0")
        buf.write("\n\5\3\5\5\5\u00e3\n\5\3\5\5\5\u00e6\n\5\3\5\5\5\u00e9")
        buf.write("\n\5\3\5\5\5\u00ec\n\5\3\5\5\5\u00ef\n\5\3\5\5\5\u00f2")
        buf.write("\n\5\3\5\5\5\u00f5\n\5\3\5\5\5\u00f8\n\5\3\5\5\5\u00fb")
        buf.write("\n\5\3\5\5\5\u00fe\n\5\3\5\5\5\u0101\n\5\3\5\5\5\u0104")
        buf.write("\n\5\3\5\5\5\u0107\n\5\3\5\5\5\u010a\n\5\3\5\5\5\u010d")
        buf.write("\n\5\3\5\5\5\u0110\n\5\3\5\5\5\u0113\n\5\3\5\5\5\u0116")
        buf.write("\n\5\3\5\5\5\u0119\n\5\3\5\5\5\u011c\n\5\3\5\5\5\u011f")
        buf.write("\n\5\3\5\5\5\u0122\n\5\3\5\5\5\u0125\n\5\3\5\5\5\u0128")
        buf.write("\n\5\3\5\5\5\u012b\n\5\3\5\5\5\u012e\n\5\3\5\5\5\u0131")
        buf.write("\n\5\3\5\5\5\u0134\n\5\3\5\5\5\u0137\n\5\3\5\5\5\u013a")
        buf.write("\n\5\3\5\5\5\u013d\n\5\3\5\5\5\u0140\n\5\3\5\5\5\u0143")
        buf.write("\n\5\3\5\5\5\u0146\n\5\3\5\5\5\u0149\n\5\3\5\5\5\u014c")
        buf.write("\n\5\3\5\5\5\u014f\n\5\3\5\5\5\u0152\n\5\3\5\5\5\u0155")
        buf.write("\n\5\3\5\5\5\u0158\n\5\5\5\u015a\n\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\5\6\u0164\n\6\3\7\3\7\3\b\3\b\3\t\3\t\5")
        buf.write("\t\u016c\n\t\3\n\3\n\6\n\u0170\n\n\r\n\16\n\u0171\3\n")
        buf.write("\5\n\u0175\n\n\3\13\3\13\3\f\3\f\3\f\3\f\6\f\u017d\n\f")
        buf.write("\r\f\16\f\u017e\3\f\3\f\6\f\u0183\n\f\r\f\16\f\u0184\5")
        buf.write("\f\u0187\n\f\3\r\3\r\6\r\u018b\n\r\r\r\16\r\u018c\3\16")
        buf.write("\3\16\6\16\u0191\n\16\r\16\16\16\u0192\3\16\3\16\3\16")
        buf.write("\6\16\u0198\n\16\r\16\16\16\u0199\5\16\u019c\n\16\3\17")
        buf.write("\3\17\6\17\u01a0\n\17\r\17\16\17\u01a1\3\17\5\17\u01a5")
        buf.write("\n\17\3\20\3\20\3\21\3\21\6\21\u01ab\n\21\r\21\16\21\u01ac")
        buf.write("\3\21\5\21\u01b0\n\21\3\22\3\22\3\22\2\2\23\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"\2\2\2\u0233\2\'\3\2\2")
        buf.write("\2\4\65\3\2\2\2\6\67\3\2\2\2\b\u0159\3\2\2\2\n\u0163\3")
        buf.write("\2\2\2\f\u0165\3\2\2\2\16\u0167\3\2\2\2\20\u016b\3\2\2")
        buf.write("\2\22\u016d\3\2\2\2\24\u0176\3\2\2\2\26\u0186\3\2\2\2")
        buf.write("\30\u0188\3\2\2\2\32\u019b\3\2\2\2\34\u019d\3\2\2\2\36")
        buf.write("\u01a6\3\2\2\2 \u01a8\3\2\2\2\"\u01b1\3\2\2\2$&\5\4\3")
        buf.write("\2%$\3\2\2\2&)\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2(*\3\2\2\2")
        buf.write(")\'\3\2\2\2*+\7\2\2\3+\3\3\2\2\2,-\5\6\4\2-.\5\b\5\2.")
        buf.write("/\5\22\n\2/\60\5\32\16\2\60\66\3\2\2\2\61\62\5\6\4\2\62")
        buf.write("\63\5\b\5\2\63\64\5\22\n\2\64\66\3\2\2\2\65,\3\2\2\2\65")
        buf.write("\61\3\2\2\2\66\5\3\2\2\2\678\7\3\2\28\7\3\2\2\29;\5\n")
        buf.write("\6\2:9\3\2\2\2:;\3\2\2\2;=\3\2\2\2<>\5\f\7\2=<\3\2\2\2")
        buf.write("=>\3\2\2\2>@\3\2\2\2?A\5\16\b\2@?\3\2\2\2@A\3\2\2\2AC")
        buf.write("\3\2\2\2BD\5\20\t\2CB\3\2\2\2CD\3\2\2\2D\u015a\3\2\2\2")
        buf.write("EG\5\n\6\2FE\3\2\2\2FG\3\2\2\2GI\3\2\2\2HJ\5\f\7\2IH\3")
        buf.write("\2\2\2IJ\3\2\2\2JL\3\2\2\2KM\5\20\t\2LK\3\2\2\2LM\3\2")
        buf.write("\2\2MO\3\2\2\2NP\5\16\b\2ON\3\2\2\2OP\3\2\2\2P\u015a\3")
        buf.write("\2\2\2QS\5\n\6\2RQ\3\2\2\2RS\3\2\2\2SU\3\2\2\2TV\5\16")
        buf.write("\b\2UT\3\2\2\2UV\3\2\2\2VX\3\2\2\2WY\5\f\7\2XW\3\2\2\2")
        buf.write("XY\3\2\2\2Y[\3\2\2\2Z\\\5\20\t\2[Z\3\2\2\2[\\\3\2\2\2")
        buf.write("\\\u015a\3\2\2\2]_\5\n\6\2^]\3\2\2\2^_\3\2\2\2_a\3\2\2")
        buf.write("\2`b\5\16\b\2a`\3\2\2\2ab\3\2\2\2bd\3\2\2\2ce\5\20\t\2")
        buf.write("dc\3\2\2\2de\3\2\2\2eg\3\2\2\2fh\5\f\7\2gf\3\2\2\2gh\3")
        buf.write("\2\2\2h\u015a\3\2\2\2ik\5\n\6\2ji\3\2\2\2jk\3\2\2\2km")
        buf.write("\3\2\2\2ln\5\20\t\2ml\3\2\2\2mn\3\2\2\2np\3\2\2\2oq\5")
        buf.write("\f\7\2po\3\2\2\2pq\3\2\2\2qs\3\2\2\2rt\5\16\b\2sr\3\2")
        buf.write("\2\2st\3\2\2\2t\u015a\3\2\2\2uw\5\n\6\2vu\3\2\2\2vw\3")
        buf.write("\2\2\2wy\3\2\2\2xz\5\20\t\2yx\3\2\2\2yz\3\2\2\2z|\3\2")
        buf.write("\2\2{}\5\16\b\2|{\3\2\2\2|}\3\2\2\2}\177\3\2\2\2~\u0080")
        buf.write("\5\f\7\2\177~\3\2\2\2\177\u0080\3\2\2\2\u0080\u015a\3")
        buf.write("\2\2\2\u0081\u0083\5\f\7\2\u0082\u0081\3\2\2\2\u0082\u0083")
        buf.write("\3\2\2\2\u0083\u0085\3\2\2\2\u0084\u0086\5\n\6\2\u0085")
        buf.write("\u0084\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0088\3\2\2\2")
        buf.write("\u0087\u0089\5\16\b\2\u0088\u0087\3\2\2\2\u0088\u0089")
        buf.write("\3\2\2\2\u0089\u008b\3\2\2\2\u008a\u008c\5\20\t\2\u008b")
        buf.write("\u008a\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u015a\3\2\2\2")
        buf.write("\u008d\u008f\5\f\7\2\u008e\u008d\3\2\2\2\u008e\u008f\3")
        buf.write("\2\2\2\u008f\u0091\3\2\2\2\u0090\u0092\5\n\6\2\u0091\u0090")
        buf.write("\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0094\3\2\2\2\u0093")
        buf.write("\u0095\5\20\t\2\u0094\u0093\3\2\2\2\u0094\u0095\3\2\2")
        buf.write("\2\u0095\u0097\3\2\2\2\u0096\u0098\5\16\b\2\u0097\u0096")
        buf.write("\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u015a\3\2\2\2\u0099")
        buf.write("\u009b\5\f\7\2\u009a\u0099\3\2\2\2\u009a\u009b\3\2\2\2")
        buf.write("\u009b\u009d\3\2\2\2\u009c\u009e\5\16\b\2\u009d\u009c")
        buf.write("\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u00a0\3\2\2\2\u009f")
        buf.write("\u00a1\5\n\6\2\u00a0\u009f\3\2\2\2\u00a0\u00a1\3\2\2\2")
        buf.write("\u00a1\u00a3\3\2\2\2\u00a2\u00a4\5\20\t\2\u00a3\u00a2")
        buf.write("\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u015a\3\2\2\2\u00a5")
        buf.write("\u00a7\5\f\7\2\u00a6\u00a5\3\2\2\2\u00a6\u00a7\3\2\2\2")
        buf.write("\u00a7\u00a9\3\2\2\2\u00a8\u00aa\5\16\b\2\u00a9\u00a8")
        buf.write("\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ac\3\2\2\2\u00ab")
        buf.write("\u00ad\5\20\t\2\u00ac\u00ab\3\2\2\2\u00ac\u00ad\3\2\2")
        buf.write("\2\u00ad\u00af\3\2\2\2\u00ae\u00b0\5\n\6\2\u00af\u00ae")
        buf.write("\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u015a\3\2\2\2\u00b1")
        buf.write("\u00b3\5\f\7\2\u00b2\u00b1\3\2\2\2\u00b2\u00b3\3\2\2\2")
        buf.write("\u00b3\u00b5\3\2\2\2\u00b4\u00b6\5\20\t\2\u00b5\u00b4")
        buf.write("\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b8\3\2\2\2\u00b7")
        buf.write("\u00b9\5\n\6\2\u00b8\u00b7\3\2\2\2\u00b8\u00b9\3\2\2\2")
        buf.write("\u00b9\u00bb\3\2\2\2\u00ba\u00bc\5\16\b\2\u00bb\u00ba")
        buf.write("\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u015a\3\2\2\2\u00bd")
        buf.write("\u00bf\5\f\7\2\u00be\u00bd\3\2\2\2\u00be\u00bf\3\2\2\2")
        buf.write("\u00bf\u00c1\3\2\2\2\u00c0\u00c2\5\20\t\2\u00c1\u00c0")
        buf.write("\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c4\3\2\2\2\u00c3")
        buf.write("\u00c5\5\16\b\2\u00c4\u00c3\3\2\2\2\u00c4\u00c5\3\2\2")
        buf.write("\2\u00c5\u00c7\3\2\2\2\u00c6\u00c8\5\n\6\2\u00c7\u00c6")
        buf.write("\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u015a\3\2\2\2\u00c9")
        buf.write("\u00cb\5\16\b\2\u00ca\u00c9\3\2\2\2\u00ca\u00cb\3\2\2")
        buf.write("\2\u00cb\u00cd\3\2\2\2\u00cc\u00ce\5\n\6\2\u00cd\u00cc")
        buf.write("\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00d0\3\2\2\2\u00cf")
        buf.write("\u00d1\5\f\7\2\u00d0\u00cf\3\2\2\2\u00d0\u00d1\3\2\2\2")
        buf.write("\u00d1\u00d3\3\2\2\2\u00d2\u00d4\5\20\t\2\u00d3\u00d2")
        buf.write("\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u015a\3\2\2\2\u00d5")
        buf.write("\u00d7\5\16\b\2\u00d6\u00d5\3\2\2\2\u00d6\u00d7\3\2\2")
        buf.write("\2\u00d7\u00d9\3\2\2\2\u00d8\u00da\5\n\6\2\u00d9\u00d8")
        buf.write("\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00dc\3\2\2\2\u00db")
        buf.write("\u00dd\5\20\t\2\u00dc\u00db\3\2\2\2\u00dc\u00dd\3\2\2")
        buf.write("\2\u00dd\u00df\3\2\2\2\u00de\u00e0\5\f\7\2\u00df\u00de")
        buf.write("\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u015a\3\2\2\2\u00e1")
        buf.write("\u00e3\5\16\b\2\u00e2\u00e1\3\2\2\2\u00e2\u00e3\3\2\2")
        buf.write("\2\u00e3\u00e5\3\2\2\2\u00e4\u00e6\5\f\7\2\u00e5\u00e4")
        buf.write("\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e8\3\2\2\2\u00e7")
        buf.write("\u00e9\5\n\6\2\u00e8\u00e7\3\2\2\2\u00e8\u00e9\3\2\2\2")
        buf.write("\u00e9\u00eb\3\2\2\2\u00ea\u00ec\5\20\t\2\u00eb\u00ea")
        buf.write("\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u015a\3\2\2\2\u00ed")
        buf.write("\u00ef\5\16\b\2\u00ee\u00ed\3\2\2\2\u00ee\u00ef\3\2\2")
        buf.write("\2\u00ef\u00f1\3\2\2\2\u00f0\u00f2\5\f\7\2\u00f1\u00f0")
        buf.write("\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f4\3\2\2\2\u00f3")
        buf.write("\u00f5\5\20\t\2\u00f4\u00f3\3\2\2\2\u00f4\u00f5\3\2\2")
        buf.write("\2\u00f5\u00f7\3\2\2\2\u00f6\u00f8\5\n\6\2\u00f7\u00f6")
        buf.write("\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u015a\3\2\2\2\u00f9")
        buf.write("\u00fb\5\16\b\2\u00fa\u00f9\3\2\2\2\u00fa\u00fb\3\2\2")
        buf.write("\2\u00fb\u00fd\3\2\2\2\u00fc\u00fe\5\20\t\2\u00fd\u00fc")
        buf.write("\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u0100\3\2\2\2\u00ff")
        buf.write("\u0101\5\n\6\2\u0100\u00ff\3\2\2\2\u0100\u0101\3\2\2\2")
        buf.write("\u0101\u0103\3\2\2\2\u0102\u0104\5\f\7\2\u0103\u0102\3")
        buf.write("\2\2\2\u0103\u0104\3\2\2\2\u0104\u015a\3\2\2\2\u0105\u0107")
        buf.write("\5\16\b\2\u0106\u0105\3\2\2\2\u0106\u0107\3\2\2\2\u0107")
        buf.write("\u0109\3\2\2\2\u0108\u010a\5\20\t\2\u0109\u0108\3\2\2")
        buf.write("\2\u0109\u010a\3\2\2\2\u010a\u010c\3\2\2\2\u010b\u010d")
        buf.write("\5\f\7\2\u010c\u010b\3\2\2\2\u010c\u010d\3\2\2\2\u010d")
        buf.write("\u010f\3\2\2\2\u010e\u0110\5\n\6\2\u010f\u010e\3\2\2\2")
        buf.write("\u010f\u0110\3\2\2\2\u0110\u015a\3\2\2\2\u0111\u0113\5")
        buf.write("\20\t\2\u0112\u0111\3\2\2\2\u0112\u0113\3\2\2\2\u0113")
        buf.write("\u0115\3\2\2\2\u0114\u0116\5\n\6\2\u0115\u0114\3\2\2\2")
        buf.write("\u0115\u0116\3\2\2\2\u0116\u0118\3\2\2\2\u0117\u0119\5")
        buf.write("\f\7\2\u0118\u0117\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011b")
        buf.write("\3\2\2\2\u011a\u011c\5\16\b\2\u011b\u011a\3\2\2\2\u011b")
        buf.write("\u011c\3\2\2\2\u011c\u015a\3\2\2\2\u011d\u011f\5\20\t")
        buf.write("\2\u011e\u011d\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0121")
        buf.write("\3\2\2\2\u0120\u0122\5\n\6\2\u0121\u0120\3\2\2\2\u0121")
        buf.write("\u0122\3\2\2\2\u0122\u0124\3\2\2\2\u0123\u0125\5\16\b")
        buf.write("\2\u0124\u0123\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0127")
        buf.write("\3\2\2\2\u0126\u0128\5\f\7\2\u0127\u0126\3\2\2\2\u0127")
        buf.write("\u0128\3\2\2\2\u0128\u015a\3\2\2\2\u0129\u012b\5\20\t")
        buf.write("\2\u012a\u0129\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012d")
        buf.write("\3\2\2\2\u012c\u012e\5\f\7\2\u012d\u012c\3\2\2\2\u012d")
        buf.write("\u012e\3\2\2\2\u012e\u0130\3\2\2\2\u012f\u0131\5\n\6\2")
        buf.write("\u0130\u012f\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u0133\3")
        buf.write("\2\2\2\u0132\u0134\5\16\b\2\u0133\u0132\3\2\2\2\u0133")
        buf.write("\u0134\3\2\2\2\u0134\u015a\3\2\2\2\u0135\u0137\5\20\t")
        buf.write("\2\u0136\u0135\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0139")
        buf.write("\3\2\2\2\u0138\u013a\5\f\7\2\u0139\u0138\3\2\2\2\u0139")
        buf.write("\u013a\3\2\2\2\u013a\u013c\3\2\2\2\u013b\u013d\5\16\b")
        buf.write("\2\u013c\u013b\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u013f")
        buf.write("\3\2\2\2\u013e\u0140\5\n\6\2\u013f\u013e\3\2\2\2\u013f")
        buf.write("\u0140\3\2\2\2\u0140\u015a\3\2\2\2\u0141\u0143\5\20\t")
        buf.write("\2\u0142\u0141\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0145")
        buf.write("\3\2\2\2\u0144\u0146\5\16\b\2\u0145\u0144\3\2\2\2\u0145")
        buf.write("\u0146\3\2\2\2\u0146\u0148\3\2\2\2\u0147\u0149\5\n\6\2")
        buf.write("\u0148\u0147\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014b\3")
        buf.write("\2\2\2\u014a\u014c\5\f\7\2\u014b\u014a\3\2\2\2\u014b\u014c")
        buf.write("\3\2\2\2\u014c\u015a\3\2\2\2\u014d\u014f\5\20\t\2\u014e")
        buf.write("\u014d\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0151\3\2\2\2")
        buf.write("\u0150\u0152\5\16\b\2\u0151\u0150\3\2\2\2\u0151\u0152")
        buf.write("\3\2\2\2\u0152\u0154\3\2\2\2\u0153\u0155\5\f\7\2\u0154")
        buf.write("\u0153\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0157\3\2\2\2")
        buf.write("\u0156\u0158\5\n\6\2\u0157\u0156\3\2\2\2\u0157\u0158\3")
        buf.write("\2\2\2\u0158\u015a\3\2\2\2\u0159:\3\2\2\2\u0159F\3\2\2")
        buf.write("\2\u0159R\3\2\2\2\u0159^\3\2\2\2\u0159j\3\2\2\2\u0159")
        buf.write("v\3\2\2\2\u0159\u0082\3\2\2\2\u0159\u008e\3\2\2\2\u0159")
        buf.write("\u009a\3\2\2\2\u0159\u00a6\3\2\2\2\u0159\u00b2\3\2\2\2")
        buf.write("\u0159\u00be\3\2\2\2\u0159\u00ca\3\2\2\2\u0159\u00d6\3")
        buf.write("\2\2\2\u0159\u00e2\3\2\2\2\u0159\u00ee\3\2\2\2\u0159\u00fa")
        buf.write("\3\2\2\2\u0159\u0106\3\2\2\2\u0159\u0112\3\2\2\2\u0159")
        buf.write("\u011e\3\2\2\2\u0159\u012a\3\2\2\2\u0159\u0136\3\2\2\2")
        buf.write("\u0159\u0142\3\2\2\2\u0159\u014e\3\2\2\2\u015a\t\3\2\2")
        buf.write("\2\u015b\u0164\7\16\2\2\u015c\u0164\7\17\2\2\u015d\u0164")
        buf.write("\7\20\2\2\u015e\u0164\7\21\2\2\u015f\u0164\7\22\2\2\u0160")
        buf.write("\u0164\7\23\2\2\u0161\u0164\7\24\2\2\u0162\u0164\7\25")
        buf.write("\2\2\u0163\u015b\3\2\2\2\u0163\u015c\3\2\2\2\u0163\u015d")
        buf.write("\3\2\2\2\u0163\u015e\3\2\2\2\u0163\u015f\3\2\2\2\u0163")
        buf.write("\u0160\3\2\2\2\u0163\u0161\3\2\2\2\u0163\u0162\3\2\2\2")
        buf.write("\u0164\13\3\2\2\2\u0165\u0166\7\n\2\2\u0166\r\3\2\2\2")
        buf.write("\u0167\u0168\7\13\2\2\u0168\17\3\2\2\2\u0169\u016c\7\f")
        buf.write("\2\2\u016a\u016c\7\r\2\2\u016b\u0169\3\2\2\2\u016b\u016a")
        buf.write("\3\2\2\2\u016c\21\3\2\2\2\u016d\u016f\5\24\13\2\u016e")
        buf.write("\u0170\5\26\f\2\u016f\u016e\3\2\2\2\u0170\u0171\3\2\2")
        buf.write("\2\u0171\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0174")
        buf.write("\3\2\2\2\u0173\u0175\5\30\r\2\u0174\u0173\3\2\2\2\u0174")
        buf.write("\u0175\3\2\2\2\u0175\23\3\2\2\2\u0176\u0177\7\26\2\2\u0177")
        buf.write("\25\3\2\2\2\u0178\u0187\7\5\2\2\u0179\u0187\7\6\2\2\u017a")
        buf.write("\u017c\7\b\2\2\u017b\u017d\7\7\2\2\u017c\u017b\3\2\2\2")
        buf.write("\u017d\u017e\3\2\2\2\u017e\u017c\3\2\2\2\u017e\u017f\3")
        buf.write("\2\2\2\u017f\u0180\3\2\2\2\u0180\u0187\7\t\2\2\u0181\u0183")
        buf.write("\7\7\2\2\u0182\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184")
        buf.write("\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0187\3\2\2\2")
        buf.write("\u0186\u0178\3\2\2\2\u0186\u0179\3\2\2\2\u0186\u017a\3")
        buf.write("\2\2\2\u0186\u0182\3\2\2\2\u0187\27\3\2\2\2\u0188\u018a")
        buf.write("\7\4\2\2\u0189\u018b\5\26\f\2\u018a\u0189\3\2\2\2\u018b")
        buf.write("\u018c\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d\3\2\2\2")
        buf.write("\u018d\31\3\2\2\2\u018e\u0190\7\27\2\2\u018f\u0191\5\34")
        buf.write("\17\2\u0190\u018f\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0190")
        buf.write("\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u019c\3\2\2\2\u0194")
        buf.write("\u0197\7\27\2\2\u0195\u0198\5 \21\2\u0196\u0198\5\34\17")
        buf.write("\2\u0197\u0195\3\2\2\2\u0197\u0196\3\2\2\2\u0198\u0199")
        buf.write("\3\2\2\2\u0199\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019a")
        buf.write("\u019c\3\2\2\2\u019b\u018e\3\2\2\2\u019b\u0194\3\2\2\2")
        buf.write("\u019c\33\3\2\2\2\u019d\u019f\5\36\20\2\u019e\u01a0\5")
        buf.write("\26\f\2\u019f\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1")
        buf.write("\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a4\3\2\2\2")
        buf.write("\u01a3\u01a5\5\30\r\2\u01a4\u01a3\3\2\2\2\u01a4\u01a5")
        buf.write("\3\2\2\2\u01a5\35\3\2\2\2\u01a6\u01a7\7\31\2\2\u01a7\37")
        buf.write("\3\2\2\2\u01a8\u01aa\5\"\22\2\u01a9\u01ab\5\26\f\2\u01aa")
        buf.write("\u01a9\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01aa\3\2\2\2")
        buf.write("\u01ac\u01ad\3\2\2\2\u01ad\u01af\3\2\2\2\u01ae\u01b0\5")
        buf.write("\30\r\2\u01af\u01ae\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0")
        buf.write("!\3\2\2\2\u01b1\u01b2\7\30\2\2\u01b2#\3\2\2\2u\'\65:=")
        buf.write("@CFILORUX[^adgjmpsvy|\177\u0082\u0085\u0088\u008b\u008e")
        buf.write("\u0091\u0094\u0097\u009a\u009d\u00a0\u00a3\u00a6\u00a9")
        buf.write("\u00ac\u00af\u00b2\u00b5\u00b8\u00bb\u00be\u00c1\u00c4")
        buf.write("\u00c7\u00ca\u00cd\u00d0\u00d3\u00d6\u00d9\u00dc\u00df")
        buf.write("\u00e2\u00e5\u00e8\u00eb\u00ee\u00f1\u00f4\u00f7\u00fa")
        buf.write("\u00fd\u0100\u0103\u0106\u0109\u010c\u010f\u0112\u0115")
        buf.write("\u0118\u011b\u011e\u0121\u0124\u0127\u012a\u012d\u0130")
        buf.write("\u0133\u0136\u0139\u013c\u013f\u0142\u0145\u0148\u014b")
        buf.write("\u014e\u0151\u0154\u0157\u0159\u0163\u016b\u0171\u0174")
        buf.write("\u017e\u0184\u0186\u018c\u0192\u0197\u0199\u019b\u01a1")
        buf.write("\u01a4\u01ac\u01af")
        return buf.getvalue()


class QuestionParser ( Parser ):

    grammarFileName = "QuestionParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "START_QUESTION", "FEEDBACK_MARKER", 
                      "MEDIA", "HYPERLINK", "ALL_CHARACTER", "ESCAPED_OPEN_BRACKET", 
                      "ESCAPED_CLOSE_BRACKET", "TITLE", "POINTS", "RANDOMIZE_TRUE", 
                      "RANDOMIZE_FALSE", "TYPE_MC", "TYPE_TF", "TYPE_MS", 
                      "TYPE_MT", "TYPE_ORD", "TYPE_FIB", "TYPE_WR", "TYPE_OTHER", 
                      "QUESTION_PREFIX", "START_ANSWER", "RIGHT_ANSWER", 
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

    ruleNames =  [ "parse_question", "question", "start_question", "question_header", 
                   "question_type", "title", "points", "randomize", "question_body", 
                   "question_prefix", "content", "feedback", "answer_list", 
                   "list_item", "list_prefix", "list_answer_item", "answer_prefix" ]

    EOF = Token.EOF
    START_QUESTION=1
    FEEDBACK_MARKER=2
    MEDIA=3
    HYPERLINK=4
    ALL_CHARACTER=5
    ESCAPED_OPEN_BRACKET=6
    ESCAPED_CLOSE_BRACKET=7
    TITLE=8
    POINTS=9
    RANDOMIZE_TRUE=10
    RANDOMIZE_FALSE=11
    TYPE_MC=12
    TYPE_TF=13
    TYPE_MS=14
    TYPE_MT=15
    TYPE_ORD=16
    TYPE_FIB=17
    TYPE_WR=18
    TYPE_OTHER=19
    QUESTION_PREFIX=20
    START_ANSWER=21
    RIGHT_ANSWER=22
    LIST_PREFIX=23

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
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==QuestionParser.START_QUESTION:
                self.state = 34
                self.question()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
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
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.start_question()
                self.state = 43
                self.question_header()
                self.state = 44
                self.question_body()
                self.state = 45
                self.answer_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.start_question()
                self.state = 48
                self.question_header()
                self.state = 49
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
            self.state = 53
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
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,98,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 55
                    self.question_type()


                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 58
                    self.title()


                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 61
                    self.points()


                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 64
                    self.randomize()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 67
                    self.question_type()


                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 70
                    self.title()


                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 73
                    self.randomize()


                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 76
                    self.points()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 79
                    self.question_type()


                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 82
                    self.points()


                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 85
                    self.title()


                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 88
                    self.randomize()


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 91
                    self.question_type()


                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 94
                    self.points()


                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 97
                    self.randomize()


                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 100
                    self.title()


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 103
                    self.question_type()


                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 106
                    self.randomize()


                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 109
                    self.title()


                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 112
                    self.points()


                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 115
                    self.question_type()


                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 118
                    self.randomize()


                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 121
                    self.points()


                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 124
                    self.title()


                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 127
                    self.title()


                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 130
                    self.question_type()


                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 133
                    self.points()


                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 136
                    self.randomize()


                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 139
                    self.title()


                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 142
                    self.question_type()


                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 145
                    self.randomize()


                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 148
                    self.points()


                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 151
                    self.title()


                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 154
                    self.points()


                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 157
                    self.question_type()


                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 160
                    self.randomize()


                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 163
                    self.title()


                self.state = 167
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 166
                    self.points()


                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 169
                    self.randomize()


                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 172
                    self.question_type()


                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 175
                    self.title()


                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 178
                    self.randomize()


                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 181
                    self.question_type()


                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 184
                    self.points()


                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 187
                    self.title()


                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 190
                    self.randomize()


                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 193
                    self.points()


                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 196
                    self.question_type()


                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 199
                    self.points()


                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 202
                    self.question_type()


                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 205
                    self.title()


                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 208
                    self.randomize()


                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 211
                    self.points()


                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 214
                    self.question_type()


                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 217
                    self.randomize()


                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 220
                    self.title()


                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 223
                    self.points()


                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 226
                    self.title()


                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 229
                    self.question_type()


                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 232
                    self.randomize()


                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 236
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 235
                    self.points()


                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 238
                    self.title()


                self.state = 242
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 241
                    self.randomize()


                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 244
                    self.question_type()


                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 247
                    self.points()


                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 250
                    self.randomize()


                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 253
                    self.question_type()


                self.state = 257
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 256
                    self.title()


                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 259
                    self.points()


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


                self.state = 269
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 268
                    self.question_type()


                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 271
                    self.randomize()


                self.state = 275
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 274
                    self.question_type()


                self.state = 278
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 277
                    self.title()


                self.state = 281
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 280
                    self.points()


                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 284
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 283
                    self.randomize()


                self.state = 287
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 286
                    self.question_type()


                self.state = 290
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 289
                    self.points()


                self.state = 293
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 292
                    self.title()


                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)
                self.state = 296
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 295
                    self.randomize()


                self.state = 299
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 298
                    self.title()


                self.state = 302
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 301
                    self.question_type()


                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 304
                    self.points()


                pass

            elif la_ == 22:
                self.enterOuterAlt(localctx, 22)
                self.state = 308
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 307
                    self.randomize()


                self.state = 311
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 310
                    self.title()


                self.state = 314
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 313
                    self.points()


                self.state = 317
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 316
                    self.question_type()


                pass

            elif la_ == 23:
                self.enterOuterAlt(localctx, 23)
                self.state = 320
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 319
                    self.randomize()


                self.state = 323
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 322
                    self.points()


                self.state = 326
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 325
                    self.question_type()


                self.state = 329
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 328
                    self.title()


                pass

            elif la_ == 24:
                self.enterOuterAlt(localctx, 24)
                self.state = 332
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 331
                    self.randomize()


                self.state = 335
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 334
                    self.points()


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
            self.state = 353
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuestionParser.TYPE_MC]:
                localctx = QuestionParser.TypeMcContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.match(QuestionParser.TYPE_MC)
                pass
            elif token in [QuestionParser.TYPE_TF]:
                localctx = QuestionParser.TypeTfContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.match(QuestionParser.TYPE_TF)
                pass
            elif token in [QuestionParser.TYPE_MS]:
                localctx = QuestionParser.TypeMsContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 347
                self.match(QuestionParser.TYPE_MS)
                pass
            elif token in [QuestionParser.TYPE_MT]:
                localctx = QuestionParser.TypeMtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 348
                self.match(QuestionParser.TYPE_MT)
                pass
            elif token in [QuestionParser.TYPE_ORD]:
                localctx = QuestionParser.TypeOrdContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 349
                self.match(QuestionParser.TYPE_ORD)
                pass
            elif token in [QuestionParser.TYPE_FIB]:
                localctx = QuestionParser.TypeFibContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 350
                self.match(QuestionParser.TYPE_FIB)
                pass
            elif token in [QuestionParser.TYPE_WR]:
                localctx = QuestionParser.TypeWrContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 351
                self.match(QuestionParser.TYPE_WR)
                pass
            elif token in [QuestionParser.TYPE_OTHER]:
                localctx = QuestionParser.TypeOtherContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 352
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
            self.state = 355
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
            self.state = 357
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
            self.state = 361
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuestionParser.RANDOMIZE_TRUE]:
                localctx = QuestionParser.RandomTrueContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.match(QuestionParser.RANDOMIZE_TRUE)
                pass
            elif token in [QuestionParser.RANDOMIZE_FALSE]:
                localctx = QuestionParser.RandomFalseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 360
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
            self.state = 363
            self.question_prefix()
            self.state = 365 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 364
                self.content()
                self.state = 367 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.MEDIA) | (1 << QuestionParser.HYPERLINK) | (1 << QuestionParser.ALL_CHARACTER) | (1 << QuestionParser.ESCAPED_OPEN_BRACKET))) != 0)):
                    break

            self.state = 370
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.FEEDBACK_MARKER:
                self.state = 369
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
            self.state = 372
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
            self.state = 388
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuestionParser.MEDIA]:
                localctx = QuestionParser.MediaContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.match(QuestionParser.MEDIA)
                pass
            elif token in [QuestionParser.HYPERLINK]:
                localctx = QuestionParser.HyperlinkContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 375
                self.match(QuestionParser.HYPERLINK)
                pass
            elif token in [QuestionParser.ESCAPED_OPEN_BRACKET]:
                localctx = QuestionParser.FibAnswerContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 376
                self.match(QuestionParser.ESCAPED_OPEN_BRACKET)
                self.state = 378 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 377
                    self.match(QuestionParser.ALL_CHARACTER)
                    self.state = 380 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==QuestionParser.ALL_CHARACTER):
                        break

                self.state = 382
                self.match(QuestionParser.ESCAPED_CLOSE_BRACKET)
                pass
            elif token in [QuestionParser.ALL_CHARACTER]:
                localctx = QuestionParser.ContentCharactersContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 384 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 383
                        self.match(QuestionParser.ALL_CHARACTER)

                    else:
                        raise NoViableAltException(self)
                    self.state = 386 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,104,self._ctx)

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
            self.state = 390
            self.match(QuestionParser.FEEDBACK_MARKER)
            self.state = 392 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 391
                self.content()
                self.state = 394 
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
            self.state = 409
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,110,self._ctx)
            if la_ == 1:
                localctx = QuestionParser.ListNoAnswerContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.match(QuestionParser.START_ANSWER)
                self.state = 398 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 397
                    self.list_item()
                    self.state = 400 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==QuestionParser.LIST_PREFIX):
                        break

                pass

            elif la_ == 2:
                localctx = QuestionParser.ListWithAnswerContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 402
                self.match(QuestionParser.START_ANSWER)
                self.state = 405 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 405
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [QuestionParser.RIGHT_ANSWER]:
                        self.state = 403
                        self.list_answer_item()
                        pass
                    elif token in [QuestionParser.LIST_PREFIX]:
                        self.state = 404
                        self.list_item()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 407 
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
            self.state = 411
            self.list_prefix()
            self.state = 413 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 412
                self.content()
                self.state = 415 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.MEDIA) | (1 << QuestionParser.HYPERLINK) | (1 << QuestionParser.ALL_CHARACTER) | (1 << QuestionParser.ESCAPED_OPEN_BRACKET))) != 0)):
                    break

            self.state = 418
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.FEEDBACK_MARKER:
                self.state = 417
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
            self.state = 420
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
            self.state = 422
            self.answer_prefix()
            self.state = 424 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 423
                self.content()
                self.state = 426 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.MEDIA) | (1 << QuestionParser.HYPERLINK) | (1 << QuestionParser.ALL_CHARACTER) | (1 << QuestionParser.ESCAPED_OPEN_BRACKET))) != 0)):
                    break

            self.state = 429
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.FEEDBACK_MARKER:
                self.state = 428
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
            self.state = 431
            self.match(QuestionParser.RIGHT_ANSWER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





