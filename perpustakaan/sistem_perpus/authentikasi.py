from django.shortcuts import redirect, render,HttpResponse

from django.contrib.auth import authenticate, login, logout

from sistem_perpus.models import *

def admin_login(request):
    template_name = "admin_login.html"
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect("/list_mahasiswa")
            else:
                return HttpResponse("Kamu Bukan Admin.")
        else:
            alert = True
            return render(request, template_name, {'alert':alert})
    return render(request, template_name)

def registrasi_mahasiswa(request):
    template_name = "registrasi_mahasiswa.html"
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        nim = request.POST['nim']
        jurusan = request.POST['jurusan']
        kelas = request.POST['kelas']
        no_antri = request.POST['no_antri']
        image = request.FILES['image']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            passnotsame = True
            return render(request, template_name, {'passnotsame':passnotsame})

        user = User.objects.create_user(username=username, email=email, password=password,first_name=first_name, last_name=last_name)
        mahasiswa = Mahasiswa.objects.create(user=user, nim=nim, jurusan=jurusan, kelas=kelas, no_antri=no_antri, image=image)
        user.save()
        mahasiswa.save()
        alert = True
        return render(request, template_name, {'alert':alert})
    return render(request, template_name)

def mahasiswa_login(request):
    template_name = "mahasiswa_login.html"
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return HttpResponse("Kamu Bukan Mahasiswa!")
                return redirect("/admin_login")
            else:
                return redirect("/profil")
        else:
            alert = True
            return render(request, template_name, {'alert':alert})
    return render(request, template_name)

def ubah_password(request):
    template_name = "ubah_password.html"
    if request.method == "POST":
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(current_password):
                u.set_password(new_password)
                u.save()
                alert = True
                return render(request, template_name, {'alert':alert})
            else:
                currpasswrong = True
                return render(request, template_name, {'currpasswrong':currpasswrong})
        except:
            pass
    return render(request, template_name)

def Logout(request):
    logout(request)
    return redirect ("/")
