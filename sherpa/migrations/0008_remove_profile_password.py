# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-31 06:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sherpa', '0007_auto_20171031_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='password',
        ),
    ]
