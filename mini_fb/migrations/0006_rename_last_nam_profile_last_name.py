# Generated by Django 3.2.8 on 2021-11-05 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0005_auto_20211105_1543'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='last_nam',
            new_name='last_name',
        ),
    ]