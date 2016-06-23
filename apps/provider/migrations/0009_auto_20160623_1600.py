# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0008_auto_20160623_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practitioner',
            name='addresses',
            field=models.ManyToManyField(to='provider.Address', null=True, blank=True),
        ),
    ]
