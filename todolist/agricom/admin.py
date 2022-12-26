from django.contrib import admin
from .models import Agricom

# Register your models here.

class BlogTaskAdmin(admin.ModelAdmin):
    list_display = ('phone_number','names','status','address')
    search_fields = ['phone_number', 'names','status']
    list_filter = ['phone_number', 'names','status']

admin.site.register( Agricom, BlogTaskAdmin)