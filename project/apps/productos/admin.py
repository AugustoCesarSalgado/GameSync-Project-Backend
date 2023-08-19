from django.contrib import admin
from django.db import models

from . import models

admin.site.site_title = 'Productos'

@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion',)
    list_filter = ('nombre',)
    search_fields = ('nombre', 'descripcion',)

@admin.register(models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'cantidad', 'fecha_ingreso', 'descripcion', 'categoria',)
    list_display_links = ('nombre',)
    list_filter = ('nombre', 'precio', 'cantidad', 'fecha_ingreso', 'categoria',)
    search_fields = ('nombre', 'precio', 'cantidad', 'fecha_ingreso', 'categoria',)
    ordering = ('nombre', 'categoria', 'fecha_ingreso',)
