# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_auto_20150611_0546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone2',
            field=models.CharField(max_length=10, blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='leadtype',
            name='type',
            field=models.CharField(max_length=2, choices=[('EX', 'Expired'), ('CA', 'Cancelled'), ('FS', 'FSBO')], default='FS'),
        ),
    ]
