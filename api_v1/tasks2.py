from api_v1.antlr.L1Lexer import L1Lexer
from api_v1.antlr.L1Listener import L1Listener
from api_v1.antlr.L1Parser import L1Parser

from api_v1.antlr.QuestionLexer import QuestionLexer
from api_v1.antlr.QuestionParserListener import QuestionParserListener
from api_v1.antlr.QuestionParser import QuestionParser

from api_v1.antlr.QconLexer import QconLexer
from api_v1.antlr.QconListener import QconListener
from api_v1.antlr.QconParser import QconParser

from api_v1.scorm.XmlWriter import XmlWriter
from api_v1.scorm.manifest import ManifestEntity, ManifestResourceEntity

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
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

from api_v1.L1Element import L1Element


import logging
# from logging.handlers import TimedRotatingFileHandler
# logname = "my_app.log"
# handler = TimedRotatingFileHandler(logname, when="midnight", interval=1)
# handler.suffix = "%Y%m%d"

L1Converter_Logger = logging.getLogger('api_v1.L1Converter')
Main_Logger = logging.getLogger('api_v1.QuestionParser')



TransactionID = None

class CustomL1ErrorListener(ErrorListener):
    def __init__(self):
        super(CustomL1ErrorListener, self).__init__()

    def syntaxError(self, recognizer, line, offendingSymbol, msg, column):
        Main_Logger.warn("["+str(TransactionID) +"]" + "ANTLR Error: line " + str(line)+ ":" + str(offendingSymbol) + " " + msg)
        pass

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        # raise Exception("ANTLR error")
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        # raise Exception("ANTLR error")
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        # raise Exception("ANTLR error")
        pass

    # def reportError(self, recognizer:Parser, e:RecognitionException):
    #     raise Exception(e)


# =============================================================================================
# =======================================L1 MAIN===============================================
# =============================================================================================
def L1Converter(question_library):
    input = InputStream(question_library.pandoc_string)
    lexer = L1Lexer(input)
    stream = CommonTokenStream(lexer)
    parser = L1Parser(stream)
    parser.addErrorListener(CustomL1ErrorListener)
    tree = parser.l1()
    #
    printer = L1Listener(question_library)
    walker = ParseTreeWalker()
    # print(tree.toStringTree(recog=parser))
    walker.walk(printer, tree)
    parsed_questions = printer.get_results()

    # Populate L1
    # Normalize array and grab indentations

    # logger.info('Something went wrong!')
    # logger.warning('Something went wrong!')
    # logger.debug('Something went wrong!')

    listofL1Elements = []
    for element in parsed_questions:
        L1 = L1Element()
        if element['listitem'] == True:
            indent_length, normalized_prefix = normalize_prefix_and_grab_indent(
                element['prefix'])
            L1.prefix = normalized_prefix
            # L1.indentlength = indent_length
        L1.content = element['content']
        L1.starmarked = element['correctprefix']
        L1.listitem = element['listitem']
        L1.questionheader = element['questionheader']
        L1.sectionheader = element['sectionheader']
        L1.endanswers = element['endanswer']
        listofL1Elements.append(L1)

    # for element in listofL1Elements:
    #     print("==============")
    #     print("PREFIX " + str(element.prefix))
    #     print("CONTENT " + str(element.content))
    #     print("STARMARKED " + str(element.starmarked))
    #     print("LISTITEM " + str(element.listitem))
    #     print("questionseparator " + str(element.questionseparator))
    #     print("answerblockseparator " + str(element.answerblockseparator))
    #     print("questionheader " + str(element.questionheader))
    #     print("sectionheader " + str(element.sectionheader))

    # Split questions

    questions_separated, number_of_questions = question_separate(
        listofL1Elements, 0, 0)

    # Check if number of questions is equal to higher index value found

    highest_numbered_index = 0
    for element in questions_separated:
        if element.prefix.isnumeric():
            if int(element.prefix) > int(highest_numbered_index):
                highest_numbered_index = element.prefix
    # print("questions detected: " + str(number_of_questions) + " expected: " + str(highest_numbered_index))

    if int(number_of_questions) != int(highest_numbered_index):
        L1Converter_Logger.error(
            "Detected: " + str(number_of_questions) + " Expected: " + str(highest_numbered_index))

    # Split AnswerBlock by marking beginning of it

    ending_found = True
    for i in range(len(questions_separated)-1, 0, -1):
        if ending_found:
            # print("check if letter a or A")
            if questions_separated[i].prefix == 'a' or questions_separated[i].prefix == 'A':
                # print("begin of answerlist found")
                # questions_separated.insert(i, '##########START_ANSWER##########')
                questions_separated[i].answerblockseparator = True
                ending_found = False
        if questions_separated[i].questionseparator:
            # print("check if ending found")
            ending_found = True
        # if questions_separated[i] == '##########END_QUESTION##########':
        #     ending_found = True

    # for line in questions_separated:
    #     print(line)

    # ADD MARKER AND APPEND ARRAYS TO ONE STRING
    collectionofstrings = []
    for i in range(0, len(questions_separated), 1):

        if questions_separated[i].sectionheader:
            collectionofstrings.append('##########_SECTION_##########\n')

        if questions_separated[i].questionheader:
            collectionofstrings.append(
                '##########_QUESTION_HEADER_##########\n')

        if questions_separated[i].questionseparator:
            collectionofstrings.append(
                '##########_START_QUESTION_##########\n')

        if questions_separated[i].answerblockseparator:
            collectionofstrings.append('##########_START_ANSWER_##########\n')

        if questions_separated[i].endanswers:
            collectionofstrings.append('##########_END_ANSWERS_##########\n')

        # THIS IS FOR LIST ITEMS
        if questions_separated[i].listitem:
            if questions_separated[i].starmarked:
                collectionofstrings.append(
                    questions_separated[i].prefix + ". \*" + questions_separated[i].content)
            else:
                collectionofstrings.append(
                    questions_separated[i].prefix + ". " + questions_separated[i].content)
        # THIS IS FOR REGULAR CONTENT (seperators, feedback markers, questionheader markers etc etc)
        else:
            collectionofstrings.append(questions_separated[i].content)

    thestring = ''
    for text in collectionofstrings:
        thestring += text

    return thestring

