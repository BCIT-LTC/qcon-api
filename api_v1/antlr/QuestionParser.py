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
        buf.write("\u01ad\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\5\3-\n\3\3\4\5\4\60\n\4\3\4\5\4")
        buf.write("\63\n\4\3\4\5\4\66\n\4\3\4\5\49\n\4\3\4\5\4<\n\4\3\4\5")
        buf.write("\4?\n\4\3\4\5\4B\n\4\3\4\5\4E\n\4\3\4\5\4H\n\4\3\4\5\4")
        buf.write("K\n\4\3\4\5\4N\n\4\3\4\5\4Q\n\4\3\4\5\4T\n\4\3\4\5\4W")
        buf.write("\n\4\3\4\5\4Z\n\4\3\4\5\4]\n\4\3\4\5\4`\n\4\3\4\5\4c\n")
        buf.write("\4\3\4\5\4f\n\4\3\4\5\4i\n\4\3\4\5\4l\n\4\3\4\5\4o\n\4")
        buf.write("\3\4\5\4r\n\4\3\4\5\4u\n\4\3\4\5\4x\n\4\3\4\5\4{\n\4\3")
        buf.write("\4\5\4~\n\4\3\4\5\4\u0081\n\4\3\4\5\4\u0084\n\4\3\4\5")
        buf.write("\4\u0087\n\4\3\4\5\4\u008a\n\4\3\4\5\4\u008d\n\4\3\4\5")
        buf.write("\4\u0090\n\4\3\4\5\4\u0093\n\4\3\4\5\4\u0096\n\4\3\4\5")
        buf.write("\4\u0099\n\4\3\4\5\4\u009c\n\4\3\4\5\4\u009f\n\4\3\4\5")
        buf.write("\4\u00a2\n\4\3\4\5\4\u00a5\n\4\3\4\5\4\u00a8\n\4\3\4\5")
        buf.write("\4\u00ab\n\4\3\4\5\4\u00ae\n\4\3\4\5\4\u00b1\n\4\3\4\5")
        buf.write("\4\u00b4\n\4\3\4\5\4\u00b7\n\4\3\4\5\4\u00ba\n\4\3\4\5")
        buf.write("\4\u00bd\n\4\3\4\5\4\u00c0\n\4\3\4\5\4\u00c3\n\4\3\4\5")
        buf.write("\4\u00c6\n\4\3\4\5\4\u00c9\n\4\3\4\5\4\u00cc\n\4\3\4\5")
        buf.write("\4\u00cf\n\4\3\4\5\4\u00d2\n\4\3\4\5\4\u00d5\n\4\3\4\5")
        buf.write("\4\u00d8\n\4\3\4\5\4\u00db\n\4\3\4\5\4\u00de\n\4\3\4\5")
        buf.write("\4\u00e1\n\4\3\4\5\4\u00e4\n\4\3\4\5\4\u00e7\n\4\3\4\5")
        buf.write("\4\u00ea\n\4\3\4\5\4\u00ed\n\4\3\4\5\4\u00f0\n\4\3\4\5")
        buf.write("\4\u00f3\n\4\3\4\5\4\u00f6\n\4\3\4\5\4\u00f9\n\4\3\4\5")
        buf.write("\4\u00fc\n\4\3\4\5\4\u00ff\n\4\3\4\5\4\u0102\n\4\3\4\5")
        buf.write("\4\u0105\n\4\3\4\5\4\u0108\n\4\3\4\5\4\u010b\n\4\3\4\5")
        buf.write("\4\u010e\n\4\3\4\5\4\u0111\n\4\3\4\5\4\u0114\n\4\3\4\5")
        buf.write("\4\u0117\n\4\3\4\5\4\u011a\n\4\3\4\5\4\u011d\n\4\3\4\5")
        buf.write("\4\u0120\n\4\3\4\5\4\u0123\n\4\3\4\5\4\u0126\n\4\3\4\5")
        buf.write("\4\u0129\n\4\3\4\5\4\u012c\n\4\3\4\5\4\u012f\n\4\3\4\5")
        buf.write("\4\u0132\n\4\3\4\5\4\u0135\n\4\3\4\5\4\u0138\n\4\3\4\5")
        buf.write("\4\u013b\n\4\3\4\5\4\u013e\n\4\3\4\5\4\u0141\n\4\3\4\5")
        buf.write("\4\u0144\n\4\3\4\5\4\u0147\n\4\3\4\5\4\u014a\n\4\3\4\5")
        buf.write("\4\u014d\n\4\5\4\u014f\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\5\5\u0159\n\5\3\6\3\6\3\7\3\7\3\b\3\b\5\b\u0161\n")
        buf.write("\b\3\t\3\t\6\t\u0165\n\t\r\t\16\t\u0166\3\t\5\t\u016a")
        buf.write("\n\t\3\n\3\n\3\13\3\13\3\13\3\13\6\13\u0172\n\13\r\13")
        buf.write("\16\13\u0173\3\13\3\13\6\13\u0178\n\13\r\13\16\13\u0179")
        buf.write("\5\13\u017c\n\13\3\f\3\f\6\f\u0180\n\f\r\f\16\f\u0181")
        buf.write("\3\r\3\r\6\r\u0186\n\r\r\r\16\r\u0187\3\r\3\r\3\r\3\r")
        buf.write("\3\r\6\r\u018f\n\r\r\r\16\r\u0190\3\r\3\r\5\r\u0195\n")
        buf.write("\r\3\16\3\16\6\16\u0199\n\16\r\16\16\16\u019a\3\16\5\16")
        buf.write("\u019e\n\16\3\17\3\17\3\20\3\20\6\20\u01a4\n\20\r\20\16")
        buf.write("\20\u01a5\3\20\5\20\u01a9\n\20\3\21\3\21\3\21\2\2\22\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \2\2\2\u022c\2\"")
        buf.write("\3\2\2\2\4,\3\2\2\2\6\u014e\3\2\2\2\b\u0158\3\2\2\2\n")
        buf.write("\u015a\3\2\2\2\f\u015c\3\2\2\2\16\u0160\3\2\2\2\20\u0162")
        buf.write("\3\2\2\2\22\u016b\3\2\2\2\24\u017b\3\2\2\2\26\u017d\3")
        buf.write("\2\2\2\30\u0194\3\2\2\2\32\u0196\3\2\2\2\34\u019f\3\2")
        buf.write("\2\2\36\u01a1\3\2\2\2 \u01aa\3\2\2\2\"#\5\4\3\2#$\7\2")
        buf.write("\2\3$\3\3\2\2\2%&\5\6\4\2&\'\5\20\t\2\'(\5\30\r\2(-\3")
        buf.write("\2\2\2)*\5\6\4\2*+\5\20\t\2+-\3\2\2\2,%\3\2\2\2,)\3\2")
        buf.write("\2\2-\5\3\2\2\2.\60\5\b\5\2/.\3\2\2\2/\60\3\2\2\2\60\62")
        buf.write("\3\2\2\2\61\63\5\n\6\2\62\61\3\2\2\2\62\63\3\2\2\2\63")
        buf.write("\65\3\2\2\2\64\66\5\f\7\2\65\64\3\2\2\2\65\66\3\2\2\2")
        buf.write("\668\3\2\2\2\679\5\16\b\28\67\3\2\2\289\3\2\2\29\u014f")
        buf.write("\3\2\2\2:<\5\b\5\2;:\3\2\2\2;<\3\2\2\2<>\3\2\2\2=?\5\n")
        buf.write("\6\2>=\3\2\2\2>?\3\2\2\2?A\3\2\2\2@B\5\16\b\2A@\3\2\2")
        buf.write("\2AB\3\2\2\2BD\3\2\2\2CE\5\f\7\2DC\3\2\2\2DE\3\2\2\2E")
        buf.write("\u014f\3\2\2\2FH\5\b\5\2GF\3\2\2\2GH\3\2\2\2HJ\3\2\2\2")
        buf.write("IK\5\f\7\2JI\3\2\2\2JK\3\2\2\2KM\3\2\2\2LN\5\n\6\2ML\3")
        buf.write("\2\2\2MN\3\2\2\2NP\3\2\2\2OQ\5\16\b\2PO\3\2\2\2PQ\3\2")
        buf.write("\2\2Q\u014f\3\2\2\2RT\5\b\5\2SR\3\2\2\2ST\3\2\2\2TV\3")
        buf.write("\2\2\2UW\5\f\7\2VU\3\2\2\2VW\3\2\2\2WY\3\2\2\2XZ\5\16")
        buf.write("\b\2YX\3\2\2\2YZ\3\2\2\2Z\\\3\2\2\2[]\5\n\6\2\\[\3\2\2")
        buf.write("\2\\]\3\2\2\2]\u014f\3\2\2\2^`\5\b\5\2_^\3\2\2\2_`\3\2")
        buf.write("\2\2`b\3\2\2\2ac\5\16\b\2ba\3\2\2\2bc\3\2\2\2ce\3\2\2")
        buf.write("\2df\5\n\6\2ed\3\2\2\2ef\3\2\2\2fh\3\2\2\2gi\5\f\7\2h")
        buf.write("g\3\2\2\2hi\3\2\2\2i\u014f\3\2\2\2jl\5\b\5\2kj\3\2\2\2")
        buf.write("kl\3\2\2\2ln\3\2\2\2mo\5\16\b\2nm\3\2\2\2no\3\2\2\2oq")
        buf.write("\3\2\2\2pr\5\f\7\2qp\3\2\2\2qr\3\2\2\2rt\3\2\2\2su\5\n")
        buf.write("\6\2ts\3\2\2\2tu\3\2\2\2u\u014f\3\2\2\2vx\5\n\6\2wv\3")
        buf.write("\2\2\2wx\3\2\2\2xz\3\2\2\2y{\5\b\5\2zy\3\2\2\2z{\3\2\2")
        buf.write("\2{}\3\2\2\2|~\5\f\7\2}|\3\2\2\2}~\3\2\2\2~\u0080\3\2")
        buf.write("\2\2\177\u0081\5\16\b\2\u0080\177\3\2\2\2\u0080\u0081")
        buf.write("\3\2\2\2\u0081\u014f\3\2\2\2\u0082\u0084\5\n\6\2\u0083")
        buf.write("\u0082\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0086\3\2\2\2")
        buf.write("\u0085\u0087\5\b\5\2\u0086\u0085\3\2\2\2\u0086\u0087\3")
        buf.write("\2\2\2\u0087\u0089\3\2\2\2\u0088\u008a\5\16\b\2\u0089")
        buf.write("\u0088\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008c\3\2\2\2")
        buf.write("\u008b\u008d\5\f\7\2\u008c\u008b\3\2\2\2\u008c\u008d\3")
        buf.write("\2\2\2\u008d\u014f\3\2\2\2\u008e\u0090\5\n\6\2\u008f\u008e")
        buf.write("\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0092\3\2\2\2\u0091")
        buf.write("\u0093\5\f\7\2\u0092\u0091\3\2\2\2\u0092\u0093\3\2\2\2")
        buf.write("\u0093\u0095\3\2\2\2\u0094\u0096\5\b\5\2\u0095\u0094\3")
        buf.write("\2\2\2\u0095\u0096\3\2\2\2\u0096\u0098\3\2\2\2\u0097\u0099")
        buf.write("\5\16\b\2\u0098\u0097\3\2\2\2\u0098\u0099\3\2\2\2\u0099")
        buf.write("\u014f\3\2\2\2\u009a\u009c\5\n\6\2\u009b\u009a\3\2\2\2")
        buf.write("\u009b\u009c\3\2\2\2\u009c\u009e\3\2\2\2\u009d\u009f\5")
        buf.write("\f\7\2\u009e\u009d\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a1")
        buf.write("\3\2\2\2\u00a0\u00a2\5\16\b\2\u00a1\u00a0\3\2\2\2\u00a1")
        buf.write("\u00a2\3\2\2\2\u00a2\u00a4\3\2\2\2\u00a3\u00a5\5\b\5\2")
        buf.write("\u00a4\u00a3\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u014f\3")
        buf.write("\2\2\2\u00a6\u00a8\5\n\6\2\u00a7\u00a6\3\2\2\2\u00a7\u00a8")
        buf.write("\3\2\2\2\u00a8\u00aa\3\2\2\2\u00a9\u00ab\5\16\b\2\u00aa")
        buf.write("\u00a9\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ad\3\2\2\2")
        buf.write("\u00ac\u00ae\5\b\5\2\u00ad\u00ac\3\2\2\2\u00ad\u00ae\3")
        buf.write("\2\2\2\u00ae\u00b0\3\2\2\2\u00af\u00b1\5\f\7\2\u00b0\u00af")
        buf.write("\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u014f\3\2\2\2\u00b2")
        buf.write("\u00b4\5\n\6\2\u00b3\u00b2\3\2\2\2\u00b3\u00b4\3\2\2\2")
        buf.write("\u00b4\u00b6\3\2\2\2\u00b5\u00b7\5\16\b\2\u00b6\u00b5")
        buf.write("\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b9\3\2\2\2\u00b8")
        buf.write("\u00ba\5\f\7\2\u00b9\u00b8\3\2\2\2\u00b9\u00ba\3\2\2\2")
        buf.write("\u00ba\u00bc\3\2\2\2\u00bb\u00bd\5\b\5\2\u00bc\u00bb\3")
        buf.write("\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u014f\3\2\2\2\u00be\u00c0")
        buf.write("\5\f\7\2\u00bf\u00be\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0")
        buf.write("\u00c2\3\2\2\2\u00c1\u00c3\5\b\5\2\u00c2\u00c1\3\2\2\2")
        buf.write("\u00c2\u00c3\3\2\2\2\u00c3\u00c5\3\2\2\2\u00c4\u00c6\5")
        buf.write("\n\6\2\u00c5\u00c4\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c8")
        buf.write("\3\2\2\2\u00c7\u00c9\5\16\b\2\u00c8\u00c7\3\2\2\2\u00c8")
        buf.write("\u00c9\3\2\2\2\u00c9\u014f\3\2\2\2\u00ca\u00cc\5\f\7\2")
        buf.write("\u00cb\u00ca\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00ce\3")
        buf.write("\2\2\2\u00cd\u00cf\5\b\5\2\u00ce\u00cd\3\2\2\2\u00ce\u00cf")
        buf.write("\3\2\2\2\u00cf\u00d1\3\2\2\2\u00d0\u00d2\5\16\b\2\u00d1")
        buf.write("\u00d0\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d4\3\2\2\2")
        buf.write("\u00d3\u00d5\5\n\6\2\u00d4\u00d3\3\2\2\2\u00d4\u00d5\3")
        buf.write("\2\2\2\u00d5\u014f\3\2\2\2\u00d6\u00d8\5\f\7\2\u00d7\u00d6")
        buf.write("\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00da\3\2\2\2\u00d9")
        buf.write("\u00db\5\n\6\2\u00da\u00d9\3\2\2\2\u00da\u00db\3\2\2\2")
        buf.write("\u00db\u00dd\3\2\2\2\u00dc\u00de\5\b\5\2\u00dd\u00dc\3")
        buf.write("\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00e0\3\2\2\2\u00df\u00e1")
        buf.write("\5\16\b\2\u00e0\u00df\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1")
        buf.write("\u014f\3\2\2\2\u00e2\u00e4\5\f\7\2\u00e3\u00e2\3\2\2\2")
        buf.write("\u00e3\u00e4\3\2\2\2\u00e4\u00e6\3\2\2\2\u00e5\u00e7\5")
        buf.write("\n\6\2\u00e6\u00e5\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e9")
        buf.write("\3\2\2\2\u00e8\u00ea\5\16\b\2\u00e9\u00e8\3\2\2\2\u00e9")
        buf.write("\u00ea\3\2\2\2\u00ea\u00ec\3\2\2\2\u00eb\u00ed\5\b\5\2")
        buf.write("\u00ec\u00eb\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u014f\3")
        buf.write("\2\2\2\u00ee\u00f0\5\f\7\2\u00ef\u00ee\3\2\2\2\u00ef\u00f0")
        buf.write("\3\2\2\2\u00f0\u00f2\3\2\2\2\u00f1\u00f3\5\16\b\2\u00f2")
        buf.write("\u00f1\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f5\3\2\2\2")
        buf.write("\u00f4\u00f6\5\b\5\2\u00f5\u00f4\3\2\2\2\u00f5\u00f6\3")
        buf.write("\2\2\2\u00f6\u00f8\3\2\2\2\u00f7\u00f9\5\n\6\2\u00f8\u00f7")
        buf.write("\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u014f\3\2\2\2\u00fa")
        buf.write("\u00fc\5\f\7\2\u00fb\u00fa\3\2\2\2\u00fb\u00fc\3\2\2\2")
        buf.write("\u00fc\u00fe\3\2\2\2\u00fd\u00ff\5\16\b\2\u00fe\u00fd")
        buf.write("\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0101\3\2\2\2\u0100")
        buf.write("\u0102\5\n\6\2\u0101\u0100\3\2\2\2\u0101\u0102\3\2\2\2")
        buf.write("\u0102\u0104\3\2\2\2\u0103\u0105\5\b\5\2\u0104\u0103\3")
        buf.write("\2\2\2\u0104\u0105\3\2\2\2\u0105\u014f\3\2\2\2\u0106\u0108")
        buf.write("\5\16\b\2\u0107\u0106\3\2\2\2\u0107\u0108\3\2\2\2\u0108")
        buf.write("\u010a\3\2\2\2\u0109\u010b\5\b\5\2\u010a\u0109\3\2\2\2")
        buf.write("\u010a\u010b\3\2\2\2\u010b\u010d\3\2\2\2\u010c\u010e\5")
        buf.write("\n\6\2\u010d\u010c\3\2\2\2\u010d\u010e\3\2\2\2\u010e\u0110")
        buf.write("\3\2\2\2\u010f\u0111\5\f\7\2\u0110\u010f\3\2\2\2\u0110")
        buf.write("\u0111\3\2\2\2\u0111\u014f\3\2\2\2\u0112\u0114\5\16\b")
        buf.write("\2\u0113\u0112\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0116")
        buf.write("\3\2\2\2\u0115\u0117\5\b\5\2\u0116\u0115\3\2\2\2\u0116")
        buf.write("\u0117\3\2\2\2\u0117\u0119\3\2\2\2\u0118\u011a\5\f\7\2")
        buf.write("\u0119\u0118\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u011c\3")
        buf.write("\2\2\2\u011b\u011d\5\n\6\2\u011c\u011b\3\2\2\2\u011c\u011d")
        buf.write("\3\2\2\2\u011d\u014f\3\2\2\2\u011e\u0120\5\16\b\2\u011f")
        buf.write("\u011e\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u0122\3\2\2\2")
        buf.write("\u0121\u0123\5\n\6\2\u0122\u0121\3\2\2\2\u0122\u0123\3")
        buf.write("\2\2\2\u0123\u0125\3\2\2\2\u0124\u0126\5\b\5\2\u0125\u0124")
        buf.write("\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0128\3\2\2\2\u0127")
        buf.write("\u0129\5\f\7\2\u0128\u0127\3\2\2\2\u0128\u0129\3\2\2\2")
        buf.write("\u0129\u014f\3\2\2\2\u012a\u012c\5\16\b\2\u012b\u012a")
        buf.write("\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012e\3\2\2\2\u012d")
        buf.write("\u012f\5\n\6\2\u012e\u012d\3\2\2\2\u012e\u012f\3\2\2\2")
        buf.write("\u012f\u0131\3\2\2\2\u0130\u0132\5\f\7\2\u0131\u0130\3")
        buf.write("\2\2\2\u0131\u0132\3\2\2\2\u0132\u0134\3\2\2\2\u0133\u0135")
        buf.write("\5\b\5\2\u0134\u0133\3\2\2\2\u0134\u0135\3\2\2\2\u0135")
        buf.write("\u014f\3\2\2\2\u0136\u0138\5\16\b\2\u0137\u0136\3\2\2")
        buf.write("\2\u0137\u0138\3\2\2\2\u0138\u013a\3\2\2\2\u0139\u013b")
        buf.write("\5\f\7\2\u013a\u0139\3\2\2\2\u013a\u013b\3\2\2\2\u013b")
        buf.write("\u013d\3\2\2\2\u013c\u013e\5\b\5\2\u013d\u013c\3\2\2\2")
        buf.write("\u013d\u013e\3\2\2\2\u013e\u0140\3\2\2\2\u013f\u0141\5")
        buf.write("\n\6\2\u0140\u013f\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u014f")
        buf.write("\3\2\2\2\u0142\u0144\5\16\b\2\u0143\u0142\3\2\2\2\u0143")
        buf.write("\u0144\3\2\2\2\u0144\u0146\3\2\2\2\u0145\u0147\5\f\7\2")
        buf.write("\u0146\u0145\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0149\3")
        buf.write("\2\2\2\u0148\u014a\5\n\6\2\u0149\u0148\3\2\2\2\u0149\u014a")
        buf.write("\3\2\2\2\u014a\u014c\3\2\2\2\u014b\u014d\5\b\5\2\u014c")
        buf.write("\u014b\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014f\3\2\2\2")
        buf.write("\u014e/\3\2\2\2\u014e;\3\2\2\2\u014eG\3\2\2\2\u014eS\3")
        buf.write("\2\2\2\u014e_\3\2\2\2\u014ek\3\2\2\2\u014ew\3\2\2\2\u014e")
        buf.write("\u0083\3\2\2\2\u014e\u008f\3\2\2\2\u014e\u009b\3\2\2\2")
        buf.write("\u014e\u00a7\3\2\2\2\u014e\u00b3\3\2\2\2\u014e\u00bf\3")
        buf.write("\2\2\2\u014e\u00cb\3\2\2\2\u014e\u00d7\3\2\2\2\u014e\u00e3")
        buf.write("\3\2\2\2\u014e\u00ef\3\2\2\2\u014e\u00fb\3\2\2\2\u014e")
        buf.write("\u0107\3\2\2\2\u014e\u0113\3\2\2\2\u014e\u011f\3\2\2\2")
        buf.write("\u014e\u012b\3\2\2\2\u014e\u0137\3\2\2\2\u014e\u0143\3")
        buf.write("\2\2\2\u014f\7\3\2\2\2\u0150\u0159\7\r\2\2\u0151\u0159")
        buf.write("\7\16\2\2\u0152\u0159\7\17\2\2\u0153\u0159\7\20\2\2\u0154")
        buf.write("\u0159\7\21\2\2\u0155\u0159\7\22\2\2\u0156\u0159\7\23")
        buf.write("\2\2\u0157\u0159\7\24\2\2\u0158\u0150\3\2\2\2\u0158\u0151")
        buf.write("\3\2\2\2\u0158\u0152\3\2\2\2\u0158\u0153\3\2\2\2\u0158")
        buf.write("\u0154\3\2\2\2\u0158\u0155\3\2\2\2\u0158\u0156\3\2\2\2")
        buf.write("\u0158\u0157\3\2\2\2\u0159\t\3\2\2\2\u015a\u015b\7\t\2")
        buf.write("\2\u015b\13\3\2\2\2\u015c\u015d\7\n\2\2\u015d\r\3\2\2")
        buf.write("\2\u015e\u0161\7\13\2\2\u015f\u0161\7\f\2\2\u0160\u015e")
        buf.write("\3\2\2\2\u0160\u015f\3\2\2\2\u0161\17\3\2\2\2\u0162\u0164")
        buf.write("\5\22\n\2\u0163\u0165\5\24\13\2\u0164\u0163\3\2\2\2\u0165")
        buf.write("\u0166\3\2\2\2\u0166\u0164\3\2\2\2\u0166\u0167\3\2\2\2")
        buf.write("\u0167\u0169\3\2\2\2\u0168\u016a\5\26\f\2\u0169\u0168")
        buf.write("\3\2\2\2\u0169\u016a\3\2\2\2\u016a\21\3\2\2\2\u016b\u016c")
        buf.write("\7\25\2\2\u016c\23\3\2\2\2\u016d\u017c\7\4\2\2\u016e\u017c")
        buf.write("\7\5\2\2\u016f\u0171\7\7\2\2\u0170\u0172\7\6\2\2\u0171")
        buf.write("\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0171\3\2\2\2")
        buf.write("\u0173\u0174\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u017c\7")
        buf.write("\b\2\2\u0176\u0178\7\6\2\2\u0177\u0176\3\2\2\2\u0178\u0179")
        buf.write("\3\2\2\2\u0179\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a")
        buf.write("\u017c\3\2\2\2\u017b\u016d\3\2\2\2\u017b\u016e\3\2\2\2")
        buf.write("\u017b\u016f\3\2\2\2\u017b\u0177\3\2\2\2\u017c\25\3\2")
        buf.write("\2\2\u017d\u017f\7\3\2\2\u017e\u0180\5\24\13\2\u017f\u017e")
        buf.write("\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u017f\3\2\2\2\u0181")
        buf.write("\u0182\3\2\2\2\u0182\27\3\2\2\2\u0183\u0185\7\26\2\2\u0184")
        buf.write("\u0186\5\32\16\2\u0185\u0184\3\2\2\2\u0186\u0187\3\2\2")
        buf.write("\2\u0187\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0189")
        buf.write("\3\2\2\2\u0189\u018a\7\27\2\2\u018a\u0195\3\2\2\2\u018b")
        buf.write("\u018e\7\26\2\2\u018c\u018f\5\36\20\2\u018d\u018f\5\32")
        buf.write("\16\2\u018e\u018c\3\2\2\2\u018e\u018d\3\2\2\2\u018f\u0190")
        buf.write("\3\2\2\2\u0190\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191")
        buf.write("\u0192\3\2\2\2\u0192\u0193\7\27\2\2\u0193\u0195\3\2\2")
        buf.write("\2\u0194\u0183\3\2\2\2\u0194\u018b\3\2\2\2\u0195\31\3")
        buf.write("\2\2\2\u0196\u0198\5\34\17\2\u0197\u0199\5\24\13\2\u0198")
        buf.write("\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u0198\3\2\2\2")
        buf.write("\u019a\u019b\3\2\2\2\u019b\u019d\3\2\2\2\u019c\u019e\5")
        buf.write("\26\f\2\u019d\u019c\3\2\2\2\u019d\u019e\3\2\2\2\u019e")
        buf.write("\33\3\2\2\2\u019f\u01a0\7\31\2\2\u01a0\35\3\2\2\2\u01a1")
        buf.write("\u01a3\5 \21\2\u01a2\u01a4\5\24\13\2\u01a3\u01a2\3\2\2")
        buf.write("\2\u01a4\u01a5\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a6")
        buf.write("\3\2\2\2\u01a6\u01a8\3\2\2\2\u01a7\u01a9\5\26\f\2\u01a8")
        buf.write("\u01a7\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\37\3\2\2\2\u01aa")
        buf.write("\u01ab\7\30\2\2\u01ab!\3\2\2\2t,/\62\658;>ADGJMPSVY\\")
        buf.write("_behknqtwz}\u0080\u0083\u0086\u0089\u008c\u008f\u0092")
        buf.write("\u0095\u0098\u009b\u009e\u00a1\u00a4\u00a7\u00aa\u00ad")
        buf.write("\u00b0\u00b3\u00b6\u00b9\u00bc\u00bf\u00c2\u00c5\u00c8")
        buf.write("\u00cb\u00ce\u00d1\u00d4\u00d7\u00da\u00dd\u00e0\u00e3")
        buf.write("\u00e6\u00e9\u00ec\u00ef\u00f2\u00f5\u00f8\u00fb\u00fe")
        buf.write("\u0101\u0104\u0107\u010a\u010d\u0110\u0113\u0116\u0119")
        buf.write("\u011c\u011f\u0122\u0125\u0128\u012b\u012e\u0131\u0134")
        buf.write("\u0137\u013a\u013d\u0140\u0143\u0146\u0149\u014c\u014e")
        buf.write("\u0158\u0160\u0166\u0169\u0173\u0179\u017b\u0181\u0187")
        buf.write("\u018e\u0190\u0194\u019a\u019d\u01a5\u01a8")
        return buf.getvalue()


