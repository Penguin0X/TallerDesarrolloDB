from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator

class Rol(models.Model):
    nombreRol = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreRol

class Personal(models.Model):
    nombrePersonal = models.CharField(max_length=255)
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT)
    telefono = models.CharField(max_length=8, unique=True, validators=[RegexValidator(r'^[0-9]{8}$')])
    usuarios = models.CharField(max_length=255)
    contraseña = models.CharField(max_length=128, validators=[MinLengthValidator(8), RegexValidator(r'^[a-zA-Z0-9]+$')])

    def __str__(self):
        return self.nombrePersonal

class Ubicacion(models.Model):
    nombreUbicacion = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombreUbicacion

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

class Stock(models.Model):
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.PROTECT)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Stock: {self.cantidad} unidades en {self.ubicacion.nombreUbicacion}"

    def restar_cantidad(self, unidades_a_restar):
        self.cantidad -= unidades_a_restar

    def aumentar_cantidad(self, unidades_a_agregar):
        self.cantidad += unidades_a_agregar

class Juego(models.Model):
    codigoDeBarra = models.CharField(max_length=250, unique=True)
    nombreJuego = models.CharField(max_length=250)
    consola = models.ForeignKey(Consola, on_delete=models.PROTECT)
    distribucion = models.ForeignKey(Distribucion, on_delete=models.PROTECT)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to='juegos/')

    def __str__(self):
        return self.nombreJuego
