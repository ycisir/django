from django.shortcuts import render
from .models import Student, ProxyStudent

def home(request):
    # model manager
    # student_data = Student.objects.all()



    # custom model manager
    # student_data = Student.students.all()
    student_data = ProxyStudent.students.get_roll_range(1,13)
    return render(request, 'school/home.html', {'students':student_data})