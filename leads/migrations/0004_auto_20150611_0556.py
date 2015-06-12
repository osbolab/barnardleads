# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_auto_20150611_0550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leadtype',
            name='id',
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone1',
            field=models.CharField(unique=True, help_text='Use the plain phone number without any punctuation (<em>e.g. 5558675309</em>)', max_length=10),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone2',
            field=models.CharField(blank=True, help_text='Use the plain phone number without any punctuation (<em>e.g. 5558675309</em>)', max_length=10),
        ),
        migrations.AlterField(
            model_name='leadtype',
            name='type',
            field=models.CharField(serialize=False, default='FS', primary_key=True, choices=[('EX', 'Expired'), ('CA', 'Cancelled'), ('FS', 'FSBO')], max_length=2),
        ),
    ]
