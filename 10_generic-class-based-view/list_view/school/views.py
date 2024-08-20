from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student

class StudentListView(ListView):
    model = Student

    # custom
    # template_name_suffix = '_get'
    # ordering = ['roll']
    # template_name = 'school/student.html'
    # context_object_name = 'students'

    def get_queryset(self):
        return Student.objects.filter(course='Django')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['freshers'] = Student.objects.all().order_by('name')
        return context

    # def get_template_names(self):
    #     if self.request.COOKIES['user'] == 'yasir':
    #         template_name = ['school/yasir.html']
    #     else:
    #         template_name = self.template_name

    #     return [template_name]
    
    