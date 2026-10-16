from django.shortcuts import render, redirect
from .models import Producto

# Create your views here.

def listado_productos(request):
    productos = Producto.objects.all()
    return render(request, "productos.html", {"productos": productos})

def crear_producto(request):
    if request.method == "POST":

        crear_producto = Producto(
            nombre = request.POST["nombre"],
            descripcion = request.POST["descripcion"],
            precio = request.POST["precio"],
            cantidad = request.POST["cantidad"],
            fecha = request.POST["fecha"],
        )
        crear_producto.save()

        return redirect("/productos/")
    return render(request, "formulario.html")

def detalle_producto(request, id):
    detalle_producto = Producto.objects.get(id=id)
    return render(
        request, 
        "detalle.html",
        {"producto": detalle_producto}
    )

def editar_producto(request, id):
    editar_producto = Producto.objects.get(id=id)

    if request.method == "POST":
        editar_producto.nombre = request.POST["nombre"]
        editar_producto.descripcion = request.POST["descripcion"]
        editar_producto.precio = request.POST["precio"]
        editar_producto.cantidad = request.POST["cantidad"]
        editar_producto.fecha = request.POST["fecha"]
       
        editar_producto.save()
        return redirect("/productos/")

    return render(
        request, "formulario.html", {"productos": editar_producto}
    )

def eliminar_producto(request, id):
    eliminar_producto = Producto.objects.get(id=id)
    eliminar_producto.delete()
    return redirect("/productos/")