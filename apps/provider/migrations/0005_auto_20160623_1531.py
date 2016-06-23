# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0004_auto_20160623_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='user',
        ),
        migrations.AddField(
            model_name='address',
            name='npi',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='practitioner',
            name='doing_business_as',
            field=models.CharField(default='', max_length=256, blank=True),
        ),
    ]
