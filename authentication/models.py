
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(AbstractUser):
    birthdate = models.DateField(null=True, blank=True)    
    def __str__(self):
        return self.username
