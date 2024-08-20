from django.urls import path
from . import views

urlpatterns = [
    path('test', views.blog, name='test'),
    path('excep', views.excep, name='excep'),
    path('user', views.user_info, name='user'),
]