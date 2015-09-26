# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150906_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Galery',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, db_index=True, blank=True, verbose_name='Название Галереи', default='')),
                ('title', models.CharField(max_length=250, blank=True, verbose_name='Заголовок в браузере')),
                ('image', models.ImageField(default='', upload_to=blog.models.make_upload_path, blank=True, verbose_name='Изображение')),
                ('metakey', models.CharField(max_length=250, blank=True, verbose_name='Ключевые слова')),
                ('metadesc', models.CharField(max_length=250, blank=True, verbose_name='Мета описание')),
                ('slug', models.CharField(max_length=250, blank=True, verbose_name='Урл')),
                ('published', models.BooleanField(default=0, verbose_name='Опубликован')),
                ('ordering', models.IntegerField(null=True, default=0, blank=True, verbose_name='Порядок сортировки')),
                ('count_posts', models.IntegerField(null=True, default=0, blank=True, verbose_name='Количество постов')),
                ('parent', models.ForeignKey(null=True, to='blog.Galery', blank=True, verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name_plural': 'Галереи',
                'ordering': ['ordering'],
                'verbose_name': 'Галерея',
            },
        ),
        migrations.AddField(
            model_name='image',
            name='galery',
            field=models.ForeignKey(related_name='c4', null=True, to='blog.Galery', blank=True, verbose_name='Галерея'),
        ),
    ]
