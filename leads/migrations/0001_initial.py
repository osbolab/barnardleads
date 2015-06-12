# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('phone1', models.CharField(max_length=10)),
                ('phone2', models.CharField(max_length=10)),
                ('created', models.DateTimeField(verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('contact', models.ForeignKey(to='leads.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='LeadType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('type', models.CharField(max_length=16)),
            ],
        ),
        migrations.AddField(
            model_name='lead',
            name='type',
            field=models.ForeignKey(to='leads.LeadType'),
        ),
    ]
