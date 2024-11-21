from django.db.models import Count
from course.models import Course
from clicks.models import ClickNote, ClickTag, ClickCourse
from notes.models import Note
from notifications.models import Notification
from tags.models import Tag


def courses_list(request):
    return {"your_courses": Course.objects.all().distinct()}


def trending(request):
    trending_notes = (
        ClickNote.objects.values("note")
        .annotate(click_count=Count("id"))
        .order_by("-click_count")
    )[:5]

    trending_tags = (
        ClickTag.objects.values("tag")
        .annotate(click_count=Count("id"))
        .order_by("-click_count")
    )[:5]

    trending_courses = (
        ClickCourse.objects.values("course")
        .annotate(click_count=Count("id"))
        .order_by("-click_count")
    )[:5]

    trending_notes = Note.objects.filter(
        id__in=[note["note"] for note in trending_notes]
    ).prefetch_related("created_by")

    trending_tags = Tag.objects.filter(id__in=[tag["tag"] for tag in trending_tags])

    trending_courses = Course.objects.filter(
        id__in=[course["course"] for course in trending_courses]
    )

    return {
        "trending_notes": trending_notes,
        "trending_tags": trending_tags,
        "trending_courses": trending_courses,
    }


def recent_posts(request):
    notes = Note.objects.all().order_by("-created_at")[:5]
    return {"recent_posts": notes}


def notifications(request):
    if not request.user.is_authenticated:
        return {}

    notifications = Notification.objects.filter(user=request.user)
    return {"notifications": notifications}
