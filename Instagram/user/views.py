from django.shortcuts import render
from django.views.generic import View


# Create your views here.

class ProfileView(View):
    template_name_anon = 'user/anonymous_profile.html'
    template_name_auth = 'user/authenticated_profile.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name_auth)
