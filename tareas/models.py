from django.db import models
from usuarios.models import Personal, Rol

class Ubicacion(models.Model):
    nombreUbicacion = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombreUbicacion

class Stock(models.Model):
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.PROTECT)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Stock: {self.cantidad} unidades en {self.ubicacion.nombreUbicacion}"

    def restar_cantidad(self, unidades_a_restar):
        self.cantidad -= unidades_a_restar

    def aumentar_cantidad(self, unidades_a_agregar):
        self.cantidad += unidades_a_agregar

class Estado(models.Model):
    nombreEstado = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreEstado

class Consola(models.Model):
    nombreConsola = models.CharField(max_length=100)
    marcaConsola = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreConsola

class Distribucion(models.Model):
    localidadDistribucion = models.CharField(max_length=100)
    siglaDistribucion = models.CharField(max_length=5)

    def __str__(self):
        return self.localidadDistribucion


class Juego(models.Model):
    codigo_barra = models.CharField(primary_key=True, max_length=100)
    nombreJuego = models.CharField(max_length=100)
    consola = models.ForeignKey(Consola, on_delete=models.CASCADE)
    distribucion = models.ForeignKey(Distribucion, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT,null=True, blank=True)
    estado = models.CharField(max_length=20, default='Activo')
    imagen = models.ImageField(upload_to='juegos/', null=True, blank=True)
    def __str__(self):
        return self.nombreJuego

