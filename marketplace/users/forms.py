from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

User = get_user_model()

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label='Email',
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email', 'placeholder': 'Email'})
    )
    username = forms.CharField(
        label='Username',
        max_length=50,
        widget=forms.TextInput(attrs={'autocomplete': 'username','placeholder': 'Username'})
    )
    password1 = forms.CharField(
        label='password1',
        max_length=50,
        widget=forms.PasswordInput(attrs={'autocomplete': 'password' ,'placeholder': 'Password'})
    )

    password2 = forms.CharField(
        label='password2',
        max_length=50,
        widget=forms.PasswordInput(attrs={'placeholder': 'Validate your password'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")