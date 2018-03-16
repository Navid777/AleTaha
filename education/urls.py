from django.conf.urls import url

from education.views import ClassList, CreateStudent, CreateTeacher, UserClassList

urlpatterns = [
    url('^class_list/$', ClassList.as_view()),
    url('^user_class_list/$', UserClassList.as_view()),
    url('^create_student/$', CreateStudent.as_view()),
    url('^create_teacher/$', CreateTeacher.as_view()),
]
