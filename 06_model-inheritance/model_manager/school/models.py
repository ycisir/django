from django.db import models
from .managers import CustomManager

class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()

    # model manager
    objects = models.Manager()

    # custom model mangager
    students = CustomManager()


class ProxyStudent(Student):
    students = CustomManager()
    class Meta:
        proxy = True
        ordering = ['name']