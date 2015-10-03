# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20150926_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='galery',
            name='category',
            field=models.ForeignKey(null=True, blank=True, to='blog.Category', related_name='c11', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='galery',
            name='post',
            field=models.ForeignKey(null=True, blank=True, to='blog.Post', related_name='c8', verbose_name='Статья'),
        ),
    ]
