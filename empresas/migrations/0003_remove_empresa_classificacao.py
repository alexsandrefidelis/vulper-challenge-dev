# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-11 17:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0002_empresa_classificacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='classificacao',
        ),
    ]
