from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser


from antlr.QconLexer import QconLexer
from antlr.QconListener import QconListener
from antlr.QconParser import QconParser
from api_v1.scorm.XmlWriter import XmlWriter

from antlr4 import *
import json
import sys
import pypandoc
from zipfile import *
from os.path import basename
from os import makedirs, path, walk
from xml.dom.minidom import parseString
from django.core.files.base import ContentFile
from django.core.files import File

from .models import QuestionLibrary
from api_v1.scorm.manifest import ManifestEntity, ManifestResourceEntity
import xml.etree.cElementTree as ET


from django_q.tasks import async_task

import logging
logger = logging.getLogger(__name__)


def parse_questions(question_library) :
    input = InputStream(question_library.pandoc_string)
    lexer = QconLexer(input)
    stream = CommonTokenStream(lexer)
    parser = QconParser(stream)
    tree = parser.qcon()
    # 
    printer = QconListener(question_library)
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    # print(tree.toStringTree(recog=parser))
    parsed_questions = printer.get_results()

    return parsed_questions




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

class CliRun(APIView):

    permission_classes = (IsAuthenticated,)

    parser_classes = [MultiPartParser]

    def post(self, request):

        # print(request.data.file)

        file_obj = request.FILES.get('file')


        # newQuiz = Quiz.objects.create(tempfile=file_obj)
        question_library = QuestionLibrary.objects.create()
        
        question_library.folder_path = '/code/temp/' + str(question_library.id)
        question_library.save()

        question_library.create_directory()
        question_library.temp_file=file_obj
        question_library.save()

        pandocstring = pypandoc.convert_file(question_library.temp_file.path, format='docx', to='markdown_github+fancy_lists+emoji+hard_line_breaks+all_symbols_escapable+escaped_line_breaks', extra_args=['--preserve-tabs', '--wrap=preserve'])

        # append newline for a quickfix for antler
        # pandocstring = "\n" + pandocstring
        question_library.pandoc_string = "\n" + pandocstring
        question_library.save()
        # Starting Antler AST conversion
        parsed_questions = parse_questions(question_library)



        file_name = "EXAM-1"
        section_name = "Section_EXAM-1"
        imageFolder = ""
        imageLocalFolder = ""
 
        questionLibraryEntity = QuestionLibraryEntity(file_name, section_name, imageFolder, imageLocalFolder)
        
        # TODO pass QuestionLibrary model
        parsedXml = XmlWriter(questionLibraryEntity, parsed_questions)

        manifestEntity = ManifestEntity()
        manifestResource = ManifestResourceEntity('res_question_library', 'webcontent', 'd2lquestionlibrary', 'questiondb.xml', 'Question Library')
        manifestEntity.addResource(manifestResource)

        manifest = parsedXml.createManifest(manifestEntity, question_library.folder_path)
        parsed_imsmanifest = ET.tostring(manifest.getroot(),encoding='utf-8', xml_declaration=True).decode()
        parsed_imsmanifest = parseString(parsed_imsmanifest)
        parsed_imsmanifest = parsed_imsmanifest.toprettyxml(indent="\t")
        question_library.imsmanifest_string = parsed_imsmanifest

        question_library.save()

        question_library.questiondb_string = parsedXml.questiondb_string
        question_library.save()

        imsmanifest_file = ContentFile(question_library.imsmanifest_string, name="imsmanifest.xml")
        question_library.imsmanifest_file = imsmanifest_file
        question_library.save()

        questiondb_file = ContentFile(question_library.questiondb_string, name="questiondb.xml")
        question_library.questiondb_file = questiondb_file
        question_library.save()


        with ZipFile(question_library.folder_path + '.zip', 'w') as myzip:
            myzip.write(question_library.questiondb_file.path, "questiondb.xml")
            myzip.write(question_library.imsmanifest_file.path, "imsmanifest.xml")
            # myzip.write(questionXMLPath, basename(questionXMLPath))
            # myzip.write(manifestXMLPath, basename(manifestXMLPath))
            for root, dirs, files in walk(questionLibraryEntity.imageLocalFolder) :
                for filename in files :
                    myzip.write(path.join(root, filename), questionLibraryEntity.imageFolder + '/' + filename)


        with open(question_library.folder_path + '.zip', 'rb') as f:
            print("------------------------")
            print(question_library.folder_path + '.zip')
            
            question_library.zip_file.save(name=str(question_library.id) + '.zip',content=File(f))
            # question_library.save()


        return Response("content")

# class QuerySession(APIView):
#     def post()
#         return "JSON object of the quiz including errors and state"


class CliUpload(APIView):

    permission_classes = (IsAuthenticated,)

    parser_classes = [MultiPartParser]

    def post(self, request):

        file_obj = request.FILES.get('file')

        print("CLIUPLOAD")
        question_library = QuestionLibrary.objects.create()
        question_library.folder_path = '/code/temp/' + str(question_library.id)
        question_library.image_path = question_library.folder_path + '/media/'

        # TODO get section name from CLI/Web
        # If no section name, use file name
        question_library.section_name = path.splitext(str(file_obj.name))[0]
        question_library.save()

        question_library.create_directory()
        question_library.temp_file=file_obj
        question_library.save()


        async_task('api_v1.tasks.runconversion', question_library)

        return Response("CliUpload")



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

