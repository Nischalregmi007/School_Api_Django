# Generated by Django 5.1.5 on 2025-04-01 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('studied_at', models.CharField(max_length=20)),
                ('parent_name', models.CharField(max_length=20)),
                ('parent_number', models.IntegerField()),
                ('status', models.CharField(default='Not_approved', max_length=20)),
            ],
        ),
    ]
