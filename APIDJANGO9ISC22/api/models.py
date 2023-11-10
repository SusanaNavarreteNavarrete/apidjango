from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)

class DatosCSV(models.Model):
    Marca_temporal = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    pregunta1 = models.CharField(max_length=100)
    pregunta2 = models.CharField(max_length=100)
    pregunta3 = models.CharField(max_length=100)
    pregunta4 = models.CharField(max_length=100)
    pregunta5 = models.CharField(max_length=100)
    pregunta6 = models.CharField(max_length=100)
    pregunta7 = models.CharField(max_length=100)
    pregunta8 = models.CharField(max_length=100)
    pregunta9 = models.CharField(max_length=100)
    pregunta10 = models.CharField(max_length=100)