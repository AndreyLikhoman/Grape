# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20150926_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='galery',
            name='category',
            field=models.ForeignKey(related_name='c8', null=True, to='blog.Category', blank=True, verbose_name='Категория'),
        ),
    ]
