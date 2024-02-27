# Generated by Django 5.0.2 on 2024-02-27 15:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=10, unique=True)),
                ('brand', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('color', models.CharField(max_length=255)),
                ('condition', models.CharField(max_length=255)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.owner')),
            ],
        ),
    ]
