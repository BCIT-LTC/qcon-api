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

from .process import run_formatter, run_sectioner

class TextConsumer(JsonWebsocketConsumer):

    uploadedfile = None

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

        try:
            new_questionlibrary = self.save_file(content)
        except FileValidationError as e:
            logger.error("FileValidationError: " + str(e))
            self.send(
                text_data=json.dumps({
                    'hostname': socket.gethostname(),
                    'data': "",
                    'status': "Error: Not a valid .docx File"
                }))
            return

        try:
            new_questionlibrary.create_pandocstring()
        except FileValidationError as e:
            logger.error("FileValidationError: " + str(e))
            self.send(
                text_data=json.dumps({
                    'hostname': socket.gethostname(),
                    'data': "",
                    'status': "Error: Not a valid .docx File"
                }))
            return
        else:
            self.send(text_data=json.dumps({
                'hostname': socket.gethostname(),
                'data': "",
                'status': "The file is valid"
            }))

        try:
            run_formatter(new_questionlibrary)
        except FormatterError as e:
            logger.error("FormatterError: " + str(e))
            self.send(text_data=json.dumps(
                {
                    'hostname': socket.gethostname(),
                    'data': "",
                    'status':
                    "Error: No contents found in the body of the file"
                }))
            return
        else:
            self.send(text_data=json.dumps({
                'hostname': socket.gethostname(),
                'data': "",
                'status': "Content Body detected"
            }))


        try:
            run_sectioner(new_questionlibrary)
        except SectionerError as e:
            logger.error("SectionerError: " + str(e))
            self.send(text_data=json.dumps(
                {
                    'hostname': socket.gethostname(),
                    'data': "",
                    'status': "Error: Sections can not be identified"
                }))
            return
        else:
            self.send(text_data=json.dumps({
                'hostname': socket.gethostname(),
                'data': "",
                'status': "sectioner complete"
            }))


        print("check if this prints")
        print(new_questionlibrary)

        # import time

        # print("sending msg 1")
        # self.send(text_data=json.dumps({
        #     'hostname': socket.gethostname(),
        #     'data': "message 1",
        #     'status': "not done"
        # }))

        # time.sleep(3)
        # print("sending msg 2")
        # self.send(text_data=json.dumps({
        #     'hostname': socket.gethostname(),
        #     'data': "message 2",
        #     'status': "not done"
        # }))

        # time.sleep(3)
        # print("sending msg 3")

        # self.send(text_data=json.dumps({
        #     'hostname': socket.gethostname(),
        #     'data': "message 3",
        #     'status': "not done"
        # }))

    def save_file(self, content):
        format, fixeddata = content.get('file').split(';base64,')
        if format == 'data:application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            received_file = ContentFile(base64.b64decode(fixeddata),
                                        name=content.get('filename'))
            newfile = QuestionLibrary.objects.create()
            newfile.temp_file = received_file
            newfile.session_id = self.sessionid
            newfile.save()
            return newfile
        else:
            raise FileValidationError("not a valid *.docx file")


class FileValidationError(Exception):
    pass


class FormatterError(Exception):
    pass


class SectionerError(Exception):
    pass