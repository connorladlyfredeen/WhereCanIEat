# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_remove_review_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='name',
            field=models.CharField(default='None', max_length=20),
            preserve_default=False,
        ),
    ]
