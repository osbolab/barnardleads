# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0017_auto_20150616_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='date',
            field=models.DateTimeField(verbose_name='placed', db_index=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='call',
            name='direction',
            field=models.ForeignKey(verbose_name='^/v', default='Outgoing', to='leads.CallDirection'),
        ),
        migrations.AlterField(
            model_name='call',
            name='scheduled',
            field=models.DateTimeField(verbose_name='rescheduled to', blank=True, default=None, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='created',
            field=models.DateTimeField(verbose_name='discovered', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='dnc',
            field=models.BooleanField(verbose_name='do not call', default=False, db_index=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='name',
            field=models.CharField(max_length=200, db_index=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='phone1',
            field=models.CharField(max_length=20, verbose_name='phone', unique=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='phone2',
            field=models.CharField(max_length=20, verbose_name='alt', blank=True, db_index=True),
        ),
    ]
