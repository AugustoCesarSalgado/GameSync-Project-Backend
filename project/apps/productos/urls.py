from django.urls import path

from . import views

app_name = 'productos'

urlpatterns = [path('', views.index, name='index'),]

# Categorias
urlpatterns += [
    path('categoria/list/', views.CategoriaList.as_view(), name='categoria_list'),
    path('categoria/create/', views.CategoriaCreate.as_view(), name='categoria_create'),
    path('categoria/detail/<int:pk>', views.CategoriaDetail.as_view(), name='categoria_detail'),
    path('categoria/update/<int:pk>', views.CategoriaUpdate.as_view(), name='categoria_update'),
    path('categoria/delete/<int:pk>', views.CategoriaDelete.as_view(), name='categoria_delete'),
]

# Productos
urlpatterns += [
    path('producto/list/', views.ProductoList.as_view(), name='producto_list'),
    path('producto/create/', views.ProductoCreate.as_view(), name='producto_create'),
    path('producto/detail/<int:pk>', views.ProductoDetail.as_view(), name='producto_detail'),
    path('producto/update/<int:pk>', views.ProductoUpdate.as_view(), name='producto_update'),
    path('producto/delete/<int:pk>', views.ProductoDelete.as_view(), name='producto_delete'),
]