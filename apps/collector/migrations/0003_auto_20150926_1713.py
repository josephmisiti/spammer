# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0002_emails_reference_url'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Emails',
            new_name='Email',
        ),
    ]
