# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-19 12:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('standardpage', '0041_merge_20180201_1432'),
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobBoardPage',
            fields=[
                ('standardpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='standardpage.StandardPage')),
            ],
            options={
                'abstract': False,
            },
            bases=('standardpage.standardpage',),
        ),
    ]
