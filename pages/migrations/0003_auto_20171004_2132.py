# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('pages', '0002_auto_20171004_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='name',
            field=models.TextField(default=b'', max_length=255),
        ),
    ]
