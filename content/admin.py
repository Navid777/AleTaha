from django.conf import settings
from django.contrib import admin, messages
from django.db.models.deletion import ProtectedError
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse

from content.models import Video, News, Image, VideoClip, ContentCategory, NewsGroup


class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    filter_horizontal = ('news_groups',)

    class Meta:
        model = Video


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    filter_horizontal = ('news_groups',)

    class Meta:
        model = News


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    filter_horizontal = ('news_groups',)

    class Meta:
        model = Image


class ClipAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    filter_horizontal = ('news_groups',)

    class Meta:
        model = VideoClip


class ContentCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

    class Meta:
        model = ContentCategory


class NewsGroupAdmin(admin.ModelAdmin):

    def delete_view(self, request, object_id, extra_context=None):
        try:
            return super().delete_view(request, object_id, extra_context)
        except ProtectedError as e:
            msg = e.args[0]
            self.message_user(request, msg, messages.ERROR)
            opts = self.model._meta
            obj_url = reverse(
                'admin:%s_%s_change' % (opts.app_label, opts.model_name),
                args=(object_id,),
                current_app=self.admin_site.name,
            )
            return HttpResponseRedirect(obj_url)

    def response_action(self, request, queryset):
        try:
            return super().response_action(request, queryset)
        except ProtectedError as e:
            msg = e.args[0]
            self.message_user(request, msg, messages.ERROR)
            opts = self.model._meta
            return_url = reverse(
                'admin:%s_%s_changelist' % (opts.app_label, opts.model_name),
                current_app=self.admin_site.name,
            )
            return HttpResponseRedirect(return_url)

    def has_delete_permission(self, request, obj=None):
        return super().has_delete_permission(request, obj) and (
            not obj or obj.title != settings.NEWS_GROUP_ALL_TITLE
        )

    def has_change_permission(self, request, obj=None):
        return super().has_change_permission(request, obj) and (
            not obj or obj.title != settings.NEWS_GROUP_ALL_TITLE
        )

    def get_queryset(self, request):
        return super(NewsGroupAdmin, self).get_queryset(request).exclude(title=settings.NEWS_GROUP_ALL_TITLE)

    class Meta:
        model = NewsGroup


admin.site.register(News, NewsAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Image, ImageAdmin)
# admin.site.register(VideoClip, ClipAdmin)
admin.site.register(ContentCategory, ContentCategoryAdmin)
admin.site.register(NewsGroup, NewsGroupAdmin)
