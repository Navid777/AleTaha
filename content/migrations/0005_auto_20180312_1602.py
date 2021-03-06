# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-12 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_auto_20180312_1602'),
        ('content', '0004_auto_20180307_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, verbose_name='عنوان')),
                ('students', models.ManyToManyField(related_name='news_groups', to='education.Student', verbose_name='هنرجویان')),
                ('teachers', models.ManyToManyField(related_name='news_groups', to='education.Teacher', verbose_name='معلمان')),
            ],
            options={
                'verbose_name': 'گروه خبری',
                'verbose_name_plural': 'گروه\u200cهای خبری',
            },
        ),
        migrations.AddField(
            model_name='image',
            name='news_groups',
            field=models.ManyToManyField(related_name='images', to='content.NewsGroup', verbose_name='مخاطبان'),
        ),
        migrations.AddField(
            model_name='news',
            name='news_groups',
            field=models.ManyToManyField(related_name='news', to='content.NewsGroup', verbose_name='مخاطبان'),
        ),
        migrations.AddField(
            model_name='video',
            name='news_groups',
            field=models.ManyToManyField(related_name='videos', to='content.NewsGroup', verbose_name='مخاطبان'),
        ),
        migrations.AddField(
            model_name='videoclip',
            name='news_groups',
            field=models.ManyToManyField(related_name='video_clips', to='content.NewsGroup', verbose_name='مخاطبان'),
        ),
    ]
