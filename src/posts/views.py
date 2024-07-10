from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from posts.forms import BlogPostForm
from posts.models import BlogPost


def blog_home(request):
    if request.user.is_authenticated:
        posts = BlogPost.objects.all().order_by("-last_updated")
    else:
        posts = BlogPost.objects.filter(published=True).order_by("-last_updated")

    paginator = Paginator(posts, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "posts/home_posts.html", context={"page_obj": page_obj})


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
