# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0010_auto_20160623_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practitioner',
            name='fhir_id',
            field=models.CharField(default='', unique=True, max_length=24, verbose_name='FHIR ID'),
        ),
        migrations.AlterField(
            model_name='practitioner',
            name='first_name',
            field=models.CharField(default='', max_length=256, blank=True),
        ),
        migrations.AlterField(
            model_name='practitioner',
            name='last_name',
            field=models.CharField(default='', max_length=256, blank=True),
        ),
    ]
