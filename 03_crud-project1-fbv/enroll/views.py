from django.shortcuts import render, HttpResponseRedirect
from .form import StudentRegistration
from .models import User
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'enroll/home.html')

# this function will add new student as well as show students
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            stud_name = fm.cleaned_data['name']
            stud_email = fm.cleaned_data['email']
            stud_pass = fm.cleaned_data['password']
            register = User(name=stud_name, email=stud_email, password=stud_pass)
            register.save()
            fm = StudentRegistration()
            messages.success(request, 'Added successfully')

    else:
        fm = StudentRegistration()

    
    stud = User.objects.all()

    return render(request, 'enroll/home.html', {'stu':stud, 'form':fm})


# this function will update and edit
def update_student(request, id):
    if request.method == 'POST':
        tmp = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=tmp)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()
            messages.success(request, 'Updated successfully')
            return HttpResponseRedirect('/')
    else:
        tmp = User.objects.get(pk=id)
        fm = StudentRegistration(instance=tmp)
    return render(request, 'enroll/update.html', {'form':fm})


# this function will delete
def delete_student(request, id):
    if request.method == 'POST':
        tmp = User.objects.get(pk=id)
        tmp.delete()
        messages.warning(request, 'Deleted successfully!')
        return HttpResponseRedirect('/')
