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

        # Join room group
        # await self.channel_layer.group_add("groupname", "channelname")

        self.accept()

        # import socket

        # await self.send(text_data=json.dumps({
        #     'hostname': socket.gethostname(),
        #     'data' : None,
        #     'progress' : "not done"
        # }))

    def disconnect(self, close_code):
        print("disconnected")
        # await self.channel_layer.group_discard("groupname", "channelname")
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

        import socket
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
        # print(text_data)
        # Send message to room group
        # await self.channel_layer.group_send(
        #     self.sessionid,
        #     {
        #         'type': 'chat_message',
        #         'message': 'somemessage'
        #     }
        # )

        # time.sleep(3)
        # print("message 1")
        # if save_result:
        #     await self.send(
        #         text_data=json.dumps({
        #             'hostname': socket.gethostname(),
        #             'data': "data after file received by API",
        #             'status': "not done"
        #         }))



        # time.sleep(5)

        # await self.send(text_data=json.dumps({
        #     'hostname': socket.gethostname(),
        #     'data': "2222",
        #     'status': "done"
        # }))

    def send_message(self, event):
        print("message is sending")
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({'message': message}))

    # async def chat_message(self, event):
    #     # Handles the "chat.message" event when it's sent to us.
    #     print("lalalalala")
    #     message = event['message']
    #     print(message)
    #     # await self.send(text_data=json.dumps({'message': message}))
    #     # await self.send(text_data=event["text"])

    def save_file(self, content):
        # text_data_json = json.loads(text_data)
        # print(text_data_json['filename'])
        # print(text_data_json['file'])
        format, fixeddata = content.get('file').split(';base64,')
        # format, fixeddata = text_data_json['file'].split(';base64,')
        print("database")
        if format == 'data:application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            received_file = ContentFile(base64.b64decode(fixeddata),
                                        name=content.get('filename'))
            newfile = QuestionLibrary.objects.create()
            newfile.temp_file = received_file
            newfile.session_id = self.sessionid
            newfile.save()
            # newfile.save()
            # print(newfile)
            # newfile = QuestionLibrary.objects.create()
            # newfile.temp_file = received_file
            # newfile.save()
            return True
        else:
            return False