from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .utils import authenticate_signup
from .models import Login
from .models import Signup
from .models import Kandidat


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')

        authenticated_user = authenticate_signup(username=username, password=password)

        if authenticated_user is not None:  # Periksa apakah autentikasi berhasil
            login(request, authenticated_user)
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

        signup_data = Signup.objects.create(username2=username, email=email, password2=password)


        # Simpan user ke dalam database
        try:
            signup_data = Signup.objects.create(username2=username, email=email, password2=password)

            # Autentikasi pengguna
            authenticated_signup_data = authenticate(request, username=email, password=password)

            if authenticated_signup_data is not None and authenticated_signup_data.is_authenticated:
                # Jika autentikasi berhasil, signup dan arahkan ke halaman submit
                login(request, authenticated_signup_data)
                return redirect('submit')
            else:
                # Jika autentikasi gagal, tampilkan pesan kesalahan
                return render(request, 'signup.html', {'error_message': 'Gagal melakukan pendaftaran'})
            
        except Exception as e:
            return render(request, 'signup.html', {'error_message': f'Gagal melakukan pendaftaran: {e}'})

    else:
        return render(request, 'signup.html')
    

def submit(request):
    return render(request, 'submit.html') 

def home(request):
    return render(request, 'home.html')

def voting(request):
    # Mengambil semua objek Kandidat dari database
    kandidat_list = Kandidat.objects.all()

    # Mengirimkan data ke template menggunakan konteks
    return render(request, 'voting.html', {'kandidat_list': kandidat_list})

def hasil(request):
    return render(request, 'hasil.html')

def about(request):
    return render(request, 'about.html')
