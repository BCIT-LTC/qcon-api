from bs4 import BeautifulSoup
from .extract_images import extract_images
from .formatter import run_formatter
from .sectioner import run_sectioner
from .splitter import run_splitter
from .endanswers import get_endanswers
from .parser import run_parser
import socket
from api_v3.tasks import MarkDownConversionError, run_pandoc_task

import logging
logger = logging.getLogger(__name__)
from api_v3.logging.contextfilter import QuestionlibraryFilenameFilter
logger.addFilter(QuestionlibraryFilenameFilter())

class Process:
    def __init__(self, questionlibrary) -> None:
        self.questionlibrary = questionlibrary
        self.images_extracted = 0
        self.subsection_count = 0
        self.questions_expected = 0
        self.questions_processed = 0
        self.endanswers_count = 0
        self.question_error_count = 0
        logger.addFilter(QuestionlibraryFilenameFilter(self.questionlibrary))

    def run_pandoc(self):
        try:
            result = run_pandoc_task.apply_async(kwargs={"questionlibrary_id":self.questionlibrary.id}, ignore_result=False)
            pandoc_task_result = result.get()
            self.questionlibrary.pandoc_output = pandoc_task_result
        except MarkDownConversionError as e:
            logger.error(e)
            raise
        try: 
            if self.questionlibrary.pandoc_output == None:
                raise MarkDownConversionError("Pandoc output string is empty")
        except Exception as e:
            logger.error(e)
            raise MarkDownConversionError(e)

    def extract_images(self):
        self.images_extracted = extract_images(self.questionlibrary)

    def run_formatter(self):
        run_formatter(self.questionlibrary)

    # This is to split sections into separate objects
    def run_sectioner(self):
        self.subsection_count = run_sectioner(self.questionlibrary)

    def run_splitter(self):
        self.questions_expected = run_splitter(self.questionlibrary)

    def get_endanswers(self):
        self.endanswers_count = get_endanswers(self.questionlibrary)

    def run_parser(self):
        run_parser(self.questionlibrary)

    def sendformat(self, status, statustext, data):

        return {
                'hostname': socket.gethostname(),
                'status': status,
                'statustext': statustext,
                'images_count': str(self.images_extracted),
                'section_count': str(self.subsection_count),
                'questions_count': str(self.questions_expected),
                'endanswer_count': str(self.endanswers_count),
                'question_error_count': str(self.question_error_count),
                'data': data
            }
# ++++++++++++++++++++++++++++++++===================================
