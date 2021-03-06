# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-05-27 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vcmapp', '0004_auto_20190526_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('position', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='releaseversion',
            name='weekly',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='releaseversion',
            name='status',
            field=models.CharField(choices=[('0', 'OPEN'), ('1', 'FINISH')], default='0', max_length=20),
        ),
    ]
