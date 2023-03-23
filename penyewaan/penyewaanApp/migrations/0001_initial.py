# Generated by Django 4.1.5 on 2023-03-22 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pasar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lokasi', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Penyewa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('tipe', models.CharField(max_length=10)),
                ('blok', models.CharField(max_length=10)),
                ('nomor', models.CharField(max_length=10)),
                ('limit', models.CharField(max_length=10)),
                ('harga', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('tempat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='penyewaanApp.pasar')),
            ],
        ),
    ]