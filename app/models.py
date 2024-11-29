from django.db import models
from ckeditor.fields import RichTextField
from hitcount.models import HitCountMixin,HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django import forms

class Blog(models.Model):
    image = models.ImageField(upload_to='Images/blog')
    title = models.CharField(max_length=70)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    

class About(models.Model):
    image = models.ImageField(upload_to='Images/about')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.description[:50]  
    

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
   
    def __str__(self):
         return f"{self.first_name} {self.email}"
    
class Services(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
