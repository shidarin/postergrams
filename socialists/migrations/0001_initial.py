# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instagram', models.CharField(default=b'', help_text=b'Instagram username, not url', max_length=30, verbose_name=b'Instagram', blank=True)),
                ('twitter', models.CharField(default=b'', help_text=b'Twitter username, not url', max_length=15, verbose_name=b'Twitter', blank=True)),
                ('behance', models.CharField(default=b'', help_text=b'Behance username, not url', max_length=64, verbose_name=b'Behance', blank=True)),
                ('facebook', models.CharField(default=b'', help_text=b'Facebook username, not url', max_length=51, verbose_name=b'Facebook', blank=True)),
                ('website', models.URLField(default=b'', help_text=b'Website. This should be a url', verbose_name=b'Website', blank=True)),
                ('email', models.EmailField(default=b'', help_text=b'Email address', max_length=75, verbose_name=b'Email', blank=True)),
                ('first_name', models.CharField(default=b'', help_text=b'May be blank if artist only goes by their alias', max_length=b'64', verbose_name=b'First Name', blank=True)),
                ('middle_name', models.CharField(default=b'', help_text=b'May be blank if artist only goes by their alias', max_length=b'64', verbose_name=b'Middle Name', blank=True)),
                ('last_name', models.CharField(default=b'', help_text=b'May be blank if artist only goes by their alias', max_length=b'64', verbose_name=b'Last Name', blank=True)),
                ('alias', models.CharField(default=b'', help_text=b'May be blank if artist only goes by their real name', max_length=b'128', verbose_name=b'Alias', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', help_text=b'Name of the event', max_length=64, verbose_name=b'Event Name')),
                ('desc', models.CharField(default=b'', help_text=b'Short description of the event', max_length=1024, verbose_name=b'Description', blank=True)),
                ('opening', models.DateTimeField(help_text=b'Day and time of the event opening reception. If no reception, just put midnight.', verbose_name=b'Opening')),
                ('closing', models.DateTimeField(help_text=b'Day and time of the event closing reception. If no reception, just put midnight.', verbose_name=b'Closing')),
                ('online_sale', models.DateTimeField(help_text=b'If prints will be available online at a certain day and time, indicate that here.', null=True, verbose_name=b'Online Sale', blank=True)),
                ('artists', models.ManyToManyField(default=b'', help_text=b'Select all artists currently known to be involved in theevent.', to='socialists.Artist', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instagram', models.CharField(default=b'', help_text=b'Instagram username, not url', max_length=30, verbose_name=b'Instagram', blank=True)),
                ('twitter', models.CharField(default=b'', help_text=b'Twitter username, not url', max_length=15, verbose_name=b'Twitter', blank=True)),
                ('behance', models.CharField(default=b'', help_text=b'Behance username, not url', max_length=64, verbose_name=b'Behance', blank=True)),
                ('facebook', models.CharField(default=b'', help_text=b'Facebook username, not url', max_length=51, verbose_name=b'Facebook', blank=True)),
                ('website', models.URLField(default=b'', help_text=b'Website. This should be a url', verbose_name=b'Website', blank=True)),
                ('email', models.EmailField(default=b'', help_text=b'Email address', max_length=75, verbose_name=b'Email', blank=True)),
                ('name', models.CharField(help_text=b'Name of the gallery, website or group', max_length=128, verbose_name=b'Name')),
                ('address', models.CharField(default=b'', help_text=b'Actual real world physical address, if any', max_length=500, verbose_name=b'Physical Address', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='host',
            field=models.ForeignKey(to='socialists.Gallery'),
            preserve_default=True,
        ),
    ]
