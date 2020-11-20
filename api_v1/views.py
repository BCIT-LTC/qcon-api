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

from os.path import basename
from os import makedirs, path, walk
from xml.dom.minidom import parseString
from django.core.files.base import ContentFile
from django.core.files import File

from .models import Quiz
from api_v1.scorm.manifest import ManifestEntity, ManifestResourceEntity

import xml.etree.cElementTree as ET

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

        manifestEntity = ManifestEntity()
        manifestResource = ManifestResourceEntity('res_question_library', 'webcontent', 'd2lquestionlibrary', 'questiondb.xml', 'Question Library')
        manifestEntity.addResource(manifestResource)

        manifest = parsedXml.createManifest(manifestEntity, new_quiz.folder_path)
        parsed_imsmanifest = ET.tostring(manifest.getroot(),encoding='utf-8', xml_declaration=True).decode()
        parsed_imsmanifest = parseString(parsed_imsmanifest)
        parsed_imsmanifest = parsed_imsmanifest.toprettyxml(indent="\t")
        new_quiz.imsmanifest_string = parsed_imsmanifest

        new_quiz.save()

        new_quiz.questiondb_string = parsedXml.questiondb_string
        new_quiz.save()

        imsmanifest_file = ContentFile(new_quiz.imsmanifest_string, name="imsmanifest.xml")
        new_quiz.imsmanifest_file = imsmanifest_file
        new_quiz.save()

        questiondb_file = ContentFile(new_quiz.questiondb_string, name="questiondb.xml")
        new_quiz.questiondb_file = questiondb_file
        new_quiz.save()


        with ZipFile(new_quiz.folder_path + '.zip', 'w') as myzip:
            myzip.write(new_quiz.questiondb_file.path, "questiondb.xml")
            myzip.write(new_quiz.imsmanifest_file.path, "imsmanifest.xml")
            # myzip.write(questionXMLPath, basename(questionXMLPath))
            # myzip.write(manifestXMLPath, basename(manifestXMLPath))
            for root, dirs, files in walk(questionLibraryEntity.imageLocalFolder) :
                for filename in files :
                    myzip.write(path.join(root, filename), questionLibraryEntity.imageFolder + '/' + filename)


        with open(new_quiz.folder_path + '.zip', 'rb') as f:
            print("------------------------")
            print(new_quiz.folder_path + '.zip')
            
            new_quiz.zip_file.save(name=str(new_quiz.id) + '.zip',content=File(f))
            # new_quiz.save()

        content = {'name': 'pandas died'}

        return Response("content")

# class QuerySession(APIView):
#     def post()
#         return "JSON object of the quiz including errors and state"



def Download(request, session, filename):

    FILE = './temp/' + str(session) + '/' + filename

    file_response = FileResponse(open(FILE, 'rb'))

    return file_response


    # return file_response

# def DownloadTest(request):

#     print("----Downloadtest----")
#     # print(session)

#     print(request)

#     ZIPFILE = './temp/EXAM-1.zip'
#     file_response = FileResponse(open(ZIPFILE, 'rb'))

#     return file_response

