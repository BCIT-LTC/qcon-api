from ast import Not
import os
import xml.etree.ElementTree as ET
import subprocess
import re
from .process_helper import trim_text

import logging
newlogger = logging.getLogger(__name__)
# from api_v3.logging.contextfilter import QuestionlibraryFilenameFilter
from api_v3.logging.logging_adapter import FilenameLoggingAdapter

def run_formatter(questionlibrary):
    # loggingfilter = QuestionlibraryFilenameFilter(questionlibrary=questionlibrary)
    # logger.addFilter(loggingfilter)
    logger = FilenameLoggingAdapter(newlogger, {'filename': os.path.basename(questionlibrary.temp_file.name)})
    
    root = None

    try:
        os.chdir('/formatter/jarfile')
        result = subprocess.run('java -cp formatter.jar:* formatter',
                                shell=True,
                                input=questionlibrary.pandoc_output.encode("utf-8"),
                                capture_output=True)
        os.chdir('/code')
        root = ET.fromstring(result.stdout.decode("utf-8"))
    except:
        FormatterError("File Not valid")
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
        raise FormatterError("Body not found")

# ==================================== END ANSWERS

    end_answers = root.find('end_answers')
    if end_answers is not None:
        questionlibrary.end_answers_raw = end_answers.text
        questionlibrary.save()
    else:
        logger.info("No endanswers found")

class FormatterError(Exception):
    def __init__(self, reason, message="Formatter Error"):
        self.reason = reason
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.message} -> {self.reason}'