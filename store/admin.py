from django.contrib import admin

from store.models import ProductCategory, Product

admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    fields = ('name',  'category',  'price', 'quantity_s', 'quantity_m', 'quantity_l', 'quantity_xl', 'image1',
              'image2', 'image3', 'image4', 'image5', 'description', 'slug')
    prepopulated_fields = {"slug": ("name",)}
