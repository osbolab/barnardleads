# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0007_leadtype_conjunction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leadtype',
            name='conjunction',
        ),
        migrations.AddField(
            model_name='calloutcome',
            name='conjunction',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
