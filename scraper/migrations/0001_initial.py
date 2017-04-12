# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbr', models.CharField(blank=True, max_length=10, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('annual_revenue', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('site', models.URLField(blank=True, null=True)),
                ('street_address1', models.CharField(blank=True, max_length=255, null=True)),
                ('street_address2', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('zip_code', models.IntegerField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('number_of_employee', models.IntegerField(blank=True, null=True)),
                ('industry', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]