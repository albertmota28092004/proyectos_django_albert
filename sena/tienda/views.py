from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
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


def catalogo(request):
    if request.session.get("logueo", False):
        c = Categoria.objects.all()

        filtro_categoria = request.GET.get("id")

        if filtro_categoria != None and filtro_categoria != '0':
            p = Producto.objects.filter(categoria_id=filtro_categoria)
        else:
            p = Producto.objects.all()

        contexto = {"categorias": c, "productos": p}
        return render(request, "tienda/catalogo/catalogo.html", contexto)
    else:
        return HttpResponseRedirect(reverse("tienda:catalogo"))


def index2(request):
    return render(request, "tienda/index2.html")


def agendarcita(request):
    return render(request, "tienda/citas.html")


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
        del request.session["carrito"]
        messages.success(request, "Cesión cerrada correctamente")
    except Exception as e:
        messages.error(request, f"Error: {e}")
    return HttpResponseRedirect(reverse("tienda:login"))


def inicioAdmin(request):
    return render(request, "tienda/inicioAdmin.html")


"""def alimento_buscar(request):
    if request.method == "POST":
        buscar = request.POST.get("buscar")
        query = Categoria.objects.filter(Q(nombre__istartswith=buscar) | Q(descripcion__istartswith=buscar))
        context = {"data": query, "buscado": buscar}
        # select * from Categoria
        return render(request, "tienda/categorias_inicio/productos/alimento.html", context)
    else:
        messages.warning(request, "No se enviaron datos...")
    return HttpResponseRedirect(reverse("tienda:alimento", args=()))"""


def categorias(request):
    query = Categoria.objects.all()
    context = {"data": query}
    return render(request, "tienda/categorias/categorias.html", context)


def categorias_formulario(request):
    return render(request, "tienda/categorias/cat-form.html")


