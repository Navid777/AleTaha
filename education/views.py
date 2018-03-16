from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from education.models import Class
from education.serializers import ClassSerializer, StudentSerializer, TeacherSerializer


class ClassList(generics.ListAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class CreateStudent(generics.CreateAPIView):
    serializer_class = StudentSerializer


class CreateTeacher(generics.CreateAPIView):
    serializer_class = TeacherSerializer


class UserClassList(generics.ListAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if hasattr(self.request.user, 'student'):
            return Class.objects.filter(students=self.request.user.student)
        if hasattr(self.request.user, 'teacher'):
            return Class.objects.filter(teachers=self.request.user.teacher)
        return None
