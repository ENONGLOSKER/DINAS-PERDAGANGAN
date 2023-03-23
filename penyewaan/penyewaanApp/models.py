from django.db import models

# Create your models here.
# tabel pasar
class Pasar(models.Model):
    lokasi  = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    update  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lokasi

# tabel penyewa
class Penyewa(models.Model):
    tempat  = models.ForeignKey(Pasar, on_delete= models.CASCADE)
    nama    = models.CharField(max_length=50)
    tp = (
        ('RUKO','RUKO'),
        ('TOKO','TOKO'),
    )
    tipe    = models.CharField(choices=tp,max_length=5)
    blk = (
        ('BLOK A','BLOK A'),
        ('BLOK B','BLOK B'),
        ('BLOK C','BLOK C'),
        ('BLOK D','BLOK D'),
    )
    blok    = models.CharField(choices=blk,max_length=10)
    nomor   = models.IntegerField()
    lmt = (
        ('1 Bulan','1 Bulan'),
        ('2 Bulan','2 Bulan'),
        ('3 Bulan','3 Bulan'),
        ('4 Bulan','4 Bulan'),
        ('5 Bulan','5 Bulan'),
        ('1/2 Tahun','1/2 Tahun'),
        ('1 Tahun','1 Tahun'),
    )
    limit   = models.CharField(choices=lmt,max_length=10)
    harga   = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama
