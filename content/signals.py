from django.conf import settings
from django.db.models import ProtectedError

from content.models import NewsGroup


def protect_news_group_all(sender, instance, using, **kwargs):
    if instance.title != settings.NEWS_GROUP_ALL_TITLE:
        pass
    else:
        raise ProtectedError(protected_objects=instance,
                             msg='دستۀ «'+settings.NEWS_GROUP_ALL_TITLE+'» را نمیتوان حذف کرد.')


def student_post_save(sender, instance, using, **kwargs):
    NewsGroup.get_news_group_all().students.add(instance)


def teacher_post_save(sender, instance, using, **kwargs):
    NewsGroup.get_news_group_all().teachers.add(instance)


