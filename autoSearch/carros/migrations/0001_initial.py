# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=140)),
                ('Type', models.CharField(max_length=140)),
                ('year', models.CharField(max_length=140)),
                ('colour', models.CharField(max_length=140)),
                ('price', models.DecimalField(decimal_places=2, max_digits=99999999)),
            ],
        ),
    ]