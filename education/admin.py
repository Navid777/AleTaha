from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError

from education.models import Class, Teacher, Student


class ClassAdmin(admin.ModelAdmin):
    class Meta:
        model = Class


class TeacherAdmin(admin.ModelAdmin):

    class Meta:
        model = Teacher


class StudentAdmin(admin.ModelAdmin):

    class Meta:
        model = Student


admin.site.register(Class, ClassAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
