from dataclasses import field, fields
from multiprocessing import context
from pkgutil import ImpImporter
from pyexpat import model
from re import template
from statistics import mode
from tokenize import group
from turtle import home
from unicodedata import name
from urllib import request
from webbrowser import Grail
from django import dispatch
from django.forms import ModelChoiceField
from django.shortcuts import get_object_or_404, render, redirect
from .decorators import allowed_users, unauthenticated_user
from django.contrib import messages
from django.contrib.auth.models import User, auth, Group
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from .forms import CustomerForm, PostForm, CommentForm, PassChangeForm
from django.contrib.auth.decorators import login_required
from .models import Customer, Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .filters import PostFilter
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    extra_context= {
        'sitename' : 'CHILEKOTHA',
        'navbar' : 'Home',
        }
    ordering = ['-date_created']
    paginate_by = 4

def about(request):
    context = {}
    context = {
        'navbar' : 'About',
    }
    return render(request, 'about.html', context)

class FindView(ListView,):
    model = Post
    template_name = 'find.html'
    extra_context= {
        'sitename' : 'CHILEKOTHA | Find',
        'navbar' : 'Find',
        }
    ordering = ['-date_created']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'    

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'postcreate.html'

    def form_valid(self, form):
        # Catch an instance of the object
        post_obj = form.save(commit=False)
        post_obj.user = self.request.user
        post_obj.save()
        self.success_url = post_obj.get_absolute_url()
        return super(PostCreateView, self).form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'postupdate.html'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'postdelete.html'
    success_url = reverse_lazy('Profile')    

class PostReview(DetailView, CreateView):
    model = Post
    form_class = CommentForm
    template_name = 'postreview.html'

    def form_valid(self, form):
        # Catch an instance of the object
        post_obj = form.save(commit=False)
        post_obj.user = self.request.user
        post_obj.post_id = self.kwargs['pk']
        post_obj.save()
        self.success_url = post_obj.get_absolute_url()
        return super(PostReview, self).form_valid(form)

@unauthenticated_user
def signup(request):
    context = {}
    context = {'sitename': 'CHILEKOTHA | SIGNUP'}
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username is taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'This email is taken')
                return redirect('signup')
            else: 
                user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                user.save();
                print("User is created")
                return redirect('login')
        
        else:
            messages.info(request, 'Password did not matched')
            return redirect('signup')
        return redirect('/')

    else:
        return render(request, 'signup.html', context)

'''
@login_required(login_url='login')
@allowed_users(allowed_roles=['Customer'])
def PasswordReset(request):
           
    return render(request, 'password_reset.html', context)
'''

@unauthenticated_user
def login(request):
    context = {}
    context ['sitename'] = "CHILEKOTHA | LOGIN"
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if request.user.is_staff:
                return redirect('admin_dash')
            else:
                return redirect('Profile')
        else:
            messages.info(request, 'Invaid Username or Password')
            return redirect('login')
    else:
        return render(request,'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('/')

class Profile(ListView):
    model = Post
    template_name = 'profile.html'
    extra_context= {
        'sitename' : 'CHILEKOTHA | Profile',
        'navbar': 'Profile'
    }
    ordering = ['-date_created']

@login_required(login_url='login')
@allowed_users(allowed_roles=['Customer'])
def setting(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('Profile')

    context = {}
    context = { 'sitename': 'CHILEKOTHA | SETTING',
                'form': form
                }
    return render(request, 'setting.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Customer'])
def contact(request):
    context = {}
    context = {
        'sitename' : 'CHILEKOTHA | CONTACT',
        'navbar' : 'Contact'
    }
    return render(request, 'contact.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_dash(request):
    user = User.objects.all()
    context = {}
    context = {
        'sitename': 'ADMIN DASHBOARD',
        'navbar': 'admin_dash',
        'user': user,
        }
    return render(request, 'admin_dash.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def admin_user_profile(request, pk):
    # user = User.objects.filter(id=pk)
    # for u in user:
    # print(u)
    context={}
    context["user"] = User.objects.get(pk=pk)
    post = Post.objects.all()
    context['post'] = post

    return render(request, 'admin_visit_profile.html',context)
    
class ProfileDeleteView(DeleteView):
    model = User
    template_name = 'user_delete.html'
    success_url = reverse_lazy('admin_dash') 

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def add_admin(request):
    context = {}
    context = {'sitename': 'Add New Admin'}
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username is taken')
                return redirect('add_admin')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'This email is taken')
                return redirect('add_admin')
            else: 
                user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name, is_staff = True)
                user.save();
                print("User is created")
                return redirect('admin_dash')
        
        else:
            messages.info(request, 'Password did not matched')
            return redirect('add_admin')
        return redirect('/')

    else:
        return render(request, 'add_user.html', context)

class PostApproveView(ListView):
    model = Post
    template_name = 'post_approve.html'

@login_required(login_url='login')
@allowed_users(allowed_roles=['Customer'])
def PostUserProfile(request, pk):
    context={}
    context["user"] = User.objects.get(pk=pk)
    post = Post.objects.all()
    context['post'] = post

    return render(request, 'post_user_profile.html',context)

class ProfileDeleteView(DeleteView):
    model = User
    template_name = 'user_delete.html'
    success_url = reverse_lazy('admin_dash')

class PassChangeView(PasswordChangeView): 
    template_name = 'password_change.html'
    form_class = PassChangeForm
    success_url = reverse_lazy('Profile')
'''
class PassResetView(PassChangeView): 
    template_name = 'password_reset.html'
    form_class = PassResetForm
    success_url = reverse_lazy('password_reset_done')'''