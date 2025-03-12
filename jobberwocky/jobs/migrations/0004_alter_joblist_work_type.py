# Generated by Django 5.1.7 on 2025-03-10 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_joblist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblist',
            name='work_type',
            field=models.CharField(choices=[('remote', 'Remote'), ('onsite', 'Onsite'), ('hybrid', 'Hybrid')], max_length=10),
        ),
    ]
