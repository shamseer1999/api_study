from django.contrib import admin
from .models import *
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','name','phone','place')
    list_display_links = ('id','name')
    search_fields = ('name',)
    list_per_page = 10
    
admin.site.register(Authors,AuthorAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display =('id','name','description','sub_title','author','published_date','created_at')
    list_display_links = ('id','name')
    search_fields = ('name','author')
    list_per_page = 10
    
admin.site.register(Blog,BlogAdmin)
