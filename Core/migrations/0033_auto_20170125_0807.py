# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-25 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0032_auto_20160924_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='contact',
            field=models.CharField(max_length=10),
        ),
    ]
