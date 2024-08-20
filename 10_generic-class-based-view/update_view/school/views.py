from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from .models import Student
from .forms import StudentForm

class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = 'school/student_form.html'
    success_url = '/thanks/'

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'school/student_form.html'
    success_url = '/thanks/'


class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'



