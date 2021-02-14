from api_v2.parser.QuestionLexer import QuestionLexer
from api_v2.parser.QuestionParserListener import QuestionParserListener
from api_v2.parser.QuestionParser import QuestionParser

from api_v2.parser.QconLexer import QconLexer
from api_v2.parser.QconListener import QconListener
from api_v2.parser.QconParser import QconParser

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

import logging
QuestionParser_Logger = logging.getLogger('api_v2.parser.QuestionParserMain')

def question_parser(question_library, text_string):
    try:
        input = InputStream(text_string)
        lexer = QuestionLexer(input)
        tokens = CommonTokenStream(lexer)
        parser = QuestionParser(tokens)
        tree = parser.parse_question()
        listener = QuestionParserListener(question_library)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        # print(tree.toStringTree(recog=parser))
        parsed_questions = listener.get_results()
        return parsed_questions
    except:
        QuestionParser_Logger.error("["+str(question_library.transaction) +"]" + "ANTLR LEXER failed and cannot continue")