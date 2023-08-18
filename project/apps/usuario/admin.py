from django.contrib import admin

from . import models

@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'correo', 'fecha_nacimiento')
    list_filter = ('nombre', 'apellido', 'fecha_nacimiento')
    search_fields = ('nombre', 'apellido', 'correo', 'fecha_nacimiento')
