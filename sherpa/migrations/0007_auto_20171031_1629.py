# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-31 06:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sherpa', '0006_remove_users_userid'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='Profile',
        ),
    ]