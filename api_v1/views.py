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
from api_v1.scorm.Zipper import XmlZipper

from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser

from os.path import basename
from os import makedirs, path, walk

from django.core.files.base import ContentFile

from .models import Quiz

import logging
logger = logging.getLogger(__name__)


def parse_questions(new_quiz) :
    input = InputStream(new_quiz.pandoc_string)
    lexer = QconLexer(input)
    stream = CommonTokenStream(lexer)
    parser = QconParser(stream)
    tree = parser.qcon()
    # 
    printer = QconListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    # print(tree.toStringTree(recog=parser))
    parsed_questions = printer.get_results()

    return parsed_questions


class QuestionLibraryEntity(object):
    def __init__(self, file_name, sectionFolderName, imageFolder, imageLocalFolder) :
        self.zipFileName = file_name
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

        file_name = "EXAM-1"
        section_name = "Section_EXAM-1"
        imageFolder = ""
        imageLocalFolder = ""
        # newQuiz = Quiz.objects.create(tempfile=file_obj)
        new_quiz = Quiz.objects.create()
        new_quiz.folder_path = '/code/temp/' + str(new_quiz.id)
        new_quiz.save()

        new_quiz.create_directory()
        new_quiz.temp_file=file_obj
        new_quiz.save()

        pandocstring = pypandoc.convert_file(new_quiz.temp_file.path, format='docx', to='markdown_github+fancy_lists+emoji+hard_line_breaks+all_symbols_escapable+escaped_line_breaks', extra_args=['--preserve-tabs', '--wrap=preserve'])

        # append newline for a quickfix for antler
        # pandocstring = "\n" + pandocstring
        new_quiz.pandoc_string = "\n" + pandocstring
        new_quiz.save()
        # Starting Antler AST conversion
        parsed_questions = parse_questions(new_quiz)

 
        questionLibraryEntity = QuestionLibraryEntity(file_name, section_name, imageFolder, imageLocalFolder)
        parsedXml = XmlWriter(questionLibraryEntity, parsed_questions)

        #TODO REMOVE createQuestionLibrary
        # XmlZipper.createQuestionLibrary(questionLibraryEntity, parsedXml.root)
        # print(parsedXml)

        new_quiz.xml_string = parsedXml.xml_string
        new_quiz.save()

        # new_quiz.zip_file = 
        content_file = ContentFile(new_quiz.xml_string, name="temp_file.xml")
        new_quiz.xml_file = content_file
        new_quiz.save()

        # new_quiz.zip_file = content_file
        # new_quiz.save()

        # new_quiz.save("xmlfilename", testfile)

    
        # if os.path.exists('/code/DATA/'):
            
        print(new_quiz.xml_file.path)
        # print(basename(new_quiz.zip_file.path))
        
        

        with ZipFile('/code/temp/' + str(new_quiz.id) + '/' + str(new_quiz.id) + '.zip', 'w') as myzip:
            myzip.write(new_quiz.xml_file.path, basename(new_quiz.xml_file.path))
		# 	myzip.write(questionXMLPath, basename(questionXMLPath))
			# 	myzip.write(manifestXMLPath, basename(manifestXMLPath))
            for root, dirs, files in walk(questionLibraryEntity.imageLocalFolder) :
                for filename in files :
                    myzip.write(path.join(root, filename), questionLibraryEntity.imageFolder + '/' + filename)


        content = {'name': 'pandas died'}

        return Response("content")

# class QuerySession(APIView):
#     def post()
#         return "JSON object of the quiz including errors and state"



# def Download(request, session):

#     print("----THIS WORKS----")
#     print(session)

#     ZIPFILE = './temp/EXAM-1.zip'

#     file_response = FileResponse(open(ZIPFILE, 'rb'))

#     return file_response

# def DownloadTest(request):

#     print("----Downloadtest----")
#     # print(session)

#     print(request)

#     ZIPFILE = './temp/EXAM-1.zip'
#     file_response = FileResponse(open(ZIPFILE, 'rb'))

#     return file_response

