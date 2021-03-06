from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError


class Class(models.Model):
    title = models.CharField(max_length=2000, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(null=True, blank=True, verbose_name='عکس')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'کلاس‌ها'
        verbose_name = 'کلاس'


def national_code_validator(national_code):
    i = len(national_code) - 2
    sum_value = 0
    position = 2
    try:
        int(national_code)
    except ValueError:
        raise ValidationError('کد ملی باید تماما عدد باشد.')
    while i >= 0:
        sum_value += int(national_code[i]) * position
        position += 1
        i -= 1
    res = sum_value % 11
    if res >= 2:
        res = 11 - res
    if res != int(national_code[-1]):
        raise ValidationError('کد ملی معتبر نیست.')


def address_validator(address):
    if len(address) < 10:
        raise ValidationError('آدرس باید حداقل 10 کاراکتر باشد.')


class Student(models.Model):
    user = models.OneToOneField(User, related_name='student', verbose_name='کاربر',
                                help_text='به عنوان یک کاربر اضافه کنید یا بسازید.')
    first_name = models.CharField(max_length=200, verbose_name='نام')
    last_name = models.CharField(max_length=200, verbose_name='نام خانوادگی')
    classes = models.ManyToManyField(Class, related_name='students', verbose_name='کلاس‌ها', blank=True)
    national_code = models.CharField(max_length=10, verbose_name='کد ملی', validators=[national_code_validator])
    address = models.TextField(verbose_name='آدرس', validators=[address_validator])
    phone = models.CharField(max_length=15, verbose_name='شماره تلفن')
    image = models.ImageField(verbose_name='عکس', null=True, blank=True)
    father_name = models.CharField(max_length=500, verbose_name='نام پدر')
    year_of_birth = models.PositiveIntegerField(verbose_name='سال تولد')

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'هنرجو'
        verbose_name_plural = 'هنرجویان'


class Teacher(models.Model):
    user = models.OneToOneField(User, related_name='teacher', verbose_name='کاربر',
                                help_text='به عنوان یک کاربر اضافه کنید یا بسازید.')
    first_name = models.CharField(max_length=200, verbose_name='نام')
    last_name = models.CharField(max_length=200, verbose_name='نام خانوادگی')
    classes = models.ManyToManyField(Class, related_name='teachers', verbose_name='کلاس‌ها', blank=True)
    national_code = models.CharField(max_length=10, verbose_name='کد ملی')
    address = models.TextField(verbose_name='آدرس', validators=[address_validator])
    phone = models.CharField(max_length=15, verbose_name='شماره تلفن')
    image = models.ImageField(verbose_name='عکس', null=True, blank=True)

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'استاد'
        verbose_name_plural = 'اساتید'


class Message(models.Model):
    sender = models.ForeignKey(Teacher, related_name='messages', verbose_name='فرستنده')
    receiver = models.ForeignKey(Class, related_name='messages', verbose_name='کلاس دریافت کننده')
    message = models.TextField(verbose_name='متن پیام')
    confirmed = models.BooleanField(default=False, verbose_name='تاییدشده')

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیامها'
