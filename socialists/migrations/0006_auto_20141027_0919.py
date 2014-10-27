# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialists', '0005_gallery_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='city',
            field=models.CharField(help_text=b"City the gallery is in. If online group, put 'Online'", max_length=64, verbose_name=b'City'),
            preserve_default=True,
        ),
    ]
