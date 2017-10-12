# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('contact_name', models.CharField(max_length=255, blank=True)),
                ('contact_email', models.EmailField(max_length=255, blank=True)),
                ('contact_subject', models.CharField(max_length=255, null=True, blank=True)),
                ('contact_message', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
