# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fhir_json_snipit', models.TextField(default='', max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Affiliation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fhir_json_snipit', models.TextField(default='', max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fhir_json_snipit', models.TextField(default='', max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('npi', models.CharField(default='', max_length=10)),
                ('fhir_id', models.CharField(default='', max_length=24)),
                ('organization_name', models.CharField(default='', max_length=256)),
                ('doing_business_as', models.CharField(default='', max_length=256)),
                ('addresses', models.ForeignKey(blank=True, to='provider.Address', null=True)),
                ('affiliations', models.ForeignKey(blank=True, to='provider.Affiliation', null=True)),
                ('licenses', models.ForeignKey(blank=True, to='provider.License', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Practitioner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('npi', models.CharField(default='', max_length=10)),
                ('fhir_id', models.CharField(default='', max_length=24)),
                ('first_name', models.CharField(default='', max_length=256)),
                ('last_name', models.CharField(default='', max_length=256)),
                ('doing_business_as', models.CharField(default='', max_length=256)),
                ('addresses', models.ForeignKey(blank=True, to='provider.Address', null=True)),
                ('affiliations', models.ForeignKey(blank=True, to='provider.Affiliation', null=True)),
                ('licenses', models.ForeignKey(blank=True, to='provider.License', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Taxonomy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fhir_json_snipit', models.TextField(default='', max_length=2000)),
            ],
        ),
        migrations.AddField(
            model_name='practitioner',
            name='taxonomies',
            field=models.ForeignKey(blank=True, to='provider.Taxonomy', null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='taxonomies',
            field=models.ForeignKey(blank=True, to='provider.Taxonomy', null=True),
        ),
    ]
