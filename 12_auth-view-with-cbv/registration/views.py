from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import TemplateView



# decorating in the class better approach than url-conf

# best way
# @method_decorator(staff_member_required, name='dispatch')
@method_decorator(login_required, name='dispatch')
class ProfileTemplateView(TemplateView):
    template_name = 'registration/profile.html'

    # 1st way
    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

