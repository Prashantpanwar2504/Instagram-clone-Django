from django.shortcuts import render, redirect
from django.views.generic import View
from authentication.forms import UserForm
from django.contrib import messages
from django.contrib.auth import (authenticate,
                                 login,
                                 logout,
                                 get_user_model)


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
        email_username = request.POST.get('email_username')
        password = request.POST.get('password')

        # what it will do it will get request, email and password and
        # check if user is authenticated or in the Database
        # so it return the object of that user we provide the email and password of, to us.
        # if user is not present in the DB then Authentication function will return none

        # case 1: when user provide username instead of email
        # if user provide the username instead of email, we need to fine the email of the user.
        # How to do that.
        # we can do one thing, we can find the object of user with the help of email_username field and them we can get
        # the email of that user with the help if '.'
        User = get_user_model()

        try:
            user_object = User.objects.get(username=email_username)  # username case
            # getting the email from the user object
            email = user_object.email
        except Exception as e:
            # case 2: when user provide email instead of username
            # making email_username, email cuz user provide email in the email_username field.
            print(e)
            email = email_username  # email case

        # case 2: when user provide email instead of username

        user = authenticate(request, email=email, password=password)

        if user is None:
            messages.error(request, "Invalid username or password.")
            return render(request, self.template_name, #context={
                #'messages': "Invalid Username or Password."}
                          )

        login(request, user)

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

# class PRView(PasswordResetView):
#     email_template_name = 'authentication/password_reset_email.html'
#     template_name = 'authentication/password_reset.html'
#
#
# class PRDoneView(PasswordResetDoneView):
#     template_name = 'authentication/password_reset_done.html'
#
#
# class PRConfirmView(PasswordResetConfirmView):
#     template_name = 'authentication/password_reset_confirm.html'
#
#
# class PRCompleteView(PasswordResetCompleteView):
#     template_name = 'authentication/password_reset_complete.html'
