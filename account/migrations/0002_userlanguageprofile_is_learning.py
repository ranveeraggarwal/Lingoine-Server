# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-12 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlanguageprofile',
            name='is_learning',
            field=models.BooleanField(default=False),
        ),
    ]
