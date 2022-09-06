import os
import logging 

class QuestionlibraryFilenameFilter(logging.Filter):
    def __init__(self, questionlibrary=None):
        self.questionlibrary = questionlibrary        
    def filter(self, record):        
        if self.questionlibrary==None:
            record.file = '--'
        else:
            if self.questionlibrary.temp_file.name != None:
                record.file = 'filename:' + os.path.basename(self.questionlibrary.temp_file.name)
            elif self.questionlibrary.filtered_main_title != None:
                record.file = 'filtered_main_title:' + os.path.basename(self.questionlibrary.filtered_main_title)                
            else:
                record.file = '--'
        return True
        
