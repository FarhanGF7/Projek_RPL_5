from django.urls import path

from sistem_perpus.views import (home, admin_login, mahasiswa_login, registrasi_mahasiswa, ubah_password, Logout,
                                 profil, edit_profil, tambah_buku, list_buku, list_mahasiswa, pinjam_buku, 
                                 list_peminjam_buku,list_buku_mahasiswa, delete_buku, delete_mahasiswa, delete_peminjam_buku)

urlpatterns = [
    path("", home, name="home"),

    path("admin_login/", admin_login, name="admin_login"),
    path("mahasiswa_login/", mahasiswa_login, name="mahasiswa_login"),
    path("registrasi_mahasiswa/", registrasi_mahasiswa, name="registrasi_mahasiswa"),
    path("ubah_password/", ubah_password, name="ubah_password"),
    path("logout/", Logout, name="logout"),

    path("profil/", profil, name="profil"),
    path("edit_profil/", edit_profil, name="edit_profil"),

    path("tambah_buku/", tambah_buku, name="tambah_buku"),
    path("list_buku/", list_buku, name="list_buku"),
    path("list_mahasiswa/", list_mahasiswa, name="list_mahasiswa"),
    path("pinjam_buku/", pinjam_buku, name="pinjam_buku"),
    path("list_peminjam_buku/", list_peminjam_buku, name="list_peminjam_buku"),
    path("list_buku_mahasiswa/", list_buku_mahasiswa, name="list_buku_mahasiswa"),

    path("delete_buku/<int:myid>/", delete_buku, name="delete_buku"),
    path("delete_mahasiswa/<int:myid>/", delete_mahasiswa, name="delete_mahasiswa"),
    path("delete_peminjam_buku/<int:myid>/", delete_peminjam_buku, name="delete_peminjam_buku"),
]