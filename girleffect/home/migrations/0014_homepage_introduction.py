# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-27 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_merge_20171122_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='introduction',
            field=models.TextField(blank=True, null=True),
        ),
    ]
