from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q
from datetime import date, time
from django.db.models import Avg, Min, Max, Sum, Count
# Create your views here.

# ================================= return new Query sets =================================
# def home(request):

#     # student_data = Student.objects.all()

#     # student_data = Student.objects.filter(marks=95)

#     # student_data = Student.objects.exclude(marks=95)

#     # Capital letter first
#     # student_data = Student.objects.order_by('name') # name = asc, -name = desc, ? = random

#     # student_data = Student.objects.order_by('id').reverse()[:3]

#     # student_data = Student.objects.values('name', 'city') # return dict

#     # student_data = Student.objects.values_list() # return tuple
#     # student_data = Student.objects.values_list('id', 'name') # return tuple
#     # student_data = Student.objects.values_list('id', 'name', named=True) # return tuple

#     # student_data = Student.objects.using('default') # which database want to use

#     # student_data = Student.objects.dates('pass_out', 'year')

#     # ==== Teacher table ====
    
#     # qs1 = Student.objects.values_list('id', 'name', named=True)
#     # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    
#     # union - eliminate same data from col1, col2, .... various cols
#     # student_data = qs2.union(qs1)
#     # student_data = qs2.union(qs1, all=True)

#     # intersection - return shared element mean both have same name and id
#     # student_data = qs2.intersection(qs1)

#     # difference - eliminate qs1
#     # student_data = qs2.difference(qs1)

#     # ====== AND / OR operator =======
#     # student_data = Student.objects.filter(id=1) & Student.objects.filter(roll=11)
#     # student_data = Student.objects.filter(id=1, roll=11)
#     # student_data = Student.objects.filter(Q(id=1) & Q(roll=11))

#     # student_data = Student.objects.filter(Q(id=1) | Q(roll=13))

#     # print(f'Return {student_data}')
#     # print()
#     # print(f'SQL Query: {student_data.query}')

#     return render(request, 'school/home.html', {'students':student_data})





# ================================= don't return new Query sets =============================

# def home(request):

    # student_data = Student.objects.get(pk=1) #use only unique val like id
    # student_data = Student.objects.get(name='Harry Potter')

    # student_data = Student.objects.first()
    # student_data = Student.objects.order_by('name').first()

    # student_data = Student.objects.last()
    # student_data = Student.objects.order_by('name').last()

    # student_data = Student.objects.latest('pass_out')

    # student_data = Student.objects.earliest('pass_out')

    # student_data = Student.objects.all()
    # print(student_data.exists())

    # one_data = Student.objects.get(pk=1)
    # print(student_data.filter(pk=one_data.pk).exists())

    # student_data = Student.objects.create(name='Ginny Weasley', roll=16, city='Catchpole', marks=93, pass_out='2024-4-3')

    # student_data, created = Student.objects.get_or_create(name='Cho Chang', roll=18, city='Witchcraft', marks=87, pass_out='2024-4-3')
    # print(created)

    # student_data = Student.objects.filter(id=1).update(city='Indian Ocean')
    # student_data = Student.objects.filter(city='Catchpole').update(marks=91) # multiple

    # student_data, created = Student.objects.update_or_create(name='Cho Chang', roll=18, city='Witchcraft', marks=87, pass_out='2024-4-3')
    # student_data, created = Student.objects.update_or_create(id=9, name='Chang', defaults={'name':'Cho Chang'})

    # objs = [
    #     Student(name='test1', roll=100, city='test city', marks=50, pass_out='2024-4-3'),
    #     Student(name='test2', roll=102, city='test1 city', marks=30, pass_out='2024-4-4'),
    #     Student(name='test3', roll=103, city='test2 city', marks=35, pass_out='2024-4-5')
    # ]
    # student_data = Student.objects.bulk_create(objs)
    # student_data = Student.objects.bulk_update(objs)

    # all_student_data = Student.objects.all()
    # for stu in all_student_data:
    #     stu.city = 'Test'
    #     all_student_data = Student.objects.bulk_update(all_student_data, ['city'])

    # student_data = Student.objects.in_bulk([1,2])
    # print(student_data[1].name)
    # print(student_data[2].name)
    # student_data = Student.objects.in_bulk([])
    # student_data = Student.objects.in_bulk()
    
    # student_data = Student.objects.get(pk=9).delete()
    # student_data = Student.objects.filter(marks=-99).delete()

    # student_data = Student.objects.get(pk=1)
    # print(student_data.count())
    # print(student_data.explain())

    # print(f'Return {student_data}')

    # return render(request, 'school/home.html', {'student':student_data})




