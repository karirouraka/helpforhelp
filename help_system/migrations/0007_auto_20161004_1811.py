# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-04 18:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('help_system', '0006_auto_20161004_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='help',
            name='date',
        ),
        migrations.DeleteModel(
            name='Date',
        ),
    ]