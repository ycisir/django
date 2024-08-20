from django.shortcuts import render


def home(request):
    context = {'home': 'active'}
    return render(request, 'core/home.html', context)