def categorias_guardar(request):
    if request.method == "POST":
        id = request.POST.get("id")
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")

        if id == "":
            # crear
            try:
                pro = Categoria(
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
                q = Categoria.objects.get(pk=id)
                q.nombre = nombre
                q.descripcion = descripcion
                q.save()
                messages.success(request, "Actualizado correctamente!!")
            except Exception as e:
                messages.error(request, f"Error. {e}")

        return HttpResponseRedirect(reverse("tienda:categorias", args=()))

    else:
        messages.warning(request, "No se enviarion datos...")
        return HttpResponseRedirect(reverse("tienda:categorias_formulario", args=()))


def categorias_eliminar(request, id):
    try:
        q = Categoria.objects.get(pk=id)
        q.delete()
        messages.success(request, "Eliminado correctamente!!")
    except Exception as e:
        messages.error(request, f"Error. {e}")
    return HttpResponseRedirect(reverse("tienda:categorias", args=()))


def categorias_editar(request, id):
    q = Categoria.objects.get(pk=id)
    contexto = {"id": id, "data": q}
    return render(request, "tienda/categorias/cat-form.html", contexto)


def productos(request):
    query = Producto.objects.all()
    context = {"data": query}
    return render(request, "tienda/productos/listar.html", context)


def productos_formulario(request):
    return render(request, "tienda/productos/pro-form.html")


def productos_guardar(request):
    if request.method == "POST":
        id = request.POST.get("id")
        nombre = request.POST.get("nombre")
        precio = request.POST.get("precio")
        fecha_compra = request.POST.get("fecha_compra")

        if id == "":
            # crear
            try:
                pro = Producto(
                    nombre=nombre,
                    precio=precio,
                    fecha_compra=fecha_compra
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
    contexto = {"id": id, "data": q}
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
    return render(request, "tienda/pedidos/pedidos.html", contexto)


def pedidos_formulario(request):
    return render(request, "tienda/pedidos/ped-form.html")


def pedidos_guardar(request):
    if request.method == "POST":
        id = request.POST.get("id")
        fecha = request.POST.get("fecha")
        descripcion = request.POST.get("descripcion")
        precio = request.POST.get("precio")
        usuario_instancia = Usuario.objects.get(pk=request.POST.get("usuario"))

        if id == "":
            # crear
            try:
                pro = Pedido(
                    nombre=fecha,
                    descripcion=descripcion,
                    precio=precio,
                    usuario=usuario_instancia
                )
                pro.save()
                messages.success(request, "Guardado correctamente!!")
            except Exception as e:
                messages.error(request, f"Error. {e}")
        else:
            # actualizar
            try:
                q = Pedido.objects.get(pk=id)
                q.fecha = fecha
                q.descripcion = descripcion
                q.precio = precio
                q.usuario = usuario_instancia
                q.save()
                messages.success(request, "Actualizado correctamente!!")
            except Exception as e:
                messages.error(request, f"Error. {e}")

        return HttpResponseRedirect(reverse("tienda:pedidos", args=()))

    else:
        messages.warning(request, "No se enviarion datos...")
        return HttpResponseRedirect(reverse("tienda:pedidos_formulario", args=()))


def pedidos_eliminar(request, id):
    try:
        q = Pedido.objects.get(pk=id)
        q.delete()
        messages.success(request, "Eliminado correctamente!!")
    except Exception as e:
        messages.error(request, f"Error. {e}")
    return HttpResponseRedirect(reverse("tienda:pedidos", args=()))


def pedidos_editar(request, id):
    q = Pedido.objects.get(pk=id)
    query = Usuario.objects.all()
    contexto = {"id": id, "data": q, "usuarios": query}
    return render(request, "tienda/pedidos/ped-form.html", contexto)


def usuarios(request):
    query = Usuario.objects.all()
    contexto = {"data": query}
    return render(request, "tienda/usuarios/usuarios.html", contexto)


def usuarios_formulario(request):
    q = request.session.get("logueo", False)
    query = Usuario.objects.get(pk=q["id"])
    contexto = {"data": query}
    return render(request, "tienda/usuarios/usu-form.html", contexto)


def usuarios_guardar(request):
    if request.method == "POST":
        id = request.POST.get("id")
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        nick = request.POST.get("nick")
        password = request.POST.get("password")
        rol = request.POST.get("rol")

        if id == "":
            # crear
            try:
                pro = Usuario(
                    nombre=nombre,
                    apellido=apellido,
                    nick=nick,
                    password=password,
                    rol=rol
                )
                pro.save()
                messages.success(request, "Guardado correctamente!!")
            except Exception as e:
                messages.error(request, f"Error. {e}")
        else:
            # actualizar
            try:
                q = Usuario.objects.get(pk=id)
                q.nombre = nombre
                q.apellido = apellido
                q.nick = nick
                q.password = password
                q.rol = rol
                q.save()
                messages.success(request, "Actualizado correctamente!!")
            except Exception as e:
                messages.error(request, f"Error. {e}")

        return HttpResponseRedirect(reverse("tienda:usuarios", args=()))

    else:
        messages.warning(request, "No se enviarion datos...")
        return HttpResponseRedirect(reverse("tienda:usuarios_formulario", args=()))


def usuarios_eliminar(request, id):
    try:
        q = Usuario.objects.get(pk=id)
        q.delete()
        messages.success(request, "Eliminado correctamente!!")
    except Exception as e:
        messages.error(request, f"Error. {e}")
    return HttpResponseRedirect(reverse("tienda:usuarios", args=()))


def citas(request):
    query = Cita.objects.all()
    contexto = {"data": query}
    return render(request, "tienda/citas/citas.html", contexto)


def citas_formulario(request):
    servicio = Servicio.objects.all()  # Obtén la lista de servicios
    usuario = Usuario.objects.filter(rol=3)  # Filtra los usuarios con rol 3 (clientes)

    context = {
        'servicio': servicio,
        'usuario': usuario,
    }

    return render(request, "tienda/citas/cit-form.html", context)


def citas_guardar(request):
    if request.method == "POST":
        id = request.POST.get("id")
        fecha_hora = request.POST.get("fecha_hora")
        servicio = Servicio.objects.get(pk=request.POST.get("servicio"))
        precio = request.POST.get("precio")
        cliente = Usuario.objects.get(pk=request.POST.get("usuario"), rol=3)

        if id == "":
            # crear
            try:
                cit = Cita(
                    fecha_hora=fecha_hora,
                    servicio=servicio,
                    precio=precio,
                    cliente=cliente,
                )
                cit.save()
                messages.success(request, "Guardado correctamente!!")
            except Exception as e:
                messages.error(request, f"Error. {e}")
        else:
            # actualizar
            try:
                q = Cita.objects.get(pk=id)
                q.fecha_hora = fecha_hora
                q.servicio = servicio
                q.precio = precio
                q.cliente = cliente
                q.save()
                messages.success(request, "Actualizado correctamente!!")
            except Exception as e:
                messages.error(request, f"Error. {e}")

        return HttpResponseRedirect(reverse("tienda:citas", args=()))

    else:
        messages.warning(request, "No se enviarion datos...")
        return HttpResponseRedirect(reverse("tienda:citas_formulario", args=()))


def citas_eliminar(request, id):
    try:
        q = Cita.objects.get(pk=id)
        q.delete()
        messages.success(request, "Eliminado correctamente!!")
    except Exception as e:
        messages.error(request, f"Error. {e}")
    return HttpResponseRedirect(reverse("tienda:citas", args=()))


def citas_editar(request, id):
    q = Cita.objects.get(pk=id)
    query = Servicio.objects.all()
    query2 = Usuario.objects.all()
    contexto = {"id": id, "data": q, "servicios": query, "clientes": query2}
    return render(request, "tienda/citas/cit-form.html", contexto)


def usuarios_editar(request, id):
    q = Usuario.objects.get(pk=id)
    contexto = {"id": id, "data": q}
    return render(request, "tienda/usuarios/usu-form.html", contexto)


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


def ver_perfil(request):
    usuario = request.session.get("logueo", False)
    q = Usuario.objects.get(pk=usuario["id"])
    contexto = {"data": q}
    return render(request, "tienda/usuarios/perfil.html", contexto)


def carrito_agregar(request):
    if request.method == "POST":
        id_producto = request.POST.get("id")
        cantidad = int(request.POST.get("cantidad"))

        if not request.session.get("carrito", False):
            request.session["carrito"] = []

        carrito = request.session.get("carrito", False)

        encontrado = False
        for p in carrito :
            if p["id"] == id_producto:
                encontrado = True
                # Si existe, incrementamos la cantidad
                p["cantidad"] += cantidad
                messages.success(request, "Producto ya en carrito, se incrementa la cantidad!!")
                break

        if not encontrado:
            # Si no existe, agrego el elemento completo, es decir, el diccionario
            carrito.append({ "id": id_producto,"cantidad": cantidad})
            messages.success(request, "Producto agregado al carrito!!")

        # Sobreescribo la sesión
        request.session["carrito"] = carrito
        print(carrito)
    else:
        messages.warning(request, "No se enviarion datos...")

    return redirect("tienda:catalogo")

def carrito_listar(request):
    carrito = request.session.get("carrito", False)
    if carrito:
        for p in carrito:
            query = Producto.objects.get(pk=p["id"])
            p["nombre"] = query.nombre
            p["precio"] = query.precio
            p["foto"] = query.foto.url

    contexto = {"datos": carrito}
    return render(request, "tienda/catalogo/listar_carrito.html", contexto)