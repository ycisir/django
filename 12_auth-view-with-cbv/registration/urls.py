from django.urls import path
from . import views
# from django.contrib.auth.decorators import login_required
# from django.contrib.admin.views.decorators import staff_member_required

# decorating in url-conf
urlpatterns = [
    path('profile/', views.ProfileTemplateView.as_view(), name='profile'),


    # path('profile/', login_required(views.ProfileTemplateView.as_view()), name='profile'),
    # path('profile/', staff_member_required(views.ProfileTemplateView.as_view()), name='profile'),
]
