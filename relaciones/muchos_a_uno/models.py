

# Create your models here.
from django.db import models

class Region(models.Model):
    nombre = models.CharField(max_length=100)

class Estado(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="estados") # en este caso si se ocupa FK cuand oes de muchos es a uno