# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-15 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safras', '0002_auto_20161127_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='safra',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
