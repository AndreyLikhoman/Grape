# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_media_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='preview',
            field=models.ImageField(default='', blank=True, upload_to=blog.models.make_upload_path, verbose_name='Изображение видео'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(default='', blank=True, upload_to=blog.models.make_upload_path, verbose_name='Видео'),
        ),
    ]
