# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20170217_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_amount_gross',
            field=models.DecimalField(decimal_places=4, max_digits=25),
        ),
    ]