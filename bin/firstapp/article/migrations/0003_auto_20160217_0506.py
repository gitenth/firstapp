# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_coments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Coments',
            new_name='Comments',
        ),
        migrations.AlterField(
            model_name='article',
            name='article_likes',
            field=models.IntegerField(default=0),
        ),
    ]
