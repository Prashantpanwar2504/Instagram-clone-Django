from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model  # it will return user model


User = get_user_model()

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = {'full_name', 'email', 'username', 'password1', 'password2'}


# UserChangeForm

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = {'full_name', 'email', 'username', }
