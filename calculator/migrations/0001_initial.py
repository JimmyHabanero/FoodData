# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('protein', models.FloatField(max_length=100)),
                ('carbs', models.FloatField(max_length=100)),
                ('fat', models.FloatField(max_length=100)),
                ('kcal', models.IntegerField()),
            ],
        ),
    ]
