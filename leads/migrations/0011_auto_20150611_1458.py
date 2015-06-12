# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0010_auto_20150611_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='contact',
        ),
        migrations.AddField(
            model_name='lead',
            name='name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lead',
            name='phone1',
            field=models.CharField(default='', max_length=10, unique=True, help_text='Use the plain phone number without any punctuation (<em>e.g. 5558675309</em>)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lead',
            name='phone2',
            field=models.CharField(max_length=10, help_text='Use the plain phone number without any punctuation (<em>e.g. 5558675309</em>)', blank=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='spouse',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
