from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre