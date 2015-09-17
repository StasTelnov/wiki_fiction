# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0002_auto_20150914_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='paper',
            field=models.ForeignKey(to='papers.Paper', related_name='comments'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='comments'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='papers'),
        ),
    ]
