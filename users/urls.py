
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from store.views import IndexView, CategoryView, CategoryNameView, ProductDetailView
from users.views import UserLoginView, UserRegistrationView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserRegistrationView.as_view(), name='registration'),
]
