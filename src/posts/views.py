from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import NoReverseMatch

from posts.forms import BlogPostForm, SearchForm
from posts.models import BlogPost
from posts.utils import get_paginated_posts


def blog_home(request):
    context = {
        "search": SearchForm(),
        "page_obj": get_paginated_posts(request)
    }
    return render(request, "posts/home_posts.html", context=context)


def blog_post_search(request, search):
    context = {
        "search": SearchForm(),
        "page_obj": get_paginated_posts(request, search)
    }
    return render(request, "posts/home_posts.html", context=context)


def blog_post_search_redirect(request):
    if "search" in request.POST:
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data["search"]
            try:
                return redirect("posts:search", search=data)
            except NoReverseMatch:
                pass
    
    return redirect("posts:home")


def blog_post_view(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    context = {"post": post}
    return render(request, "posts/view_posts.html", context=context)


@login_required(login_url="admin:index")
def blog_post_create(request):
    context: dict = {}
    if request.method == "POST":
        form: BlogPostForm = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:home")
    else:
        context["form"] = BlogPostForm()

    return render(request, "posts/create_posts.html", context=context)


@login_required(login_url="admin:index")
def blog_post_edit(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    context: dict = {}
    context["post_title"] = post.title
    if request.method == "POST":
        form: BlogPostForm = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("posts:home")
    else:
        context["form"] = BlogPostForm(instance=post)

    return render(request, "posts/edit_posts.html", context=context)


@login_required(login_url="admin:index")
def blog_post_delete(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    context = {"post": post}

    if request.method == "POST":
        post.delete()
        return redirect("posts:home")

    return render(request, "posts/delete_posts.html", context=context)
