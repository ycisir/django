from django.urls import path
from . import views

urlpatterns = [
    path('technologies', views.skills, name='technologies')
]
