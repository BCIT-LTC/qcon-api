from api_v1.antlr.QconLexer import QconLexer
from api_v1.antlr.QconListener import QconListener
from api_v1.antlr.QconParser import QconParser
from api_v1.scorm.XmlWriter import XmlWriter
from api_v1.scorm.manifest import ManifestEntity, ManifestResourceEntity

from antlr4 import *
import json
import sys
import pypandoc
import re
from zipfile import *
from os.path import basename
from os import makedirs, path, walk
from xml.dom.minidom import parseString
from django.core.files.base import ContentFile
from django.core.files import File
from datetime import datetime
import xml.etree.cElementTree as ET

import time

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

    print(datetime.now().strftime("%H:%M:%S"), "Starting task ID:", question_library.id)

    start = time.time()
    question_library.checkpoint = 0
    question_library.checkpoint_failed = 0
    question_library.save()

    # Pandoc string create ===================================================================================
    print(datetime.now().strftime("%H:%M:%S"), "Pandoc processing...")
    try:
        pandocstring = pypandoc.convert_file(question_library.temp_file.path, format='docx', to='markdown_github+fancy_lists+emoji+hard_line_breaks+all_symbols_escapable+escaped_line_breaks+grid_tables', extra_args=['--extract-media='+ question_library.folder_path, '--no-highlight', '--self-contained', '--atx-headers', '--preserve-tabs', '--wrap=preserve'])
        question_library.pandoc_string = "\n" + pandocstring
        question_library.checkpoint = 1
        question_library.save()

        print(datetime.now().strftime("%H:%M:%S"), "Pandoc Done!")
    except:
        question_library.checkpoint_failed = 1
        question_library.save()
        return "Error at Checkpoint 1"
   

    # Starting Antler AST conversion
    # Antler parsing  ===================================================================================
    print(datetime.now().strftime("%H:%M:%S"), "Antlr processing...")
    try:
        parsed_questions = parse_questions(question_library)
        print(datetime.now().strftime("%H:%M:%S"), "Antlr Done!")
        question_library.checkpoint = 2
        question_library.save()
    except:
        question_library.checkpoint_failed = 2
        question_library.save()
        return "Error at Checkpoint 2"

    # ImsManifest string create ===================================================================================
    print(datetime.now().strftime("%H:%M:%S"), "Creating imsmanifext string...")
    try:              
        parsed_xml = XmlWriter(question_library, parsed_questions)
        manifest_entity = ManifestEntity()
        manifest_resource_entity = ManifestResourceEntity('res_question_library', 'webcontent', 'd2lquestionlibrary', 'questiondb.xml', 'Question Library')
        manifest_entity.add_resource(manifest_resource_entity)

        manifest = parsed_xml.create_manifest(manifest_entity, question_library.folder_path)
        parsed_imsmanifest = ET.tostring(manifest.getroot(),encoding='utf-8', xml_declaration=True).decode()
        parsed_imsmanifest = parseString(parsed_imsmanifest)
        parsed_imsmanifest = parsed_imsmanifest.toprettyxml(indent="\t")
        question_library.imsmanifest_string = parsed_imsmanifest
        question_library.checkpoint = 3
        question_library.save()

        print(datetime.now().strftime("%H:%M:%S"), "imsmanifext string created!")
    except:
        question_library.save()
        return "Error at Checkpoint 3"

    # ImsManifest Save File ===================================================================================

    try:
        print(datetime.now().strftime("%H:%M:%S"), "Creating questiondb string...")
        questiondb_string = parsed_xml.questiondb_string
        img_elements = re.findall(r"\<img.*?\>", questiondb_string, re.MULTILINE)

        for idx, img in enumerate(img_elements):
            element = re.findall(r"src=\"(.*?)\"", img, re.MULTILINE)
            new_img = '<img src="{0}" alt="{1}" />'.format('./media/' + basename(element[0]), basename(element[0]))
            questiondb_string = questiondb_string.replace(img_elements[idx], new_img)

        question_library.questiondb_string = questiondb_string
        question_library.save()

        imsmanifest_file = ContentFile(question_library.imsmanifest_string, name="imsmanifest.xml")
        question_library.imsmanifest_file = imsmanifest_file
        question_library.checkpoint = 4;
        question_library.save()
        print(question_library.imsmanifest_file.name)
        print(datetime.now().strftime("%H:%M:%S"), "questiondb string created!")
    except:
        question_library.save()
        return "Error at Checkpoint 4"
    # Questiondb string create ===================================================================================

    print(datetime.now().strftime("%H:%M:%S"), "Creating imsmanifest.xml and questiondb.xml...")
    try:        
        questiondb_file = ContentFile(question_library.questiondb_string, name="questiondb.xml")
        question_library.questiondb_file = questiondb_file
        question_library.checkpoint = 5;
        question_library.save()

        print(datetime.now().strftime("%H:%M:%S"), "imsmanifest.xml and questiondb.xml created!")
    except:
        question_library.checkpoint_failed = 5
        question_library.save()
        return "Error at Checkpoint 5"

    # Questiondb string create ===================================================================================
    print(datetime.now().strftime("%H:%M:%S"), "Creating scorm zip file...")
    try:
        with ZipFile(question_library.folder_path + "/" + question_library.section_name + '.zip', 'w') as myzip:
            myzip.write(question_library.questiondb_file.path, "questiondb.xml")
            myzip.write(question_library.imsmanifest_file.path, "imsmanifest.xml")
            for root, dirs, files in walk(question_library.image_path) :
                for filename in files :
                    myzip.write(path.join(root, filename), '/media/' + filename)
                    
        question_library.zip_file.name = str(question_library.id) + "/" + question_library.section_name + '.zip'
        question_library.save()
        end = time.time()
        question_library.checkpoint = 6;
        question_library.time_delta = end-start
        question_library.save()
        print(datetime.now().strftime("%H:%M:%S"), "Scorm zip file created!")
        print("\n")
    except:
        question_library.checkpoint_failed = 6
        question_library.save()
        return "Error at Checkpoint 6"
    
    return "Task {} Finished successfully".format(question_library.id) 