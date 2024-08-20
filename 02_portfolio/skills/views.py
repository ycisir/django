from django.shortcuts import render

def skills(request):
    context = {'skills': 'active'}
    return render(request, 'skills/skills.html', context)
