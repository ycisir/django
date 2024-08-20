from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.views.generic import TemplateView

class ContactFormView(FormView):
    template_name = 'school/contact.html'
    form_class = ContactForm # used to recognize which form if there are multiple forms
    success_url = '/thankyou/'
    initial = {'name': 'Your name'}

    def form_valid(self, form):
        # print(form)
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['message'])
        return super().form_valid(form)


class ThanksTemplateView(TemplateView):
    template_name = 'school/thankyou.html'