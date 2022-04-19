from cProfile import label
from dataclasses import field, fields
import email
from logging import PlaceHolder
from msilib.schema import Class
from operator import mod
from pyexpat import model
from random import choices
from secrets import choice
from statistics import mode
from tkinter import Widget
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
from django import forms
from .models import *

choices1 = Location.objects.all().values_list('name','name')

choices2 = RentFor.objects.all().values_list('name','name')

choices3 = [('1','1'),('2','2'),('3','3'),('4','4'),('5','5')]

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']
        labels = {
            "nid" : "NID"
        }

        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control'}),
            'first_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.TextInput(attrs={'class': 'form-control'}),
            'nid' : forms.TextInput(attrs={'class': 'form-control'}),
            'phone' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['user', 'date_created']

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
            'bed_room' :  forms.NumberInput(attrs={'class': 'form-control'}),
            'wash_room' :  forms.NumberInput(attrs={'class': 'form-control'}),
            'belcony' : forms.NumberInput(attrs={'class': 'form-control'}),
            'drawing_room' : forms.NumberInput(attrs={'class': 'form-control'}),
            'dyning_room' : forms.NumberInput(attrs={'class': 'form-control'}),
            'price' : forms.NumberInput(attrs={'class': 'form-control '}),
            'address' : forms.TextInput(attrs={'class': 'form-control'}),
            'rent_for' :forms.Select(choices=choices2, attrs={'class': 'form-control'}),
            'location' : forms.Select(choices=choices1, attrs={'class': 'form-control'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['post', 'date_created', 'user']

        labels = {
            "feedback" : ""
        }

        widgets = {
            'feedback' : forms.Textarea(attrs={'PlaceHolder':'Write your feedback', 'class': 'form-control'}),
            'star' : forms.Select(choices=choices3, attrs={'class': 'form-control'})
        }

class PassChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type' : 'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type' : 'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type' : 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


''''
class PassResetForm(PasswordResetForm):
    email = forms.CharField(widget=forms.EmailField(attrs={'class': 'form-control', 'type' : 'email'}))

    class Meta:
        model = User
        fields = ('email') '''