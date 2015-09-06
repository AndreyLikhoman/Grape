# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150906_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(blank=True, verbose_name='Название', default='', max_length=250)),
                ('image', models.ImageField(blank=True, upload_to=blog.models.make_upload_path, verbose_name='Изображение', default='')),
            ],
            options={
                'verbose_name_plural': 'Изображения',
                'verbose_name': 'Изображение',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to=blog.models.make_upload_path, verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='image',
            name='post',
            field=models.ForeignKey(to='blog.Post', related_name='c3', verbose_name='Пост', null=True, blank=True),
        ),
    ]
