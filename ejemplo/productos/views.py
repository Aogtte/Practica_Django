from django.shortcuts import render, redirect
from .models import producto

def crear(request):
    if request.method == 'POST':
        prod = producto(
            nombre = request.POST["nombre"],
            categoria = request.POST["categoria"],
            precio = request.POST["precio"],
            cantidad = request.POST["cantidad"],
            estado = request.POST["estado"]
        )
        prod.save()
        return redirect('/productos/lista/')
    return render(request, "formulario.html")

def listar(request):
    productos = producto.objects.all()
    return render(
        request,
        "lista.html",
        {"productos": productos}
    )

def detalle(request, id):
    prod = producto.objects.get(id=id)
    return render(
        request, 
        "detalle.html",
        {"producto": prod}
    )

def editar(request, id):
    prod = producto.objects.get(id=id)
    
    if request.method == "POST":
        prod.nombre = request.POST["nombre"]
        prod.categoria = request.POST["categoria"]
        prod.precio = request.POST["precio"]
        prod.cantidad = request.POST["cantidad"]
        prod.estado = request.POST["estado"]

        prod.save()
        return redirect('/productos/lista/')

    return render(
        request,
        "formulario.html",
        {"producto": prod}
    )

def eliminar(request, id):
    prod = producto.objects.get(id=id)
    prod.delete()
    return redirect('/productos/lista/')