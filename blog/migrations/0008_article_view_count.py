# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-02-03 00:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190202_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='view_count',
            field=models.IntegerField(default=0, verbose_name='觀看數'),
        ),
    ]