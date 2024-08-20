from django.shortcuts import render

def learn_django(request):
    return render(request, 'course/course_django.html', {'course': ''})

def learn_python(request):
    return render(request, 'course/course_python.html', {'course': 'python'})

def learn_flask(request):
    return render(request, 'course/course_flask.html', {'course': 'flask'})

def top_courses(request):
    return render(request, 'course/top_courses.html')