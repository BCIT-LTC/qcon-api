import json
from channels.generic.websocket import JsonWebsocketConsumer
from channels.db import database_sync_to_async
from django.core.files.base import ContentFile
import base64

from .models import QuestionLibrary
import socket

import time


class TextConsumer(JsonWebsocketConsumer):

    uploadedfile = None

    def connect(self):
        print("connected")
        sessionid = None
        # print(self.scope['url_route']['kwargs']['session_id'])
        self.sessionid = self.scope['url_route']['kwargs']['session_id']

        self.channel_layer.group_add(self.sessionid, self.channel_name)

        self.accept()

        # await self.send(text_data=json.dumps({
        #     'hostname': socket.gethostname(),
        #     'data' : None,
        #     'progress' : "not done"
        # }))

    def disconnect(self, close_code):
        print("disconnected")
        self.channel_layer.group_discard(self.sessionid, self.channel_name)
        pass

    def receive_json(self, content, **kwargs):
        # text_data_json = json.loads(text_data)
        # message = text_data_json['message']
        print("sync")
        try:
            # print(json.loads(text_data)['filename'])
            # database_sync_to_async(self.save_file)(content)
            self.save_file(content)
        except:
            # print(json.loads(text_data))
            # save_result = await database_sync_to_async(self.save_file)(text_data)
            pass

        import time

        print("sending msg 1")
        self.send(text_data=json.dumps({
            'hostname': socket.gethostname(),
            'data': "message 1",
            'status': "not done"
        }))

        time.sleep(3)
        print("sending msg 2")
        self.send(text_data=json.dumps({
            'hostname': socket.gethostname(),
            'data': "message 2",
            'status': "not done"
        }))

        time.sleep(3)
        print("sending msg 3")

        self.send(text_data=json.dumps({
            'hostname': socket.gethostname(),
            'data': "message 3",
            'status': "not done"
        }))

    # def send_message(self, event):
    #     print("message is sending")
    #     message = event['message']

    #     # Send message to WebSocket
    #     self.send(text_data=json.dumps({'message': message}))

    def save_file(self, content):
        format, fixeddata = content.get('file').split(';base64,')
        print("database")
        if format == 'data:application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            received_file = ContentFile(base64.b64decode(fixeddata),
                                        name=content.get('filename'))
            newfile = QuestionLibrary.objects.create()
            newfile.temp_file = received_file
            newfile.session_id = self.sessionid
            newfile.save()
            return True
        else:
            return False