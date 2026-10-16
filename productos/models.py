from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length = 20)   
    descripcion = models.CharField(max_length = 200)   
    precio = models.DecimalField(max_digits = 12, decimal_places = 2)   
    cantidad = models.IntegerField()   
    fecha = models.DateField()