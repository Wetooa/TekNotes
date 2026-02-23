import json
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Room, Message


class ChatRoom(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        rooms = Room.objects.filter(users=user)
        rooms_with_users = []

        for room in rooms:
            other_users = room.users.exclude(id=user.id)
            rooms_with_users.append({"room": room, "users": other_users})

        context = {
            "rooms_with_users": rooms_with_users,
        }

        return render(request, "chat/chatroom.html", context)

    def post(self, request):
        sender = request.user
        receiver_username = request.POST.get("receiver")
        try:
            receiver = User.objects.get(username=receiver_username)
        except User.DoesNotExist:
            return render(
                request, "chat/chatroom.html", {"error": "User does not exist"}
            )

        room = self.create_or_enter_room(sender, receiver)
        return redirect("chat:room", room_name=room.id)

    def create_or_enter_room(self, sender, receiver):
        sender_rooms = set(Room.objects.filter(users=sender).values_list("id", flat=True))
        receiver_rooms = set(Room.objects.filter(users=receiver).values_list("id", flat=True))
        common_rooms = sender_rooms.intersection(receiver_rooms)

        if common_rooms:
            room = Room.objects.get(id=common_rooms.pop())
        else:
            room = Room.objects.create(room_name=f"{sender.username}_{receiver.username}")
            room.users.add(sender, receiver)

        return room


class MessageView(LoginRequiredMixin, View):
    def get(self, request, room_name):
        sender = request.user
        try:
            room = Room.objects.get(id=room_name)
        except Room.DoesNotExist:
            return redirect("chat:create-room")

        if not room.users.filter(id=sender.id).exists():
            return redirect("chat:create-room")

        messages = Message.objects.filter(room=room).order_by("created_at")
        other_users = room.users.exclude(id=sender.id)
        receiver = other_users.first()

        context = {
            "messages": messages,
            "sender": sender,
            "room_name": str(room.id),
            "receiver": receiver.username if receiver else "",
        }
        return render(request, "chat/message.html", context)


@login_required
def chat_rooms_api(request):
    user = request.user
    rooms = Room.objects.filter(users=user)
    data = []

    for room in rooms:
        other_user = room.users.exclude(id=user.id).first()
        if not other_user:
            continue

        last_message = Message.objects.filter(room=room).order_by("-created_at").first()

        avatar_url = ""
        if hasattr(other_user, "profile") and other_user.profile.avatar:
            avatar_url = other_user.profile.avatar.url

        data.append({
            "room_id": str(room.id),
            "other_user": {
                "username": other_user.username,
                "first_name": other_user.first_name,
                "avatar_url": avatar_url,
            },
            "last_message": last_message.message if last_message else "",
            "last_message_time": last_message.created_at.isoformat() if last_message else None,
        })

    data.sort(key=lambda r: r["last_message_time"] or "", reverse=True)
    return JsonResponse({"rooms": data})
