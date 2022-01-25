import os
import xml.etree.ElementTree as ET


def create_section_name():
    pass

def run_formatter(questionlibrary):

    os.chdir('/formatter/jarfile')
    destination = '/code/temp/' + str(questionlibrary.id) + '/'
    os.system('java -cp formatter.jar:* formatter ' + destination)
    os.chdir('/code')

    tree = ET.parse('/code/temp/' + str(questionlibrary.id) + '/' + 'formatter.xml')
    root = tree.getroot()
    for child in root:
        print(child.tag, child.attrib)


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