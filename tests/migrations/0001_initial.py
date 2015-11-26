# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0020_add_index_on_page_first_published_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessChild',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, to='wagtailcore.Page', serialize=False, parent_link=True, auto_created=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BusinessIndex',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, to='wagtailcore.Page', serialize=False, parent_link=True, auto_created=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BusinessSubIndex',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, to='wagtailcore.Page', serialize=False, parent_link=True, auto_created=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='EventIndex',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, to='wagtailcore.Page', serialize=False, parent_link=True, auto_created=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='EventPage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, to='wagtailcore.Page', serialize=False, parent_link=True, auto_created=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SimplePage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, to='wagtailcore.Page', serialize=False, parent_link=True, auto_created=True)),
                ('content', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='StreamPage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, to='wagtailcore.Page', serialize=False, parent_link=True, auto_created=True)),
                ('body', wagtail.wagtailcore.fields.StreamField((('text', wagtail.wagtailcore.blocks.CharBlock()), ('rich_text', wagtail.wagtailcore.blocks.RichTextBlock())))),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
