# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0009_auto_20160623_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='addresses',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='affiliations',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='licenses',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='taxonomies',
        ),
        migrations.RemoveField(
            model_name='practitioner',
            name='addresses',
        ),
        migrations.RemoveField(
            model_name='practitioner',
            name='affiliations',
        ),
        migrations.RemoveField(
            model_name='practitioner',
            name='licenses',
        ),
        migrations.RemoveField(
            model_name='practitioner',
            name='taxonomies',
        ),
        migrations.AddField(
            model_name='affiliation',
            name='npi',
            field=models.CharField(default='', max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='license',
            name='npi',
            field=models.CharField(default='', max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='taxonomy',
            name='npi',
            field=models.CharField(default='', max_length=10, blank=True),
        ),
    ]
