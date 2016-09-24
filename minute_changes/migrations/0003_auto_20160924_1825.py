# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 18:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minute_changes', '0002_auto_20160918_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chordpair',
            name='chord1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='chord1', to='chords.Chord'),
        ),
        migrations.AlterField(
            model_name='chordpair',
            name='chord2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='chord2', to='chords.Chord'),
        ),
        migrations.DeleteModel(
            name='Chord',
        ),
    ]