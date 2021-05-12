from api_v2.questionsplitter.L1Lexer import L1Lexer
from api_v2.questionsplitter.L1Listener import L1Listener
from api_v2.questionsplitter.L1Parser import L1Parser

from api_v2.questionsplitter.L1Element import L1Element

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

import pypandoc
import re
import logging
L1Converter_Logger = logging.getLogger('api_v2.questionsplitter.L1Converter')


def L1Converter(question_library):
    try:
        input = InputStream(question_library.pandoc_string)
        lexer = L1Lexer(input)
        stream = CommonTokenStream(lexer)
        parser = L1Parser(stream)
        # parser.addErrorListener(CustomL1ErrorListener)
        tree = parser.l1()
        #
        printer = L1Listener(question_library)
        walker = ParseTreeWalker()
        # print(tree.toStringTree(recog=parser))
        walker.walk(printer, tree)
        parsed_questions = printer.get_results()
    except:
        L1Converter_Logger.error("[" + str(question_library.transaction.id) +
                                 "]" +
                                 "ANTLR LEXER failed and cannot continue")
        question_library.error = "Error Splitting the questions"
        question_library.save()

    # Populate L1
    # Normalize array and grab indentations
    listofL1Elements = []
    for element in parsed_questions:
        L1 = L1Element()
        if element['listitem'] == True:
            normalized_prefix = normalize_prefix(element['prefix'])
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
    #     print("endanswer" + str(element.endanswers))

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
        L1Converter_Logger.error("Detected: " + str(number_of_questions) +
                                 " Expected: " + str(highest_numbered_index))
        question_library.error = "Detected: " + str(
            number_of_questions) + " Expected: " + str(highest_numbered_index)
        question_library.save()

    # Split AnswerBlock by marking beginning of it

    ending_found = True
    for i in range(len(questions_separated) - 1, 0, -1):
        if ending_found:
            # print("check if letter a or A")
            if questions_separated[i].prefix == 'a' or questions_separated[
                    i].prefix == 'A':
                # print("begin of answerlist found")
                # questions_separated.insert(i, '##########START_ANSWER##########')
                questions_separated[i].answerblockseparator = True
                ending_found = False
        if questions_separated[i].questionseparator:
            # print("check if ending found")
            ending_found = True
        # if questions_separated[i] == '##########END_QUESTION##########':
        #     ending_found = True

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
                collectionofstrings.append(questions_separated[i].prefix +
                                           ". \*" +
                                           questions_separated[i].content)
            else:
                collectionofstrings.append(questions_separated[i].prefix +
                                           ". " +
                                           questions_separated[i].content)
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

        # Test EDGE cases
        # if check_fib(data[index].content):
        #     data[index].questionseparator = True
        #     return data, question + 1

        if data[index].prefix.isnumeric():
            if int(data[index].prefix) == int(question + 1):
                data[index].questionseparator = True
                return data, question + 1

        return data, question

    if data[index].prefix.isnumeric():
        # print("it is num")
        if int(question) == 0:
            # print("first question")
            if int(data[index].prefix) == 1:
                data[index].questionseparator = True
                # print("================================================")
                return question_separate(data, index + 1, question + 1)
        # ++++++++++

        # try to find the next increment
        if int(data[index].prefix) == int(question + 1):
            # is this one FIB
            # print("found next increment")
            if check_fib(data[index].content):
                # print("FIB found")
                data[index].questionseparator = True
                return question_separate(data, index + 1, question + 1)
            else:
                # print("NO FIB")

                # look for letters before this

                # print("check if previous is listitem")
                # print(data[index-1].listitem)

                if data[index - 1].listitem:
                    if data[index -
                            1].prefix.islower() or data[index -
                                                        1].prefix.isupper():
                        data[index].questionseparator = True
                        return question_separate(data, index + 1, question + 1)
                    else:
                        # print("check if number before skipping to next one ")
                        # check if number before skipping to next one
                        if data[index - 1].prefix.isnumeric():
                            # print("check if previous one is a separator  ")
                            # check if previous one is a separator
                            if data[index - 1].questionseparator:
                                # print("if it is then mark this one and continue")
                                # if it is then mark this one and continue
                                data[index].questionseparator = True
                                return question_separate(
                                    data, index + 1, question + 1)
                        else:
                            # if it is not numeric then it has to be a list separator
                            # continue checking the previous one to this if it is letter
                            # if it is then mark and continue
                            # print("if it is not numeric then it has to be a list separator ")
                            if data[index - 2].prefix.islower() or data[
                                    index - 2].prefix.isupper():
                                data[index].questionseparator = True
                                return question_separate(
                                    data, index + 1, question + 1)
                            else:
                                # if it is not letter just continue
                                # print("if it is not letter just continue ")
                                return question_separate(
                                    data, index + 1, question)

                        return question_separate(data, index + 1, question)
                else:
                    # Previous is Questionheader item this means Mark it as separator and continue
                    # print("previous is not a listItem possibly a Questionheader item")
                    data[index].questionseparator = True
                    return question_separate(data, index + 1, question + 1)

            # return question_separate(data, index+1,question)
        else:
            return question_separate(data, index + 1, question)
    else:
        return question_separate(data, index + 1, question)


# =============================================================================================
# ===============================HELPER FUNCTIONS==============================================
# =============================================================================================


def find_index_of_next_number(data, startindex):
    index = int(startindex) + 1
    while data[index].prefix.isnumeric() == False:
        # print("hhhHJKDLLKDHJS " + str(index) + " " + str(len(data)) )
        if int(index) == (len(data) - 1):
            break
        index += 1

    if int(index) == (len(data) - 1):
        # print("next number not found EOL")
        return 0
    return index


def find_index_of_previous_number(data, startindex):
    index = startindex - 1
    while data[index].prefix.isnumeric() == False:
        index -= 1
    return index


def check_fib(content):
    # Create HTML string first to filter out images and other tags that will interfere with the regex
    html_text = pypandoc.convert_text(
        content,
        format="markdown_github+fancy_lists+emoji+task_lists+hard_line_breaks",
        to="html",
        extra_args=["--mathml", '--ascii'])
    x = re.search(r"\[(.*?)\]", html_text)
    if x:
        # print("FIB found in detector")

        return True
    else:
        return False


def normalize_prefix(prefix):
    # x = re.findall("^(\\n)(.*)([a-zA-Z0-9]{1,2})", prefix)
    x = re.sub("\n", "", prefix)
    x = re.search("[a-zA-Z0-9]{1,3}", x)
    # x = re.findall("^(\\n)\s*([a-zA-Z0-9]*)", prefix)
    normalized_prefix = str(x.group())
    return normalized_prefix


def normalize_content(content):
    # TODO: function to clean up extra characters on the content
    return content