# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-15 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_produto_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
