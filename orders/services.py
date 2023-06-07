import os
import uuid
import requests
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template import loader
from dotenv import load_dotenv
from yookassa import Payment, Configuration

from orders.models import Order
from store.models import Basket, Product

load_dotenv()

Configuration.account_id = os.getenv('YOOKASSA_ACCOUNT_ID')
Configuration.secret_key = os.getenv('YOOKASSA_SECRET_KEY')


def create_new_payment(self):
    """Создание нового платежа. Редирект на оплату"""
    payment = Payment.create({
        "amount": {
            "value": f"{self.object.basket_history['Общая сумма заказа']}",
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://932a-79-136-214-97.ngrok-free.app "
        },
        "capture": True,
        "description": f"Заказ №{self.object.id}"
    }, uuid.uuid4())
    return payment


def create_form_instance_basket_history(self):
    """Суммирует все корзины в один заказ"""
    baskets = Basket.objects.filter(user=self.request.user)
    result = {
        'Товар': [basket.de_json() for basket in baskets],
        'Общая сумма заказа': float(baskets.total_sum()),
    }
    return result


def payment_succeeded(answer):
    """Действия при успешно платеже. Обновление бд, отправка тг уведомлений"""
    order_id = answer['object']['description'].split('№')[1]
    order = Order.objects.get(id=order_id)
    order.update_after_payment()
    _payment_succeeded_email(order)
    requests.post(
        f'https://api.telegram.org/bot{os.getenv("BOT_TOKEN")}/sendMessage?chat_id={os.getenv("CHAT_ID1")}'
        f'&text=Оплачен новый заказ! Его id:{order_id}\nПодробнее: {os.getenv("DOMAIN_NAME")}/admin/orders/order/{order_id}/change/')
    # requests.post(
    #     f'https://api.telegram.org/bot{os.getenv("BOT_TOKEN")}/sendMessage?chat_id={os.getenv("CHAT_ID2")}'
    #     f'&text=Оплачен новый заказ! Его id:{order_id}\nПодробнее: {os.getenv("DOMAIN_NAME")}/admin/orders/order/{order_id}/change/')


def _payment_succeeded_email(order):
    subject = f'Заказ №{order.id} создан!'
    message = f'Заказ №{order.id} создан!'
    result = []
    for tovar in order.basket_history['Товар']:
        id = tovar['id товара'],
        result.append({
            'size': tovar['размер'],
            'count': tovar['Количество'],
            'product': Product.objects.get(id=id[0]),
            'price_with_count': int(int(tovar['Количество']) * Product.objects.get(id=id[0]).price)
        })
    html_message = loader.render_to_string(
        'orders/email_order_create.html',
        {
            'order': order,
            'full_price': order.basket_history['Общая сумма заказа'],
            'zakaz': result
        }
    )
    send_mail(
        subject=subject,
        html_message=html_message,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=(order.initiator.email,),
        fail_silently=False,
    )


def get_cdek_info(city_name):
    """Через апи сдэк получает информацию о доставке"""
    auth_text = {
        'grant_type': 'client_credentials',
        'client_id': os.getenv('CDEK_CLIENT_ID'),
        'client_secret': os.getenv('CDEK_CLIENT_SECRET'),
    }
    params_for_auth = requests.post('https://api.edu.cdek.ru/v2/oauth/token?parameters', params=auth_text)
    params_for_auth = params_for_auth.json()
    city_id = _get_city_id(city_name, params_for_auth)
    params = {
        "type": 1,
        "date": "2020-11-03T11:49:32+0700",
        "currency": 1,
        "lang": "rus",
        "from_location": {
            "code": 281
        },
        "to_location": {
            "code": city_id
        },
        "packages": [
            {
                "height": 17,
                "length": 12,
                "weight": 400,
                "width": 9
            }
        ]
    }

    response = requests.post('https://api.edu.cdek.ru/v2/calculator/tarifflist', json=params,
                             headers={
                                 'Authorization': f'{params_for_auth["token_type"]} {params_for_auth["access_token"]}'})
    response = response.json()
    try:
        response = response['tariff_codes'][0]
        print(response)
        delivery_info = {
            'price': response['delivery_sum'],
            'period_min': int(response['period_min']),
            'period_max': int(response['period_max']),
        }
        return delivery_info
    except:
        return None


def _get_city_id(city_name, params_for_auth):
    """По названию города определяет его id в СДЭК"""
    city_info = requests.get(f'https://api.cdek.ru/v2/location/cities/?city={city_name}',
                             headers={
                                 'Authorization': f'{params_for_auth["token_type"]} {params_for_auth["access_token"]}'})
    city_info = city_info.json()
    print(city_info)
    return city_info[0]['code']
