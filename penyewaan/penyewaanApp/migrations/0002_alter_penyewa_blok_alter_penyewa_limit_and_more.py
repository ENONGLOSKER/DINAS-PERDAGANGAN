# Generated by Django 4.1.5 on 2023-03-22 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penyewaanApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penyewa',
            name='blok',
            field=models.CharField(choices=[('a', 'BLOK A'), ('b', 'BLOK B'), ('c', 'BLOK C'), ('d', 'BLOK D')], max_length=10),
        ),
        migrations.AlterField(
            model_name='penyewa',
            name='limit',
            field=models.CharField(choices=[('1', '1 Bulan'), ('2', '2 Bulan'), ('3', '3 Bulan'), ('4', '4 Bulan'), ('5', '5 Bulan'), ('1/2', '1/2 Tahun'), ('1th', '1 Tahun')], max_length=10),
        ),
        migrations.AlterField(
            model_name='penyewa',
            name='nomor',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='penyewa',
            name='tipe',
            field=models.CharField(choices=[('R', 'RUKO'), ('T', 'TOKO')], max_length=5),
        ),
    ]
