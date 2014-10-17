# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import json

from django.db import models, migrations


def load_data(apps, schema_editor):
    filename = os.path.join(
        os.path.dirname(__file__),
        '../data',
        'ubigeo_reniec.json'
    )
    Ubigeo = apps.get_model('ubigeo', 'Ubigeo')
    with open(filename) as f:
        Ubigeo.objects.bulk_create(
            [Ubigeo(**entry) for entry in json.loads(f.read())]
        )


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ubigeo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('reniec', models.CharField(blank=True, max_length=6)),
                ('inei', models.CharField(blank=True, max_length=6)),
                ('parent', models.ForeignKey(null=True, blank=True, to='ubigeo.Ubigeo')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.RunPython(load_data)
    ]
