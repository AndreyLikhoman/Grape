# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150926_0833'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Название Видео', db_index=True, default='', blank=True)),
                ('title', models.CharField(verbose_name='Заголовок в браузере', max_length=250, blank=True)),
                ('image', models.ImageField(verbose_name='Видео', upload_to=blog.models.make_upload_path, default='', blank=True)),
                ('metakey', models.CharField(verbose_name='Ключевые слова', max_length=250, blank=True)),
                ('metadesc', models.CharField(verbose_name='Мета описание', max_length=250, blank=True)),
                ('slug', models.CharField(verbose_name='Урл', max_length=250, blank=True)),
                ('published', models.BooleanField(verbose_name='Опубликован', default=0)),
                ('ordering', models.IntegerField(verbose_name='Порядок сортировки', null=True, blank=True, default=0)),
                ('count_posts', models.IntegerField(verbose_name='Количество постов', null=True, blank=True, default=0)),
                ('parent', models.ForeignKey(null=True, blank=True, verbose_name='Родительская категория', to='blog.Media')),
            ],
            options={
                'verbose_name': 'Видеотека',
                'verbose_name_plural': 'Видеотеки',
                'ordering': ['ordering'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='Название', max_length=250, default='', blank=True)),
                ('video', models.FileField(verbose_name='Изображение', upload_to=blog.models.make_upload_path, default='', blank=True)),
                ('media', models.ForeignKey(null=True, blank=True, verbose_name='Галерея', related_name='c6', to='blog.Media')),
                ('post', models.ForeignKey(null=True, blank=True, verbose_name='Пост', related_name='c5', to='blog.Post')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
            },
        ),
    ]
