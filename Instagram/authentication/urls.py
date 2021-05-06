from django.contrib import admin
from django.urls import path, include
from authentication.views import (
    SignInView,
    SignUpView,
    SignOutView,
    )

urlpatterns = [
    path('', SignInView.as_view(), name='signin_view'),
    path('signup/', SignUpView.as_view(), name='signup_view'),
    path('signout/', SignOutView.as_view(), name='signout_view'),
]