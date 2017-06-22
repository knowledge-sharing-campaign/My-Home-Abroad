# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-22 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20170622_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
