from django.shortcuts import render, redirect
from django.views.generic import View
from authentication.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView


# Create your views here


class SignInView(View):
    template_name = 'authentication/signin.html'

    def get(self, request, *args, **kwargs):
        # always remember request object always have the instance of user, which is currently loggedin.
        if request.user.is_authenticated:
            return redirect('home_feed')

        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        # user login logic
        email = request.POST.get('email')
        password = request.POST.get('password')

        # what it will do it will get request, email and password and
        # check if user is authenticated or in the Database
        # so it return the object of that user we provide the email and password of, to us.
        # if user is not present in the DB then Authentication function will return none
        user = authenticate(request, email=email, password=password)

        if user is None:
            return render(request, self.template_name)
        login(request, user)
        print(user)

        return redirect('home_feed')


class SignUpView(View):
    template_name = 'authentication/signup.html'
    form_class = UserForm

    def get(self, request, *args, **kwargs):
        # always remember request object always have the instance of user, which is currently loggedin.
        if request.user.is_authenticated:
            return redirect('home_feed')

        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin_view')

        context = {'form': form}
        return render(request, self.template_name, context)


class SignOutView(View):
    def post(self, request, *args, **kwargs):
        # logout he user and redirect to the signin page
        logout(request)
        # Redirect to a success page.
        return redirect('signin_view')


class PRView(PasswordResetView):
    template_name = 'authentication/password_reset.html'


class PRConfirmView(PasswordResetConfirmView):
    template_name = 'authentication/password_reset_confirm.html'
