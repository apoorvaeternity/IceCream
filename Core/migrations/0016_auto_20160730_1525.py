# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-30 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0015_auto_20160730_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='designer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='registration',
            name='hosteler',
            field=models.BooleanField(default=False),
        ),
    ]