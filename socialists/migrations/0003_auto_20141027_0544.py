# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialists', '0002_auto_20141027_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='artists',
            field=models.ManyToManyField(help_text=b'Select all artists currently known to be involved in the event.', to='socialists.Artist', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='desc',
            field=models.TextField(default=b'', help_text=b'Short description of the event', verbose_name=b'Description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gallery',
            name='address',
            field=models.TextField(default=b'', help_text=b'Actual real world physical address, if any', verbose_name=b'Physical Address', blank=True),
            preserve_default=True,
        ),
    ]
