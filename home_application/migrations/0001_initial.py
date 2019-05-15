# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-05-15 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(unique=True)),
                ('system', models.CharField(max_length=64)),
                ('disk', models.CharField(max_length=30, unique=True)),
            ],
        ),
    ]
