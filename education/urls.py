from django.conf.urls import url

from education.views import ClassList

urlpatterns = [
    url('class_list/$', ClassList.as_view()),
]