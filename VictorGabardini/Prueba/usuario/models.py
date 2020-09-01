from django.db import models

# Create your models here.


class Usuario(models.Model):
	usuario_id = models.IntegerField(primary_key=True, editable=False)
	nombre = models.CharField(max_length=60)
	telefono = models.CharField(max_length=30)
	email = models.CharField(max_length=254)
	contrasena = models.CharField(max_length=20)
	domicilio = models.CharField(max_length=100)

class Producto(models.Model):
#	producto_id = models.IntegerField(primary_key=True, editable=False)
	nombre = models.CharField(max_length=60)
	descripcion = models.TextField()
	precio = models.FloatField()