# =============================================================================================
# ===============================Question Splitter=============================================
# =============================================================================================


def question_separate(data, index, question):
    # print("++++++++++++++")
    # print("index: " + str(index))
    # print("question " + str(question))
    # print("prefix " + str(data[index].prefix))
    # print("content " + str(data[index].content))

    if index == len(data) - 1:

        if check_fib(data[index].content):
            # print("FIB found at end")
            data[index].questionseparator = True
            return data

        # print("END question_separate")
        return data, question
    # else:
    #     return question_separate(data,index+1, question)
    if data[index].prefix.isnumeric():
        # print("it is num")
        if int(question) == 0:
            # print("first question")
            if int(data[index].prefix) == 1:
                data[index].questionseparator = True
                # print("================================================")
                return question_separate(data, index+1, question+1)
        # ++++++++++

        # try to find the next increment
        if int(data[index].prefix) == int(question+1):
            # is this one FIB
            # print("found next increment")
            if check_fib(data[index].content):
                # print("FIB found")
                data[index].questionseparator = True
                return question_separate(data, index+1, question+1)
            else:
                # print("NO FIB")

                # look for letters before this
                if data[index-1].prefix.islower() or data[index-1].prefix.isupper():
                    data[index].questionseparator = True
                    return question_separate(data, index+1, question+1)
                else:
                    # print("check if number before skipping to next one ")
                    # check if number before skipping to next one
                    if data[index-1].prefix.isnumeric():
                        # print("check if previous one is a separator  ")
                        # check if previous one is a separator
                        if data[index-1].questionseparator:
                            # print("if it is then mark this one and continue")
                            # if it is then mark this one and continue
                            data[index].questionseparator = True
                            return question_separate(data, index+1, question+1)
                    else:
                        # if it is not numeric then it has to be a list separator
                        # continue checking the previous one to this if it is letter
                        # if it is then mark and continue
                        # print("if it is not numeric then it has to be a list separator ")
                        if data[index-2].prefix.islower() or data[index-2].prefix.isupper():
                            data[index].questionseparator = True
                            return question_separate(data, index+1, question+1)
                        else:
                            # if it is not letter just continue
                            # print("if it is not letter just continue ")
                            return question_separate(data, index+1, question)

                    return question_separate(data, index+1, question)
            # return question_separate(data, index+1,question)
        else:
            return question_separate(data, index+1, question)
    else:
        return question_separate(data, index+1, question)

# =============================================================================================
# ===============================HELPER FUNCTIONS==============================================
# =============================================================================================


