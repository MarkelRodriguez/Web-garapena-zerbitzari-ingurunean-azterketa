# Generated by Django 3.1.4 on 2023-10-17 08:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alokairuak', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etxea',
            name='pertsona_kop',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]