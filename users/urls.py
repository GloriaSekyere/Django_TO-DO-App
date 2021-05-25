from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [

    # Login and Logout views
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    # User registration
    path('register/', views.register, name='register'),

    # User profile
    path('profile/<int:pk>/', views.profile, name='profile'),
]
