from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from .models import Categoria, Producto
from django.db.models import Q


# Create your views here.

def index(request):
    return render(request, "tienda/index.html")


def login(request):
    return render(request, "tienda/login.html")


def inicioAdmin(request):
    return render(request, "tienda/inicioAdmin.html")


def categorias(request):
    return render(request, "tienda/categorias/listar.html")


def alimento(request):
    result = Categoria.objects.all()
    context = {"data": result}
    # select * from Categoria
    return render(request, "tienda/categorias_inicio/productos/alimento.html", context)


def alimento_crear_formulario(request):
    return render(request, "tienda/categorias_inicio/productos/form.html")


def alimento_editar_formulario(request, id):
    q = Categoria.objects.get(pk=id)
    contexto = {"id": id, "data": q}
    return render(request, "tienda/categorias_inicio/productos/form.html", contexto)


def alimento_eliminar_formulario(request, id):
    try:
        q = Categoria.objects.get(pk=id)
        q.delete()
        messages.success(request, "Eliminado correctamente!!")
    except Exception as e:
        messages.error(request, f"Error. {e}")
    return HttpResponseRedirect(reverse("tienda:alimento", args=()))


def alimento_guardar(request):
    if request.method == "POST":
        id = request.POST.get("id")
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")

        if id == "":
            # crear
            try:
                cat = Categoria(
                    nombre=nombre,
                    descripcion=descripcion
                )
                cat.save()
                messages.success(request, "Guardado correctamente!!")
            except Exception as e:
                messages.error(request, f"Error. {e}")
        else:
            # actualizar
            try:
                q = Categoria.objects.get(pk=id)
                q.nombre = nombre
                q.descripcion = descripcion
                q.save()
                messages.success(request, "Actualizado correctamente!!")
            except Exception as e:
                messages.error(request, f"Error. {e}")

        return HttpResponseRedirect(reverse("tienda:alimento", args=()))

    else:
        messages.warning(request, "No se enviarion datos...")
        return HttpResponseRedirect(reverse("tienda:form", args=()))


def alimento_buscar(request):
    if request.method == "POST":
        buscar = request.POST.get("buscar")
        query = Categoria.objects.filter(Q(nombre__istartswith=buscar) | Q(descripcion__istartswith=buscar))
        context = {"data": query, "buscado": buscar}
        # select * from Categoria
        return render(request, "tienda/categorias_inicio/productos/alimento.html", context)
    else:
        messages.warning(request, "No se enviaron datos...")
    return HttpResponseRedirect(reverse("tienda:alimento", args=()))


def delimpieza(request):
    return render(request, "tienda/categorias_inicio/productos/delimpieza.html")


def vacunas(request):
    return render(request, "tienda/categorias_inicio/productos/vacunas.html")


def estetica(request):
    return render(request, "tienda/categorias_inicio/servicios/estetica.html")


def salud(request):
    return render(request, "tienda/categorias_inicio/servicios/salud.html")


def vacunacion(request):
    return render(request, "tienda/categorias_inicio/servicios/vacunacion.html")


def historia(request):
    return render(request, "tienda/categorias_inicio/quienesSomos/historia.html")


def nuestroequipo(request):
    return render(request, "tienda/categorias_inicio/quienesSomos/nuestroequipo.html")


def patrocinios(request):
    return render(request, "tienda/categorias_inicio/quienesSomos/patrocinios.html")


def contactanos(request):
    return render(request, "tienda/categorias_inicio/contactanos/contactanos.html")
