from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse


def blog(request):
    print('I\'m blog view')
    return HttpResponse('This is blog page')

def excep(request):
    print('I\'m exception view')
    a = 10/0
    return HttpResponse('This is exception page')

def user_info(request):
    context = {'name': 'Jack'}
    return TemplateResponse(request, 'blog/user.html', context)