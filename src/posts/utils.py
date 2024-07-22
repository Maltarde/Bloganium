from django.core.paginator import Paginator

from posts.models import BlogPost


def _get_posts(request, search=""):
    if search:
        if request.user.is_authenticated:
            posts = BlogPost.objects.filter(title__icontains=search).order_by("-last_updated")
        else:
            posts = BlogPost.objects.filter(title__icontains=search, published=True).order_by("-last_updated")
    else:
        if request.user.is_authenticated:
            posts = BlogPost.objects.all().order_by("-last_updated")
        else:
            posts = BlogPost.objects.filter(published=True).order_by("-last_updated")
    
    return posts


def get_paginated_posts(request, search=""):
    posts = _get_posts(request, search=search)
    paginator = Paginator(posts, 8)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)
