from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=30)
    autor = models.CharField(max_length=20)
    genero = models.CharField(max_length=10)
    editorial = models.CharField(max_length=10)
    anio = models.IntegerField()
    
    def __init__(self,titulo,autor,genero,editorial,anio):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.editorial = editorial
        self.anio = anio

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    dni = models.IntegerField()

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=True)
    