from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

from notifications.models import Notification, NotificationType

from .models import Note, Like, Dislike
from .models import Comment


@login_required
def comment(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    content = request.POST.get("comment", "")
    if content:
        Comment.objects.create(user=request.user, note=note, content=content)

    if note.created_by != request.user:
        Notification.objects.create(
            user=note.created_by,
            sender=request.user,
            notification_type=NotificationType.COMMENT_NOTE,
            object_id=note_id,
        )

    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))


@login_required
@require_POST
def like(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    like, created = Like.objects.get_or_create(user=request.user, note=note)

    if not created:
        like.delete()
    elif note.created_by != request.user:
        Notification.objects.create(
            user=note.created_by,
            sender=request.user,
            notification_type=NotificationType.LIKE_NOTE,
            object_id=note_id,
        )

    Dislike.objects.filter(user=request.user, note=note).delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))


@login_required
@require_POST
def dislike(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    dislike, created = Dislike.objects.get_or_create(user=request.user, note=note)

    if not created:
        dislike.delete()

    Like.objects.filter(user=request.user, note=note).delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
