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

from api_v1.scorm.XmlWriter import XmlWriter

logger = logging.getLogger(__name__)



def main(test) :
    input = FileStream(test)
    lexer = QconLexer(input)
    stream = CommonTokenStream(lexer)
    parser = QconParser(stream)
    tree = parser.qcon()

    printer = QconListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    parsedQuestions = printer.getresults()

    # parsedXml = XmlWriter(parsedQuestions)
    # parsedXml.getXml()

class TestEndpoint(APIView):
    def post(self, request, format=None):

        # logger.info(request.data['filename'])

        # logger.info(request.session.get())

        lex = main("./antlr/test3.txt")



        return Response('lex')