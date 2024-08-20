from django.urls import path
from student import views

urlpatterns = [
    # path('set', views.setcookie, name='set'),
    # path('get', views.getcookie, name='get'),
    # path('del', views.delcookie, name='del'),

    path('set', views.setsession, name='set'),
    path('get', views.getsession, name='get'),
    path('del', views.delsession, name='del'),

    # path('set', views.settestcookie, name='set'),
    # path('check', views.checktestcookie, name='check'),
    # path('del', views.deltestcookie, name='del'),
]
