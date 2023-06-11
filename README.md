#  test_store
 Реальный проект интернет магазина одежды который написан на Python с использованием веб-фреймворка Django.
## Обзор
Приложение для интернет-магазина предлагает основные функции для покупателей, такие как просмотр товаров, добавление товаров в корзину и оформление заказов. Подключена платежная система. Расчет стоймости и сроков доставки. Кроме того, в приложении есть возможности для управления товарами и обработки заказов.

### Функционал покупателя: 
- Просмотр товаров по категориям.
- Просмотр подробной информации о товаре.
- Добавление товаров в корзину, выбор размера и количества.
- Оформление заказа с указанием деталей доставки.
- Оплата осуществляется через сервис Юкасса.
- Просмотр и история заказов для авторизованных пользователей.

### Функционал администратора:
Для входа в админ-панель необходимо дописать в адресной строке /admin, после Вы попадете на страницу авторизации где нужно ввести данные в формате email:password.
- Оповещение в тг о новых заказах
- На главной вы можете посмотреть: сумму проданных товаров, кол-во проданных товаров, кол-во товаров в наличии.
- На главной странце так же можно узнать подробные данные о покупателях: номер заказа, почта покупателя, способ оплаты, дата покупки, сумма и данные которые были высланы по почте.
- Возможность добавлять, удалять или редактировать товары на странице "Товары", так же можно посмотреть и информацию о товаре.


## Установка и настройка скрипта:

### Запуск скрипта на локальном компьютере:
- Склонируйте этот репозиторий на локальный компьютер
- Установите необходимые зависимости `pip install -r requirements.txt`
- Далее необходимо настроить переменные среды. Создайте файл `.env` в корне вашего интернет-магазина и запишите туда значения для переменных:


### Описание переменных:
| Переменная      | Описание                                                   |
| --------------- |------------------------------------------------------------|
| DATABASES_USER    | Имя пользователя БД PostgreSQL                             |
| DATABASES_PASSWORD   | Пароль пользователя БД PostgreSQL                          |
| DATABASES_HOST     | По умолчанию localhost                                     |
| DATABASES_PORT  | По умолчанию 5432                                          |
| DATABASES_NAME | Имя БД PostgreSQL                                          |
| EMAIL_HOST_USER | Логин от почты для отправки данных покупателю              |
| EMAIL_HOST_PASSWORD | Пароль от почты                                            |
| SECRET_KEY | Django ключ                                                |
| YOOKASSA_ACCOUNT_ID    | Аккаунт id Юкасса для работоспособности системы оплаты           |
| YOOKASSA_SECRET_KEY   | Секретный ключ Юкасса для работоспособности системы оплаты |
| CDEK_CLIENT_ID| Аккаунт id CDEK для расчета стоймости доставки                                           |
| CDEK_CLIENT_SECRET| Секретный ключ CDEK для расчета стоймости доставки                                           |
| DOMAIN_NAME  | По умолчанию http://127.0.0.1:8000                                              |

`.env` файл:
```bash
DATABASES_USER=postgres
DATABASES_PASSWORD=
DATABASES_HOST=
DATABASES_PORT=
DATABASES_NAME=

EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=

YOOKASSA_ACCOUNT_ID=
YOOKASSA_SECRET_KEY= 

CDEK_CLIENT_ID=
CDEK_CLIENT_SECRET

SECRET_KEY=
DOMAIN_NAME=
```
- Установите БД PostgreSQL на ваш компьютер.
- После этого, введите `python manage.py runserver` и перейдите по адресу `127.0.0.1:8000`, вы увидите уже рабочий интернет-магазин который запущен у вас на локальном компьютере.


