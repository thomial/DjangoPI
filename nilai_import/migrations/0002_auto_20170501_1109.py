# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nilai_import', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regresi_korelasi',
            name='hasil_regresi',
        ),
        migrations.AddField(
            model_name='regresi_korelasi',
            name='hasil_regresi_a',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='regresi_korelasi',
            name='hasil_regresi_b',
            field=models.FloatField(null=True),
        ),
    ]