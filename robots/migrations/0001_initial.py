# Generated by Django 5.1 on 2024-08-26 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('idle', 'Idle'), ('busy', 'Busy'), ('charging', 'Charging')], max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('battery_level', models.IntegerField()),
            ],
        ),
    ]
