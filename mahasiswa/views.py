from django.shortcuts import render, redirect
from .models import Mahasiswa
from django.contrib.auth.decorators import login_required


def index(request):
    context = {
        'judul': 'Halo Mahasiswa',
        'deskripsi': 'Contoh halaman index menggunakan Django templates dan static files.'
    }
    return render(request, 'mahasiswa/index.html', context)


# Proteksi halaman daftar mahasiswa
@login_required(login_url='/accounts/login/')
def daftar_mahasiswa(request):
    mahasiswas = Mahasiswa.objects.all()
    return render(request, 'mahasiswa/daftar.html', {'mahasiswas': mahasiswas})


# Proteksi halaman tambah data mahasiswa
@login_required(login_url='/accounts/login/')
def tambah_mahasiswa(request):
    if request.method == 'POST':
        nim = request.POST['nim']
        nama = request.POST['nama']
        programstudi = request.POST['programstudi']
        Mahasiswa.objects.create(nim=nim, nama=nama, programstudi=programstudi)
        return redirect('daftar_mahasiswa')
    return render(request, 'mahasiswa/tambah.html')


# Proteksi halaman edit data mahasiswa
@login_required(login_url='/accounts/login/')
def edit_mahasiswa(request, id):
    mhs = Mahasiswa.objects.get(id=id)
    if request.method == 'POST':
        mhs.nim = request.POST['nim']
        mhs.nama = request.POST['nama']
        mhs.programstudi = request.POST['programstudi']
        mhs.save()
        return redirect('daftar_mahasiswa')
    return render(request, 'mahasiswa/edit.html', {'mhs': mhs})


# Proteksi halaman hapus data mahasiswa
@login_required(login_url='/accounts/login/')
def hapus_mahasiswa(request, id):
    mhs = Mahasiswa.objects.get(id=id)
    mhs.delete()
    return redirect('daftar_mahasiswa')
