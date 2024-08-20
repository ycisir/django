from typing import Any
from django.shortcuts import render
from .models import Student
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

class StudentDetailView(DetailView):
    model = Student

    # custom things
    # template_name = 'school/student.html'
    # context_object_name = 'stu'
    # pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_students'] = self.model.objects.all().order_by('name')
        return context




class StudentListView(ListView):
    model = Student