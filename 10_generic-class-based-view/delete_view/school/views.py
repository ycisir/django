from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
    success_url = '/updated/'

class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/deleted/'
    # template_name = 'something'


class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'

class UpdateTemplateView(TemplateView):
    template_name = 'school/update.html'

class DeleteTemplateView(TemplateView):
    template_name = 'school/deleted.html'