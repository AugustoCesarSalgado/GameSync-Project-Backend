from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    precio = models.PositiveIntegerField(null=False)
    cantidad = models.PositiveBigIntegerField(null=False)
    fecha_ingreso = models.DateField(default=timezone.now, null=False)
    descripcion = models.CharField(max_length=250, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.nombre} - ${self.precio}. Cantidad: {self.cantidad}. Categoria: {self.categoria}. Ingresado el {self.fecha_ingreso}'
