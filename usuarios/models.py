from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
from django.contrib.auth.models import User

class Rol(models.Model):
    nombreRol = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreRol


class Personal(models.Model):
    nombrePersonal = models.CharField(max_length=255)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=8)
    usuarios = models.OneToOneField(User, on_delete=models.CASCADE)  
    contraseña = models.CharField(max_length=255)
    

    def __str__(self):
        return self.nombrePersonal