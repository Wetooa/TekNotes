from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, default="No bio yet.")
    avatar = models.ImageField(default="avatars/default.jpg", upload_to="avatars/")
    location = models.CharField(max_length=30, blank=True)

    def __str__(self):
