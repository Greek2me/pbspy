# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pbspy', '0014_auto_20150113_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='last_update_attempt',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 13, 19, 3, 19, 827268)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='update_date',
            field=models.DateTimeField(null=True),
        ),
    ]
