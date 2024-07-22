from django.urls import path
from posts.views import *

app_name = "posts"

urlpatterns = [
    path("", blog_home, name="home"),
    path("create/", blog_post_create, name="create"),
    path("search/", blog_post_search_redirect, name="search_redirect"),
    path("<slug:slug>/", blog_post_view, name="view"),
    path("edit/<slug:slug>/", blog_post_edit, name="edit"),
    path("delete/<slug:slug>/", blog_post_delete, name="delete"),
    path("search/<str:search>/", blog_post_search, name="search"),
]
