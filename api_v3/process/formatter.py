from ast import Not
import os
import xml.etree.ElementTree as ET
import subprocess
import logging
logger = logging.getLogger(__name__)
import re
from .process_helper import trim_text

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
        logger.error("File Not valid")
        return

# ==================================== UNUSED CONTENT

    unused_content = root.find('unused_content')
    if unused_content is not None:
        questionlibrary.formatter_error = "unused content found in document header. Please review"

# ==================================== SECTION INFO

    sectioninfo_extracted = '' 
    sectioninfo = root.find('sectioninfo')
    if sectioninfo is not None:
        # IF TITLE IS FOUND IT WILL REPLACE THE TITLE THAT WAS CAPTURED FROM FILENAME 
        titlepart = re.search(r'(.|\n)*(?=#.?section)', sectioninfo.text)
        if titlepart is not None:
            questionlibrary.main_title = trim_text(titlepart.group())
        sectioninfopart = re.search(r'\n#.?section(.|\n)*', sectioninfo.text)
        if sectioninfopart is not None:
            sectioninfo_extracted = sectioninfopart.group()    
        questionlibrary.save()

# ==================================== BODY

    body = root.find('body')
    if body is not None:
        questionlibrary.formatter_output = sectioninfo_extracted + body.text
        questionlibrary.save()
    else:
        logger.error("Body not found")
        raise FormatterError
        return

# ==================================== END ANSWERS

    end_answers = root.find('end_answers')
    if end_answers is not None:
        questionlibrary.end_answers_raw = end_answers.text
        questionlibrary.save()
    else:
        pass


class FormatterError(Exception):

    def __init__(self, message="Formatter error"):
        super().__init__(message)
    def __str__(self):
        return f'{self.message}'