from django.shortcuts import render

from notifications.models import Notification, NotificationType

# Create your views here.


def index(request):
    return render(request, "index.html")
