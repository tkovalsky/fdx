# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 15:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('number', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('trade_date', models.DateTimeField()),
                ('settlement_date', models.DateTimeField()),
                ('account_type', models.CharField(blank=True, choices=[('c', 'Cash'), ('m', 'Margin'), ('s', 'Short')], default='c', max_length=1)),
                ('transaction_type', models.CharField(choices=[('b', 'Buy'), ('bx', 'Buy Cancel'), ('bo', 'Buy Option'), ('bc', 'Buy Cover'), ('d', 'Dividend'), ('s', 'Sell'), ('sx', 'Sell Cancel'), ('so', 'Sell Option'), ('ss', 'Sell Short')], help_text='type', max_length=4)),
                ('symbol', models.CharField(max_length=10)),
                ('cusip', models.CharField(blank=True, max_length=10, null=True)),
                ('quantity', models.DecimalField(decimal_places=4, max_digits=10)),
                ('price', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fee', models.DecimalField(decimal_places=4, max_digits=10)),
                ('cents_per_share', models.DecimalField(decimal_places=4, default=0.03, max_digits=10)),
                ('transaction_amount_gross', models.DecimalField(decimal_places=4, max_digits=10)),
                ('sleeve', models.CharField(choices=[('e', 'Equity'), ('b', 'Bonds'), ('u', 'Unmanaged'), ('n', 'None')], default='n', max_length=1)),
                ('broker_of_record', models.CharField(default='FDX', max_length=4)),
                ('reason', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-trade_date'],
            },
        ),
        migrations.AddField(
            model_name='account',
            name='transactions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.Transaction'),
        ),
    ]
