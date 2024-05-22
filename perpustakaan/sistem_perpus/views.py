from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from sistem_perpus.models import *
from sistem_perpus.authentikasi import *
from sistem_perpus.forms import *

from datetime import date

# Create your views here.
def home(request):
    template_name = "index.html"
    return render(request, template_name)

@login_required(login_url = '/admin_login')
def tambah_buku(request):
    template_name = "tambah_buku.html"
    if request.method == "POST":
        judul = request.POST['judul']
        author = request.POST['author']
        nomor_buku = request.POST['nomor_buku']
        kategori = request.POST['kategori']

        buku = Buku.objects.create(judul=judul, author=author, nomor_buku=nomor_buku, kategori=kategori)
        buku.save()
        alert = True
        context = {
            'alert':alert
        }
        return render(request, template_name, context)
    return render(request, template_name)


@login_required(login_url = '/admin_login')
def list_buku(request):
    template_name = "list_buku.html"
    list_buku = Buku.objects.all()
    context = {
        'list_buku': list_buku
    }
    return render(request, template_name, context)

@login_required(login_url = '/admin_login')
def list_mahasiswa(request):
    template_name = "list_mahasiswa.html"
    list_mahasiswa = Mahasiswa.objects.all()
    context = {
        'list_mahasiswa':list_mahasiswa
    }
    return render(request, template_name, context)

@login_required(login_url = '/admin_login')
def pinjam_buku(request):
    template_name = "pinjam_buku.html"
    form = PinjamBukuForm()
    if request.method == "POST":
        form = PinjamBukuForm(request.POST)
        if form.is_valid():
            obj = PinjamBuku()
            obj.id_mahasiswa = request.POST['nama2']
            obj.nomor_buku = request.POST['nomor_buku2']
            obj.save()
            alert = True
            context = {
                'obj':obj,
                'alert':alert
            }
            return render(request, template_name, context)
    context = {
        'form':form
    }
    return render(request, template_name, context)

@login_required(login_url = '/admin_login')
def list_peminjam_buku(request):
    template_name = "list_peminjam_buku.html"
    list_peminjam = PinjamBuku.objects.all()
    details = []
    for i in list_peminjam:
        days = (date.today()-i.tanggal_peminjaman)
        d=days.days
        denda=0
        if d>14:
            day=d-14
            denda=day*5
        buku = list(models.Buku.objects.filter(nomor_buku=i.nomor_buku))
        mahasiswa = list(models.Mahasiswa.objects.filter(user=i.id_mahasiswa))
        i=0
        for j in buku:
            t=(mahasiswa[i].user,mahasiswa[i].user_id,buku[i].judul,buku[i].nomor_buku,list_peminjam[0].tanggal_peminjaman,list_peminjam[0].tenggat_peminjaman,denda)
            i=i+1
            details.append(t)
    context = {
        'list_peminjam':list_peminjam,
        'details':details
    }
    return render(request, template_name, context)

@login_required(login_url = '/mahasiswa_login')
def list_buku_mahasiswa(request):
    template_name = "list_buku_mahasiswa.html"
    mahasiswa = Mahasiswa.objects.filter(user_id=request.user.id)
    list_buku = PinjamBuku.objects.filter(id_mahasiswa=mahasiswa[0].user_id)
    list = []

    for i in list_buku:
        buku = Buku.objects.filter(nomor_buku=i.nomor_buku)
        for data in buku:
            days=(date.today()-i.tanggal_peminjaman)
            d=days.days
            denda=0
            if d>14:
                day=d-14
                denda=day*5
            t=(request.user.id, request.user.get_full_name, data.judul,data.author,list_buku[0].tanggal_peminjaman, list_buku[0].tenggat_peminjaman, denda)
            list.append(t)
        
    context = {
        'list': list
    }
    return render(request, template_name, context)

def delete_buku(request, myid):
    buku = Buku.objects.filter(id=myid)
    buku.delete()
    return redirect("/list_buku")

def delete_mahasiswa(request, myid):
    mahasiswa = Mahasiswa.objects.filter(id=myid)
    mahasiswa.delete()
    return redirect("/list_mahasiswa")

def delete_peminjam_buku(request, myid):
    peminjam_buku = PinjamBuku.objects.filter(id_mahasiswa=myid)
    peminjam_buku.delete()
    return redirect("/list_peminjam_buku")

@login_required(login_url = '/mahasiswa_login')
def profil(request):
    template_name = "profil.html"
    return render(request, template_name)

@login_required(login_url = '/mahasiswa_login')
def edit_profil(request):
    template_name = "edit_profil.html"
    mahasiswa = Mahasiswa.objects.get(user=request.user)
    if request.method == "POST":
        email = request.POST['email']
        nim = request.POST['nim']
        jurusan = request.POST['jurusan']
        kelas = request.POST['kelas']
        no_antri = request.POST['no_antri']

        mahasiswa.user.email = email
        mahasiswa.nim = nim
        mahasiswa.jurusan = jurusan
        mahasiswa.kelas = kelas
        mahasiswa.no_antri = no_antri
        mahasiswa.user.save()
        mahasiswa.save()
        alert = True
        context = {
            'alert': alert
        }
        return render(request, template_name, context)
    return render(request, template_name)


