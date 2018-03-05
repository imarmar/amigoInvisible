# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-03-05 15:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The ID provided by PhenoTips for this participant (starts with P)', max_length=255, verbose_name='PhenoTips ID')),
                ('email', models.CharField(help_text='The internal ID you use for the participant you are submitting.', max_length=255, verbose_name='Internal Participant ID')),
                ('partner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Participant')),
            ],
        ),
    ]
