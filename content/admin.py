from django.contrib import admin

from content.models import Video, News, Image, VideoClip


class VideoAdmin(admin.ModelAdmin):

    class Meta:
        model = Video


class NewsAdmin(admin.ModelAdmin):

    class Meta:
        model = News


class ImageAdmin(admin.ModelAdmin):

    class Meta:
        model = Image


class ClipAdmin(admin.ModelAdmin):

    class Meta:
        model = VideoClip


admin.site.register(News, NewsAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(VideoClip, ClipAdmin)
