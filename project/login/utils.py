from .models import Signup  # Mengimpor model Signup
from django.contrib.auth.hashers import check_password

def authenticate_signup(username=None, password=None):
    try:
        user = Signup.objects.get(username2=username)  # Mengambil pengguna berdasarkan username2
        if check_password(password, user.password2):  # Memverifikasi password
            return user  # Jika autentikasi berhasil, kembalikan pengguna
    except Signup.DoesNotExist:
        return None  # Jika pengguna tidak ditemukan, kembalikan None
    return None  # Jika autentikasi gagal, kembalikan None
