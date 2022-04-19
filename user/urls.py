from re import template
from unicodedata import name
from django.urls import path
from .views import HomeView, Profile, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostReview, ProfileDeleteView, PostApproveView, FindView, PassChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns = [
    path("", HomeView.as_view(), name="HomeView"),
    path("about", views.about, name="about"),
    path("find", (FindView.as_view()), name="FindView"),

    path("detail/<int:pk>", login_required(login_url='login')(PostDetailView.as_view()), name="PostDetail"),
    path("detail/<int:pk>/edit", login_required(login_url='login')(PostUpdateView.as_view()), name="PostUpdate"),
    path("detail/<int:pk>/delete", login_required(login_url='login')(PostDeleteView.as_view()), name="PostDelete"),
    path("create_post", login_required(login_url='login')(PostCreateView.as_view()), name="PostCreate"),
    path("detail/<int:pk>/review", login_required(login_url='login')(PostReview.as_view()), name="PostReview"),

    path("posts", login_required(login_url='login')(PostApproveView.as_view()), name="PostApprove"),

    path("user_profie/<int:pk>", views.PostUserProfile, name="PostUserProfile"),

    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login" ),
    path("logout", views.logout, name="logout"),

    path("profile", login_required(login_url='login')(Profile.as_view()), name="Profile"),
    path("setting", views.setting, name="setting"),

    path("contact", views.contact, name="contact"),
    path("admin_dash", views.admin_dash, name="admin_dash"),
    path("add_admin", views.add_admin, name="add_admin"),

    path("change_password", PassChangeView.as_view(), name="change_password"),
    #path("change_password", auth_views.PasswordChangeView.as_view(template_name="password_change.html"), name = "change_password"),
    #path("reset_password_email", PassResetView.as_view(), name = "reset_password"),
    path("reset_password_email", auth_views.PasswordResetView.as_view(), name = "reset_password"),
    path("reset_password_sent", auth_views.PasswordResetDoneView.as_view(), name = "password_reset_done"),
    path("reset_password_/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name = "password_reset_confirm"),
    path("reset_password_complete", auth_views.PasswordResetCompleteView.as_view(), name = "password_reset_complete"),

    path("u_profile/<int:pk>/", views.admin_user_profile, name="AdminToUserProfile"),

    path("u_profile/<int:pk>/delete_user", login_required(login_url='login')(ProfileDeleteView.as_view()), name="ProfileDelete"),
]