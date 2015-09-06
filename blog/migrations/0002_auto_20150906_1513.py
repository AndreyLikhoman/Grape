# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Название RU', max_length=250)),
                ('title', models.CharField(blank=True, verbose_name='Заголовок в браузере', max_length=250)),
                ('metakey', models.CharField(blank=True, verbose_name='Ключевые слова', max_length=250)),
                ('metadesc', models.CharField(blank=True, verbose_name='Мета описание', max_length=250)),
                ('state', models.IntegerField(null=True, blank=True, choices=[(1, 'Новый'), (2, 'Активный'), (3, 'Архив')], verbose_name='Состояние', default=1)),
                ('slug', models.CharField(blank=True, verbose_name='Урл', max_length=250)),
                ('short_text', models.TextField(blank=True, verbose_name='Короткое описание EN')),
                ('video', models.CharField(blank=True, verbose_name='Видео id в кратком описании', max_length=250)),
                ('full_text', models.TextField(blank=True, verbose_name='Полное описание EN')),
                ('date', models.DateField(verbose_name='Дата публикации', auto_now_add=True)),
                ('published', models.BooleanField(verbose_name='Опубликован')),
                ('show', models.BooleanField(verbose_name='Всегда вверху')),
                ('ordering', models.IntegerField(null=True, blank=True, verbose_name='Порядок сортировки', default=0)),
                ('comments_count', models.IntegerField(null=True, blank=True, verbose_name='Количество коментариев', default=0)),
                ('raiting', models.DecimalField(verbose_name='Рейтинг', max_digits=3, decimal_places=2, default=0.0)),
                ('count_view', models.IntegerField(null=True, blank=True, verbose_name='Количество просмотров', default=0)),
                ('reit', models.DecimalField(max_digits=2, blank=True, decimal_places=1, null=True, verbose_name='Рейтинг', default=0.0)),
                ('count_votes', models.IntegerField(null=True, blank=True, verbose_name='Количество голосов', default=0)),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Название', db_index=True, max_length=250, unique=True)),
                ('slug', models.CharField(blank=True, verbose_name='Урл', max_length=250)),
                ('published', models.BooleanField(verbose_name='Опубликован')),
                ('ordering', models.IntegerField(null=True, blank=True, verbose_name='Порядок сортировки', default=0)),
                ('count_posts', models.IntegerField(null=True, blank=True, verbose_name='Количество постов', default=0)),
            ],
            options={
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.RemoveField(
            model_name='articles',
            name='in_category',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'ordering': ['ordering'], 'verbose_name_plural': 'Категории'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='alias',
        ),
        migrations.RemoveField(
            model_name='category',
            name='descript',
        ),
        migrations.AddField(
            model_name='category',
            name='count_posts',
            field=models.IntegerField(null=True, blank=True, verbose_name='Количество постов', default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='metadesc',
            field=models.CharField(blank=True, verbose_name='Мета описание', max_length=250),
        ),
        migrations.AddField(
            model_name='category',
            name='metakey',
            field=models.CharField(blank=True, verbose_name='Ключевые слова', max_length=250),
        ),
        migrations.AddField(
            model_name='category',
            name='ordering',
            field=models.IntegerField(null=True, blank=True, verbose_name='Порядок сортировки', default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, to='blog.Category', null=True, verbose_name='Родительская категория'),
        ),
        migrations.AddField(
            model_name='category',
            name='published',
            field=models.BooleanField(verbose_name='Опубликован', default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(blank=True, verbose_name='Урл', max_length=250),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(verbose_name='Название', db_index=True, blank=True, max_length=250, default='', unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(blank=True, verbose_name='Заголовок в браузере', max_length=250),
        ),
        migrations.DeleteModel(
            name='Articles',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, to='blog.Category', null=True, verbose_name='Категория', related_name='c1'),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(null=True, blank=True, to='blog.Tags', verbose_name='Теги', related_name='c2'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name='Пользователь'),
        ),
    ]
