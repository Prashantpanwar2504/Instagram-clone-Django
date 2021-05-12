from django.contrib import admin
from django.urls import path, include
from authentication.views import (
    SignInView,
    SignUpView,
    SignOutView,
)
from django.contrib.auth.views import (PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView
                                       )

urlpatterns = [
    path('', SignInView.as_view(), name='signin_view'),
    path('signup/', SignUpView.as_view(), name='signup_view'),
    path('signout/', SignOutView.as_view(), name='signout_view'),


    path('password/reset/', PasswordResetView.as_view(
        template_name='authentication/password_reset.html',  # keyworded argument
        email_template_name='authentication/password_reset_email.html'
    ),
         name='password_reset'),
    path('password/reset/done/', PasswordResetDoneView.as_view(
        template_name='authentication/password_reset_done.html'
    ), name='password_reset_done'),

    path('password/reset/confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(
        template_name='authentication/password_reset_confirm.html'
    ), name='password_reset_confirm'),

    path('password/reset/complete', PasswordResetCompleteView.as_view(
        template_name='authentication/password_reset_complete.html'
    ), name='password_reset_complete'),

]
