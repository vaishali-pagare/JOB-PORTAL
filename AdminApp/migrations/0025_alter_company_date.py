# Generated by Django 4.1.2 on 2022-12-01 17:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0024_alter_company_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]