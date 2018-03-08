from rest_framework import serializers

from education.models import Class


class ClassSerializer(serializers.ModelSerializer):
    teachers = serializers.StringRelatedField()

    class Meta:
        model = Class
        fields = ('title', 'image', 'teachers')
        read_only_fields = ('title', 'image', 'teachers')
