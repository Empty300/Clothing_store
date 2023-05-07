from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView

from store.models import ProductCategory, Product, Basket


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

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if 'Size' in request.POST and 'Quantity' in request.POST:
        if baskets.exists() and baskets.first().size == request.POST['Size']:
            basket = baskets.first()
            basket.quantity += int(request.POST['Quantity'])
            basket.save()
        else:
            Basket.objects.create(user=request.user, product=product,
                                  quantity=request.POST['Quantity'], size=request.POST['Size'])
    elif 'Quantity' in request.POST:
        if baskets.exists():
            basket = baskets.first()
            basket.quantity += int(request.POST['Quantity'])
            basket.save()
        else:
            Basket.objects.create(user=request.user, product=product,
                                  quantity=request.POST['Quantity'])
    else:
        Basket.objects.create(user=request.user, product=product,
                              quantity=1)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove_all(request, basket_id):
    test = Basket.objects.all().filter(user=request.user)
    test.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])