class QuestionParser ( Parser ):

    grammarFileName = "QuestionParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "FEEDBACK_MARKER", "MEDIA", "HYPERLINK", 
                      "ALL_CHARACTER", "ESCAPED_OPEN_BRACKET", "ESCAPED_CLOSE_BRACKET", 
                      "TITLE", "POINTS", "RANDOMIZE_TRUE", "RANDOMIZE_FALSE", 
                      "TYPE_MC", "TYPE_TF", "TYPE_MS", "TYPE_MT", "TYPE_ORD", 
                      "TYPE_FIB", "TYPE_WR", "TYPE_OTHER", "QUESTION_PREFIX", 
                      "START_ANSWER", "END_ANSWER", "RIGHT_ANSWER", "LIST_PREFIX" ]

    RULE_parse_question = 0
    RULE_question = 1
    RULE_question_header = 2
    RULE_question_type = 3
    RULE_title = 4
    RULE_points = 5
    RULE_randomize = 6
    RULE_question_body = 7
    RULE_question_prefix = 8
    RULE_content = 9
    RULE_feedback = 10
    RULE_answer_list = 11
    RULE_list_item = 12
    RULE_list_prefix = 13
    RULE_list_answer_item = 14
    RULE_answer_prefix = 15

    ruleNames =  [ "parse_question", "question", "question_header", "question_type", 
                   "title", "points", "randomize", "question_body", "question_prefix", 
                   "content", "feedback", "answer_list", "list_item", "list_prefix", 
                   "list_answer_item", "answer_prefix" ]

    EOF = Token.EOF
    FEEDBACK_MARKER=1
    MEDIA=2
    HYPERLINK=3
    ALL_CHARACTER=4
    ESCAPED_OPEN_BRACKET=5
    ESCAPED_CLOSE_BRACKET=6
    TITLE=7
    POINTS=8
    RANDOMIZE_TRUE=9
    RANDOMIZE_FALSE=10
    TYPE_MC=11
    TYPE_TF=12
    TYPE_MS=13
    TYPE_MT=14
    TYPE_ORD=15
    TYPE_FIB=16
    TYPE_WR=17
    TYPE_OTHER=18
    QUESTION_PREFIX=19
    START_ANSWER=20
    END_ANSWER=21
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

        def question(self):
            return self.getTypedRuleContext(QuestionParser.QuestionContext,0)


        def EOF(self):
            return self.getToken(QuestionParser.EOF, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.question()
            self.state = 33
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


        def getRuleIndex(self):
            return QuestionParser.RULE_question

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class QuestionWithoutAnswersContext(QuestionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuestionParser.QuestionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def question_header(self):
            return self.getTypedRuleContext(QuestionParser.Question_headerContext,0)

        def question_body(self):
            return self.getTypedRuleContext(QuestionParser.Question_bodyContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuestionWithoutAnswers" ):
                listener.enterQuestionWithoutAnswers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuestionWithoutAnswers" ):
                listener.exitQuestionWithoutAnswers(self)


    class QuestionWithAnswersContext(QuestionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QuestionParser.QuestionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def question_header(self):
            return self.getTypedRuleContext(QuestionParser.Question_headerContext,0)

        def question_body(self):
            return self.getTypedRuleContext(QuestionParser.Question_bodyContext,0)

        def answer_list(self):
            return self.getTypedRuleContext(QuestionParser.Answer_listContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuestionWithAnswers" ):
                listener.enterQuestionWithAnswers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuestionWithAnswers" ):
                listener.exitQuestionWithAnswers(self)



    def question(self):

        localctx = QuestionParser.QuestionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_question)
        try:
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = QuestionParser.QuestionWithAnswersContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.question_header()
                self.state = 36
                self.question_body()
                self.state = 37
                self.answer_list()
                pass

            elif la_ == 2:
                localctx = QuestionParser.QuestionWithoutAnswersContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.question_header()
                self.state = 40
                self.question_body()
                pass


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
        self.enterRule(localctx, 4, self.RULE_question_header)
        self._la = 0 # Token type
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,97,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 44
                    self.question_type()


                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 47
                    self.title()


                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 50
                    self.points()


                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 53
                    self.randomize()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 56
                    self.question_type()


                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 59
                    self.title()


                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 62
                    self.randomize()


                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 65
                    self.points()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 68
                    self.question_type()


                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 71
                    self.points()


                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 74
                    self.title()


                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 77
                    self.randomize()


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 80
                    self.question_type()


                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 83
                    self.points()


                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 86
                    self.randomize()


                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 89
                    self.title()


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 92
                    self.question_type()


                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 95
                    self.randomize()


                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 98
                    self.title()


                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 101
                    self.points()


                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 104
                    self.question_type()


                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 107
                    self.randomize()


                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 110
                    self.points()


                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 113
                    self.title()


                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 116
                    self.title()


                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 119
                    self.question_type()


                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 122
                    self.points()


                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 125
                    self.randomize()


                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 128
                    self.title()


                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 131
                    self.question_type()


                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 134
                    self.randomize()


                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 137
                    self.points()


                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 140
                    self.title()


                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 143
                    self.points()


                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 146
                    self.question_type()


                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 149
                    self.randomize()


                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 152
                    self.title()


                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 155
                    self.points()


                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 158
                    self.randomize()


                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 161
                    self.question_type()


                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 164
                    self.title()


                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 167
                    self.randomize()


                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 170
                    self.question_type()


                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 173
                    self.points()


                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 176
                    self.title()


                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 179
                    self.randomize()


                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 182
                    self.points()


                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 185
                    self.question_type()


                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 188
                    self.points()


                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 191
                    self.question_type()


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


                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
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


                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 206
                    self.randomize()


                self.state = 210
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 209
                    self.title()


                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 212
                    self.points()


                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 215
                    self.title()


                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 218
                    self.question_type()


                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 221
                    self.randomize()


                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 224
                    self.points()


                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 227
                    self.title()


                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 230
                    self.randomize()


                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 233
                    self.question_type()


                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 236
                    self.points()


                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 239
                    self.randomize()


                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 242
                    self.question_type()


                self.state = 246
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 245
                    self.title()


                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 248
                    self.points()


                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 251
                    self.randomize()


                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 254
                    self.title()


                self.state = 258
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 257
                    self.question_type()


                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 261
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 260
                    self.randomize()


                self.state = 264
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 263
                    self.question_type()


                self.state = 267
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 266
                    self.title()


                self.state = 270
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 269
                    self.points()


                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 273
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 272
                    self.randomize()


                self.state = 276
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 275
                    self.question_type()


                self.state = 279
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 278
                    self.points()


                self.state = 282
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 281
                    self.title()


                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)
                self.state = 285
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 284
                    self.randomize()


                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 287
                    self.title()


                self.state = 291
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 290
                    self.question_type()


                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 293
                    self.points()


                pass

            elif la_ == 22:
                self.enterOuterAlt(localctx, 22)
                self.state = 297
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 296
                    self.randomize()


                self.state = 300
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 299
                    self.title()


                self.state = 303
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 302
                    self.points()


                self.state = 306
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 305
                    self.question_type()


                pass

            elif la_ == 23:
                self.enterOuterAlt(localctx, 23)
                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 308
                    self.randomize()


                self.state = 312
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 311
                    self.points()


                self.state = 315
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 314
                    self.question_type()


                self.state = 318
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 317
                    self.title()


                pass

            elif la_ == 24:
                self.enterOuterAlt(localctx, 24)
                self.state = 321
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.RANDOMIZE_TRUE or _la==QuestionParser.RANDOMIZE_FALSE:
                    self.state = 320
                    self.randomize()


                self.state = 324
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.POINTS:
                    self.state = 323
                    self.points()


                self.state = 327
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QuestionParser.TITLE:
                    self.state = 326
                    self.title()


                self.state = 330
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.TYPE_MC) | (1 << QuestionParser.TYPE_TF) | (1 << QuestionParser.TYPE_MS) | (1 << QuestionParser.TYPE_MT) | (1 << QuestionParser.TYPE_ORD) | (1 << QuestionParser.TYPE_FIB) | (1 << QuestionParser.TYPE_WR) | (1 << QuestionParser.TYPE_OTHER))) != 0):
                    self.state = 329
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
        self.enterRule(localctx, 6, self.RULE_question_type)
        try:
            self.state = 342
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuestionParser.TYPE_MC]:
                localctx = QuestionParser.TypeMcContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.match(QuestionParser.TYPE_MC)
                pass
            elif token in [QuestionParser.TYPE_TF]:
                localctx = QuestionParser.TypeTfContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                self.match(QuestionParser.TYPE_TF)
                pass
            elif token in [QuestionParser.TYPE_MS]:
                localctx = QuestionParser.TypeMsContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 336
                self.match(QuestionParser.TYPE_MS)
                pass
            elif token in [QuestionParser.TYPE_MT]:
                localctx = QuestionParser.TypeMtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 337
                self.match(QuestionParser.TYPE_MT)
                pass
            elif token in [QuestionParser.TYPE_ORD]:
                localctx = QuestionParser.TypeOrdContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 338
                self.match(QuestionParser.TYPE_ORD)
                pass
            elif token in [QuestionParser.TYPE_FIB]:
                localctx = QuestionParser.TypeFibContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 339
                self.match(QuestionParser.TYPE_FIB)
                pass
            elif token in [QuestionParser.TYPE_WR]:
                localctx = QuestionParser.TypeWrContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 340
                self.match(QuestionParser.TYPE_WR)
                pass
            elif token in [QuestionParser.TYPE_OTHER]:
                localctx = QuestionParser.TypeOtherContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 341
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
        self.enterRule(localctx, 8, self.RULE_title)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
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
        self.enterRule(localctx, 10, self.RULE_points)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
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
        self.enterRule(localctx, 12, self.RULE_randomize)
        try:
            self.state = 350
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuestionParser.RANDOMIZE_TRUE]:
                localctx = QuestionParser.RandomTrueContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.match(QuestionParser.RANDOMIZE_TRUE)
                pass
            elif token in [QuestionParser.RANDOMIZE_FALSE]:
                localctx = QuestionParser.RandomFalseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 349
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
        self.enterRule(localctx, 14, self.RULE_question_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.question_prefix()
            self.state = 354 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 353
                self.content()
                self.state = 356 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.MEDIA) | (1 << QuestionParser.HYPERLINK) | (1 << QuestionParser.ALL_CHARACTER) | (1 << QuestionParser.ESCAPED_OPEN_BRACKET))) != 0)):
                    break

            self.state = 359
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.FEEDBACK_MARKER:
                self.state = 358
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
        self.enterRule(localctx, 16, self.RULE_question_prefix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
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
        self.enterRule(localctx, 18, self.RULE_content)
        self._la = 0 # Token type
        try:
            self.state = 377
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QuestionParser.MEDIA]:
                localctx = QuestionParser.MediaContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 363
                self.match(QuestionParser.MEDIA)
                pass
            elif token in [QuestionParser.HYPERLINK]:
                localctx = QuestionParser.HyperlinkContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 364
                self.match(QuestionParser.HYPERLINK)
                pass
            elif token in [QuestionParser.ESCAPED_OPEN_BRACKET]:
                localctx = QuestionParser.FibAnswerContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 365
                self.match(QuestionParser.ESCAPED_OPEN_BRACKET)
                self.state = 367 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 366
                    self.match(QuestionParser.ALL_CHARACTER)
                    self.state = 369 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==QuestionParser.ALL_CHARACTER):
                        break

                self.state = 371
                self.match(QuestionParser.ESCAPED_CLOSE_BRACKET)
                pass
            elif token in [QuestionParser.ALL_CHARACTER]:
                localctx = QuestionParser.ContentCharactersContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 373 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 372
                        self.match(QuestionParser.ALL_CHARACTER)

                    else:
                        raise NoViableAltException(self)
                    self.state = 375 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,103,self._ctx)

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
        self.enterRule(localctx, 20, self.RULE_feedback)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(QuestionParser.FEEDBACK_MARKER)
            self.state = 381 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 380
                self.content()
                self.state = 383 
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
        def END_ANSWER(self):
            return self.getToken(QuestionParser.END_ANSWER, 0)
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
        def END_ANSWER(self):
            return self.getToken(QuestionParser.END_ANSWER, 0)
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
        self.enterRule(localctx, 22, self.RULE_answer_list)
        self._la = 0 # Token type
        try:
            self.state = 402
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,109,self._ctx)
            if la_ == 1:
                localctx = QuestionParser.ListNoAnswerContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 385
                self.match(QuestionParser.START_ANSWER)
                self.state = 387 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 386
                    self.list_item()
                    self.state = 389 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==QuestionParser.LIST_PREFIX):
                        break

                self.state = 391
                self.match(QuestionParser.END_ANSWER)
                pass

            elif la_ == 2:
                localctx = QuestionParser.ListWithAnswerContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 393
                self.match(QuestionParser.START_ANSWER)
                self.state = 396 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 396
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [QuestionParser.RIGHT_ANSWER]:
                        self.state = 394
                        self.list_answer_item()
                        pass
                    elif token in [QuestionParser.LIST_PREFIX]:
                        self.state = 395
                        self.list_item()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 398 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==QuestionParser.RIGHT_ANSWER or _la==QuestionParser.LIST_PREFIX):
                        break

                self.state = 400
                self.match(QuestionParser.END_ANSWER)
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
        self.enterRule(localctx, 24, self.RULE_list_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.list_prefix()
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

            self.state = 411
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.FEEDBACK_MARKER:
                self.state = 410
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
        self.enterRule(localctx, 26, self.RULE_list_prefix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
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
        self.enterRule(localctx, 28, self.RULE_list_answer_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.answer_prefix()
            self.state = 417 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 416
                self.content()
                self.state = 419 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QuestionParser.MEDIA) | (1 << QuestionParser.HYPERLINK) | (1 << QuestionParser.ALL_CHARACTER) | (1 << QuestionParser.ESCAPED_OPEN_BRACKET))) != 0)):
                    break

            self.state = 422
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==QuestionParser.FEEDBACK_MARKER:
                self.state = 421
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
        self.enterRule(localctx, 30, self.RULE_answer_prefix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.match(QuestionParser.RIGHT_ANSWER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





