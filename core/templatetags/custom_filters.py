from django import template
from django import template
from django.utils import timezone
import re
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def is_liked(note, user):
    return note.likes.filter(user=user).exists()

@register.filter
def is_disliked(note, user):
    return note.dislikes.filter(user=user).exists()

@register.simple_tag(name='highlight')
def highlight(text, query, style):
    if not query:
        return text 
    
    query_terms = query.split()
    escaped_terms = [re.escape(term) for term in query_terms]
    joined_pattern = '|'.join(escaped_terms)
    
    def get_replacement(match):
        match_text = match.group(0)
        if style == 'note_title':
            return f'<span class="bg-yellow-300">{match_text}</span>'
        elif style == 'user':
            return f'<span class="font-medium bg-yellow-300">{match_text}</span>'
        elif style == 'note_detail':
            return f'<span class="bg-yellow-300">{match_text}</span>'
        else:
            return match_text  
    
    
    highlighted = re.sub(f"({joined_pattern})", get_replacement, text, flags=re.IGNORECASE)

    return mark_safe(highlighted)

@register.filter(name='formattime')
def formattime(value):
    if isinstance(value, timezone.datetime):
        now = timezone.now()
        diff = now - value

        days = diff.days
        seconds = diff.seconds
        hours = seconds // 3600
        minutes = (seconds // 60) % 60

        if days > 0:
            return f"{days}d ago"
        elif hours > 0:
            return f"{hours}h ago"
        elif minutes > 0:
            return f"{minutes}m ago"
        else:
            return "Just now"
    return value