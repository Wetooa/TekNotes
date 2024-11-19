from django.db import models
from authentication.models import User

# Create your models here.


class NotificationType(models.TextChoices):
    LIKE_POST = "like", "Liked your post"
    LIKE_COMMENT = "like", "Liked your comment"
    COMMENT_POST = "comment", "Commented on your post"
    FOLLOW_USER = "follow", "Followed you"
    MENTION_USER = "mention", "Mentioned you"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)

    notification_type = models.CharField(
        max_length=20,
        choices=NotificationType.choices,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_read = models.BooleanField(default=False)


class NotificationComment(Notification):
    pass
