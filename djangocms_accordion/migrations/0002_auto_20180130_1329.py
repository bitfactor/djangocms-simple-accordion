# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-30 11:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_accordion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accordiontab',
            name='extra',
            field=models.CharField(blank=True, default=b'', max_length=32, verbose_name='extra information'),
        ),
        migrations.AlterField(
            model_name='accordioncontainer',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_accordion_accordioncontainer', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='accordiontab',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_accordion_accordiontab', serialize=False, to='cms.CMSPlugin'),
        ),
    ]
