# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0005_auto_20160623_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='npi',
            field=models.CharField(default='', max_length=10),
        ),
    ]
