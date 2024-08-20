from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from myapp.forms import LoginForm
from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name= 'myapp/home.html'

class DashboardTemplateView(TemplateView):
    template_name= 'myapp/dashboard.html'

class MyLoginView(LoginView):
    template_name= 'myapp/login.html'
    authentication_form = LoginForm

class MyLogoutView(LogoutView):
    template_name= 'myapp/logout.html'

class MyPasswordChangeView(PasswordChangeView):
    template_name='myapp/change_pass.html'
    success_url= '/change-password-done/'

class MyPasswordChangeDoneView(PasswordChangeDoneView):
    template_name='myapp/change_pass_done.html'