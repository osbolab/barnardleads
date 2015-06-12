# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0015_auto_20150611_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='dnc',
            field=models.BooleanField(verbose_name='Do not call this lead', default=False),
        ),
    ]
