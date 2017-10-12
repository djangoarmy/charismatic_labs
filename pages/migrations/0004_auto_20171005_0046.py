# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20171004_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='portfolio_category',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='pages.PortfolioCategory', null=True),
        ),
    ]
