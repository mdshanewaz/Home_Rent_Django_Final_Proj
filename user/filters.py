from ast import Expression
from dataclasses import field
from pydoc import classname
from random import choices
from secrets import choice
from tkinter import Label, Widget
from django import forms
import django_filters 
from .models import *

choices1 = Location.objects.all().values_list('name','name')

choices2 = RentFor.objects.all().values_list('name','name')

class PostFilter(django_filters.FilterSet):
    location = django_filters.ChoiceFilter(
        choices=choices1,
        widget=forms.Select(attrs={'class': 'form-control'}))
    
    rent_for = django_filters.ChoiceFilter(
        choices=choices2,
        widget=forms.Select(attrs={'class': 'form-control'}))
    
    price = django_filters.AllValuesFilter(
        widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Post
        fields = ('location', 'rent_for', 'price')


        
        