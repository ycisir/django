"""
URL configuration for class_based_view project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.Home.as_view(), name='home'),
    # path('f1', views.fun, {'template_name':'school/f1.html'} ,name='fi'),
    # path('f2', views.fun, {'template_name':'school/f2.html'} ,name='f2'),
    # path('child', views.HomeChild.as_view(name='harry'), name='child'),
    # path('news1', views.News.as_view(template_name='school/f1.html'), name='news1'),
    # path('news2', views.News.as_view(template_name='school/f2.html'), name='news2'),
    # path('news2', views.News.as_view(), name='news2'),


    # path('', views.TemplateView.as_view(template_name='school/home.html'), name='home'),
    # path('', views.HomeTemplateView.as_view(extra_context={'course':'Django'}), name='home'),
    # path('home/<str:cl>', views.HomeTemplateView.as_view(extra_context={'course':'Django'}), name='cl'),

    path('', views.TemplateView.as_view(template_name='school/home.html'), name='home'),
    path('home/', views.RedirectView.as_view(url='/'), name='home'),
    # path('github/', views.RedirectView.as_view(url='https://www.github.com'), name='github'),
    # path('github/', views.GithubRedirectView.as_view(), name='github'),
    path('index/', views.RedirectView.as_view(pattern_name='home'), name='index'),

    path('home/<int:id>', views.HomeRedirectView.as_view(), name='home'),
    path('roll/<int:id>', views.TemplateView.as_view(template_name='school/home.html'), name='id'),

    # path('home/<slug:post>', views.HomeRedirectView.as_view(), name='home'),
    # path('post/<slug:post>', views.TemplateView.as_view(template_name='school/home.html'), name='post'),
]
