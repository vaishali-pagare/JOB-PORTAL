# Generated by Django 4.1.2 on 2022-12-09 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0038_alter_job_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image1',
            field=models.ImageField(default='abc.jpg', upload_to='media'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='image',
            field=models.ImageField(default='abc.jpg', upload_to='media'),
        ),
    ]
