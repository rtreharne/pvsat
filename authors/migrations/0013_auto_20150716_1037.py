# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0012_auto_20150716_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='delivery',
            field=models.CharField(default=b'OR', max_length=2, choices=[(b'Oral', b'Oral'), (b'Poster', b'Poster')]),
        ),
    ]
