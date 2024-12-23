from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your username",
                "class": "placeholder-gray-500 text-gray-700 dark:text-gray-50 bg-transparent border-none focus:outline-none flex-1",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Your password",
                "class": "placeholder-gray-500 text-gray-700 dark:text-gray-50 bg-transparent border-none focus:outline-none flex-1",
            }
        )
    )


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "autocomplete": "off",
                "placeholder": "Username",
                "class": "placeholder-gray-500 text-gray-700 dark:text-gray-50 bg-transparent border-none focus:outline-none flex-1",
            }
        )
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "autocomplete": "off",
                "placeholder": "First name",
                "class": "placeholder-gray-500 text-gray-700 dark:text-gray-50 bg-transparent border-none focus:outline-none w-full",
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "autocomplete": "off",
                "placeholder": "Last name",
                "class": "placeholder-gray-500 text-gray-700 dark:text-gray-50 bg-transparent border-none focus:outline-none w-full",
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "autocomplete": "off",
                "placeholder": "Email address",
                "class": "placeholder-gray-500 text-gray-700 dark:text-gray-50 bg-transparent border-none focus:outline-none flex-1",
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "off",
                "placeholder": "Password",
                "class": "placeholder-gray-500 text-gray-700 dark:text-gray-50 bg-transparent border-none focus:outline-none flex-1",
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "off",
                "placeholder": "Confirm password",
                "class": "placeholder-gray-500 text-gray-700 dark:text-gray-50 bg-transparent border-none focus:outline-none flex-1",
            }
        )
    )
