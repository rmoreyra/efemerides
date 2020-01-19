# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2020-01-18 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('efemerides', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='efemerides',
            old_name='osb_list',
            new_name='msj_efem',
        ),
        migrations.RemoveField(
            model_name='efemerides',
            name='ti_flow_name',
        ),
        migrations.AddField(
            model_name='efemerides',
            name='date_efem',
            field=models.DateTimeField(null=True),
        ),
    ]
