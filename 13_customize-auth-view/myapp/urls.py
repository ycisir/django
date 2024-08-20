from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('dashboard/', views.DashboardTemplateView.as_view(), name='dashboard'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    path('change-password/', views.MyPasswordChangeView.as_view(), name='change_password'),
    path('change-password-done/', views.MyPasswordChangeDoneView.as_view(), name='change_password_done'),
]