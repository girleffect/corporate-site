# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-21 09:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0008_auto_20170921_1020'),
        ('countries', '0013_auto_20170920_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryPageRelatedPartner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partners', to='countries.CountryPage')),
                ('related_partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='country_partners', to='partners.Partner')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
