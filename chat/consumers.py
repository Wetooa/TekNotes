import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from chat.models import *

class ChatConsumer(AsyncWebsocketConsumer):
    def close_code_debugger(self, close_code):
        if close_code == 1000:
            print("WebSocket disconnected: Normal closure (the purpose of the connection has been fulfilled).")
        elif close_code == 1001:
            print("WebSocket disconnected: Going away (the server or client is going away).")
        elif close_code == 1002:
            print("WebSocket disconnected: Protocol error (an endpoint is terminating the connection due to a protocol error).")
        elif close_code == 1003:
            print("WebSocket disconnected: Unsupported data (the server is not accepting the type of data being sent).")
        elif close_code == 1007:
            print("WebSocket disconnected: Invalid frame payload data (the server is terminating the connection because it received data that is inconsistent with the data type).")
        else:
            print(f"WebSocket disconnected: Unknown close code {close_code}.")
            
    async def connect(self):
        self.room_name = f"room_{self.scope['url_route']['kwargs']['room_name']}"
        self.room_group_name = 'chat_%s' % self.room_name
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        self.close_code_debugger(close_code)
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        
    # When the socket.send() method is called, the WebSocket connection transmits the message to the server.
    # The receive method is automatically triggered to handle the incoming message.
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json
        # Trigger send_message method
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_message',
                'message': text_data_json,
            }
        )
    async def send_message(self, event):
        print("Message Sent!!.....?")
        data = event['message']
        await self.create_message(data=data)
        response_data = {
            'sender': data['sender'],
            'message': data['message']
        }
        await self.send(text_data=json.dumps({'message': response_data}))
        
    # This decorator is part of Django Channels and is used to allowsynchronous database 
    # operations to be called from asynchronous code (like your WebSocket consumers).
    @database_sync_to_async 
    def create_message(self, data):
        get_room_by_name = Room.objects.get(room_name=data['room_name'])
        if not Message.objects.filter(message=data['message']).exists():
            new_message = Message(room=get_room_by_name, sender=data['sender'], message=data['message'])
            new_message.save()