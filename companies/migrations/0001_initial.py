# Generated by Django 4.2.15 on 2024-08-20 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('cif', models.CharField(max_length=100, unique=True)),
                ('city', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
