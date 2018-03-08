from rest_framework import generics
from content.models import News, Video, Image, VideoClip, ContentCategory
from content.serializers import NewsSerializer, VideoSerializer, ImageSerializer, VideoClipSerializer, \
    ContentCategorySerializer


class NewsList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class VideoList(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class ImageList(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class VideoClipList(generics.ListAPIView):
    queryset = VideoClip.objects.all()
    serializer_class = VideoClipSerializer


class ContentCategoryList(generics.ListAPIView):
    queryset = ContentCategory.objects.all()
    serializer_class = ContentCategorySerializer
