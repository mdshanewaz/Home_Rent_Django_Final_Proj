from django.contrib import admin
from .models import Customer, Admin, Post, Comment, Location, RentFor

# Register your models here.

admin.site.register(Customer)
admin.site.register(Admin)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Location)
admin.site.register(RentFor)

