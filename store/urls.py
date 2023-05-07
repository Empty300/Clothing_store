
from django.contrib import admin
from django.urls import path, include

from store.views import IndexView, CategoryView, CategoryNameView, ProductDetailView, basket_add, basket_remove

app_name = 'store'

urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
    path('categories/', CategoryView.as_view(), name='category_page'),
    path('<int:category_id>/', CategoryNameView.as_view(), name='categories'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
