from django.urls import path
from . import views

urlpatterns = [
    path('all_project', views.proj, name='all_project')
]
