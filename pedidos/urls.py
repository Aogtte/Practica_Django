from django.urls import path
from . import views

urlpatterns = [
    path("pedidos/", views.listado_pedidos),
    path("pedidos/crear/", views.crear),
    path("pedidos/detalle/<int:id>/", views.detalle),
    path("pedidos/editar/<int:id>/", views.editar),
    path("pedidos/eliminar/<int:id>/", views.eliminar_pedido),
]