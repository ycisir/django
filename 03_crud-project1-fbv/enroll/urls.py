from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_show, name='home'),
    path('delete/<int:id>', views.delete_student, name='delete'),
    path('update/<int:id>', views.update_student, name='update'),
]

