from django.db import models


class ContentCategory(models.Model):
    title = models.CharField(max_length=1000, verbose_name='عنوان')
    description = models.TextField(null=True, blank=True, verbose_name='توضیحات')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته‌ی محتوا'
        verbose_name_plural = 'دسته‌های محتوا'


class Video(models.Model):
    video = models.FileField(upload_to='videos/', verbose_name='ویدیو')
    title = models.CharField(max_length=1000, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    category = models.ForeignKey(ContentCategory, related_name='videos', verbose_name='دسته')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ویدیو'
        verbose_name_plural = 'ویدیوها'


class VideoClip(models.Model):
    video = models.FileField(upload_to='videos/', verbose_name='ویدیو')
    title = models.CharField(max_length=1000, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    category = models.ForeignKey(ContentCategory, related_name='video_clips', verbose_name='دسته')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'کلیپ'
        verbose_name_plural = 'کلیپ‌ها'


class Image(models.Model):
    image = models.FileField(upload_to='videos/', verbose_name='عکس')
    title = models.CharField(max_length=1000, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    category = models.ForeignKey(ContentCategory, related_name='images', verbose_name='دسته')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'عکس'
        verbose_name_plural = 'عکس‌ها'


class News(models.Model):
    title = models.CharField(max_length=1000, verbose_name='عنوان')
    description = models.TextField(verbose_name='متن')
    image = models.ImageField(null=True, blank=True, verbose_name='عکس')
    category = models.ForeignKey(ContentCategory, related_name='news', verbose_name='دسته')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'خبر'
        verbose_name_plural = 'اخبار'
