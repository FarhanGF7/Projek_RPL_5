# Generated by Django 5.0.6 on 2024-05-19 09:57

import django.db.models.deletion
import sistem_perpus.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Buku",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("judul", models.CharField(max_length=200)),
                ("author", models.CharField(max_length=200)),
                ("nomor_buku", models.PositiveIntegerField()),
                ("kategori", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="PinjamBuku",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nomor_buku", models.CharField(max_length=13)),
                ("id_mahasiswa", models.CharField(blank=True, max_length=100)),
                ("tanggal_peminjaman", models.DateField(auto_now=True)),
                (
                    "tenggat_peminjaman",
                    models.DateField(default=sistem_perpus.models.deadline),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Mahasiswa",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nim", models.CharField(blank=True, max_length=13, unique=True)),
                ("kelas", models.CharField(max_length=10)),
                ("jurusan", models.CharField(max_length=200)),
                ("image", models.ImageField(blank=True, upload_to="")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
