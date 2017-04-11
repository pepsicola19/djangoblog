# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-12 08:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='draft',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='news',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 1, 12, 8, 44, 22, 898000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
