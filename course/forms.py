from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'description', 'color']
    
    def clean_code(self):
        code = self.cleaned_data.get('code')
        if len(code) > 20:
            raise forms.ValidationError("Course code cannot be longer than 20 characters.")
        return code

    code = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Code',
        'class': 'placeholder-gray-500 text-gray-700 dark:text-gray-50 bg-transparent border-none focus:outline-none w-full',
    }))

    description = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Description',
        'class': 'placeholder-gray-500 text-gray-700 dark:text-gray-50 bg-transparent border-none focus:outline-none w-full',
    }))

    color = forms.ChoiceField(choices=Course.COLORS, widget=forms.Select(attrs={
        'class': 'text-gray-700 dark:text-gray-50 bg-transparent border-none focus:outline-none',
    }))