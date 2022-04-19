from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from turtle import title
from urllib import request
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=20, null=True, blank=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=20, null=True, blank=True)
    nid = models.CharField(max_length=20, null=True, blank=True)
    img = models.ImageField(default="default.png", null=True, blank=True,)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username

class Post(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=500)
    bed_room = models.PositiveIntegerField(null=True, blank=True)
    wash_room = models.PositiveIntegerField(null=True, blank=True)
    belcony = models.PositiveIntegerField(null=True, blank=True)
    drawing_room =models.PositiveIntegerField(null=True, blank=True)
    dyning_room =models.PositiveIntegerField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    rent_for = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=20, blank=True, null=True,)
    photo = models.ImageField(null=True, blank=True)    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('PostDetail', args=[str(self.id)])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", blank=True, null=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    feedback = models.TextField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    star = models.IntegerField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('PostDetail', kwargs={'pk':self.post.pk})

class Admin(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=20, null=True, blank=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    img = models.ImageField(default="default.png", null=True, blank=True,)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username

class Location(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name

class RentFor(models.Model):
    name = models.CharField(max_length=10, null= True, blank= True)

    def __str__(self):
        return self.name