# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0009_auto_20150611_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='lead',
            field=models.ForeignKey(to='leads.Lead'),
        ),
    ]
