from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView

from store.models import ProductCategory, Product


class IndexView(ListView):
    template_name = 'store/index_page.html'
    model = ProductCategory


class CategoryView(ListView):
    template_name = 'store/category.html'
    model = ProductCategory




class CategoryNameView(ListView):
    template_name = 'store/shop_list.html'
    model = Product


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryNameView, self).get_context_data()
        context['category_name'] = ProductCategory.objects.get(id=self.kwargs['category_id'])

        return context

    def get_queryset(self):
        queryset = Product.objects.filter(category_id=self.kwargs['category_id'])
        return queryset


class ProductDetailView(DetailView):
    template_name = 'store/product.html'
    model = Product