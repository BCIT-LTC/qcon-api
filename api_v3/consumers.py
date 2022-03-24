import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.core.files.base import ContentFile

from .models import QuestionLibrary

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

    async def receive(self, bytes_data):
        # text_data_json = json.loads(text_data)
        # message = text_data_json['message']

        # print(bytes_data)
        # import socket
        await database_sync_to_async(self.save_file)(bytes_data)

        import socket
        await self.send(text_data=json.dumps({
            'hostname': socket.gethostname(),
            'data' : "data after file received by API",
            'progress' : "done"
        }))

    def save_file(self, bytes_data):

        received_file = ContentFile(bytes_data, name='foo.docx')

        newfile = QuestionLibrary.objects.create()
        newfile.temp_file = received_file
        newfile.save()

        # image = ImageFile(io.BytesIO(image_bytes), name='foo.jpg')  # << the answer!
        # new_message = Message.objects.create(image=image)

        return 