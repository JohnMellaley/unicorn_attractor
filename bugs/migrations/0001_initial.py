# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-07 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bugs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('description', models.TextField()),
                ('vote', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
    ]