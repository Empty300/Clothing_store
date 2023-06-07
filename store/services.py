from store.models import Basket, Product


def basket_delete(basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()


def add_to_basket(request, product_id):
    """Добавление товара в корзину"""
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product, size=request.POST['Size'])
    if 'Size' in request.POST and 'Quantity' in request.POST:
        if baskets.exists():
            _if_basket_exists(request, baskets)
        else:
            Basket.objects.create(user=request.user, product=product,
                                  quantity=request.POST['Quantity'], size=request.POST['Size'])
    elif 'Size' in request.POST:
        if baskets.exists():
            _if_basket_exists(request, baskets)
        else:
            Basket.objects.create(user=request.user, product=product,
                                  quantity=1, size=request.POST['Size'])


def _if_basket_exists(request, baskets):
    """Добавление quantity к товару который уже в корзине"""
    basket = baskets.first()
    basket.quantity += int(request.POST['Quantity'])
    basket.save()
