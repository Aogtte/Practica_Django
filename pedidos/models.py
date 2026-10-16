from django.db import models

# Create your models here.
class Pedido(models.Model):
    numero_pedido = models.IntegerField()   
    nombre_cliente = models.CharField(max_length = 20)
    fecha = models.DateField()
    descripcion = models.CharField(max_length = 200)
    valor = models.DecimalField(max_digits = 12, decimal_places = 2)
    estado = models.CharField()
    usuario = models.CharField(max_length = 20)