# ====================================== Field lookups ==================================

# def home(request):
    # where, i=insensitive means [y or Y] both same
    # student_data = Student.objects.all()

    # student_data = Student.objects.filter(name__exact='Harry Potter')
    # student_data = Student.objects.filter(name__iexact='harry potter')

    # student_data = Student.objects.filter(name__contains='a')
    # student_data = Student.objects.filter(name__icontains='a')

    # student_data = Student.objects.filter(id__in=[1,3,5])

    # student_data = Student.objects.filter(marks__in=[93, 91, 95])

    # student_data = Student.objects.filter(marks__gt=85)
    # student_data = Student.objects.filter(marks__gte=85)
    # student_data = Student.objects.filter(marks__lt=85)
    # student_data = Student.objects.filter(marks__lte=85)

    # student_data = Student.objects.filter(name__startswith='h')
    # student_data = Student.objects.filter(name__istartswith='h')

    # student_data = Student.objects.filter(name__endswith='y')
    # student_data = Student.objects.filter(name__iendswith='y')

    # student_data = Student.objects.filter(pass_out__range=('2021-08-01', '2021-10-01'))

    # student_data = Student.objects.filter(admission_time__date=date(2021, 9, 1))
    # student_data = Student.objects.filter(admission_time__date__gt=date(2021, 9, 1))

    # student_data = Student.objects.filter(pass_out__year=2021)
    # student_data = Student.objects.filter(pass_out__year__gt=2021)
    # student_data = Student.objects.filter(pass_out__year__gte=2021)

    # student_data = Student.objects.filter(pass_out__month=9)
    # student_data = Student.objects.filter(pass_out__month__gt=9)
    # student_data = Student.objects.filter(pass_out__month__gte=9)

    # student_data = Student.objects.filter(pass_out__day=1)

    # student_data = Student.objects.filter(pass_out__week_day=4)
    
    # student_data = Student.objects.filter(pass_out__quarter=3)

    # student_data = Student.objects.filter(admission_time__time__gt=time(12,00))

    # student_data = Student.objects.filter(admission_time__hour__gt=5)
    # student_data = Student.objects.filter(admission_time__minute=45)
    # student_data = Student.objects.filter(admission_time__second=5)

    # student_data = Student.objects.filter(roll__isnull=False)

    # print(f'Return: {student_data}')
    # print(f'Query: {student_data.query}')
    # return render(request, 'school/home.html', {'students':student_data})



# ====================================== Aggregation ==================================

# def home(request):

#     student_data = Student.objects.all()
#     avg = student_data.aggregate(Avg('marks'))
#     total = student_data.aggregate(Sum('marks'))
#     min = student_data.aggregate(Min('marks'))
#     max = student_data.aggregate(Max('marks'))
#     cnt = student_data.aggregate(Count('marks'))
#     # print(avg)

#     context = {'students':student_data, 'avg':avg, 'total':total, 'min':min, 'max':max, 'cnt':cnt}

#     print(f'Return: {student_data}')
#     print(f'Query: {student_data.query}')
#     return render(request, 'school/home.html', context)



# ====================================== Q objects ==================================

# def home(request):
    # student_data = Student.objects.filter(Q(id=5) & Q(roll=16))

    # student_data = Student.objects.filter(Q(id=5) | Q(roll=7))

    # student_data = Student.objects.filter(~Q(id=4))


    # print(f'Return: {student_data}')
    # print(f'Query: {student_data.query}')
    # return render(request, 'school/home.html', {'students':student_data})



# ====================================== Limiting QuerySet ==================================

def home(request):

    student_data = Student.objects.all()[:3]

    print(f'Return: {student_data}')
    print()
    print(f'Query: {student_data.query}')
    return render(request, 'school/home.html', {'students':student_data})