from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from .models import *
from django.db.models import Q


# Create your views here.

def index(request):
    if request.session.get("logueo", False):
        return render(request, "tienda/index.html")
    else:
        return HttpResponseRedirect(reverse("tienda:login"))


def login(request):
    if request.method == "POST":
        usuario = request.POST.get("nick")
        clave = request.POST.get("password")

        try:
            q = Usuario.objects.get(nick=usuario, password=clave)
            messages.success(request, f"Bienvenido sr(a) {q.nombre}!!")
            datos = {
                "rol": q.rol,
                "nombre_rol": q.get_rol_display(),
                "nombre": f"{q.nombre} {q.apellido}",
                "foto": q.foto.url if q.foto else "/media/fotos/default.png",
                "id": q.id
            }
            request.session["logueo"] = datos
            return HttpResponseRedirect(reverse("tienda:index"))
        except Usuario.DoesNotExist:
            messages.error(request, "Usuario o contraseña no válidos...")
            return render(request, "tienda/iniciarSesion_Registrarse.html")
    else:
        if request.session.get("logueo", False):
            return HttpResponseRedirect(reverse("tienda:index"))
        else:
            return render(request, "tienda/iniciarSesion_Registrarse.html")


def logout(request):
    try:
        del request.session["logueo"]
        messages.success(request, "Cesión cerrada correctamente")
    except Exception as e:
        messages.error(request, f"Error: {e}")
    return HttpResponseRedirect(reverse("tienda:login"))


def inicioAdmin(request):
    return render(request, "tienda/inicioAdmin.html")


def categorias(request):
    return render(request, "tienda/categorias/listar.html")


def alimento(request):
    sesion = request.session.get("logueo", False)
    if sesion["nombre_rol"] != "Usuario":
        result = Categoria.objects.all()
        context = {"data": result}
        # select * from Categoria
        return render(request, "tienda/categorias_inicio/productos/alimento.html", context)
    else:
        messages.warning(request, "Usted no tiene permisos para acceder..." )
        return HttpResponseRedirect(reverse("tienda:login"))


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


def productos(request):
    query = Producto.objects.all()
    context = {"data": query}
    return render(request, "tienda/productos/listar.html", context)


def productos_formulario(request):
    query = Categoria.objects.all()
    contexto = {"categorias": query}
    return render(request, "tienda/productos/pro-form.html", contexto)


def productos_guardar(request):
    if request.method == "POST":
        id = request.POST.get("id")
        nombre = request.POST.get("nombre")
        precio = request.POST.get("precio")
        fecha_compra = request.POST.get("fecha_compra")
        # Foráneas deben ser instancias de su clase
        categoria_instancia = Categoria.objects.get(pk=request.POST.get("categoria"))

        if id == "":
            # crear
            try:
                pro = Producto(
                    nombre=nombre,
                    precio=precio,
                    fecha_compra=fecha_compra,
                    categoria=categoria_instancia
                )
                pro.save()
                messages.success(request, "Guardado correctamente!!")
            except Exception as e:
                messages.error(request, f"Error. {e}")
        else:
            # actualizar
            try:
                q = Producto.objects.get(pk=id)
                q.nombre = nombre
                q.precio = precio
                q.fecha_compra = fecha_compra
                q.categoria = categoria_instancia
                q.save()
                messages.success(request, "Actualizado correctamente!!")
            except Exception as e:
                messages.error(request, f"Error. {e}")

        return HttpResponseRedirect(reverse("tienda:productos", args=()))

    else:
        messages.warning(request, "No se enviarion datos...")
        return HttpResponseRedirect(reverse("tienda:productos_formulario", args=()))


def productos_eliminar(request, id):
    try:
        q = Producto.objects.get(pk=id)
        q.delete()
        messages.success(request, "Eliminado correctamente!!")
    except Exception as e:
        messages.error(request, f"Error. {e}")
    return HttpResponseRedirect(reverse("tienda:productos", args=()))


def productos_editar(request, id):
    q = Producto.objects.get(pk=id)
    query = Categoria.objects.all()
    contexto = {"id": id, "data": q, "categorias": query}
    return render(request, "tienda/productos/pro-form.html", contexto)


def servicios(request):
    query = Servicio.objects.all()
    contexto = {"data": query}
    return render(request, "tienda/servicios/servicios.html", contexto)


def servicios_formulario(request):
    return render(request, "tienda/servicios/ser-form.html")


def servicios_guardar(request):
    if request.method == "POST":
        id = request.POST.get("id")
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")

        if id == "":
            # crear
            try:
                pro = Servicio(
                    nombre=nombre,
                    descripcion=descripcion
                )
                pro.save()
                messages.success(request, "Guardado correctamente!!")
            except Exception as e:
                messages.error(request, f"Error. {e}")
        else:
            # actualizar
            try:
                q = Servicio.objects.get(pk=id)
                q.nombre = nombre
                q.descripcion = descripcion
                q.save()
                messages.success(request, "Actualizado correctamente!!")
            except Exception as e:
                messages.error(request, f"Error. {e}")

        return HttpResponseRedirect(reverse("tienda:servicios", args=()))

    else:
        messages.warning(request, "No se enviarion datos...")
        return HttpResponseRedirect(reverse("tienda:servicios_formulario", args=()))


def servicios_eliminar(request, id):
    try:
        q = Servicio.objects.get(pk=id)
        q.delete()
        messages.success(request, "Eliminado correctamente!!")
    except Exception as e:
        messages.error(request, f"Error. {e}")
    return HttpResponseRedirect(reverse("tienda:servicios", args=()))


def servicios_editar(request, id):
    q = Servicio.objects.get(pk=id)
    contexto = {"id": id, "data": q}
    return render(request, "tienda/servicios/ser-form.html", contexto)


def pedidos(request):
    query = Pedido.objects.all()
    contexto = {"data": query}
    return render(request, "tienda/servicios/servicios.html", contexto)


def delimpieza(request):
    return render(request, "tienda/categorias_inicio/productos/delimpieza.html")


def vacunas(request):
    return render(request, "tienda/categorias_inicio/productos/vacunas.html")


def estetica(request):
    return render(request, "tienda/categorias_inicio/servicios/estetica.html")


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
