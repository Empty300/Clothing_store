
from django.db import models

from main import settings


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='Название категории')
    description = models.TextField(null=True, blank=True, verbose_name='Описание (не обязательно)')
    image = models.ImageField(upload_to='category_images', verbose_name='Фото')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Категории товаров"


class Product(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Наименование'
    )
    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=8,
        decimal_places=2,
        default=0,
        null=True,

    )
    quantity_s = models.PositiveIntegerField(
        verbose_name='Количество на складе размер s',
        default=0
    )
    quantity_m = models.PositiveIntegerField(
        verbose_name='Количество на складе размер m',
        default=0
    )
    quantity_l = models.PositiveIntegerField(
        verbose_name='Количество на складе размер l',
        default=0
    )
    quantity_xl = models.PositiveIntegerField(
        verbose_name='Количество на складе размер xl',
        default=0
    )
    image1 = models.ImageField(upload_to='product_images', verbose_name='Фото 1', blank=True)
    image2 = models.ImageField(upload_to='product_images', verbose_name='Фото 2', blank=True)
    image3 = models.ImageField(upload_to='product_images', verbose_name='Фото 3', blank=True)
    image4 = models.ImageField(upload_to='product_images', verbose_name='Фото 4', blank=True)
    image5 = models.ImageField(upload_to='product_images', verbose_name='Фото 5', blank=True)

    category = models.ForeignKey(
        to=ProductCategory,
        on_delete=models.CASCADE,
        verbose_name="Категория",
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="URL"
    )
    description = models.TextField(
        verbose_name='Полное описание',
        blank=True,
        null=True,
    )


    class Meta:
        verbose_name_plural = "Товары"

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'