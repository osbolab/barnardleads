# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0014_auto_20150611_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeadStatus',
            fields=[
                ('status', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='lead',
            name='status',
            field=models.ForeignKey(default='Cold', to='leads.LeadStatus'),
        ),
    ]
