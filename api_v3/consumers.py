import json
from channels.generic.websocket import JsonWebsocketConsumer
from channels.db import database_sync_to_async
from django.core.files.base import ContentFile
import base64

from .models import QuestionLibrary
import socket

import time
import logging
logger = logging.getLogger(__name__)

from .process import extract_images, run_formatter, run_sectioner, run_splitter, run_parser, get_endanswers
from .serializers import JsonResponseSerializer


class TextConsumer(JsonWebsocketConsumer):

    images_count = 0
    questions_count = 0
    endanswer_count = 0

    def connect(self):
        print("connected")
        sessionid = None
        # print(self.scope['url_route']['kwargs']['session_id'])
        self.sessionid = self.scope['url_route']['kwargs']['session_id']
        self.channel_layer.group_add(self.sessionid, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        print("disconnected")
        self.channel_layer.group_discard(self.sessionid, self.channel_name)
        pass

    def receive_json(self, content, **kwargs):
        new_questionlibrary = None

###########################################
        # Save the file
###########################################
        try:
            new_questionlibrary = self.save_file(content)
        except FileValidationError as e:
            logger.error("FileValidationError: " + str(e))
            self.send(text_data=json.dumps(self.sendformat("Error", "Not a valid .docx File", "")))
            # close connection
            self.send(text_data=json.dumps(self.sendformat("Close", "", "")))
            return
        
###########################################
        # create_pandocstring
###########################################

        try:
            new_questionlibrary.create_pandocstring()
        except FileValidationError as e:
            logger.error("FileValidationError: " + str(e))
            self.send(
                text_data=json.dumps(self.sendformat("Error", "File unreadable", "")))
            # close connection
            self.send(text_data=json.dumps(self.sendformat("Close", "", "")))
            return
        else:
            self.send(text_data=json.dumps(self.sendformat("Busy", "The file is valid", "")))

###########################################
        # Extract Images
###########################################

        try:
            self.images_count = extract_images(new_questionlibrary)
        except ImageExtractError as e:
            self.send(text_data=json.dumps(self.sendformat("Warn", "Images extraction failed", "")))
        else:
            self.send(text_data=json.dumps(self.sendformat("Busy", "Images found", "")))

##########################################
        # run_formatter
##########################################

        try:
            run_formatter(new_questionlibrary)
        except:
            logger.error("FormatterError")
            self.send(text_data=json.dumps(self.sendformat("Error", "No contents found in the body of the file", "")))
            # close connection
            self.send(text_data=json.dumps(self.sendformat("Close", "", "")))
            return
        else:
            self.send(text_data=json.dumps(self.sendformat("Busy", "Content Body detected", "")))

##########################################
        # run_sectioner
##########################################

        try:
            run_sectioner(new_questionlibrary)
        except SectionerError as e:
            logger.error("SectionerError: " + str(e))
            self.send(text_data=json.dumps(self.sendformat("Error", "Sections can not be identified", "")))
            # close connection
            self.send(text_data=json.dumps(self.sendformat("Close", "", "")))            
            return
        else:
            self.send(text_data=json.dumps(self.sendformat("Busy", "Sectioner complete", "")))

##########################################
        # run_splitter
##########################################

        try:
            self.questions_count = run_splitter(new_questionlibrary)
        except SplitterError as e:
            logger.error("SplitterError: " + str(e))
            self.send(text_data=json.dumps(self.sendformat("Error", "Splitter failed", "")))
            # close connection
            self.send(text_data=json.dumps(self.sendformat("Close", "", "")))
            return
        else:
            self.send(text_data=json.dumps(self.sendformat("Busy", "Splitter complete", "")))

###########################################
        # Grab end answers
###########################################

        try:
            self.endanswer_count = get_endanswers(new_questionlibrary)
        except ImageExtractError as e:
            self.send(text_data=json.dumps(self.sendformat("Busy", "Endanswers not found", "")))
        else:
            self.send(text_data=json.dumps(self.sendformat("Busy", "End answers found", "")))

###########################################
        # run_parser
###########################################

        try:
            run_parser(new_questionlibrary)
        except ParserError as e:
            logger.error("ParserError: " + str(e))
            self.send(text_data=json.dumps(self.sendformat("Error", "Parser failed", "")))
                # close connection
            self.send(text_data=json.dumps(self.sendformat("Close", "", "")))
            return
        else:
            self.send(text_data=json.dumps(self.sendformat("Busy", "Parser complete", "")))

###########################################
        # Add Images back
###########################################


    # TODO
    # need to query and iterate all question and add images


###########################################
        # serialize and send response
###########################################

        serialized_ql = JsonResponseSerializer(new_questionlibrary)
        self.send(text_data=json.dumps(self.sendformat("Done", "", serialized_ql.data)))
######################### Close Connection
        self.send(text_data=json.dumps(self.sendformat("Close", "", "")))

    def sendformat(self, status, statustext, data):

        return {
                'hostname': socket.gethostname(),
                'status': status,
                'statustext': statustext,
                'images_count': str(self.images_count),
                'questions_count': str(self.questions_count),
                'endanswer_count': str(self.endanswer_count),
                'data': data
            }

    def save_file(self, content):
        format, fixeddata = content.get('file').split(';base64,')
        received_file = ContentFile(base64.b64decode(fixeddata),
                                    name=content.get('filename'))
        newfile = QuestionLibrary.objects.create()
        newfile.temp_file = received_file
        newfile.session_id = self.sessionid
        newfile.save()
        return newfile

        # if format == 'data:application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        #     received_file = ContentFile(base64.b64decode(fixeddata),
        #                                 name=content.get('filename'))
        #     newfile = QuestionLibrary.objects.create()
        #     newfile.temp_file = received_file
        #     newfile.session_id = self.sessionid
        #     newfile.save()
        #     return newfile
        # else:
        #     raise FileValidationError("not a valid *.docx file")

class ImageExtractError(Exception):
    pass

class FileValidationError(Exception):
    pass


class FormatterError(Exception):
    pass


class SectionerError(Exception):
    pass

class SplitterError(Exception):
    pass

class ParserError(Exception):
    pass