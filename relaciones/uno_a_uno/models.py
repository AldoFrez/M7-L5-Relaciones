
from django.db import models

class Trabajador(models.Model): #  el models convierte este objeto tabla el modelo
    nombre = models.CharField(max_length=100)

class Curriculum(models.Model): # convierte de clase curriculoum con 3 columnas, ID, trabajador, y documento,
    trabajador = models.OneToOneField(Trabajador, on_delete=models.CASCADE) # relacion 1 es a 1, hereda el ID del trabajador
    documento = models.TextField()
# Create your models here. hayy 2 id, un id de trabajadsor de curriculum, el de trabajador 1 tiene relacion 
