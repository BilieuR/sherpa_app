# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-31 06:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sherpa', '0005_auto_20171031_0138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='userId',
        ),
    ]