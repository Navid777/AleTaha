from rest_framework import generics

from education.models import Class
from education.serializers import ClassSerializer, StudentSerializer, TeacherSerializer


class ClassList(generics.ListAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class CreateStudent(generics.CreateAPIView):
    serializer_class = StudentSerializer


class CreateTeacher(generics.CreateAPIView):
    serializer_class = TeacherSerializer
