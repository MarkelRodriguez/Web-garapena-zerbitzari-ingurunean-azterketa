# Generated by Django 3.1.4 on 2023-10-17 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etxea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('izena', models.CharField(max_length=100)),
                ('herria', models.CharField(max_length=100)),
                ('pertsona_kop', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pertsona',
            fields=[
                ('dni', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('izena', models.CharField(max_length=100)),
                ('abizena', models.CharField(max_length=100)),
                ('emaila', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Alokairua',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alokairu_data_hasi', models.DateField(null=True)),
                ('alokairu_data_bukatu', models.DateField(null=True)),
                ('etxea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alokairuak.etxea')),
                ('pertsona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alokairuak.pertsona')),
            ],
        ),
    ]