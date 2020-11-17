from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from antlr4 import *
from antlr.QconLexer import QconLexer
from antlr.QconListener import QconListener
from antlr.QconParser import QconParser
import sys
import logging
import json
import pypandoc
from zipfile import *
from api_v1.scorm.XmlWriter import XmlWriter

logger = logging.getLogger(__name__)



def main(test) :
    input = InputStream(test)
    
    lexer = QconLexer(input)
    stream = CommonTokenStream(lexer)
    parser = QconParser(stream)
    tree = parser.qcon()

    printer = QconListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    # print(tree.toStringTree(recog=parser))
    parsedQuestions = printer.getresults()

    parsedXml = XmlWriter(parsedQuestions)
    # parsedXml.getXml()

class TestEndpoint(APIView):
    def post(self, request, format=None):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
       
        # logger.info(request.data['filename'])
        # logger.info(request.session.get())

        # tempPath = './antlr/test3.txt'
        # with open(tempPath,"r") as file:
        #     fileText = file.read()
        #     pandocstring = pypandoc.convert_text(fileText, format='rst', to='gfm+fancy_lists+emoji', extra_args=['--preserve-tabs', '--wrap=preserve'])

        filePath = './temp/test6.docx'
        pandocstring = pypandoc.convert_file(filePath, format='docx', to='markdown_github+fancy_lists+emoji+hard_line_breaks+all_symbols_escapable+escaped_line_breaks', extra_args=['--preserve-tabs', '--wrap=preserve'])
        print(pandocstring)
        
        with open("./temp/test4.txt","w+") as file:
            file.write("\n" + pandocstring)
            file.close()
        
        lex = main("\n" + pandocstring)

        return Response('DONE')