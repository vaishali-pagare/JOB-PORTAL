# Generated by Django 4.1.2 on 2022-12-08 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0037_alter_job_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='Education',
            field=models.CharField(max_length=40),
        ),
    ]
