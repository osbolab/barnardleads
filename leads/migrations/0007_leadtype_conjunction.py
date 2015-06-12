# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0006_auto_20150611_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='leadtype',
            name='conjunction',
            field=models.CharField(max_length=20, default=''),
            preserve_default=False,
        ),
    ]
