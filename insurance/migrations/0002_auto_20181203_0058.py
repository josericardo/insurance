# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-03 00:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumberField',
            fields=[
                ('risktypefield_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='insurance.RiskTypeField')),
            ],
            options={
                'manager_inheritance_from_future': True,
            },
            bases=('insurance.risktypefield',),
        ),
        migrations.CreateModel(
            name='NumberValue',
            fields=[
                ('value_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='insurance.Value')),
                ('value', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
            options={
                'manager_inheritance_from_future': True,
            },
            bases=('insurance.value',),
        ),
        migrations.AlterField(
            model_name='risktypefield',
            name='risk_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='insurance.RiskType'),
        ),
    ]
