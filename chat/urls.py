from django.urls import path,include
from .views import *

urlpatterns = [
    path('', ChatRoom.as_view(), name="create-room"),
    path('<str:UUID>/<str:sender>/', MessageView.as_view(),  name='room'),
]