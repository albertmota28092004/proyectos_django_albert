from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import *
from django.db.models import Q
from django.db import IntegrityError, transaction


# Create your views here.

def index(request):
    if request.session.get("logueo", False):
        return render(request, "tienda/index.html")
    else:
        return HttpResponseRedirect(reverse("tienda:login"))


def catalogo(request, abrir_off_canva=False):
    if abrir_off_canva == "si":
        print("Sí abrir")
    else:
        print("No abrir")
    if request.session.get("logueo", False):
        c = Categoria.objects.all()

        filtro_categoria = request.GET.get("id")

        if filtro_categoria != None and filtro_categoria != '0':
            p = Producto.objects.filter(categoria_id=filtro_categoria)
            request.session["submenu"] = int(filtro_categoria)
        else:
            p = Producto.objects.all()
            request.session["submenu"] = 0

        contexto = {"categorias": c, "productos": p}
        return render(request, "tienda/catalogo/catalogo.html", contexto)
    else:
        return HttpResponseRedirect(reverse("tienda:login"))


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
            request.session["carrito"] = []
            request.session["cantidad_productos"] = 0
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
    carrito = request.session.get("carrito", False)
    try:
        del request.session["logueo"]
        if carrito:
            del request.session["carrito"]
            del request.session["cantidad_productos"]
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
    categoria = Categoria.objects.all()

    context = {'categoria': categoria}
    return render(request, "tienda/productos/pro-form.html", context)


