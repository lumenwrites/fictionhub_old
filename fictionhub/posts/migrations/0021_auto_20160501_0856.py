# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0020_auto_20160426_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
