# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-30 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sherpa', '0003_auto_20171030_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='image',
            field=models.CharField(default='NULL', max_length=499),
        ),
    ]
