from django.contrib import admin
from .models import Student, Teacher
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city', 'marks', 'pass_out', 'admission_time']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'emp_num', 'city', 'salary', 'join_date']