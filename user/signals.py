from unicodedata import name
from urllib import request
from django.contrib.auth.models import Group 
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import Customer, Admin
from django.dispatch import receiver


@receiver(post_save, sender=User)
def user_profile(sender, instance, created, **kwargs):
    if created and instance.is_staff == True:
        group = Group.objects.get(name='Admin')
        instance.groups.add(group)
        Admin.objects.create(
            user=instance,
            username=instance.username,
            first_name = instance.first_name,
            last_name = instance.last_name,
            email = instance.email
            ) 
        #print('Hello 1')
    
    elif created and instance.is_staff == False:
        group = Group.objects.get(name='Customer')
        instance.groups.add(group)
        Customer.objects.create(
            user=instance,
            username=instance.username,
            first_name = instance.first_name,
            last_name = instance.last_name,
            email = instance.email
            ) 
        #print('Hello 2')

post_save.connect(user_profile, sender=User)
       
