import re
import os
import subprocess

from pathlib import Path


def convert_txt(questionlibrary):

    try:
        os.chdir('/code/temp')
        # result = subprocess.run('soffice --headless --convert-to pdf --outdir . 7741.docx')
        subprocess.run(["soffice", "--headless", "--convert-to", "txt", "--outdir", str(questionlibrary.id), questionlibrary.temp_file.name], capture_output=True)
        path = Path(questionlibrary.temp_file.name)
        if path.is_file():
            # print(path.name)
            # print(path.stem)
            txt_file_path = str(questionlibrary.id)+ "/" + path.stem + ".txt"
            f = open(txt_file_path ,"r")
            lines = f.read()
            questionlibrary.txt_output = '\n' + lines
            questionlibrary.save()
        else:
            raise ConvertTxtError("text file not found")
        os.chdir('/code')            
    except Exception as e:
        raise ConvertTxtError(e)


class ConvertTxtError(Exception):
    def __init__(self, reason, message="general error"):
        self.reason = reason
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} -> {self.reason}'