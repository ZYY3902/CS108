# Generated by Django 3.2.8 on 2021-12-06 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_alter_part_part_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='part',
            field=models.ManyToManyField(related_name='_project_employee_part_+', to='project.Employee'),
        ),
        migrations.AlterField(
            model_name='part',
            name='part_id',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
