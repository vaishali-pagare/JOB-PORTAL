# Generated by Django 4.1.2 on 2022-12-01 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0018_delete_company'),
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
                ('password', models.CharField(max_length=25)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.industry')),
            ],
            options={
                'db_table': 'Company',
            },
        ),
    ]
