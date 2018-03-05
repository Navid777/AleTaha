from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = (
        ('T', 'تعزیه'),
        ('O', 'عمومی')
    )
    title = models.CharField(max_length=2000, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(verbose_name='تصویر')
    price = models.PositiveIntegerField(verbose_name='قیمت (تومان)')
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, verbose_name='دسته')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'محصولات'
        verbose_name = 'محصول'
