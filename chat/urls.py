from django.urls import path,include
from .views import *

urlpatterns = [
    path('', CreateRoom.as_view(), name="create-room"),
    path('<str:room_name>/<str:username>/', MessageView.as_view(),  name='room'),
]