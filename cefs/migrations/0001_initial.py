# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('date_completed', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='supChapter',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('completedCourse', models.BooleanField(default=False)),
                ('chapter', models.ForeignKey(to='cefs.Chapter')),
            ],
        ),
    ]
