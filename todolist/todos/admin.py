from django.contrib import admin
from .models import BlogTask

# Register your models here.

class BlogTaskAdmin(admin.ModelAdmin):
    list_display = ('title','description','completed')
    search_fields = ['title', 'user']
    list_filter = ['title', 'user']

admin.site.register( BlogTask, BlogTaskAdmin)
