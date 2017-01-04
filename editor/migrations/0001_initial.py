# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 00:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=64, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('version', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.IntegerField(db_index=True, default=0)),
                ('time', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('parent_version', models.IntegerField(default=0)),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='documentchange',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.User'),
        ),
        migrations.AddField(
            model_name='documentchange',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.Document'),
        ),
        migrations.AlterUniqueTogether(
            name='documentchange',
            unique_together=set([('document', 'author', 'parent_version'), ('document', 'version')]),
        ),
    ]
