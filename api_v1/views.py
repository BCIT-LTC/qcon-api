from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from antlr4 import *
from antlr.QconLexer import QconLexer
from antlr.QconListener import QconListener
from antlr.QconParser import QconParser
import sys
import json
import pypandoc
from zipfile import *
from api_v1.scorm.XmlWriter import XmlWriter
from django.http import FileResponse

from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser

from .models import Quiz

import logging
logger = logging.getLogger(__name__)


def main(test) :
    input = InputStream(test)
    
    lexer = QconLexer(input)
    stream = CommonTokenStream(lexer)
    parser = QconParser(stream)
    tree = parser.qcon()
    # 
    printer = QconListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    # print(tree.toStringTree(recog=parser))
    parsedQuestions = printer.getresults()

    fileName = "EXAM-1"
    sectionFolderName = "Section_EXAM-1"
    imageFolder = ""
    imageLocalFolder = ""

    questionLibraryEntity = QuestionLibraryEntity(fileName, sectionFolderName, imageFolder, imageLocalFolder)
    parsedXml = XmlWriter(questionLibraryEntity, parsedQuestions)
    # parsedXml.getXml()


class QuestionLibraryEntity(object):
    def __init__(self, fileName, sectionFolderName, imageFolder, imageLocalFolder) :
        self.zipFileName = fileName
        self.sectionFolderName = sectionFolderName if sectionFolderName else self.zipFileName
        self.imageFolder = imageFolder if imageFolder else ''
        self.imageLocalFolder = imageLocalFolder


class Upload(APIView):
    def post(self, request, format=None):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
       
        # logger.info(request.data['filename'])
        # logger.info(request.session.get())

        # tempPath = './antlr/test3.txt'
        # with open(tempPath,"r") as file:
        #     fileText = file.read()
        #     pandocstring = pypandoc.convert_text(fileText, format='rst', to='gfm+fancy_lists+emoji', extra_args=['--preserve-tabs', '--wrap=preserve'])

        #  Starting Document validation
        # TODO Check if valid DOCx file

        # Creating Model instance
        # TODO create new model instance

        #  Starting Markdown conversion
        filePath = './temp/test6.docx'
        pandocstring = pypandoc.convert_file(filePath, format='docx', to='markdown_github+fancy_lists+emoji+hard_line_breaks+all_symbols_escapable+escaped_line_breaks', extra_args=['--preserve-tabs', '--wrap=preserve'])
        print(pandocstring)        
        #  Finished Markdown conversion 

        # model.state = "markdown finished"

        # Creating Temp file
        with open("./temp/test4.txt","w+") as file:
            file.write("\n" + pandocstring)
            file.close()
        
        # Starting Antler AST conversion
        lex = main("\n" + pandocstring)

        return Response('Reference number')

class CliUpload(APIView):

    permission_classes = (IsAuthenticated,)

    parser_classes = [MultiPartParser]

    def post(self, request):

        # print(request.data.file)

        file_obj = request.FILES.get('file')

        print(file_obj)
        # print(file_obj.name)

        # newQuiz = Quiz.objects.create(tempfile=file_obj)
        newQuiz = Quiz.objects.create()
        newQuiz.tempfile=file_obj
        newQuiz.save()

        # newQuiz.tempfile=file_obj
        # newQuiz.save()

        # pandocstring = pypandoc.convert_file(filePath, format='docx', to='markdown_github+fancy_lists+emoji+hard_line_breaks+all_symbols_escapable+escaped_line_breaks', extra_args=['--preserve-tabs', '--wrap=preserve'])
        # print(request.data.file)

        content = {'name': 'pandas died'}

        return Response("content")

# class QuerySession(APIView):
#     def post()
#         return "JSON object of the quiz including errors and state"



def Download(request, session):

    print("----THIS WORKS----")
    print(session)

    ZIPFILE = './temp/EXAM-1.zip'

    file_response = FileResponse(open(ZIPFILE, 'rb'))

    return file_response

def DownloadTest(request):

    print("----Downloadtest----")
    # print(session)

    print(request)

    ZIPFILE = './temp/EXAM-1.zip'
    file_response = FileResponse(open(ZIPFILE, 'rb'))

    return file_response

