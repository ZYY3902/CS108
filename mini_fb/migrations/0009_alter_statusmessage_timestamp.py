# Generated by Django 3.2.8 on 2021-11-08 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0008_alter_statusmessage_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusmessage',
            name='timestamp',
            field=models.TextField(blank=True),
        ),
    ]
