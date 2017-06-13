# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=15)),
                ('lastname', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=25)),
                ('nationality', models.CharField(max_length=40)),
                ('phone', models.IntegerField(max_length=12)),
                ('gender', models.CharField(max_length=7)),
                ('DOB', models.IntegerField(max_length=3)),
            ],
        ),
    ]
