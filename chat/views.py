from django.shortcuts import render, redirect
from django.views import View
from chat.models import *
# Create your views here.
class ChatRoom(View):
    def get(self, request):
        return render(request, 'chat/chatroom.html')
    
    def Create_or_Enter_room(self, sender, receiver):
        rooms_with_sender = ChatUsers.objects.filter(users=sender).values_list('room', flat=True)
        rooms_with_receiver = ChatUsers.objects.filter(users=receiver).values_list('room', flat=True)
        common_rooms = set(rooms_with_sender).intersection(set(rooms_with_receiver))
        
        if common_rooms:
            room_id = common_rooms.pop()
            room = Room.objects.get(id=room_id)
        else:
            room = Room.objects.create(room_name=f"{sender}_{receiver}")
            ChatUsers.objects.create(room=room, users=sender)
            ChatUsers.objects.create(room=room, users=receiver)

        return room

        
class MessageView(View):
     def get(self, request, sender, receiver):
        chatroom = ChatRoom()
        room = chatroom.create_or_enter_room(sender, receiver)
        get_messages = Message.objects.filter(room=room)
        users_in_room = ChatUsers.objects.filter(room=room).values_list('users', flat=True)
        context = {
            'messages': get_messages,
            'user': sender,
            'room_name': room.room_name,
            'users_in_room': users_in_room
        }
        return render(request, 'chat/message.html', context)