from django.core.cache import cache
from django.db.models import Count
from course.models import Course
from clicks.models import ClickNote, ClickTag, ClickCourse
from notes.models import Note
from notifications.models import Notification
from tags.models import Tag

TRENDING_CACHE_TTL = 300
RECENT_POSTS_CACHE_TTL = 60


def courses_list(request):
    if not request.user.is_authenticated:
        return {"your_courses": Course.objects.none()}
    return {
        "your_courses": Course.objects.filter(
            created_by=request.user
        ).distinct()
    }


def trending(request):
    cache_key = "trending_data"
    cached = cache.get(cache_key)
    if cached is not None:
        return cached

    trending_note_ids = list(
        ClickNote.objects.values("note")
        .annotate(click_count=Count("id"))
        .order_by("-click_count")
        .values_list("note", flat=True)[:5]
    )

    trending_tag_ids = list(
        ClickTag.objects.values("tag")
        .annotate(click_count=Count("id"))
        .order_by("-click_count")
        .values_list("tag", flat=True)[:5]
    )

    trending_course_ids = list(
        ClickCourse.objects.values("course")
        .annotate(click_count=Count("id"))
        .order_by("-click_count")
        .values_list("course", flat=True)[:5]
    )

    trending_notes = Note.objects.filter(
        id__in=trending_note_ids,
        is_private=False,
        is_archived=False,
    ).select_related("created_by")

    trending_tags = Tag.objects.filter(id__in=trending_tag_ids)

    trending_courses = Course.objects.filter(id__in=trending_course_ids)

    result = {
        "trending_notes": trending_notes,
        "trending_tags": trending_tags,
        "trending_courses": trending_courses,
    }
    cache.set(cache_key, result, TRENDING_CACHE_TTL)
    return result


def recent_posts(request):
    cache_key = "recent_posts"
    cached = cache.get(cache_key)
    if cached is not None:
        return cached

    notes = Note.objects.filter(is_private=False, is_archived=False).order_by(
        "-created_at"
    )[:5]
    result = {"recent_posts": notes}
    cache.set(cache_key, result, RECENT_POSTS_CACHE_TTL)
    return result


def notifications(request):
    if not request.user.is_authenticated:
        return {}

    user_notifications = Notification.objects.filter(user=request.user)
    return {"notifications": user_notifications}
