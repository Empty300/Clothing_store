
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from orders.views import OrderCreateView
from store.views import IndexView, CategoryView, CategoryNameView, ProductDetailView
from users.views import UserLoginView, UserRegistrationView, UserProfileView

app_name = 'orders'

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order_create'),


]

