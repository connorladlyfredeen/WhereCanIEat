# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='city',
            field=models.CharField(default='None', max_length=20),
            preserve_default=False,
        ),
    ]