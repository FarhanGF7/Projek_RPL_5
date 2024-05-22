from django import forms
from django.contrib.auth.models import User
from . import models

class PinjamBukuForm(forms.Form):
    nomor_buku2 = forms.ModelChoiceField(queryset=models.Buku.objects.all(), empty_label="Judul Buku [Nomor Buku]", to_field_name="nomor_buku", label="Buku (Judul dan Nomor Buku)")
    nama2 = forms.ModelChoiceField(queryset=models.Mahasiswa.objects.all(), empty_label="Nama [Fakultas] [Kelas] [No Antri]", to_field_name="user", label="Detail Mahasiswa")
    
    nomor_buku2.widget.attrs.update({'class': 'form-control'})
    nama2.widget.attrs.update({'class':'form-control'})