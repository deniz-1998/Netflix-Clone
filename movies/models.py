from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Kategori(models.Model):
    name=models.CharField(max_length=50,verbose_name="Kategori Adı")

    def __str__(self):
        return self.name

class Movies(models.Model):
    filmismi=models.CharField(max_length=200,verbose_name="Film Adı")
    aciklama=models.TextField(max_length=600)
    resim=models.FileField(upload_to='afis',null=True,blank=True)
    kategori=models.ForeignKey(Kategori,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.filmismi

class Izlenenler(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    izlenen=models.ManyToManyField('Movies',null=True)
    def __str__(self):
        return self.user.username