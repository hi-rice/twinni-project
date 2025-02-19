# Generated by Django 5.1 on 2024-08-29 06:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(default='user', max_length=30),
        ),
        migrations.CreateModel(
            name='UserEmailSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_host', models.CharField(max_length=100)),
                ('email_port', models.IntegerField()),
                ('email_use_tls', models.BooleanField(default=True)),
                ('email_host_user', models.EmailField(max_length=254)),
                ('email_host_password', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
