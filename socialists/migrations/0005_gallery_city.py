# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialists', '0004_auto_20141027_0546'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='city',
            field=models.CharField(default=b'', help_text=b"City the gallery is in. If online group, put 'Online'", max_length=64, verbose_name=b'City', blank=True),
            preserve_default=True,
        ),
    ]
