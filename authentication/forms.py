from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from authentication.models import Users

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Users
        fields = ('username', 'email', 'phone_number')  # Add your custom fields

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Users
        fields = ('username', 'email', 'phone_number')
