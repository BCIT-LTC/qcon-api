import json
from channels.generic.websocket import WebsocketConsumer

class TextConsumer(WebsocketConsumer):
    def connect(self):
        print("connecteddd")
        self.accept()

    def disconnect(self, close_code):
        print("DISSconnecteddd")
        pass

    def receive(self, text_data):
        # text_data_json = json.loads(text_data)
        # message = text_data_json['message']

        print(text_data)

        self.send(text_data=json.dumps({
            'message': text_data
        }))