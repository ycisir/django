from django.urls import path
from enroll import views
# from . import views, converters


# register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    # path('students/', views.details, name='details'),
    # path('registration/', views.register, name='register'),
    # path('success/', views.done, name='success'),
    # path('student/<int:id>/', views.show_details, name='details'),
    path('login/', views.login_page, name='login'),
    # path('session/<yyyy:year>/', views.show_session, name='session'),
    path('signup/', views.signup_page, name='signup'),
    path('profile/', views.profile_page, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    # path('changepasswordwithold/', views.change_pass_with_old, name='changepasswordwithold'),
    path('changepassword/', views.change_pass, name='changepassword'),
    path('userdetails/<int:id>', views.user_details, name='userdetails'),
]