# Generated by Django 5.1.7 on 2025-03-09 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobtUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('salary_range_min', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('salary_range_max', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('position_wanted', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Job User',
                'verbose_name_plural': 'Job Users',
            },
        ),
    ]
