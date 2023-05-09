from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from orders.views import yookassa_webhook_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls', namespace='index')),
    path('users/', include('users.urls', namespace='users')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('webhook/yookassa', yookassa_webhook_view, name='stripe_yookassa'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

