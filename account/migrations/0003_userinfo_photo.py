# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2019-02-24 05:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_userinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
