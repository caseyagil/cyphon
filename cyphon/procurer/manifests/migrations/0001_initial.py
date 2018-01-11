# -*- coding: utf-8 -*-
# Copyright 2017 Dunbar Cybersecurity.
#
# This file is part of Cyphon Engine.
#
# Cyphon Engine is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Cyphon Engine is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Cyphon Engine. If not, see <http://www.gnu.org/licenses/>.
#
# Generated by Django 1.11.2 on 2017-12-12 16:05
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplyorders', '0001_initial'),
        ('stamps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manifest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='data')),
                ('stamp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stamps.Stamp', verbose_name='stamp')),
                ('supply_order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manifests', related_query_name='manifest', to='supplyorders.SupplyOrder', verbose_name='supply order')),
            ],
            options={
                'verbose_name_plural': 'manifests',
                'verbose_name': 'Manifest',
            },
        ),
    ]