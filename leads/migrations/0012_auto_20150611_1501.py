# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0011_auto_20150611_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='type',
            field=models.ForeignKey(default='Expired', to='leads.LeadType'),
        ),
    ]
