from django import forms
from user.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model #it will return user model



class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = {'full_name', 'email', 'username', 'password1', 'password2'}