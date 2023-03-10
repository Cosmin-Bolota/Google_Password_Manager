# Generated by Django 4.1.5 on 2023-01-27 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('passwords', '0003_rename_password_password_pwd'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPW',
            fields=[
                ('domain', models.CharField(blank=True, max_length=200, null=True)),
                ('pwd', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Password',
        ),
    ]
