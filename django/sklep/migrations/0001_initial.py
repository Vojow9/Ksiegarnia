# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('tableOfContents', models.TextField()),
                ('price', models.IntegerField()),
                ('published_date', models.DateTimeField(null=True, blank=True)),
            ],
        ),
    ]
