import os
import logging 

class QuestionlibraryFilenameFilter(logging.Filter):
    def __init__(self, questionlibrary):
        self.questionlibrary = questionlibrary       
    def filter(self, record):
        record.file = os.path.basename(self.questionlibrary.temp_file.name)
        return True