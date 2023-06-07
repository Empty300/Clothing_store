from django.contrib import admin

from store.models import ProductCategory, Product, Basket, Collections

admin.site.register(ProductCategory)

admin.site.register(Collections)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    fields = ('name',  'category',  'price', 'quantity_s', 'quantity_m', 'quantity_l', 'quantity_xl', 'image1',
              'image2', 'image3', 'image4', 'image5', 'description', 'collection', 'slug')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_timestamp', 'size', 'quantity')
    fields = ('user', 'product', 'created_timestamp', 'size', 'quantity')
    readonly_fields = ['created_timestamp']