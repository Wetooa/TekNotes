from django import template

register = template.Library()

@register.filter
def is_liked(note, user):
    return note.likes.filter(user=user).exists()

@register.filter
def is_disliked(note, user):
    return note.dislikes.filter(user=user).exists()