def productos_guardar(request):
    if request.method == "POST":
        id = request.POST.get("id")
        nombre = request.POST.get("nombre")
        precio = request.POST.get("precio")
        fecha_compra = request.POST.get("fecha_compra")
        categoria = Categoria.objects.get(pk=request.POST.get("categoria"))

        if id == "":
            # crear
            try:
                pro = Producto(
                    nombre=nombre,
                    precio=precio,
                    fecha_compra=fecha_compra,
                    categoria=categoria
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
                q.categoria = categoria
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
    contexto = {"id": id, "data": q, "categoria": query}
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
    usuario = Usuario.objects.filter(rol=3)

    context = {
        'usuario': usuario
    }
    return render(request, "tienda/pedidos/ped-form.html", context)


def pedidos_guardar(request):
    if request.method == "POST":
        id = request.POST.get("id")
        fecha = request.POST.get("fecha")
        descripcion = request.POST.get("descripcion")
        precio = request.POST.get("precio")
        cliente = Usuario.objects.get(pk=request.POST.get("usuario"), rol=3)

        if id == "":
            # crear
            try:
                ped = Pedido(
                    fecha=fecha,
                    descripcion=descripcion,
                    precio=precio,
                    cliente=cliente,
                )
                ped.save()
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
                q.cliente = cliente
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
    contexto = {"id": id, "data": q, "cliente": query}
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

def mis_compras(request):
    ventas = Venta.objects.all()
    detalle_ventas = DetalleVenta.objects.all()
    subtotal_por_venta = []

    for venta in ventas:
        detalles = detalle_ventas.filter(venta=venta)
        subtotal = sum(detalle.cantidad * detalle.precio_historico for detalle in detalles)
        subtotal_por_venta.append(subtotal)

    contexto = {'data': zip(ventas, subtotal_por_venta)}
    return render(request, "tienda/usuarios/mis_compras.html", contexto)



def carrito_agregar(request):
    if request.method == "POST":
        id_producto = request.POST.get("id")
        cantidad = int(request.POST.get("cantidad"))

        if not request.session.get("carrito", False):
            request.session["carrito"] = []
            request.session["cantidad_productos"] = 0

        carrito = request.session.get("carrito", False)

        # Buscar producto para obtener stock
        pro = Producto.objects.get(pk=id_producto)

        encontrado = False
        for p in carrito:
            if p["id"] == id_producto:
                encontrado = True
                # Si existe y no supera el stock, incrementamos la cantidad
                if cantidad > 0 and (p["cantidad"] + cantidad) <= pro.stock:
                    p["cantidad"] += cantidad
                    messages.success(request, "Producto ya en carrito, se incrementa la cantidad!!")
                else:
                    messages.warning(request, "La cantidad supera el stock del producto...")
                break

        if not encontrado:
            # Si no existe, agrego el elemento completo, es decir, el diccionario
            if cantidad <= pro.stock:
                carrito.append({"id": id_producto, "cantidad": cantidad})
                messages.success(request, "Producto agregado al carrito!!")
            else:
                messages.warning(request, "La cantidad supera el stock del producto...")

        # Sobreescribo la sesión
        request.session["carrito"] = carrito
        request.session["cantidad_productos"] = len(request.session["carrito"])
        print(carrito)
    else:
        messages.warning(request, "No se enviarion datos...")

    return redirect("tienda:catalogo", abrir_off_canva="si")


def carrito_actualizar(request):
    if request.method == "GET":
        id_producto = request.GET.get("id")
        cantidad = int(request.GET.get("cantidad"))

        carrito = request.session.get("carrito", False)

        # Buscar producto para obtener stock
        pro = Producto.objects.get(pk=id_producto)

        encontrado = False
        for p in carrito:
            if p["id"] == id_producto:
                encontrado = True
                # Si existe y no supera el stock, incrementamos la cantidad
                if cantidad > 0 and (p["cantidad"] + cantidad) <= pro.stock:
                    p["cantidad"] = cantidad
                break

        # Sobreescribo la sesión
        request.session["carrito"] = carrito
        return HttpResponse("OK")
    else:
        messages.warning("No se enviarion datos...")
        return HttpResponse("Error")


def carrito_listar(request):
    carrito = request.session.get("carrito", False)
    if carrito is not False:
        total = 0
        for indice, p in enumerate(carrito):
            try:
                query = Producto.objects.get(pk=p["id"])
                p["nombre"] = query.nombre
                p["precio"] = query.precio
                p["foto"] = query.foto.url
                p["stock"] = query.stock
                p["subtotal"] = p["cantidad"] * query.precio
                total += p["subtotal"]
            except Producto.DoesNotExist:
                print(f"No existe {p}")
                # Caso especial, se eliminó un producto de la DB, entonces elimino de carrito.
                carrito.pop(indice)
                request.session["carrito"] = carrito

    contexto = {"datos": carrito, "total": total}
    return render(request, "tienda/catalogo/listar_carrito.html", contexto)


def carrito_eliminar_producto(request, id):
    if request.method == "GET":
        carrito = request.session.get("carrito", False)
        if carrito:
            if int(id) == 0:
                carrito.clear()
            else:
                encontrado = False
                cont = 0
                for p in carrito:
                    if int(p["id"]) == id:
                        encontrado = True
                        # Sí existe, lo eliminamos
                        carrito.remove(p)
                        messages.success(request, "Producto eliminado!!")
                        break
                    cont += 1

            request.session["carrito"] = carrito
            request.session["cantidad_productos"] = len(request.session["carrito"])
        else:
            messages.warning(request, "Carrito vacío...")
    else:
        messages.warning(request, "No se enviaron datos...")

    return redirect("tienda:catalogo", abrir_off_canva='si')


@transaction.atomic
def establecer_venta(request):
    # ============= transacción ================
    try:
        # Crear el encabezado de la venta

        logueo = request.session.get("logueo", False)

        user = Usuario.objects.get(pk=logueo["id"])

        query_venta = Venta(usuario=user)
        query_venta.save()

        # Obtener ID inmediatamente
        id_venta = Venta.objects.latest('id')

        # Obtengo el objeto venta a través de su ID
        # v = Venta.objects.get(pk=id_venta)

        # Obtengo el objeto venta a través de su ID
        carrito = request.session.get("carrito", False)
        for p in carrito:
            # Obtengo el objeto producto a través de su ID
            try:
                p_object = Producto.objects.get(pk=p["id"])
            except Producto.DoesNotExist:
                messages.error(request, f"El producto {p} ya no existe")
                raise Exception(f"No se pudo realizar la compra, El producto {p} ya no existe..")

            if p_object.stock >= p["cantidad"]:
                # Asociar los productos del carrito la ID de la venta, previamente creado...
                q = DetalleVenta(
                    venta=id_venta,
                    producto=p_object,
                    cantidad=p["cantidad"],
                    precio_historico=p_object.precio
                )
                q.save()
                # Disminuir stock de productos
                p_object.stock -= p["cantidad"]
                p_object.save()
            else:
                messages.warning(request,
                                 f"El producto {p_object} no cuenta con suficientes unidades. Solo tiene {p_object.stock}")
                raise ValueEerror(
                    f"El producto {p_object} no cuenta con suficientes unidades. Solo tiene {p_object.stock}")

        # Vaciar carrito y redirigir a inicio
        carrito.clear()
        request.session["carrito"] = carrito
        request.session["cantidad_productos"] = 0

        messages.success(request, f"Muchas gracias por su compra << {id_venta} >>!!")

        return redirect("tienda:catalogo", abrir_off_canva='no')

        # ============= fin transacción si todo ok ================
    except Exception as e:
        # **************** si ERROR ***************
        transaction.set_rollback(True)
        # rollback
        messages.error(request, f"Ocurrió un error, intente de nuevo. {e}")
        return redirect("tienda:catalogo", abrir_off_canva='si')
    # ===== fin ====
