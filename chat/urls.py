from django.urls import path
from .views import ChatRoom, MessageView, chat_rooms_api

app_name = "chat"

urlpatterns = [
    path("", ChatRoom.as_view(), name="create-room"),
    path("api/rooms/", chat_rooms_api, name="api-rooms"),
    path("<str:room_name>/", MessageView.as_view(), name="room"),
]
