import json

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView

from common.views import CommonMixin
from orders.cities import cities
from orders.forms import OrderForm
from orders.services import (create_form_instance_basket_history,
                             create_new_payment, get_cdek_info,
                             payment_succeeded)


class OrderCreateView(CommonMixin, CreateView):
    template_name = 'orders/checkout.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_create')
    title = 'Giant - Создать заказ'

    def get(self, request, *args, **kwargs):
        form = OrderForm
        if request.GET.get('city'):
            delivery_info = get_cdek_info(request.GET.get('city'))
        else:
            delivery_info = get_cdek_info('Москва')
        if delivery_info:
            return render(request, 'orders/checkout.html', {
                'main_city': request.GET.get('city') if request.GET.get('city') else 'Москва',
                'form': form,
                'cities': cities,
                'delivery_info': delivery_info
            })
        else:
            return render(request, 'orders/checkout.html', {'form': form,
                                                            'cities': cities})

    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        if form.is_valid():
            super(OrderCreateView, self).post(request, *args, **kwargs)
            return redirect(create_new_payment(self).confirmation.confirmation_url)
        else:
            if form.errors['telephone'][0]:
                form.errors['telephone'][0] = 'Введите корректный номер телефона в формате +79248347257'
            return render(request, 'orders/checkout.html', {'form': form})

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        form.instance.email = self.request.user.email
        form.instance.basket_history = create_form_instance_basket_history(self)
        return super(OrderCreateView, self).form_valid(form)


@csrf_exempt
def yookassa_webhook_view(request):
    answer = json.loads(request.body)
    if answer['object']['status'] == 'succeeded':
        payment_succeeded(answer)
    return HttpResponse(status=200)