def find_index_of_next_number(data, startindex):
    index = int(startindex)+1
    while data[index].prefix.isnumeric() == False:
        # print("hhhHJKDLLKDHJS " + str(index) + " " + str(len(data)) )
        if int(index) == (len(data)-1):
            break
        index += 1

    if int(index) == (len(data)-1):
        # print("next number not found EOL")
        return 0
    return index


def find_index_of_previous_number(data, startindex):
    index = startindex-1
    while data[index].prefix.isnumeric() == False:
        index -= 1
    return index


def check_fib(content):
    # Create HTML string first to filter out images and other tags that will interfere with the regex
    html_text = pypandoc.convert_text(
        content, format="markdown_github+fancy_lists+emoji+task_lists+hard_line_breaks", to="html", extra_args=["--mathml", '--ascii'])
    x = re.search(r"\[(.*?)\]", html_text)
    if x:
        # print("FIB found in detector")
        return True
    else:
        return False


def normalize_prefix_and_grab_indent(prefix):
    # TODO: function to clean up extra characters on the prefix
    x = re.findall("^(\\n)(>?[ ]*)([a-zA-Z0-9]+)", prefix)
    # print("indent length " + str(len(x[0][1])))
    # print("normalized prefix " + str(x[0][2]))
    indent_length = len(x[0][1])
    normalized_prefix = str(x[0][2])

    return indent_length, normalized_prefix


def normalize_content(content):
    # TODO: function to clean up extra characters on the content
    return content


def remove_prefix(text, prefix):
    return re.sub(r'^{0}'.format(re.escape(prefix)), '', text)

# =============================================================================================
# =================================RUN CONVERSION==============================================
# =============================================================================================


def question_parser(question_library, text_string):
    input = InputStream(text_string)
    lexer = QuestionLexer(input)
    tokens = CommonTokenStream(lexer)
    parser = QuestionParser(tokens)
    tree = parser.parse_question()
    listener = QuestionParserListener(question_library)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    # print(tree.toStringTree(recog=parser))
    parsed_questions = listener.get_results()

    return parsed_questions


