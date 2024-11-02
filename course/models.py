from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    COLORS = [
        ('red-500', 'Red'),
        ('orange-500', 'Orange'),
        ('amber-500', 'Amber'),
        ('lime-500', 'Lime'),
        ('green-500', 'Green'),
        ('emerald-500', 'Emerald'),
        ('teal-500', 'Teal'),
        ('cyan-500', 'Cyan'),
        ('blue-500', 'Blue'),
        ('indigo-500', 'Indigo'),
        ('violet-500', 'Violet'),
        ('purple-500', 'Purple'),
        ('fuchsia-500', 'Fuschia'),
        ('pink-500', 'Pink'),
    ]

    code = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    color = models.CharField(max_length=20, choices=COLORS, default='gray-500')
    created_by = models.ForeignKey(User, related_name='courses', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.code} - {self.description}'
