from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from user.views import (
    ProfileView,
    ProfileEditView,
)

urlpatterns = [
    path(
        'in/<str:username>/',
        login_required(ProfileView.as_view()),
        name='profile_view'
    ),
    path(
        'in/<str:username>/edit/',
        login_required(ProfileEditView.as_view()),
        name='profile_edit_view'
    ),

]
