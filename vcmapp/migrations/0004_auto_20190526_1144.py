# Generated by Django 2.2.1 on 2019-05-26 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vcmapp', '0003_auto_20190429_1927'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='releaseversion',
            options={'ordering': ['-id']},
        ),
        migrations.AlterUniqueTogether(
            name='releaseversion',
            unique_together=set(),
        ),
    ]
