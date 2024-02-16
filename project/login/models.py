from django.db import models
from django.contrib.auth.backends import BaseBackend

    
class Login (models.Model):
    username = models.CharField(max_length=200, null=False, blank=False)
    password = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
       return self.username
    
    
class Signup(models.Model):
    username2 = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    password2 = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.username2
    
class Kandidat(models.Model):
    foto1 = models.ImageField(upload_to='login/static/img', null=False, blank=False)
    nama_kandidat1 = models.CharField(max_length=100)
    foto2 = models.ImageField(upload_to='login/static/img', null=False, blank=False)
    nama_kandidat2 = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nama_kandidat1} {self.foto1} vs {self.nama_kandidat2} {self.foto2}"


