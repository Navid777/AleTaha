from django.db import models


class ProductCategory(models.Model):
    title = models.CharField(max_length=1000, verbose_name='عنوان')
    description = models.TextField(null=True, blank=True, verbose_name='توضیحات')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته‌ی محصول'
        verbose_name_plural = 'دسته‌های محصول'


class Product(models.Model):
    title = models.CharField(max_length=2000, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(verbose_name='تصویر')
    price = models.PositiveIntegerField(verbose_name='قیمت (تومان)')
    category = models.ForeignKey(ProductCategory, related_name='products', verbose_name='دسته')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'محصولات'
        verbose_name = 'محصول'
