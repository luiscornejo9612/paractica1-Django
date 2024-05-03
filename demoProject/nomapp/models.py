from django.db import models

# Create your models here.
class Rol(models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self):
        return self.nom

class Usuari(models.Model):
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    assignatures = models.CharField(max_length=100)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    def __str__(self):
        return f'{Usuari.nom}'


