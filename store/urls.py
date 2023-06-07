
from django.urls import path

from store.views import IndexView, CategoryView, CategoryNameView, ProductDetailView, basket_add, basket_remove, \
    AboutUsView, CollectionNameView

app_name = 'store'

urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
    path('about_us/', AboutUsView.as_view(), name='about_us'),
    path('categories/', CategoryView.as_view(), name='category_page'),
    path('categories/<int:category_id>/', CategoryNameView.as_view(), name='categories'),
    path('collections/<int:collection_id>/', CollectionNameView.as_view(), name='collections'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
