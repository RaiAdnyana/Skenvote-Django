from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from .models import Image, Gambar, Login
from django.contrib.auth.models import User


def login(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')

        User= Login(username=username,password=password)
        User.save()

        # Autentikasi pengguna menggunakan backend autentikasi kustom
        authenticated_user = authenticate(request, username=username, password=password)

        if authenticated_user is not None:  
            auth_login(request, authenticated_user)
            return redirect('home')
        else:
            return render(request, 'index.html', {'error_message': 'Authentication failed'})
        
    else:
        return render(request, 'index.html')
    


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('Username2')
        email = request.POST.get('Email2')
        password = request.POST.get('Password2')

        # Membuat pengguna baru
        user = User.objects.create_user(username=username, email=email, password=password)

        # Autentikasi pengguna
        authenticated_signup = authenticate(request, username=username, password=password)

        if authenticated_signup is not None:
            # Jika autentikasi berhasil, lakukan login dan arahkan ke halaman beranda
            auth_login(request, authenticated_signup)
            return redirect('submit')
        else:
            # Jika autentikasi gagal, tampilkan pesan kesalahan
            return render(request, 'signup.html', {'error_message': 'Autentikasi gagal'})
    else:
        return render(request, 'signup.html')

    

def submit(request):
    return render(request, 'submit.html') 

def home(request):
    return render(request, 'home.html')

def voting(request):
    image_pics = Image.objects.all()  # Query images from Image model
    gambar_pics = Gambar.objects.all()  # Query images from Gambar model

    # Pass both sets of objects to the template context using different variables
    context = {
        'image_pics': image_pics,
        'gambar_pics': gambar_pics,
    }
    return render(request, 'voting.html', context)

def hasil(request):
    return render(request, 'hasil.html')

def about(request):
    return render(request, 'about.html')

def BerhasilVoting(request):
    return render(request, 'BerhasilVoting.html')

