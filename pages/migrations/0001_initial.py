# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('aboutus_heading', models.TextField(default=b'ABOUT US', max_length=255)),
                ('aboutus_subheading', models.TextField(default=b'', max_length=255)),
                ('aboutus_text', models.TextField(default=b'', max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='AboutUsContent',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('name', models.TextField(default=b'', max_length=255)),
                ('development_percent', models.TextField(default=b'', max_length=255)),
                ('image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.TextField(default=b'STAY CONNECTED', max_length=255)),
                ('description', models.TextField(default=b'', max_length=255)),
                ('facebook_link', models.TextField(help_text=b'If any of link is set empty then we will not show the icon.', max_length=255, null=True, blank=True)),
                ('twitter_link', models.TextField(max_length=255, null=True, blank=True)),
                ('google_link', models.TextField(max_length=255, null=True, blank=True)),
                ('instagram_link', models.TextField(max_length=255, null=True, blank=True)),
                ('pinterest_link', models.TextField(max_length=255, null=True, blank=True)),
                ('skype_link', models.TextField(max_length=255, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('company_name', models.TextField(default=b'Charismatic Labs', max_length=255)),
                ('banner_heading', models.TextField(default=b'Charismatic Labs', max_length=255)),
                ('banner_text', models.TextField(default=b'', max_length=255)),
                ('copyright_text', models.TextField(default=b'', max_length=255)),
                ('banner_image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('name', models.TextField(default=b'OUR TEAM', max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PortfolioCategory',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('name', models.TextField(default=b'OUR TEAM', max_length=255)),
                ('internal_name', models.TextField(default=b'', help_text=b'This is used for categorisation(enter internal name without any space)', max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PortfolioHeading',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.TextField(default=b'OUR WORKS', max_length=255)),
                ('description', models.TextField(default=b'', max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ServiceHeading',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.TextField(default=b'OUR SERVICES', max_length=255)),
                ('description', models.TextField(default=b'', max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ServicePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.TextField(default=b'', max_length=255)),
                ('description', models.TextField(default=b'', max_length=255)),
                ('icon', models.TextField(default=b'fa-code', max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='TeamHeading',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.TextField(default=b'OUR TEAM', max_length=255)),
                ('description', models.TextField(default=b'', max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='TeamPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('name', models.TextField(default=b'', max_length=255)),
                ('designation', models.TextField(default=b'', max_length=255)),
                ('description', models.TextField(default=b'', max_length=255)),
                ('facebook_link', models.TextField(default=b'', max_length=255)),
                ('twitter_link', models.TextField(default=b'', max_length=255)),
                ('google_link', models.TextField(default=b'', max_length=255)),
                ('avatar', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='portfolio_category',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailcore.Page', null=True),
        ),
    ]
