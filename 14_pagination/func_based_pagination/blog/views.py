from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

def post_list(request):
    all_posts = Post.objects.all().order_by('id')
    paginator = Paginator(all_posts, per_page=3, orphans=1)
    page_number = request.GET.get('page')
    pages = paginator.get_page(page_number)
    print(f'all posts: {all_posts}')
    print()
    print(f'paginator: {paginator}')
    print()
    print(f'page number: {page_number}')
    print()
    print(f'pages: {pages}')
    return render(request, 'blog/home.html', {'pages':pages})