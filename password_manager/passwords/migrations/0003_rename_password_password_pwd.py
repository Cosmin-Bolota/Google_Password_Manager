# Generated by Django 4.1.5 on 2023-01-27 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passwords', '0002_alter_password_domain_alter_password_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='password',
            old_name='password',
            new_name='pwd',
        ),
    ]
