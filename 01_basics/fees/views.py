from django.shortcuts import render

def fees_django(request):
    return render(request, 'fees/fees_django.html', {'fees':1100, 'course':'django'})

def fees_python(request):
    return render(request, 'fees/fees_python.html', {'fees':900, 'course':'python'})
