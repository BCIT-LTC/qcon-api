import os
import subprocess
import xml.etree.ElementTree as ET
from ..models import Section
from ..models import Question
from .process_helper import trim_text
import logging
logger = logging.getLogger(__name__)
from api_v3.logging.contextfilter import QuestionlibraryFilenameFilter

def run_splitter(questionlibrary):
    logger.addFilter(QuestionlibraryFilenameFilter(questionlibrary=questionlibrary))
    sections = Section.objects.filter(question_library=questionlibrary)
    questions_count = 0
    section_order = 1
    for section in sections:
        questions_count_section = 0
        try:
            questions_count_section = split_questions(section)
            section.order = section_order
            section_order += 1
            section.save()
        except SplitterError as e:
            logger.warn("No questions detected. Discarding empty section")
        questions_count += questions_count_section
        # remove empty sections
        if questions_count_section == 0:        
            section.delete()
    return questions_count

def split_questions(sectionobject):
    root = None
    try:
        os.chdir('/splitter/jarfile')
        result = subprocess.run(
            'java -cp splitter.jar:* splitter',
            shell=True,
            input=sectionobject.raw_content.encode("utf-8"),
            capture_output=True)
        os.chdir('/code')
        root = ET.fromstring(result.stdout.decode("utf-8"))
    except:
        raise SplitterError("Splitter failed")   

    questions_found = 0
    try:    
        for question in root:
            questionobject = Question.objects.create(
                section=sectionobject)
            questionobject.save()
            content = question.find('content')
            if content is not None:
                # Filter out empty questions
                if len(trim_text(content.text)) > 0:
                    questions_found += 1
                    questionobject.raw_content = content.text
            questionobject.save()
    except:
        raise SplitterError("Splitter failed")
    return questions_found

class SplitterError(Exception):
    def __init__(self, reason, message="Splitter Error"):
        self.reason = reason
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.message} -> {self.reason}'