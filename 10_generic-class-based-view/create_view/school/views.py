from django.forms import BaseModelForm
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .models import Student
from django import forms
from .forms import StudentForm 

# =============== 1st way to use css in form ==================
# class StudentCreateView(CreateView):
#     model = Student
#     fields = ['name', 'email', 'password']
#     # success_url = '/thanks/' # also do in models

#     def get_form(self):
#         form = super().get_form()
#         form.fields['name'].widget = forms.TextInput(attrs={
#             'class':'my-class',
#             'placeholder':'Your name'
#             })
#         form.fields['email'].widget = forms.EmailInput(attrs={
#             'class':'my-class',
#             'placeholder':'Your email'
#             })
#         form.fields['password'].widget = forms.PasswordInput(attrs={
#             'class':'my-class',
#             'placeholder':'Password'
#             })
#         return form



# =============== 2nd way to use css in form best way ==================
class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = 'school/student_form.html'


class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'


class StudentDetailView(DetailView):
    model = Student