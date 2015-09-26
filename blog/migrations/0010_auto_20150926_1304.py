# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_galery_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galery',
            name='category',
        ),
        migrations.AddField(
            model_name='galery',
            name='post',
            field=models.ForeignKey(related_name='c8', null=True, blank=True, verbose_name='Категория', to='blog.Post'),
        ),
    ]
