import os
import subprocess
import xml.etree.ElementTree as ET
from ..models import Section
from ..models import Question
# from .process_helper import trim_text
from api_v3.tasks import trim_text
import logging
newlogger = logging.getLogger(__name__)
from api_v3.logging.logging_adapter import FilenameLoggingAdapter

class Splitter:
    def __init__(self, questionlibrary) -> None:
        self.questionlibrary = questionlibrary
        self.total_questions_found = 0
        self.section_order = 1

    def run_splitter(self):
        logger = FilenameLoggingAdapter(newlogger, {
            'filename': self.questionlibrary.temp_file.name,
            'user_ip': self.questionlibrary.user_ip
            })
        sections = Section.objects.filter(question_library=self.questionlibrary)
        for section in sections:
            try:
                section.questions_expected = self.split_questions(section)
                section.order = self.section_order
                self.section_order += 1
                section.save()
            except SplitterError as e:
                logger.debug("No questions detected. Discarding empty section")
                section.delete()
            # remove empty sections
            if section.questions_expected == 0:        
                section.delete()
        # return questions_count
        return self.total_questions_found

    def split_questions(self, sectionobject):
        logger = FilenameLoggingAdapter(newlogger, {
            'filename': self.questionlibrary.temp_file.name,
            'user_ip': self.questionlibrary.user_ip
            })
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
            sectionobject.error = "ANTLR"
            raise SplitterError("ANTLR")

        section_questions_found = 0
        try:    
            for question in root:
                questionobject = Question.objects.create(
                    section=sectionobject)
                questionobject.save()
                content = question.find('content')
                if content is not None:
                    # Filter out empty questions
                    if len(trim_text(content.text)) > 0:
                        self.total_questions_found += 1
                        questionobject.index = self.total_questions_found
                        section_questions_found += 1
                        questionobject.raw_content = content.text
                questionobject.save()
        except:
            sectionobject.error = "Failed to process questions in section"
            raise SplitterError("Failed to process questions in section")
        return section_questions_found

class SplitterError(Exception):
    def __init__(self, reason, message="Splitter Error"):
        self.reason = reason
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.message} -> {self.reason}'