import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TextConsumer(AsyncWebsocketConsumer):
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

        print(bytes_data)
        # import socket

        import socket
        await self.send(text_data=json.dumps({
            'hostname': socket.gethostname(),
            'data' : "data after file received by API",
            'progress' : "done"
        }))