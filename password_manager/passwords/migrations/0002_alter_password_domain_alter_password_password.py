# Generated by Django 4.1.5 on 2023-01-22 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passwords', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password',
            name='domain',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='password',
            name='password',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
