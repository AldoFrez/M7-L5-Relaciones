from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100) # un cliente puede comprar varios productos, varios productos pueden ser comprados varios clientes

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    clientes = models.ManyToManyField(Cliente, through='Compra') # may to many

class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateField()

# Create your models here.
