from django import template
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
            return f'<span class="highlight highlight_note_title">{match_text}</span>'
        elif style == 'user':
            return f'<span class="highlight highlight_user">{match_text}</span>'
        elif style == 'note_detail':
            return f'<span class="highlight highlight_note_detail">{match_text}</span>'
        else:
            return match_text  
    
    
    highlighted = re.sub(f"({joined_pattern})", get_replacement, text, flags=re.IGNORECASE)

    return mark_safe(highlighted)
