from django.db import models

# Create your models here.
class Libro(models.Model):
    ISBN = models.CharField(max_length=100, verbose_name="ISBN", unique=True)
    titulo = models.CharField(max_length=100, verbose_name="Titulo")
    autor = models.CharField(max_length=100, verbose_name="Autor")
    precio = models.IntegerField(verbose_name="Precio")

    def __str__(self):
        return f"ISBN:{self.ISBN} Título:{self.titulo} Autor:{self.autor} Precio:{self.precio}"

class Cliente(models.Model):   
    dni = models.IntegerField(verbose_name="DNI", unique=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    email = models.EmailField(max_length=100, verbose_name="Email")

    def nombre_apellido(self):
        return f"{self.nombre} {self.apellido}"
    
    def __str__(self):
        return f"DNI:{self.dni} Nombre y Apellido:{self.nombre_apellido} Email:{self.email}"

class Pedido(models.Model):
    pedido = models.CharField(max_length=100, verbose_name="Pedido")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fechaPedido = models.DateField(verbose_name="Fecha de Pedido")
    cantidad = models.IntegerField(verbose_name="Cantidad")

    def __str__(self):
        return f"Pedido:{self.pedido} Cliente:{self.cliente} Libro:{self.libro} Fecha de Pedido:{self.fechaPedido} Cantidad:{self.cantidad}"