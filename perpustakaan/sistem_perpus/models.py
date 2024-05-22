from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta
# Create your models here.


class Buku(models.Model):
    judul = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    nomor_buku = models.PositiveIntegerField()
    kategori = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.judul} [{self.nomor_buku}]"

class Mahasiswa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nim = models.CharField(max_length=13, blank=True, unique=True)
    kelas = models.CharField(max_length=10)
    jurusan = models.CharField(max_length=200)
    no_antri = models.CharField(max_length=3, blank=True)
    image = models.ImageField(upload_to="", blank=True)

    def __str__(self):
        return f"{self.user} [{self.jurusan}] [{self.kelas}] [{self.no_antri}]"

def deadline():
    return datetime.today() + timedelta(days=14)

class PinjamBuku(models.Model):
    nomor_buku = models.CharField(max_length=13)
    id_mahasiswa = models.CharField(max_length=100, blank=True) 
    tanggal_peminjaman = models.DateField(auto_now=True)
    tenggat_peminjaman = models.DateField(default=deadline)

    def __str__(self):
        return f"{self.id_mahasiswa}"