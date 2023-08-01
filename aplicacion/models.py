from django.db import models

# Create your models here.
# Create your models here.
class Gatito(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    raza = models.CharField(max_length=100)
    
     
    def __str__(self):
        return self.nombre


class Adoptante(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.CharField(max_length=50)
    direccion = models.EmailField()
    correo = models.CharField(max_length=50)

class Personal(models.Model):
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
