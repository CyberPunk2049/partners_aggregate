# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 11:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banks',
            options={'verbose_name': 'Банк', 'verbose_name_plural': 'Банки'},
        ),
        migrations.AlterModelOptions(
            name='stocks',
            options={'verbose_name': 'Скидка', 'verbose_name_plural': 'Скидки'},
        ),
        migrations.AlterModelOptions(
            name='stores',
            options={'verbose_name': 'Партнёр', 'verbose_name_plural': 'Партнёры'},
        ),
    ]
