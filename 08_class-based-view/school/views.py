from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ContactForm
from django.http import HttpResponse
from django.views.generic.base import TemplateView, RedirectView

# class Home(View):
#     name = 'Jack'
#     def get(self, request):
#         return HttpResponse(self.name)
    

# class HomeChild(Home):
#     def get(self, request):
#         return HttpResponse(self.name)

# class Home(View):
#     def get(self, request):
#         form = ContactForm()
#         return render(request, 'school/home.html', {'form':form})
    
#     def post(self, request):
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data['name'])
#             print(form.cleaned_data['email'])
#             return HttpResponse('Form submitted successfully!')


# ========= use single view function to render multiple template file ===========
# def fun(request, template_name):
#     template_name = template_name
#     context = {'info': 'Django is best framework for backend development.'}
#     return render(request, template_name, context)


# class News(View):
#     template_name = ''
#     def get(self, request):
#         context = {'info': 'Django is best framework for backend development.'}
#         return render(request, self.template_name, context)




# ====================== TemplateView ===================
# class HomeTemplateView(TemplateView):
#     template_name = 'school/home.html'


# class HomeTemplateView(TemplateView):
#     template_name = 'school/home.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['name'] = 'Yasir'
#         context['roll'] = 19
#         # context = {
#         #     in this way extra context does not work
#         #     'name': 'Yasir',
#         #     'roll': 19,
#         # }
#         print(context)
#         print(kwargs)
#         return context
    


# =============================== RedirectView =========================
# class GithubRedirectView(RedirectView):
#     url = 'https://www.github.com'
#     pattern_name = ''


class HomeRedirectView(RedirectView):
    pattern_name = 'id'
    permanent = True
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        return super().get_redirect_url(*args, **kwargs)