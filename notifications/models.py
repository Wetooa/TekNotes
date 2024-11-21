from django.db import models
from django.urls import reverse
from authentication.models import User


class NotificationType(models.TextChoices):
    LIKE_NOTE = "like_note", "Liked your note"
    LIKE_COMMENT = "like_comment", "Liked your comment"
    COMMENT_NOTE = "comment_note", "Commented on your post"
    FOLLOW_USER = "follow_user", "Followed you"


class Notification(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notifications"
    )
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sent_notifications",
        null=True,
        blank=True,
    )
    notification_type = models.CharField(
        max_length=20,
        choices=NotificationType.choices,
        default=NotificationType.LIKE_NOTE,
    )

    object_id = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.sender} {self.get_notification_type_display()}"

    def get_content(self):
        if self.notification_type == NotificationType.LIKE_NOTE:
            return "liked your note!"
        if self.notification_type == NotificationType.LIKE_COMMENT:
            return "liked your comment!"
        elif self.notification_type == NotificationType.COMMENT_NOTE:
            return "commented on your note!"
        elif self.notification_type == NotificationType.FOLLOW_USER:
            return "followed you!"
        return ""

    def get_url(self):
        if self.notification_type == NotificationType.LIKE_NOTE:
            return reverse("notes:note_detail", args=[self.object_id])
        if self.notification_type == NotificationType.LIKE_COMMENT:
            return reverse("notes:note_detail", args=[self.object_id])
        elif self.notification_type == NotificationType.COMMENT_NOTE:
            return reverse("notes:note_detail", args=[self.object_id])
        elif self.notification_type == NotificationType.FOLLOW_USER:
            return reverse("authentication:profile", args=[self.object_id])
        return "#"
