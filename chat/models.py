from django.db import models
import uuid

# Create your models here.
class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room_name = models.CharField(max_length=255)
    users = models.ManyToManyField('auth.User', related_name='rooms')

    def __str__(self):
        return self.room_name
    
class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sender = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return str(self.room)
    
class ChatUsers(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    users = models.CharField(max_length=255)

    def __str__(self):
        return self.users