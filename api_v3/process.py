import os

def create_section_name():
    pass


# Input markdown , Output Root elements(optional RootHeader, Mandatory Body and optional Answers)
# No writing to model here
# def markdown_to_root_elements(questionlibrary):

#     from api_v3.formatter.formatter import formatter
#     formatter(questionlibrary)

#     pass


def run_formatter(questionlibrary):

    os.chdir('/formatter/jarfile')
    # filename = '/code/temp/' +  questionlibrary.pandoc_output_file.name
    destination = '/code/temp/' + str(questionlibrary.id) + '/'
    # print(destination)
    os.system('java -cp formatter.jar:* formatter ' + destination)
    os.chdir('/code')

    pass


# Input Body , Output Array of 1 or more sections
# No writing to model here
def body_to_sections():
    pass


# Input section, Output Array of 1 or more Questions
# No writing to model here
def section_to_questions():
    pass


# This function will most likely writes directly to model. Might need to move to model instead
def run_parser():
    pass


def process(questionlibrary):

    # ====================== Convert to markdown
    # print(questionlibrary.pandoc_string)
    run_formatter(questionlibrary)
    
    pass