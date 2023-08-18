from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    correo = models.EmailField(null=False)
    fecha_nacimiento = models.DateField(null=False)
    def __str__(self):
        return f'{self.nombre}, {self.apellido}, {self.correo}, {self.fecha_nacimiento}'
