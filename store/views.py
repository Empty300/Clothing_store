from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView

from common.views import CommonMixin
from store.models import Collections, Product, ProductCategory
from store.services import add_to_basket, basket_delete


class IndexView(CommonMixin, ListView):
    template_name = 'store/index_page.html'
    model = ProductCategory
    title = 'Giant - Главная'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['collections'] = Collections.objects.all()
        return context


class CategoryView(CommonMixin, ListView):
    template_name = 'store/category.html'
    model = ProductCategory
    title = 'Giant - Категории'


class CategoryNameView(ListView):
    template_name = 'store/shop_list.html'
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryNameView, self).get_context_data()
        category_name = ProductCategory.objects.get(id=self.kwargs['category_id'])
        context['category_name'] = category_name
        context['title'] = f'Giant - {category_name}'

        return context

    def get_queryset(self):
        queryset = Product.objects.filter(category_id=self.kwargs['category_id'])
        return queryset


class ProductDetailView(DetailView):
    template_name = 'store/product.html'
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDetailView, self).get_context_data()
        context['title'] = f"Giant - {Product.objects.get(slug=self.kwargs['slug']).name}"
        context['also_like'] = Product.objects.all().exclude(slug=self.kwargs['slug']).order_by('?')

        return context


@login_required
def basket_add(request, product_id):
    add_to_basket(request, product_id)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class AboutUsView(CommonMixin, ListView):
    template_name = 'store/about_us.html'
    model = ProductCategory
    title = 'Giant - О нас'


class CollectionNameView(ListView):
    template_name = 'store/collection_list.html'
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CollectionNameView, self).get_context_data()
        collection_name = Collections.objects.get(id=self.kwargs['collection_id'])
        context['collection_name'] = collection_name
        context['title'] = f'Giant - {collection_name}'

        return context

    def get_queryset(self):
        queryset = Product.objects.filter(collection_id=self.kwargs['collection_id'])
        return queryset


@login_required
def basket_remove(request, basket_id):
    basket_delete(basket_id)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
