from django.urls import path
from . import views

urlpatterns = [
    path('', views.UploadImageFormView.as_view(), name='home'),
]