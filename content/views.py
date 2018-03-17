from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from content.models import News, Video, Image, VideoClip, ContentCategory, NewsGroup
from content.serializers import NewsSerializer, VideoSerializer, ImageSerializer, VideoClipSerializer, \
    ContentCategorySerializer


class NewsList(generics.ListAPIView):
    serializer_class = NewsSerializer
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'student'):
            return News.objects.filter(news_groups__students=user.student)
        elif hasattr(user, 'teacher'):
            return News.objects.filter(news_groups__teachers=user.teacher)
        return News.objects.filter(news_groups=NewsGroup.get_news_group_all())


class VideoList(generics.ListAPIView):
    serializer_class = VideoSerializer
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'student'):
            return Video.objects.filter(news_groups__students=user.student)
        elif hasattr(user, 'teacher'):
            return Video.objects.filter(news_groups__teachers=user.teacher)
        return Video.objects.filter(news_groups=NewsGroup.get_news_group_all())


class ImageList(generics.ListAPIView):
    serializer_class = ImageSerializer
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'student'):
            return Image.objects.filter(news_groups__students=user.student)
        elif hasattr(user, 'teacher'):
            return Image.objects.filter(news_groups__teachers=user.teacher)
        return Image.objects.filter(news_groups=NewsGroup.get_news_group_all())


class VideoClipList(generics.ListAPIView):
    serializer_class = VideoClipSerializer
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'student'):
            return VideoClip.objects.filter(news_groups__students=user.student)
        elif hasattr(user, 'teacher'):
            return VideoClip.objects.filter(news_groups__teachers=user.teacher)
        return VideoClip.objects.filter(news_groups=NewsGroup.get_news_group_all())


class ContentCategoryList(generics.ListAPIView):
    queryset = ContentCategory.objects.all()
    serializer_class = ContentCategorySerializer

    def get_queryset(self):
        kwargs = {}
        if self.request.GET.get('model', None) in {'news', 'videos', 'images', 'video_clips'}:
            kwargs = {self.request.GET['model']: None}
        return ContentCategory.objects.all().exclude(**kwargs)
