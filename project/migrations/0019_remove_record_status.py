# Generated by Django 3.2.8 on 2021-12-07 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0018_alter_record_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='status',
        ),
    ]
