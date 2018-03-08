from django.conf.urls import url

from content.views import NewsList, VideoList, ImageList, VideoClipList, ContentCategoryList

urlpatterns = [
    url('news_list/$', NewsList.as_view()),
    url('video_list/$', VideoList.as_view()),
    url('image_list/$', ImageList.as_view()),
    url('video_clip_list/$', VideoClipList.as_view()),
    url('category_list/$', ContentCategoryList.as_view()),
]