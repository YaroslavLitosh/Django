from django.contrib import admin
from .models import Post, Like


class LikeTabularInLine(admin.TabularInline):
    model = Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [LikeTabularInLine]
    class Meta:
        model = Post
