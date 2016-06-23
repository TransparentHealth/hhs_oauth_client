# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0002_auto_20160621_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='addresses',
        ),
        migrations.AddField(
            model_name='organization',
            name='addresses',
            field=models.ManyToManyField(to='provider.Address', blank=True),
        ),
        migrations.RemoveField(
            model_name='organization',
            name='affiliations',
        ),
        migrations.AddField(
            model_name='organization',
            name='affiliations',
            field=models.ManyToManyField(to='provider.Affiliation', blank=True),
        ),
        migrations.RemoveField(
            model_name='organization',
            name='licenses',
        ),
        migrations.AddField(
            model_name='organization',
            name='licenses',
            field=models.ManyToManyField(to='provider.License', blank=True),
        ),
        migrations.RemoveField(
            model_name='organization',
            name='taxonomies',
        ),
        migrations.AddField(
            model_name='organization',
            name='taxonomies',
            field=models.ManyToManyField(to='provider.Taxonomy', blank=True),
        ),
        migrations.AlterField(
            model_name='practitioner',
            name='addresses',
            field=models.ManyToManyField(to='provider.Address', blank=True),
        ),
        migrations.RemoveField(
            model_name='practitioner',
            name='affiliations',
        ),
        migrations.AddField(
            model_name='practitioner',
            name='affiliations',
            field=models.ManyToManyField(to='provider.Affiliation', blank=True),
        ),
        migrations.RemoveField(
            model_name='practitioner',
            name='licenses',
        ),
        migrations.AddField(
            model_name='practitioner',
            name='licenses',
            field=models.ManyToManyField(to='provider.License', blank=True),
        ),
        migrations.RemoveField(
            model_name='practitioner',
            name='taxonomies',
        ),
        migrations.AddField(
            model_name='practitioner',
            name='taxonomies',
            field=models.ManyToManyField(to='provider.Taxonomy', blank=True),
        ),
    ]
