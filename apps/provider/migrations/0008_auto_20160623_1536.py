# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0007_auto_20160623_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practitioner',
            name='npi',
            field=models.CharField(default='', unique=True, max_length=10),
        ),
    ]
