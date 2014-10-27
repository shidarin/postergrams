# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='artists',
            field=models.ManyToManyField(help_text=b'Select all artists currently known to be involved in theevent.', to='socialists.Artist', null=True, blank=True),
            preserve_default=True,
        ),
    ]
