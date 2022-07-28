from os import access
from pyexpat import model
from unicodedata import name
from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
   signup_as = models.CharField(max_length=10, choices= (('Instructor', 'Instructor'), ('Student', 'Student')))

   # def __str__(self):
   #    return self.username


class Feature(models.Model):
   name = models.CharField(max_length=100)
   details = models.CharField(max_length=1000)

class newFeatures(models.Model):
   name = models.CharField(max_length=100)
   details = models.CharField(max_length=500)

class Post(models.Model):
   title = models.CharField(max_length= 100)
   blog_related_to = models.CharField(max_length=200)
   blog_desc = models.CharField(max_length=100000)
   created_at = models.DateTimeField(default=datetime.now, blank=True)