from aifc import Error
import os
import xml.etree.ElementTree as ET
import logging
import subprocess
import sys

logger = logging.getLogger(__name__)


def create_section_name():
    pass

# This is to split end_answers and body and trim the unused data at the top
def run_formatter(questionlibrary):

    os.chdir('/formatter/jarfile')
    result = subprocess.run('java -cp formatter.jar:* formatter',
                            shell=True,
                            input=questionlibrary.pandoc_output.encode(),
                            capture_output=True)
    os.chdir('/code')

    root = None
    try:
        root = ET.fromstring(result.stdout.decode("utf-8"))
    except:
        pass

    try:
        if root[0].tag == "body" :
            questionlibrary.formatter_output = root[0].text
            questionlibrary.save()
            pass
        else:
            logger.error("Body not found")
    except:
        logger.error("Body not found")

    try:
        if root[1].tag == "end_answers" :
            questionlibrary.end_answers = root[1].text
            questionlibrary.save()
        else:
            logger.error("Answer Section not found")
    except:
        logger.error("Answer section not found")

# This is to split sections into separate objects
def run_sectioner(questionlibrary):

    pass


# Input section, Output Array of 1 or more Questions
# No writing to model here
def section_to_questions():
    pass


# This function will most likely writes directly to model. Might need to move to model instead
def run_parser():
    pass


def process(questionlibrary):

    # ====================== 
    run_formatter(questionlibrary)
    run_sectioner(questionlibrary)
    
    pass