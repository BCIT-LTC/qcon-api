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


class QuestionLibraryEntity(object):
    def __init__(self, file_name, sectionFolderName, imageFolder, imageLocalFolder) :
        self.zipFileName = file_name
        self.sectionFolderName = sectionFolderName if sectionFolderName else self.zipFileName
        self.imageFolder = imageFolder if imageFolder else ''
        self.imageLocalFolder = imageLocalFolder


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


def runconversion(question_library):

    print("This is the task boiiiiii")
    print(question_library)


    # Pandoc string create ===================================================================================

    pandocstring = pypandoc.convert_file(question_library.temp_file.path, format='docx', to='markdown_github+fancy_lists+emoji+hard_line_breaks+all_symbols_escapable+escaped_line_breaks', extra_args=['--preserve-tabs', '--wrap=preserve'])
    question_library.pandoc_string = "\n" + pandocstring
    question_library.save()
    # Starting Antler AST conversion


    # Antler parsing  ===================================================================================

    parsed_questions = parse_questions(question_library)



    # ImsManifest string create ===================================================================================

    file_name = "EXAM-1"
    section_name = "Section_EXAM-1"
    imageFolder = ""
    imageLocalFolder = ""

    questionLibraryEntity = QuestionLibraryEntity(file_name, section_name, imageFolder, imageLocalFolder)
    
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


    # ImsManifest Save File ===================================================================================


    question_library.questiondb_string = parsedXml.questiondb_string
    question_library.save()

    imsmanifest_file = ContentFile(question_library.imsmanifest_string, name="imsmanifest.xml")
    question_library.imsmanifest_file = imsmanifest_file
    question_library.save()

    # Questiondb string create ===================================================================================

    questiondb_file = ContentFile(question_library.questiondb_string, name="questiondb.xml")
    question_library.questiondb_file = questiondb_file
    question_library.save()

    # Questiondb string create ===================================================================================

    with ZipFile(question_library.folder_path + '.zip', 'w') as myzip:
        myzip.write(question_library.questiondb_file.path, "questiondb.xml")
        myzip.write(question_library.imsmanifest_file.path, "imsmanifest.xml")
        # for root, dirs, files in walk(questionLibraryEntity.imageLocalFolder) :
        #     for filename in files :
        #         myzip.write(path.join(root, filename), questionLibraryEntity.imageFolder + '/' + filename)

    print(question_library.folder_path)

    with open(question_library.folder_path + '.zip', 'rb') as f:
        print("------------------------")
        print(question_library.folder_path + '.zip')
        
        question_library.zip_file.save(name=str(question_library.id) + '.zip',content=File(f))


    return None