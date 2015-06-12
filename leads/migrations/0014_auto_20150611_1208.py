# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0013_auto_20150611_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='phone1',
            field=models.CharField(unique=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='lead',
            name='phone2',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
