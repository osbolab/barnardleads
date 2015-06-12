# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0005_auto_20150611_0641'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='When was the lead discovered?'),
        ),
        migrations.AlterField(
            model_name='call',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='When was the call was placed?'),
        ),
        migrations.AlterField(
            model_name='call',
            name='outcome',
            field=models.ForeignKey(to='leads.CallOutcome', default='Missed'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created'),
        ),
    ]
