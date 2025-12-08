from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# === LOGIN VIEW ===
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Berhasil login!')
            return redirect('daftar_mahasiswa')  # arahkan ke halaman utama mahasiswa
        else:
            messages.error(request, 'Username atau password salah.')
    return render(request, 'accounts/login.html')


# === LOGOUT VIEW ===
def logout_view(request):
    logout(request)
    messages.info(request, 'Anda telah logout.')
    return redirect('/accounts/login/')
