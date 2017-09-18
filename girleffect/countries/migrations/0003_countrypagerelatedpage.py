# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 10:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0001_initial'),
        ('countries', '0002_auto_20170811_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryPageRelatedPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='solutions.SolutionPage')),
                ('source_page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_pages', to='countries.CountryPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]