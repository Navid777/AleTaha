from django.apps import AppConfig
from django.db.models.signals import pre_delete, post_save


class ContentConfig(AppConfig):
    name = 'content'
    verbose_name = 'محتوا'

    def ready(self):
        from .signals import protect_news_group_all, student_post_save,  teacher_post_save
        from .models import NewsGroup
        NewsGroup.get_news_group_all()  # to create the "all" news group.
        pre_delete.connect(receiver=protect_news_group_all, dispatch_uid='news_group_all_pre_delete_signal',
                           sender='content.NewsGroup')
        post_save.connect(receiver=student_post_save, dispatch_uid='student_post_save_signal',
                          sender='education.Student')
        post_save.connect(receiver=teacher_post_save, dispatch_uid='teacher_post_save_signal',
                          sender='education.Teacher')
