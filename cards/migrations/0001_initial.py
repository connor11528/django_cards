# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('suit', models.PositiveSmallIntegerField(choices=[(0, b'spade'), (1, b'club'), (2, b'diamond'), (3, b'heart')])),
                ('rank', models.CharField(max_length=5)),
            ],
        ),
    ]
