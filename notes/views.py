from django.http import HttpResponseRedirect
from clicks.models import ClickNote, ClickTag, ClickCourse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import NoteForm
from tags.models import Tag
from .models import Note

@login_required
def tek_a_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.created_by = request.user

            note.save()

            tag_input = request.POST.get("tags", "")
            if tag_input:
                tag_names = [tag.strip() for tag in tag_input.split(",")]
                for tag_name in tag_names:
                    if tag_name:
                        tag, created = Tag.objects.get_or_create(name=tag_name)
                        note.tags.add(tag)

            return render(request, "core/loading.html", {"success": True, "message": f"Teking note..."})
    else:
        form = NoteForm()

    return render(request, "notes/tek_a_note.html", {"form": form})


def save_note_clicks(note):
    ClickNote.objects.create(note=note)

    for tag in note.tags.all():
        ClickTag.objects.create(tag=tag)

    if note.course:
        ClickCourse.objects.create(course=note.course)


def note_detail(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        return render(request, "notes/note_missing.html", {"note_id": note_id})

    if note.created_by != request.user and (note.is_private or note.is_archived):
        return render(request, "notes/note_restricted.html", {"note_id": note_id})

    save_note_clicks(note)
    return render(request, "notes/note_detail.html", {"note": note})


@login_required
def delete_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        return render(request, "notes/note_missing.html", {"note_id": note_id})

    for tag in note.tags.all():
        if tag.notes.count() == 1:
            tag.delete()

    note.delete()

    return render(request, "core/loading.html", {"success": True, "message": f"Deleting note (id: {note_id})"})


@login_required
def archive_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        return render(request, "notes/note_missing.html", {"note_id": note_id})

    note.is_archived = not note.is_archived
    note.save()

    if (request.GET.get('note_detail')):
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
    return render(request, "core/loading.html", {"success": True, "message": f"Archiving note (id: {note_id})"})


@login_required
def hide_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        return render(request, "notes/note_missing.html", {"note_id": note_id})

    note.is_private = not note.is_private
    note.save()

    if (request.GET.get('note_detail')):
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
    return render(request, "core/loading.html", {"success": True, "message": f"Hiding note (id: {note_id})"})

@login_required
def edit_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        return render(request, "notes/note_missing.html", {"note_id": note_id})
    
    tags = ", ".join(tag.name for tag in note.tags.all())

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            updated_note = form.save(commit=False)
            updated_note.created_by = request.user
            updated_note.save()

            tag_input = request.POST.get("tags", "")
            if tag_input:
                tag_names = [tag.strip() for tag in tag_input.split(",")]
                note.tags.clear()
                for tag_name in tag_names:
                    if tag_name:
                        tag, created = Tag.objects.get_or_create(name=tag_name)
                        updated_note.tags.add(tag)

            return render(request, "core/loading.html", {"success": True, "message": f"Saving note..."})
    else:
        form = NoteForm(instance=note)

    return render(request, "notes/edit_note.html", {"form": form, "note": note, "tags": tags})