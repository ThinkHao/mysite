# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2019-03-02 06:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20190302_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 2, 6, 42, 55, 884380, tzinfo=utc)),
        ),
    ]
