from rest_framework import serializers

from content.models import News, ContentCategory, Video, VideoClip, Image


class ContentCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ContentCategory
        fields = ('id', 'title', 'description')
        read_only_fields = ('id', 'title', 'description')


class NewsSerializer(serializers.ModelSerializer):
    category = ContentCategorySerializer()

    class Meta:
        model = News
        fields = ('id', 'title', 'description', 'category')
        read_only_fields = ('id', 'title', 'description', 'category')


class VideoSerializer(serializers.ModelSerializer):
    category = ContentCategorySerializer()

    class Meta:
        model = Video
        fields = ('id', 'title', 'description', 'category', 'video')
        read_only_fields = ('id', 'title', 'description', 'category', 'video')


class VideoClipSerializer(serializers.ModelSerializer):
    category = ContentCategorySerializer()

    class Meta:
        model = VideoClip
        fields = ('id', 'title', 'description', 'category', 'video')
        read_only_fields = ('id', 'title', 'description', 'category', 'video')


class ImageSerializer(serializers.ModelSerializer):
    category = ContentCategorySerializer()

    class Meta:
        model = Image
        fields = ('id', 'title', 'description', 'category', 'image')
        read_only_fields = ('id', 'title', 'description', 'category', 'image')
