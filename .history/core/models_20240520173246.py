from django.db import models

# Create your models here.
class libro(models.Model):
    titulo = models.CharField(max_length=30)
    autor = models.CharField(max_length=20)
    genero = models.CharField(max_length=10)
    editorial = models.CharField(max_length=10)
    año = models.DecimalField()