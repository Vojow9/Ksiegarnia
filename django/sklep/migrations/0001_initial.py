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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('author', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('tableOfContents', models.TextField()),
                ('price', models.IntegerField()),
                ('ebook', models.CharField(max_length=30)),
                ('paper', models.CharField(max_length=30)),
                ('graphics', models.TextField()),
                ('published_date', models.DateTimeField(null=True, blank=True)),
            ],
        ),
    ]
