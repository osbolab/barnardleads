# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0008_auto_20150611_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='call',
            name='contact',
        ),
        migrations.AlterField(
            model_name='calloutcome',
            name='conjunction',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
