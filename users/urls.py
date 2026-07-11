from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import userLoginView , ProfileView , UserUpdateView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', userLoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', ProfileView.as_view(template_name='users/profile.html'), name='profile'),
    path('profile/edit/', UserUpdateView.as_view(template_name='users/edit_profile.html'), name='edit-profile'),
]