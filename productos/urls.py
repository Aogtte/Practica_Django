from django.urls import path
from . import views

urlpatterns = [
    path("productos/", views.listado_productos),
    path("productos/crear/", views.crear_producto),
    path("productos/detalle/<id>/", views.detalle_producto),
    path("productos/editar/<id>/", views.editar_producto),
    path("productos/eliminar/<id>/", views.eliminar_producto),
]