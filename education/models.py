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
    first_name = models.CharField(max_length=200, verbose_name='نام')
    last_name = models.CharField(max_length=200, verbose_name='نام خانوادگی')
    classes = models.ManyToManyField(Class, related_name='students', verbose_name='کلاس‌ها')
    national_code = models.CharField(max_length=10, verbose_name='کد ملی')
    address = models.TextField(verbose_name='آدرس')
    phone = models.CharField(max_length=15, verbose_name='شماره تلفن')
    image = models.ImageField(verbose_name='عکس')
    father_name = models.CharField(max_length=500, verbose_name='نام پدر')
    year_of_birth = models.PositiveIntegerField(verbose_name='سال تولد')

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'هنرآموز'
        verbose_name_plural = 'هنرآموزان'


class Teacher(models.Model):
    user = models.ForeignKey(User, related_name='teachers', verbose_name='کاربر')
    first_name = models.CharField(max_length=200, verbose_name='نام')
    last_name = models.CharField(max_length=200, verbose_name='نام خانوادگی')
    classes = models.ManyToManyField(Class, related_name='teachers', verbose_name='کلاس‌ها')
    national_code = models.CharField(max_length=10, verbose_name='کد ملی')
    address = models.TextField(verbose_name='آدرس')
    phone = models.CharField(max_length=15, verbose_name='شماره تلفن')
    image = models.ImageField(verbose_name='عکس')

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'معلم'
        verbose_name_plural = 'معلمان'
