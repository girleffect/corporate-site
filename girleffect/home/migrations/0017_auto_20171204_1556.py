# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-04 15:56
from __future__ import unicode_literals
from django.apps import apps
from django.db import migrations

ArticlePage = apps.get_model('articles', 'ArticlePage')
HomePage = apps.get_model('home', 'HomePage')
CountryPage = apps.get_model('countries', 'CountryPage')
PersonPage = apps.get_model('people', 'PersonPage')
SolutionPage = apps.get_model('solutions', 'SolutionPage')
StandardPage = apps.get_model('standardpage', 'StandardPage')
StandardIndex = apps.get_model('standardpage', 'StandardIndex')


def heading_to_aligned(block):
    if block['type'] == "heading":
        heading_value = block['value']
        block['type'] = "aligned_heading"
        block['value'] = {
            'text': heading_value,
            'size': 'h2',
            'alignment': 'left'
        }
    return


def aligned_to_heading(block):
    if block['type'] == "aligned_heading":
        heading_value = block['value']['text']
        block['type'] = "heading"
        block['value'] = heading_value
    return


def migrate_headings(apps, schema_editor):
    querysets = [
        ArticlePage.objects.all(), HomePage.objects.all(),
        CountryPage.objects.all(), PersonPage.objects.all(),
        SolutionPage.objects.all(), StandardPage.objects.all(),
        StandardIndex.objects.all()
    ]

    for queryset in querysets:
        for page in queryset:
            if hasattr(page, 'body'):
                for block in page.body.stream_data:
                    heading_to_aligned(block)
            if hasattr(page, 'biography'):
                for block in page.biography.stream_data:
                    heading_to_aligned(block)
            page.save()

    return


def migrate_headings_back(apps, schema_editor):
    querysets = [
        ArticlePage.objects.all(), HomePage.objects.all(),
        CountryPage.objects.all(), PersonPage.objects.all(),
        SolutionPage.objects.all(), StandardPage.objects.all(),
        StandardIndex.objects.all()
    ]
    for queryset in querysets:
        for page in queryset:
            if hasattr(page, 'body'):
                for block in page.body.stream_data:
                    aligned_to_heading(block)
            if hasattr(page, 'biography'):
                for block in page.biography.stream_data:
                    aligned_to_heading(block)
            page.save()
        return


class Migration(migrations.Migration):
    dependencies = [
        ('home', '0016_auto_20171204_1555'),
    ]

    operations = [
        migrations.RunPython(migrate_headings, reverse_code=migrate_headings_back),
    ]
