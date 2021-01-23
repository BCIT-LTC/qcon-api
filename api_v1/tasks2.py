from api_v1.antlr.L1Lexer import L1Lexer
from api_v1.antlr.L1Listener import L1Listener
from api_v1.antlr.L1Parser import L1Parser

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

from api_v1.L1Element import L1Element

# =============================================================================================
# =======================================L1 MAIN===============================================
# =============================================================================================
def parse_questions(question_library) :
    input = InputStream(question_library.pandoc_string)
    lexer = L1Lexer(input)
    stream = CommonTokenStream(lexer)
    parser = L1Parser(stream)
    tree = parser.l1()
    # 
    printer = L1Listener(question_library)
    walker = ParseTreeWalker()
    # print(tree.toStringTree(recog=parser))
    walker.walk(printer, tree)
    parsed_questions = printer.get_results()

    print("L1 done")

    # Populate L1 
    # Normalize array and grab indentations

    listofL1Elements = []    
    for element in parsed_questions:        
        L1 = L1Element()
        if element['listitem'] == True:
            indent_length, normalized_prefix = normalize_prefix_and_grab_indent(element['prefix'])
            L1.prefix = normalized_prefix
            L1.indentlength = indent_length  
        L1.content = element['content']
        L1.starmarked = element['correctprefix']
        L1.listitem = element['listitem']
        listofL1Elements.append(L1)

    # for element in listofL1Elements:
    #     print("==============")
    #     print("PREFIX " + str(element.prefix))
    #     print("CONTENT " + str(element.content))
    #     print("STARMARKED " + str(element.starmarked))
    #     print("LISTSEP " + str(element.listseparator))
    #     print("INDENTLEN " + str(element.indentlength))

    # Split questions
    
    questions_separated = question_separate(listofL1Elements, 0, 0)

    # for element in questions_separated:
    #     print(element)

    # Split AnswerBlock by marking beginning of it
    
    ending_found = True
    for i in range(len(questions_separated)-1, 0, -1):
        # print(questions_separated[i].prefix)
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

    # compile array or strings 
    collectionofstrings = []
    for i in range(0, len(questions_separated), 1):
        
        if questions_separated[i].questionseparator:
            collectionofstrings.append('##########START_QUESTION########\n')

        if questions_separated[i].answerblockseparator:
            collectionofstrings.append('##########START_ANSWER##########\n')
        
        # THIS IS FOR LIST ITEMS
        if questions_separated[i].listitem:
            if questions_separated[i].starmarked:
                collectionofstrings.append(questions_separated[i].prefix + "*." + questions_separated[i].content)
            else:
                collectionofstrings.append(questions_separated[i].prefix + "." + questions_separated[i].content)
        # THIS IS FOR REGULAR CONTENT (seperators, feedback markers, questionheader markers etc etc)
        else:
            collectionofstrings.append(questions_separated[i].content)


    thestring = ''
    for text in collectionofstrings:
        thestring += text
    print(thestring)
    # TODO: pass the split questions to the L2 grammar

    return None

# =============================================================================================
# ===============================Question Splitter=============================================
# =============================================================================================

def question_separate(data,index,question):
    # print("++++++++++++++")
    # print("index: " + str(index))
    # print("question " + str(question))
    # print("content " + str(data[index].content))

    if index == len(data) - 1:
        print("END question_separate")
        return data
    # else:
    #     return question_separate(data,index+1, question)
    if data[index].prefix.isnumeric():
        # print("it is num")
        if int(question) == 0:
            # print("first question")
            if int(data[index].prefix) == 1:
                data[index].questionseparator = True
                # print("================================================")
                return question_separate(data, index+1,question+1)
        # ++++++++++

        # try to find the next increment 
        if int(data[index].prefix) == int(question+1):
            #is this one FIB
            print("found next increment")
            if check_fib(data[index].content):
                print("FIB found")
                data[index].questionseparator = True
                return question_separate(data, index+1,question+1)
            else:
                # print("NO FIB")

                # look for letters before this
                if data[index-1].prefix.islower() or data[index-1].prefix.isupper():
                    data[index].questionseparator = True
                    return question_separate(data, index+1,question+1)
                else:
                    # print("check if number before skipping to next one ")
                    # check if number before skipping to next one 
                    if data[index-1].prefix.isnumeric():
                        # print("check if previous one is a separator  ")
                        # check if previous one is a separator 
                        if data[index-1].questionseparator:
                            # print("if it is then mark this one and continue")
                            #if it is then mark this one and continue
                            data[index].questionseparator = True
                            return question_separate(data, index+1,question+1)
                    else:
                        # if it is not numeric then it has to be a list separator 
                        # continue checking the previous one to this if it is letter
                        # if it is then mark and continue
                        # print("if it is not numeric then it has to be a list separator ")
                        if data[index-2].prefix.islower() or data[index-2].prefix.isupper():
                            data[index].questionseparator = True
                            return question_separate(data, index+1,question+1)
                        else:
                            # if it is not letter just continue 
                            # print("if it is not letter just continue ")
                            return question_separate(data, index+1,question)

                    return question_separate(data, index+1,question)
            # return question_separate(data, index+1,question)
        else:
            return question_separate(data, index+1,question)
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
        print("next number not found EOL")
        return 0
    return index

