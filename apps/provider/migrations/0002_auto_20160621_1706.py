# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practitioner',
            name='addresses',
        ),
        migrations.AddField(
            model_name='practitioner',
            name='addresses',
            field=models.ManyToManyField(to='provider.Address', null=True, blank=True),
        ),
    ]
