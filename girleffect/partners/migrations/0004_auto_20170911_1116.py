# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-11 10:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0003_auto_20170911_1105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partner',
            old_name='link',
            new_name='internal_link',
        ),
    ]
