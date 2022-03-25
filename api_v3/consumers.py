import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.core.files.base import ContentFile
import base64

from .models import QuestionLibrary
import socket

class TextConsumer(AsyncWebsocketConsumer):

    uploadedfile = None

    async def connect(self):
        print("connected")
        await self.accept()

        # import socket
        
        # await self.send(text_data=json.dumps({
        #     'hostname': socket.gethostname(),
        #     'data' : None,
        #     'progress' : "not done"
        # }))

    async def disconnect(self, close_code):
        print("disconnected")
        pass

    async def receive(self, text_data):
        # text_data_json = json.loads(text_data)
        # message = text_data_json['message']

        # print(bytes_data)
        # import socket
        await database_sync_to_async(self.save_file)(text_data)

        await self.send(text_data=json.dumps({
            'hostname': socket.gethostname(),
            'data' : "data after file received by API",
            'status' : "done"
        }))

    def save_file(self, text_data):
        text_data_json = json.loads(text_data)
        # print(text_data_json['filename'])
        # print(text_data_json['file'])
        format, fixeddata = text_data_json['file'].split(';base64,')

        if format == 'data:application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            received_file = ContentFile(base64.b64decode(fixeddata), name=text_data_json['filename'])
            newfile = QuestionLibrary.objects.create()
            newfile.temp_file = received_file
            newfile.save()
            
        return 