# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hub',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('slug', models.SlugField(default='', max_length=64)),
                ('users_can_create_children', models.BooleanField(default=False)),
                ('description', models.TextField(max_length=512, blank=True)),
                ('parent', models.ForeignKey(related_name='children', null=True, blank=True, default=None, to='hubs.Hub')),
            ],
        ),
    ]
