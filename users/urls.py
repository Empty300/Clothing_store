from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import (PasswordResetView, UserLoginView, UserProfileView,
                         UserRegistrationView, password_reset)

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserRegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
    path('password_reset/', password_reset, name='password_reset'),
    path('password_reset/new_pass/<uidb64>/<token>/', PasswordResetView.as_view(), name='new_pass'),
]
