# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-16 17:04
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20160830_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
