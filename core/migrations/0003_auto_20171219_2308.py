# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-20 02:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171219_0819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arte',
            old_name='email',
            new_name='usuario',
        ),
    ]
