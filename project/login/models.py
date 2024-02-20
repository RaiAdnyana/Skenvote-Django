from django.db import models
    

class Image(models.Model):
    caption=models.CharField(max_length=30)
    image=models.ImageField(upload_to="img/%y")
    def str(self):
        return self.caption


class Gambar(models.Model):
    deskripsi=models.CharField(max_length=30)
    foto=models.ImageField(upload_to="img/%y")
    def str(self):
        return self.deskripsi
    
class Login(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.username


