from django.contrib import admin

from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'initiator', 'status', 'created')
    fields = (
        'id', 'created',
        ('fio', 'email',),
        ('city', 'address', 'telephone'),
        ('order_notes',),
        'basket_history', 'status', 'initiator',
    )
    readonly_fields = ('id', 'created', 'initiator')
