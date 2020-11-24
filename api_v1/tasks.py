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

    print("Starting task ID:", question_library.id)
    print()


    # Pandoc string create ===================================================================================

    pandocstring = pypandoc.convert_file(question_library.temp_file.path, format='docx', to='markdown_github+fancy_lists+emoji+hard_line_breaks+all_symbols_escapable+escaped_line_breaks', extra_args=['--resource-path='+ question_library.folder_path, '--extract-media='+ question_library.folder_path, '--preserve-tabs', '--wrap=preserve'])
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

    
    parsedXml = XmlWriter(question_library, parsed_questions)

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
    
    with ZipFile(question_library.folder_path + "/" + str(question_library.id) + '.zip', 'w') as myzip:
        myzip.write(question_library.questiondb_file.path, "questiondb.xml")
        myzip.write(question_library.imsmanifest_file.path, "imsmanifest.xml")
        for root, dirs, files in walk(question_library.image_path) :
            for filename in files :
                myzip.write(path.join(root, filename), '/media/' + filename)

    print(question_library.folder_path + "/" + str(question_library.id) +'.zip')
    question_library.zip_file.name = question_library.folder_path + "/" + str(question_library.id) + '.zip'
    question_library.save()

    return None