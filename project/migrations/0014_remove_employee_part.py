# Generated by Django 3.2.8 on 2021-12-06 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0013_auto_20211206_0459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='part',
        ),
    ]
