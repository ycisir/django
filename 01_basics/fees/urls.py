from django.urls import path
from . import views

urlpatterns = [
    path('django', views.fees_django, name='fees_django'),
    path('python', views.fees_python, name='fees_python'),
]
