# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-29 03:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171128_2309'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='arte',
            options={'verbose_name': 'Arte', 'verbose_name_plural': 'Artes'},
        ),
        migrations.AlterModelOptions(
            name='imagens',
            options={'verbose_name': 'Imagem', 'verbose_name_plural': 'Imagens'},
        ),
    ]
