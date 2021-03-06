# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-04 02:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0028_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'verbose_name': '关于我们',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='AgreementPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'verbose_name': '用户协议',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='IndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='+', serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'verbose_name': '首页',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='WhateverPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
