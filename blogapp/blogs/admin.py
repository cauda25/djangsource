from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "created_at"]
