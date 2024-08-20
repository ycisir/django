from django.shortcuts import render
from .models import User, Page, Post, Song

def home(request):
    return render(request, 'myapp/home.html')

def user_data(request):
    d1 = User.objects.all()
    d2 = User.objects.filter(mypage__page_category='Ship')# page model ki field
    d3 = User.objects.filter(song__song_duration=3)# song model ki field
    d4 = User.objects.filter(mypost__post_publish_date='2024-06-20')# post model ki field
    d5 = User.objects.filter(email='hgranger@hogwarts.edu')# post model ki field
    return render(request, 'myapp/user.html', {'d1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})

def page_data(request):
    d1 = Page.objects.all()
    d2 = Page.objects.filter(page_category='Magic')
    d3 = Page.objects.filter(user__email='hpotter@hogwarts.edu')
    return render(request, 'myapp/page.html', {'d1':d1, 'd2':d2, 'd3':d3})

def post_data(request):
    d1 = Post.objects.all()
    d2 = Post.objects.filter(post_publish_date='2024-06-20')
    d3 = Post.objects.filter(user__username='jack')
    return render(request, 'myapp/post.html', {'d1':d1, 'd2':d2, 'd3':d3})

def song_data(request):
    d1 = Song.objects.all()
    d2 = Song.objects.filter(song_duration=3)
    d3 = Song.objects.filter(user__username='harry')
    return render(request, 'myapp/song.html', {'d1':d1, 'd2':d2, 'd3':d3})