# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-04-29 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vcmapp', '0002_auto_20190423_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='releaseversion',
            name='compiler',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='releaseversion',
            name='verifier',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='releaseversion',
            name='vpm',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='releaseversion',
            name='customer_name',
            field=models.CharField(max_length=30),
        ),
    ]
