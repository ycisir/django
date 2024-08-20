from django.shortcuts import render

def proj(request):
    context = {'project': 'active'}
    return render(request, 'project/project.html', context)
