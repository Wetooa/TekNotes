from django import forms
from .models import Note, Course


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content", "course", "tags", "is_private"]

    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        empty_label=None,
        widget=forms.Select(
            attrs={
                "class": "placeholder-gray-500 text-gray-700 bg-transparent border-none focus:outline-none flex-1 w-full"
            }
        ),
        required=False,
    )

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Title",
                "class": "placeholder-gray-500 font-medium text-xl text-gray-700 bg-transparent border-none focus:outline-none",
            }
        )
    )

    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Content",
                "class": "placeholder-gray-500 text-gray-700 bg-transparent border-none focus:outline-none flex-1 resize-none",
                "rows": 10,
            }
        )
    )

    tags = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Tags (separate with comma)",
                "class": "placeholder-gray-500 text-gray-700 bg-transparent border-none focus:outline-none flex-1",
            }
        ),
        required=False,
    )

    is_private = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={"class": "border-2 border-rose-700 w-4 h-4"}),
    )
