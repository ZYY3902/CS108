# Generated by Django 3.2.8 on 2021-12-01 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_part_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='part',
            field=models.ManyToManyField(related_name='_project_employee_part_+', to='project.Employee'),
        ),
    ]
