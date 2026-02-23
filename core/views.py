from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Exists, OuterRef, Subquery
from notes.models import Note
from course.models import Course
from tags.models import Tag
from comments.models import Like, Dislike

NOTES_PER_PAGE = 30


def _paginate_notes(request, queryset):
    paginator = Paginator(queryset, NOTES_PER_PAGE)
    page_number = request.GET.get("page", 1)
    return paginator.get_page(page_number)


def _annotate_likes(queryset, user):
    if not user.is_authenticated:
        return queryset
    return queryset.annotate(
        _liked_by_user=Exists(Like.objects.filter(note=OuterRef("pk"), user=user)),
        _disliked_by_user=Exists(Dislike.objects.filter(note=OuterRef("pk"), user=user)),
    )


def index(request):
    all_notes = _annotate_likes(
        Note.objects.filter(is_archived=False, is_private=False).order_by("-modified_at"),
        request.user,
    )
    notes = _paginate_notes(request, all_notes)
    courses = Course.objects.filter(note__in=all_notes).distinct()
    tags = Tag.objects.filter(notes__in=all_notes).distinct()

    return render(
        request, "core/index.html", {"notes": notes, "courses": courses, "tags": tags}
    )


@login_required
def notebook(request):
    all_notes = _annotate_likes(
        Note.objects.filter(created_by=request.user, is_archived=False).order_by("-modified_at"),
        request.user,
    )
    notes = _paginate_notes(request, all_notes)
    courses = Course.objects.filter(note__in=all_notes).distinct()
    tags = Tag.objects.filter(notes__in=all_notes).distinct()

    return render(
        request,
        "core/notebook.html",
        {"notes": notes, "courses": courses, "tags": tags},
    )


@login_required
def archive(request):
    all_notes = _annotate_likes(
        Note.objects.filter(created_by=request.user, is_archived=True).order_by("-modified_at"),
        request.user,
    )
    notes = _paginate_notes(request, all_notes)
    courses = Course.objects.filter(note__in=all_notes).distinct()
    tags = Tag.objects.filter(notes__in=all_notes).distinct()

    return render(
        request,
        "core/archive.html",
        {"notes": notes, "courses": courses, "tags": tags},
    )


@login_required
def likes(request):
    latest_likes = Like.objects.filter(note=OuterRef("pk"), user=request.user).order_by(
        "-created_at"
    )
    all_liked = _annotate_likes(
        Note.objects.filter(likes__user=request.user, is_private=False)
        .annotate(like_created_at=Subquery(latest_likes.values("created_at")[:1]))
        .distinct()
        .order_by("-like_created_at"),
        request.user,
    )
    notes = _paginate_notes(request, all_liked)

    courses = Course.objects.filter(note__in=all_liked).distinct()
    tags = Tag.objects.filter(notes__in=all_liked).distinct()

    return render(
        request, "core/likes.html", {"notes": notes, "courses": courses, "tags": tags}
    )
