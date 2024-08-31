# Generated by Django 5.1 on 2024-08-29 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='robot',
            name='model_number',
            field=models.CharField(default='DEFAULT_MODEL_NUMBER', max_length=100),
        ),
        migrations.AddField(
            model_name='robot',
            name='temperature',
            field=models.FloatField(default=0.0),
        ),
    ]
