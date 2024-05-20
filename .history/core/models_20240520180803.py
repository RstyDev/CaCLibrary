from django.db import models

# Create your models here.
class libro(models.Model):
    id = models.UUIDField(auto_created=true,)
    titulo = models.CharField(max_length=30)
    autor = models.CharField(max_length=20)
    genero = models.CharField(max_length=10)
    editorial = models.CharField(max_length=10)
    año = models.IntegerField(max_length=4)
    
