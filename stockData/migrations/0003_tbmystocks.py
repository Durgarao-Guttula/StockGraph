# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockData', '0002_auto_20170507_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbMyStocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Symbol', models.CharField(max_length=140, unique=True)),
            ],
        ),
    ]
