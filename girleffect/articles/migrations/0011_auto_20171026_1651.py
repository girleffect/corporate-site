# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-26 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_rename_news_models_to_article_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='publication_date',
            field=models.DateTimeField(blank=True, help_text='Use this field to override the date that the article appears to have been published.', null=True),
        ),
    ]
