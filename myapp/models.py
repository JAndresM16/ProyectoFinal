from django.db import models

class Usuario(models.Model):
    usuario = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    edad = models.IntegerField()
    pais = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario

class Revision(models.Model):
    codigo = models.CharField(max_length=50)
    C_filtro = models.CharField(max_length=100)
    C_aceite = models.CharField(max_length=20)
    C_freno = models.CharField(max_length=20)
    Revision_vehiculo = models.CharField(max_length=50)
   

    def __str__(self):
        return self.Revision
    
class Inventario(models.Model):
    mercaderia = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    marca = models.CharField(max_length=50)
    fecha = models.DateField
    

    def __str__(self):
        return self.Inventario

class Repuesto(models.Model):
    
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    marca = models.CharField(max_length=50)
    tipo_moto =  models.CharField(max_length=50)
    

    def __str__(self):
        return self.Repuesto
