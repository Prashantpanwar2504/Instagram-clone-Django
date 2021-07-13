from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import get_user_model
from user.forms import UserEditForm
from django.contrib import messages

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
        username = kwargs.get('username')

        if username != request.user.username:
            return HttpResponse('<center><h1>This Page Does not Exists.</h1></center>')

        form = self.form_class(instance=request.user)
        context = {'form': form}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile_edit_view', request.user.username)
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
            context = {'form':form}
            return  render(request, self.template_name, context=context)