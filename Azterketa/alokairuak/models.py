from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Etxea(models.Model):
    izena = models.CharField(max_length=100)
    herria = models.CharField(max_length=100)
    pertsona_kop = models.IntegerField(validators=[
        MinValueValidator(0)])
    
    def __str__(self):
        return self.izena
    
class Pertsona(models.Model):
    dni = models.CharField(max_length=50,primary_key=True)
    izena = models.CharField(max_length=100)
    abizena = models.CharField(max_length=100)
    emaila = models.CharField(max_length=100)
    
    def __str__(self):
        return self.izena
    
class Alokairua(models.Model):

    pertsona = models.ForeignKey(Pertsona,on_delete=models.CASCADE)
    etxea = models.ForeignKey(Etxea,on_delete=models.CASCADE)

    alokairu_data_hasi = models.DateField(null=True)
    alokairu_data_bukatu = models.DateField(null=True)