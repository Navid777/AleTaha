from django.contrib import admin

from education.models import Class, Teacher, Student


class ClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

    class Meta:
        model = Class


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone')
    filter_horizontal = ('classes',)

    class Meta:
        model = Teacher


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone')
    filter_horizontal = ('classes',)

    class Meta:
        model = Student


admin.site.register(Class, ClassAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
