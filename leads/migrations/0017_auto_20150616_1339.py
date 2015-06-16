# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0016_lead_dnc'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallDirection',
            fields=[
                ('direction', models.CharField(primary_key=True, max_length=20, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='call',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='placed'),
        ),
        migrations.AlterField(
            model_name='call',
            name='scheduled',
            field=models.DateTimeField(blank=True, default=None, verbose_name='rescheduled to', null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Discovered'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='dnc',
            field=models.BooleanField(default=False, verbose_name='Do not call'),
        ),
        migrations.AddField(
            model_name='call',
            name='direction',
            field=models.ForeignKey(to='leads.CallDirection', default='Outgoing'),
        ),
    ]
