# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 05:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_auto_20160426_0442'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='daily',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='rational',
            field=models.BooleanField(default=False),
        ),
    ]
