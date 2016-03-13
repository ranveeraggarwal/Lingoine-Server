# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-13 04:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_usertoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlanguageprofile',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='language.Language'),
        ),
    ]