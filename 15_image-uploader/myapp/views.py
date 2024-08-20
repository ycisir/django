from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ImageForm
from django.contrib import messages
from django.views.generic.edit import FormView
from .models import Image


class UploadImageFormView(FormView):
    template_name = 'myapp/home.html'
    form_class = ImageForm
    success_url = '/'


    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Uploaded successfully!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["images"] = Image.objects.all()
        print(context)
        return context

    