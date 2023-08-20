from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView

from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.index, name='index'),
    
]