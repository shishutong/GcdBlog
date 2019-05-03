# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-04-25 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='number',
            field=models.IntegerField(default=1, verbose_name='分类数目'),
        ),
        migrations.AddField(
            model_name='tag',
            name='number',
            field=models.IntegerField(default=1, verbose_name='标签数目'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20, verbose_name='博客类别'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=20, verbose_name='博客标签'),
        ),
    ]