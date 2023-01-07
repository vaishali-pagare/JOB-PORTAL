# Generated by Django 4.1.2 on 2022-11-30 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0007_alter_userinfo_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=20, unique=True)),
                ('phone', models.IntegerField()),
                ('person', models.CharField(max_length=25)),
                ('pincode', models.IntegerField()),
                ('address1', models.CharField(max_length=25)),
                ('image1', models.ImageField(default='abc.jpg', upload_to='Images')),
            ],
            options={
                'db_table': 'Company',
            },
        ),
    ]
