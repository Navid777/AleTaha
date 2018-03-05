from django.db import models


class Video(models.Model):
    CATEGORY_CHOICES = (
        ('N', 'خبر'),
        ('R', 'روضه‌خوانی'),
        ('M', 'مرثیه')
    )
    video = models.FileField(upload_to='videos/', verbose_name='ویدیو')
    title = models.CharField(max_length=1000, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, verbose_name='دسته')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ویدیو'
        verbose_name_plural = 'ویدیوها'


class VideoClip(models.Model):
    CATEGORY_CHOICES = (
        ('O', 'عمومی'),
        ('T', 'تعزیه')
    )
    video = models.FileField(upload_to='videos/', verbose_name='ویدیو')
    title = models.CharField(max_length=1000, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, verbose_name='دسته')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'کلیپ'
        verbose_name_plural = 'کلیپ‌ها'


class Image(models.Model):
    CATEGORY_CHOICES = (
        ('G', 'قودجان'),
        ('H', 'همایش'),
        ('T', 'تعزیه'),
        ('M', 'مراسمات و برنامه‌ها')
    )
    image = models.FileField(upload_to='videos/', verbose_name='عکس')
    title = models.CharField(max_length=1000, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, verbose_name='دسته')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'عکس'
        verbose_name_plural = 'عکس‌ها'


class News(models.Model):
    CATEGORY_CHOICES = (
        ('G', 'قودجان'),
        ('M', 'مجمع تعزیه آل طه'),
        ('O', 'عمومی')
    )
    title = models.CharField(max_length=1000, verbose_name='عنوان')
    description = models.TextField(verbose_name='متن')
    image = models.ImageField(null=True, blank=True, verbose_name='عکس')
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, verbose_name='دسته')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'خبر'
        verbose_name_plural = 'اخبار'
