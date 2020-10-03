from django.contrib import admin
from .models import Post
# Register your models here.

class Postadmin(admin.ModelAdmin):
    list_display = ['title','timestamp', 'update', ]
    list_filter = ['timestamp', 'update']
    search_fields = ['content', 'title', 'timestamp', 'update']
    list_display_links = ['update']
    list_editable = ['title']
    class Meta:
        model = Post
admin.site.register(Post, Postadmin)