# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150906_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(unique=True, db_index=True, blank=True, max_length=250, default='', verbose_name='Название Категории'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='c2', to='blog.Tags', verbose_name='Теги', blank=True),
        ),
        migrations.AlterField(
            model_name='tags',
            name='name',
            field=models.CharField(unique=True, db_index=True, max_length=250, verbose_name='Название тэга'),
        ),
    ]
