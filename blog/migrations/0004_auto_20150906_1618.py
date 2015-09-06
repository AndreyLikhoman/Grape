# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150906_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='full_text_en',
            field=models.TextField(blank=True, verbose_name='Полное описание EN'),
        ),
        migrations.AddField(
            model_name='post',
            name='short_text_en',
            field=models.TextField(blank=True, verbose_name='Короткое описание EN'),
        ),
        migrations.AlterField(
            model_name='post',
            name='full_text',
            field=models.TextField(blank=True, verbose_name='Полное описание RU'),
        ),
        migrations.AlterField(
            model_name='post',
            name='short_text',
            field=models.TextField(blank=True, verbose_name='Короткое описание RU'),
        ),
    ]
