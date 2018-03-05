from django.contrib.auth.models import User
from django.db import models


class Class(models.Model):
    title = models.CharField(max_length=2000, verbose_name='عنوان')
    image = models.ImageField(null=True, blank=True, verbose_name='عکس')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'کلاس‌ها'
        verbose_name = 'کلاس'


class Student(models.Model):
    user = models.ForeignKey(User, related_name='students', verbose_name='کاربر')
    classes = models.ManyToManyField(Class, related_name='students', verbose_name='کلاس‌ها')
    national_code = models.CharField(max_length=10, verbose_name='کد ملی')
    address = models.TextField(verbose_name='آدرس')
    phone = models.CharField(max_length=15, verbose_name='شماره تلفن')
    image = models.ImageField(verbose_name='عکس')

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'هنرآموز'
        verbose_name_plural = 'هنرآموزان'


class Teacher(models.Model):
    user = models.ForeignKey(User, related_name='teachers', verbose_name='کاربر')
    classes = models.ManyToManyField(Class, related_name='teachers', verbose_name='کلاس‌ها')
    national_code = models.CharField(max_length=10, verbose_name='کد ملی')
    address = models.TextField(verbose_name='آدرس')
    phone = models.CharField(max_length=15, verbose_name='شماره تلفن')
    image = models.ImageField(verbose_name='عکس')

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'معلم'
        verbose_name_plural = 'معلمان'
