from django.contrib import admin
from django.shortcuts import render
from .models import Contact,Services,Blog,About
from django.utils.html import format_html

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name',"full_name","email")
    readonly_fields = ['id']

    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))
  

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('img','description')
    readonly_fields = ['id']
     
    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))
    
@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title','description')
    readonly_fields = ['id']
     



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('img','title','description')
    readonly_fields = ['id']
     
    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))