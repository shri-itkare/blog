from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'author', 'created_at')
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'body')
    date_hierarchy = 'created_at'