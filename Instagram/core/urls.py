from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from core.views import (
    HomeView,
)

urlpatterns = [
    path('feed/', login_required(HomeView.as_view()), name='home_feed'),

]
