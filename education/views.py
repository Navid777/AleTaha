from rest_framework import generics

from education.models import Class
from education.serializers import ClassSerializer


class ClassList(generics.ListAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
