# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170722_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='block_number',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
