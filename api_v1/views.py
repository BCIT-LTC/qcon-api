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


logger = logging.getLogger(__name__)



def main(test) :
    input = FileStream(test)
    lexer = QconLexer(input)
    stream = CommonTokenStream(lexer)
    parser = QconParser(stream)
    tree = parser.qcon()
    # print(parserjson)
    # output = open("output.html","w")

    printer = QconListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    # print(tree.getChild(1))
    # print(tree.toStringTree(recog=parser))
    # output.close()

    # return printer

class TestEndpoint(APIView):
    def post(self, request, format=None):

        # logger.info(request.data['filename'])

        # logger.info(request.session.get())

        lex = main("./antlr/test3.txt")



        return Response('lex')