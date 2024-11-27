from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from chat.models import *
# Create your views here.


class ChatRoom(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        room_ids= ChatUsers.objects.filter(users=user).values_list('room', flat=True)
        print("Rooms avail: ", room_ids)
        users = [] 
        for(room_id) in room_ids:
            room = (Room.objects.get(id=room_id))
            users.append(room.users.exclude())
        room = Room.objects.get(id=room_id)

        for room in rooms:
            room_user = (room.users).first()
            room_users.append(room_user)
            
        context = {
            'rooms': rooms,
            'room_users': room_users,
        }
        print("Rooms Users: ", room_users)
        return render(request, 'chat/chatroom.html', context)
    
    def post(self, request):
        sender = request.user
        receiver_username = request.POST.get('receiver')
        try:
            receiver = User.objects.get(username=receiver_username)
            print("The receiver exists: ", receiver)
        except User.DoesNotExist:
            print("I DID NOT FIND ANY RECEIVERS")
            return render(request, 'chat/chatroom.html', {'error': 'User does not exist'})
            

        room = self.Create_or_Enter_room(sender, receiver)
        return redirect('chat:room', UUID=room.id, sender=sender.username)       
    
    def Create_or_Enter_room(self, sender, receiver):
        rooms_with_sender = ChatUsers.objects.filter(users=sender).values_list('room', flat=True)
        print("Rooms with sender: ", rooms_with_sender)
        rooms_with_receiver = ChatUsers.objects.filter(users=receiver).values_list('room', flat=True)
        print("Rooms with receiver: ", rooms_with_receiver)
        common_rooms = set(rooms_with_sender).intersection(set(rooms_with_receiver))
        print("Common rooms: ", common_rooms)
        
        if common_rooms:
            room_id = common_rooms.pop()
            print("Room ID: ", room_id)
            room = Room.objects.get(id=room_id)
            print("Room Used: ", room)
        else:
            room = Room.objects.create(room_name=f"{sender}_{receiver}")
            Room.objects.create(users=sender, room=room)
            Room.objects.create(users=receiver, room=room)
            ChatUsers.objects.create(room=room, users=sender)
            ChatUsers.objects.create(room=room, users=receiver)
            print("Created Room: ", room," Sender: ", sender, " Receiver: ", receiver)

        return room

        
class MessageView(View):
     def get(self, request, UUID, sender):
        get_room = Room.objects.get(id=UUID)
        get_messages = Message.objects.filter(room=get_room)
        receiver = ChatUsers.objects.filter(room=get_room).exclude(users=sender).values_list('users', flat=True)
        context = {
            'messages': get_messages,
            'sender': sender,
            'room_name': get_room.room_name,
            'receiver': receiver
        }
        return render(request, 'chat/message.html', context)