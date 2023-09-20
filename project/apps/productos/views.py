from typing import Any
from django import forms
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .models import Producto
from django.http import HttpRequest, HttpResponse

from . import models, forms

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    productos_registrados = Producto.objects.all()
    context = {'productos': productos_registrados}
    return render(request, 'productos/index.html', context)

#####Categoria######

# Listar Categorias
class CategoriaList(ListView):
    model = models.Categoria

# Crear Categorias
class CategoriaCreate(CreateView):
    model = models.Categoria
    form_class = forms.CategoriaForm
    success_url = reverse_lazy('productos:categoria_list')

# Ver detalles de Categorias
class CategoriaDetail(DetailView):
    model = models.Categoria

# Actualizar datos de Categorias
class CategoriaUpdate(UpdateView):
    model = models.Categoria
    form_class = forms.CategoriaForm
    success_url = reverse_lazy('productos:categoria_list')

# Eliminar Categorias
class CategoriaDelete(DeleteView):
    model = models.Categoria
    success_url = reverse_lazy('productos:categoria_list')

#####Productos#####

# Listar Productos
class ProductoList(ListView):
    model = models.Producto

    def get_queryset(self) -> QuerySet[Any]:
        if self.request.GET.get('consulta'):
            consulta = self.request.GET.get('consulta')
            object_list = models.Producto.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Producto.objects.all()
        return object_list
    
# Crear Productos
class ProductoCreate(CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy('productos:producto_list')

# Ver detalles de Productos
class ProductoDetail(DetailView):
    model = models.Producto

# Actualizar datos de Productos
class ProductoUpdate(UpdateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy('productos:producto_list')

class ProductoDelete(DeleteView):
    model = models.Producto
    success_url = reverse_lazy('productos:producto_list')


 
