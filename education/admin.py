from django.contrib import admin

from education.models import Class, Teacher, Student, Message


class ClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

    class Meta:
        model = Class


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone')
    filter_horizontal = ('classes',)
    list_display_links = ('id', 'first_name', 'last_name')

    class Meta:
        model = Teacher


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone')
    filter_horizontal = ('classes',)
    list_display_links = ('id', 'first_name', 'last_name')

    class Meta:
        model = Student


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'sender', 'receiver', 'confirmed')
    list_filter = ('confirmed',)
    list_display_links = ('id', 'message')

    class Meta:
        model = Message


admin.site.register(Class, ClassAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Message, MessageAdmin)
