# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20150603_0235'),
        ('profiles', '0002_auto_20150603_0236'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='comments_downvoted',
            field=models.ManyToManyField(blank=True, related_name='downvoters', to='comments.Comment'),
        ),
        migrations.AddField(
            model_name='user',
            name='comments_upvoted',
            field=models.ManyToManyField(blank=True, related_name='upvoters', to='comments.Comment'),
        ),
    ]