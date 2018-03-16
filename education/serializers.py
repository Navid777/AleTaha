from django.contrib.auth.models import User
from rest_framework import serializers

from education.models import Class, Teacher, Student


def unique_username(username):
    try:
        User.objects.get(username=username)
        raise serializers.ValidationError('کاربری با این نام کاربری وجود دارد')
    except User.DoesNotExist:
        pass


class TeacherSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(write_only=True, validators=[User.username_validator, unique_username])

    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name', 'national_code', 'address', 'phone', 'username', 'password')

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        user = User.objects.create_user(username=username, password=password)
        student = Teacher.objects.create(**validated_data, user=user)
        return student


class ClassSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True)

    class Meta:
        model = Class
        fields = ('id', 'title', 'image', 'teachers', 'description')
        read_only_fields = ('title', 'image', 'teachers')


class StudentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(write_only=True, validators=[User.username_validator, unique_username])

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'national_code', 'classes', 'address', 'phone', 'father_name',
                  'year_of_birth', 'password', 'username')
        read_only_fields = ('classes',)

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        user = User.objects.create_user(username=username, password=password)
        student = Student.objects.create(**validated_data, user=user)
        return student
