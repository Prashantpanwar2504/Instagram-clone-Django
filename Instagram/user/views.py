from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import get_user_model
from user.forms import UserEditForm

# Create your views here.
User = get_user_model()


class ProfileView(View):
    template_name_anom = 'user/anonymous_profile.html'
    template_name_auth = 'user/authenticated_profile.html'

    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            return HttpResponse('<center><h1>This User Does not Exists.</h1></center>')

        context = {'user': user}

        if username == request.user.username:
            return render(request, self.template_name_auth, context=context)
        else:
            return render(request, self.template_name_anom, context=context)


class ProfileEditView(View):
    template_name = 'user/profile_edit.html'
    form_class = UserEditForm
    def get(self, request, *args, **kwargs):
        form = self.form_class
        context = {'form':form}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        pass
