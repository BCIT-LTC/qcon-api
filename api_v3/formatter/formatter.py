# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from api_v3.formatter.formatterLexer import formatterLexer
from api_v3.formatter.formatterListener import formatterListener
from api_v3.formatter.formatterParser import formatterParser


from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

def formatter(question_library):

    try:
        input = InputStream(question_library.pandoc_string)
        lexer = formatterLexer(input)
        stream = CommonTokenStream(lexer)
        parser = formatterParser(stream)
        tree = parser.formatter()
        #
        printer = formatterListener()
        walker = ParseTreeWalker()
        # print(tree.toStringTree(recog=parser))
        walker.walk(printer, tree)
        result = printer.get_results()
    except Exception as e: 

        print("ANTLR ERROR: " + str(e))
        pass

    print("HEADER================")
    if result[0] is not None:
        print(result[0])  
    print("sections================")
    if result[1] is not None:
        for val in result[1]:
            print(val)   
    print("answers================")
    if result[2] is not None:
        print(result[2])   

    pass