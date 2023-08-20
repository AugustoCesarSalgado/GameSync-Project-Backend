from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DetailView

from .models import Producto
from django.http import HttpRequest, HttpResponse

from . import models

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def index(request):
    productos_registrados = Producto.objects.all()
    context = {'productos': productos_registrados}
    return render(request, 'productos/index.html', context)




 
