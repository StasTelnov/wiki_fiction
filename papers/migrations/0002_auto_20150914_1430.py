# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='tag',
        ),
        migrations.AddField(
            model_name='paper',
            name='tags',
            field=models.ManyToManyField(to='papers.Tag', related_name='papers'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='paper',
            name='rating',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
