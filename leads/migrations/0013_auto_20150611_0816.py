# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0012_auto_20150611_1501'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calloutcome',
            old_name='conjunction',
            new_name='past_tense',
        ),
        migrations.AlterField(
            model_name='call',
            name='scheduled',
            field=models.DateTimeField(blank=True, verbose_name='If the call was rescheduled, when to?', default=None, null=True),
        ),
    ]
