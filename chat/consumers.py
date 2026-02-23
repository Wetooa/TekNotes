import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.user = self.scope['user']

        if not self.user.is_authenticated:
            await self.close()
            return

        room_exists = await self.get_room(self.room_name)
        if not room_exists:
            await self.close()
            return

        self.room_group_name = "room_%s" % self.room_name
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        if hasattr(self, 'room_group_name'):
            await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_message',
                'message': message,
            }
        )

    async def send_message(self, event):
        data = event['message']
        await self.create_message(data=data)
        response_data = {
            'sender': data['sender'],
            'message': data['message']
        }
        await self.send(text_data=json.dumps({'message': response_data}))

    @database_sync_to_async
    def get_room(self, room_id):
        from chat.models import Room
        return Room.objects.filter(id=room_id).exists()

    @database_sync_to_async
    def create_message(self, data):
        from chat.models import Room, Message
        try:
            room = Room.objects.get(id=data['room_name'])
            Message.objects.create(
                room=room,
                sender=data['sender'],
                message=data['message'],
            )
        except Room.DoesNotExist:
            pass