def runconversion(question_library):

    # print(datetime.now().strftime("%H:%M:%S"), "Starting task ID:", question_library.id)
    # Main_Logger.info("Transaction Started : " + "[" + str(question_library.id) + "]")
    Main_Logger.info("["+str(question_library.id) + "] " +
                     "<<<<<<<<<<Transaction Started<<<<<<<<<<")
    global TransactionID
    TransactionID = question_library.id
    # start = time.time()
    # question_library.checkpoint = 0
    # question_library.checkpoint_failed = 0
    # question_library.save()

    # Pandoc string create ===================================================================================
    # print(datetime.now().strftime("%H:%M:%S"), "Pandoc processing...")
    try:
        pandocstring = pypandoc.convert_file(question_library.temp_file.path, format='docx', to='markdown_github+fancy_lists+emoji+hard_line_breaks+all_symbols_escapable+escaped_line_breaks+grid_tables+startnum', extra_args=[
                                             '--extract-media=' + question_library.folder_path, '--no-highlight', '--self-contained', '--atx-headers', '--preserve-tabs', '--wrap=preserve'])
        question_library.pandoc_string = "\n" + pandocstring
        # question_library.checkpoint = 1
        question_library.save()
        # raise Exception('')
        Main_Logger.info("["+str(question_library.id) +
                         "] " + "Markdown String Created")
        # print(datetime.now().strftime("%H:%M:%S"), "Pandoc Done!")
    except Exception as e:
        # question_library.checkpoint_failed = 1
        Main_Logger.error("["+str(question_library.id) +
                          "] " + "Markdown String Failed")
        return None

    # Starting Antler AST conversion
    # Antler parsing  ===================================================================================
    # print(datetime.now().strftime("%H:%M:%S"), "Antlr processing...")

    try:
        L1_result = L1Converter(question_library)
        L1_result = "\n" + L1_result
        parsed_questions_result = question_parser(question_library, L1_result)
        # print(datetime.now().strftime("%H:%M:%S"), "Antlr Done!")
        # question_library.checkpoint = 2
        question_library.save()
        # raise Exception('')
        Main_Logger.info(
            "["+str(question_library.id) + "] " + "Parser Finished")
    except Exception as e:
        Main_Logger.error(
            "["+str(question_library.id) + "] " + "Parser Failed")
        return None

    # ImsManifest string create ===================================================================================
    # print(datetime.now().strftime("%H:%M:%S"), "Creating imsmanifext string...")
    try:
        parsed_xml = XmlWriter(question_library, parsed_questions_result)
        manifest_entity = ManifestEntity()
        manifest_resource_entity = ManifestResourceEntity(
            'res_question_library', 'webcontent', 'd2lquestionlibrary', 'questiondb.xml', 'Question Library')
        manifest_entity.add_resource(manifest_resource_entity)
        manifest = parsed_xml.create_manifest(
            manifest_entity, question_library.folder_path)
        parsed_imsmanifest = ET.tostring(
            manifest.getroot(), encoding='utf-8', xml_declaration=True).decode()
        parsed_imsmanifest = parseString(parsed_imsmanifest)
        parsed_imsmanifest = parsed_imsmanifest.toprettyxml(indent="\t")
        question_library.imsmanifest_string = parsed_imsmanifest
        question_library.save()

        Main_Logger.info("["+str(question_library.id) +
                         "] " + "imsmanifest String Created")
        # print(datetime.now().strftime("%H:%M:%S"), "imsmanifext string created!")
    except Exception as e:
        Main_Logger.error("["+str(question_library.id) +
                          "] " + "imsmanifest String Failed")
        return None

    # ImsManifest Save File ===================================================================================

    try:
        # print(datetime.now().strftime("%H:%M:%S"), "Creating questiondb string...")
        questiondb_string = parsed_xml.questiondb_string
        img_elements = re.findall(
            r"\<img.*?\>", questiondb_string, re.MULTILINE)

        for idx, img in enumerate(img_elements):
            element = re.findall(r"src=\"(.*?)\"", img, re.MULTILINE)
            new_img = '<img src="{0}" alt="{1}" />'.format(
                './media/' + basename(element[0]), basename(element[0]))
            questiondb_string = questiondb_string.replace(
                img_elements[idx], new_img)

        question_library.questiondb_string = questiondb_string
        question_library.save()

        imsmanifest_file = ContentFile(
            question_library.imsmanifest_string, name="imsmanifest.xml")
        question_library.imsmanifest_file = imsmanifest_file
        # question_library.checkpoint = 4;
        question_library.save()
        Main_Logger.info("["+str(question_library.id) +
                         "] " + "QuestionDB String Created")
        # print(question_library.imsmanifest_file.name)
        # print(datetime.now().strftime("%H:%M:%S"), "questiondb string created!")
    except Exception as e:
        Main_Logger.error("["+str(question_library.id) +
                          "] " + "QuestionDB String Failed")
        return None
    # Questiondb string create ===================================================================================

    # print(datetime.now().strftime("%H:%M:%S"), "Creating imsmanifest.xml and questiondb.xml...")
    try:
        questiondb_file = ContentFile(
            question_library.questiondb_string, name="questiondb.xml")
        question_library.questiondb_file = questiondb_file
        # question_library.checkpoint = 5;
        question_library.save()
        Main_Logger.info(
            "["+str(question_library.id) + "] " + "XML files Created")
        # print(datetime.now().strftime("%H:%M:%S"), "imsmanifest.xml and questiondb.xml created!")
    except Exception as e:
        Main_Logger.error(
            "["+str(question_library.id) + "] " + "XML files Failed")
        return None

    # Questiondb string create ===================================================================================
    # print(datetime.now().strftime("%H:%M:%S"), "Creating scorm zip file...")
    try:
        with ZipFile(question_library.folder_path + "/" + question_library.section_name + '.zip', 'w') as myzip:
            myzip.write(question_library.questiondb_file.path,
                        "questiondb.xml")
            myzip.write(question_library.imsmanifest_file.path,
                        "imsmanifest.xml")
            for root, dirs, files in walk(question_library.image_path):
                for filename in files:
                    myzip.write(path.join(root, filename),
                                '/media/' + filename)

        question_library.zip_file.name = str(
            question_library.id) + "/" + question_library.section_name + '.zip'
        question_library.save()
        Main_Logger.info(
            "["+str(question_library.id) + "] " + "ZIP file Created")
    except Exception as e:
        Main_Logger.error(
            "["+str(question_library.id) + "] " + "ZIP file Failed")
        return None

    Main_Logger.info("["+str(question_library.id) + "] " +
                     ">>>>>>>>>>Transaction Finished>>>>>>>>>>")
    return None