def find_index_of_previous_number(data, startindex):
    index = startindex-1
    while data[index].prefix.isnumeric() == False:
        index -= 1
    return index

def check_fib(content):
    x = re.search("[\[.*,.*\]]", content)
    if x:
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

    return indent_length,normalized_prefix

def normalize_content(content):
    # TODO: function to clean up extra characters on the content
    return content

def remove_prefix(text, prefix):
    return re.sub(r'^{0}'.format(re.escape(prefix)), '', text)

'''
def apply_question_separator(questionindex, listofL1Elements, mainindex, questions_separated, baselevel):

    print("==========")
    # print("MAIN INDEX: " + str(mainindex))
    # print("QUESTION INDEX: " + str(questionindex))
    print("CURRENT LINE: " + str(listofL1Elements[mainindex].prefix))
    # print("CURRENT CONTENT: " + str(listofL1Elements[mainindex].content))
    # print("INDENT: " + str(listofL1Elements[mainindex].indentlength))
    print("++++++++++")
    # base case
    # check if end of list
    if mainindex == len(listofL1Elements) - 1:
        print("END check recursive")
        L1 = L1Element()
        # L1.prefix='##########END_QUESTION##########'
        L1.questionseparator = True
        questions_separated.append(L1) 
        return questions_separated

    if listofL1Elements[mainindex].listseparator:
        print("SEPARTORO FOUNDD")    
        print("Compare " + listofL1Elements[mainindex+1].prefix +" "+ str(questionindex+1))
        
        # Check if next element is number        
        if listofL1Elements[mainindex+1].prefix.isnumeric():
            # Check if next element is increment of lastquestion
            if int(listofL1Elements[mainindex+1].prefix) == int(questionindex+1):
        #     # listofL1Elements[mainindex].questionseparator = True;
        #     questions_separated.append(listofL1Elements[mainindex])
                print("SEPARTORO APPLIED")
                L1 = L1Element()
                L1.questionseparator = True
                questions_separated.append(L1) 
                return apply_question_separator(questionindex, listofL1Elements, mainindex+1, questions_separated, baselevel)
            else:
                print("SEPARTORO forward")
                questions_separated.append(listofL1Elements[mainindex]) 
                return apply_question_separator(questionindex, listofL1Elements, mainindex+1, questions_separated, baselevel)
        return apply_question_separator(questionindex, listofL1Elements, mainindex+1, questions_separated, baselevel)

    if listofL1Elements[mainindex].prefix.isnumeric():
        print("nummber iss FOUNDD")
        print("sep befpre "+ str(listofL1Elements[mainindex-1].listseparator))
        if listofL1Elements[mainindex-1].listseparator:  # question seperator added before
            print("check previous for separator")
            print(str(listofL1Elements[mainindex].prefix) + " "+ str(questionindex+1))
            if int(listofL1Elements[mainindex].prefix) == int(questionindex+1):
                print("isincrment here ")
                questions_separated.append(listofL1Elements[mainindex])
                return apply_question_separator(int(listofL1Elements[mainindex].prefix), listofL1Elements, mainindex+1, questions_separated, baselevel)
            else:
                print("is not increment")
                questions_separated.append(listofL1Elements[mainindex])
                return apply_question_separator(questionindex, listofL1Elements, mainindex+1, questions_separated, baselevel)
        else: # no question seperator added before

            if listofL1Elements[mainindex].prefix == int(questionindex+1): # is increment
                #check if previous element was number
                if listofL1Elements[mainindex-1].prefix.isnumeric():
                    #check if FIB

                    # else 
                    # do not increment question
                    L1 = L1Element()
                    L1.questionseparator = True
                    questions_separated.append(L1) 
                    return apply_question_separator(questionindex+1, listofL1Elements, mainindex+1, questions_separated, baselevel)
            questions_separated.append(listofL1Elements[mainindex])
            return apply_question_separator(questionindex, listofL1Elements, mainindex+1, questions_separated, baselevel)
    else:
        if listofL1Elements[mainindex].listseparator is not True:
            print("letterrrrr")
            questions_separated.append(listofL1Elements[mainindex])
            return apply_question_separator(questionindex, listofL1Elements, mainindex+1, questions_separated, baselevel)
'''


def runconversion(question_library):

    print(datetime.now().strftime("%H:%M:%S"), "Starting task ID:", question_library.id)

    start = time.time()
    question_library.checkpoint = 0
    question_library.checkpoint_failed = 0
    question_library.save()

    # Pandoc string create ===================================================================================
    print(datetime.now().strftime("%H:%M:%S"), "Pandoc processing...")
    try:
        pandocstring = pypandoc.convert_file(question_library.temp_file.path, format='docx', to='markdown_github+fancy_lists+emoji+hard_line_breaks+all_symbols_escapable+escaped_line_breaks+grid_tables+startnum', extra_args=['--extract-media='+ question_library.folder_path, '--no-highlight', '--self-contained', '--atx-headers', '--preserve-tabs', '--wrap=preserve'])
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
        
    return "Task {} Finished successfully".format(question_library.id) 