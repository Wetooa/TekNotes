from django.db import models
from django.contrib.auth.models import User
from notes.models import Note

class Comment(models.Model):
    content = models.TextField()
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} commented '{self.content}' on {self.note.title}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'note'], name='unique_like_per_user_note')
        ]

    def __str__(self):
        return f"{self.user.username} likes {self.note.title}"


class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dislikes')
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='dislikes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'note'], name='unique_dislike_per_user_note')
        ]

    def __str__(self):
        return f"{self.user.username} dislikes {self.note.title}"