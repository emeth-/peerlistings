# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('tx_id', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('game_name', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('currency_name', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('currency_amount', models.IntegerField(default=0, null=True, blank=True)),
                ('details', models.TextField(null=True, blank=True)),
                ('cost', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('seller_address', models.CharField(default=b'', max_length=255, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Listing',
                'verbose_name_plural': 'Listings',
            },
        ),
        migrations.DeleteModel(
            name='Fish',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
