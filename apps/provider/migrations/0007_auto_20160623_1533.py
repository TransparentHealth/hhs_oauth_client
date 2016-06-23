# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0006_auto_20160623_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='npi',
            field=models.CharField(default='', max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='practitioner',
            name='npi',
            field=models.CharField(default='', max_length=10),
        ),
    ]
