# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-14 14:12
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0008_auto_20171109_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='description',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, help_text="The statistic. For example, '66% of girls complete primary school'", max_length=180, verbose_name='Description'),
        ),
    ]
