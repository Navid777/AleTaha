from django.conf.urls import url

from education.views import ClassList, CreateStudent, CreateTeacher, UserClassList, sign_up_for_class

urlpatterns = [
    url('^class_list/$', ClassList.as_view()),
    url('^user_class_list/$', UserClassList.as_view()),
    url('^create_student/$', CreateStudent.as_view()),
    url('^create_teacher/$', CreateTeacher.as_view()),
    url('^sign_up_for_class/(?P<class_id>\d+)$', sign_up_for_class),
]
