# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-05-15 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0002_host_add_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='disk',
            field=models.CharField(max_length=30),
        ),
    ]