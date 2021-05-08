from django.contrib import admin
from django.urls import path, include
from authentication.views import (
    SignInView,
    SignUpView,
    SignOutView,
    PRView,
    PRConfirmView,
    )

urlpatterns = [
    path('', SignInView.as_view(), name='signin_view'),
    path('signup/', SignUpView.as_view(), name='signup_view'),
    path('signout/', SignOutView.as_view(), name='signout_view'),
    path('password/reset/', PRView.as_view(), name='password_reset'),
    #path('password/reset/done/', name='password_reset_done'),
    path('password/reset/confirm/<uidb64>/<token>',PRConfirmView.as_view(), name='password_reset_confirm'),
    #path('password/reset/complete', name='password_reset_complete'),

]