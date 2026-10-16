from django.shortcuts import render, redirect
from .models import Pedido

# Create your views here.

def listado_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, "pedidos.html", {"pedidos": pedidos})

def crear(request):
    if request.method == "POST":
        nuevo_pedido = Pedido(
            numero_pedido = request.POST["numero_pedido"],
            nombre_cliente = request.POST["nombre_cliente"],
            fecha = request.POST["fecha"],
            descripcion = request.POST["descripcion"],
            valor = request.POST["valor"],
            estado = request.POST["estado"],
            usuario = request.POST["usuario"],
        )
        nuevo_pedido.save()
        return redirect("/pedidos/")
    
    return render(request, "formulario_pedidos.html")

def detalle(request, id):
    mas_informacion = Pedido.objects.get(id=id)
    return render(
        request, 
        "detalle_pedidos.html",
        {"pedido": mas_informacion}
    )

def editar(request, id):
    editar_pedido = Pedido.objects.get(id=id)

    if request.method == "POST":
        editar_pedido.numero_pedido = request.POST["numero_pedido"]
        editar_pedido.nombre_cliente = request.POST["nombre_cliente"]
        editar_pedido.fecha = request.POST["fecha"]
        editar_pedido.descripcion = request.POST["descripcion"]
        editar_pedido.valor = request.POST["valor"]
        editar_pedido.estado = request.POST["estado"]
        editar_pedido.usuario = request.POST["usuario"]
        editar_pedido.save()
        return redirect("/pedidos/")

    return render(
        request, "formulario_pedidos.html", {"pedido": editar_pedido}
    )

def eliminar_pedido(request, id):
    eliminar_pedido = Pedido.objects.get(id=id)
    eliminar_pedido.delete()
    return redirect("/pedidos/")