from django.shortcuts import render, redirect
from django.views import View
from chat.models import *
# Create your views here.
class CreateRoom(View):
    def get(self, request):
        return render(request, 'chat/chatroom.html')
    def post(self, request):
        if request.method == 'POST':
            username = request.POST['username']
            room = request.POST['room']
            try:
                get_room = Room.objects.get(room_name = room)
                return redirect('chat:room', room_name=room, username=username)
            except Room.DoesNotExist:
                # new_room = Room.objects.create(room_name = room)
                new_room = Room(room_name = room)
                new_room.save()
                return redirect('chat:room', room_name=room, username=username)
        return redirect('chat:create-room')
class MessageView(View):
    def get(self, request, room_name, username):
        get_room = Room.objects.get(room_name=room_name)
        get_messages = Message.objects.filter(room=get_room)
        context = {
                    "messages": get_messages,
                    "user": username,
                    "room_name": room_name,
                  }
        return render(request, 'chat/message.html', context) 