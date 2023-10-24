from django.urls import path
from posts.views import blog_home, blog_post_create, blog_post_edit, blog_post_view, blog_post_delete

app_name = "posts"

urlpatterns = [
    path("", blog_home, name="home"),
    path("create/", blog_post_create, name="create"),
    path("<slug:slug>/", blog_post_view, name="view"),
    path("edit/<slug:slug>/", blog_post_edit, name="edit"),
    path("delete/<slug:slug>/", blog_post_delete, name="delete"),
]
