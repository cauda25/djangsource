from django.urls import path
from . import views

app_name = "blogs"

urlpatterns = [
    path("", views.blogs_list, name="list"),
    path("<int:pk>/", views.blogs_detail, name="detail"),
    path("create/", views.blogs_create, name="create"),
    path("<int:pk>/update/", views.blogs_update, name="update"),
    path("<int:pk>/delete/", views.blogs_delete, name="delete"),
    path("comment/create/", views.comment_create, name="comment_create"),
    path("<int:pk>/post/like/", views.post_like, name="post_like"),
]
