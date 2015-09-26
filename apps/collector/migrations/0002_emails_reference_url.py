# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emails',
            name='reference_url',
            field=models.URLField(null=True),
            preserve_default=True,
        ),
    ]
