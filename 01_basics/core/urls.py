from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', views.home, name='home'),
    path('', cache_page(10)(views.home), name='home'),

]