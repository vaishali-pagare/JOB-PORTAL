# Generated by Django 4.1.2 on 2022-11-28 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usereducation',
            name='year',
            field=models.IntegerField(),
        ),
    ]
