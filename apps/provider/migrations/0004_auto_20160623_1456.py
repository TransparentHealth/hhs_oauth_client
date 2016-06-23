# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('provider', '0003_auto_20160623_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='practitioner',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='practitioner',
            name='fhir_id',
            field=models.CharField(default='', unique=True, max_length=24),
        ),
        migrations.AlterField(
            model_name='practitioner',
            name='npi',
            field=models.CharField(default='', unique=True, max_length=10),
        ),
    ]
