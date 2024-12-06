from django.urls import path,include
from .views import *

app_name = "chat"


urlpatterns = [
    path('', ChatRoom.as_view(), name="create-room"),
    path('<str:room_name>/', MessageView.as_view(),  name='room'),
]