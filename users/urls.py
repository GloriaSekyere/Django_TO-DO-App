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

    # User profile page
    path('profile/<int:pk>/', views.profile, name='profile'),
    # Edit profile page
    path('profile/edit_profile/', views.edit_profile, name='edit_profile'),

    # Password reset
    path('password_reset/', views.PasswordReset.as_view(), name='password_reset'),
    
    path('password_reset_done/', 
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), 
        name='password_reset_done'),
    
    path('password_reset_confirm/<uidb64>/<token>/', 
        views.PasswordResetConfirm.as_view(), 
        name='password_reset_confirm'),   
    
    path('password_reset_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), 
        name='password_reset_complete'),    
]
