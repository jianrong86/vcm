# Generated by Django 2.2.1 on 2019-06-02 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vcmapp', '0005_auto_20190527_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='releaseversion',
            name='build_type',
            field=models.CharField(blank=True, choices=[('0', '1st build'), ('1', 'Re-build')], default='0', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='releaseversion',
            name='re_release_reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='releaseversion',
            name='rebuild_reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='releaseversion',
            name='release_type',
            field=models.CharField(blank=True, choices=[('0', '1st release'), ('1', 'Re-release')], default='0', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='releaseversion',
            name='self_test_result',
            field=models.CharField(blank=True, choices=[('0', 'PASS'), ('1', 'FAIL')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='releaseversion',
            name='val_verify_result',
            field=models.CharField(blank=True, choices=[('0', 'PASS'), ('1', 'FAIL')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='releaseversion',
            name='weekly',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
