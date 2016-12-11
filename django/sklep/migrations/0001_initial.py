# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('ISBN', models.IntegerField()),
                ('description', models.TextField()),
                ('tableOfContents', models.TextField()),
                ('price', models.IntegerField()),
                ('ebook', models.BooleanField()),
                ('graphics', models.TextField()),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(to='sklep.Author')),
            ],
        ),
    ]
