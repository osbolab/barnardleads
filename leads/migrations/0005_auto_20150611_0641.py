# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0004_auto_20150611_0556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date', models.DateTimeField(verbose_name='When the call was placed')),
                ('scheduled', models.DateTimeField(verbose_name='If the call was rescheduled, when?', null=True, blank=True, default=None)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CallOutcome',
            fields=[
                ('outcome', models.CharField(max_length=20, serialize=False, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='spouse',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='leadtype',
            name='type',
            field=models.CharField(max_length=20, serialize=False, primary_key=True),
        ),
        migrations.AddField(
            model_name='call',
            name='contact',
            field=models.ForeignKey(to='leads.Contact'),
        ),
        migrations.AddField(
            model_name='call',
            name='lead',
            field=models.ForeignKey(blank=True, default=None, null=True, to='leads.Lead'),
        ),
        migrations.AddField(
            model_name='call',
            name='outcome',
            field=models.ForeignKey(to='leads.CallOutcome'),
        ),
    ]
