from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from user.views import (
    ProfileView,
)

urlpatterns = [
    path('<str:username>/', login_required(ProfileView.as_view()), name='profile_view'),

]
