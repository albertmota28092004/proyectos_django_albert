from django.urls import path

from . import views

app_name = "tienda"

urlpatterns = [
    path("", views.index, name="index"),
    path("index2/", views.index2, name="index2"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("agendarcita/", views.agendarcita, name="agendarcita"),
    path("inicioAdmin/", views.inicioAdmin, name="inicioAdmin"),
    path("productos/", views.productos, name="productos"),
    path("productos_formulario/", views.productos_formulario, name="productos_formulario"),
    path("productos_guardar/", views.productos_guardar, name="productos_guardar"),
    path("productos_editar/<int:id>/", views.productos_editar, name="productos_editar"),
    path("productos_eliminar/<int:id>/", views.productos_eliminar, name="productos_eliminar"),
    path("servicios/", views.servicios, name="servicios"),
    path("servicios_formulario/", views.servicios_formulario, name="servicios_formulario"),
    path("servicios_guardar/", views.servicios_guardar, name="servicios_guardar"),
    path("servicios_editar/<int:id>/", views.servicios_editar, name="servicios_editar"),
    path("servicios_eliminar/<int:id>/", views.servicios_eliminar, name="servicios_eliminar"),
    path("pedidos/", views.pedidos, name="pedidos"),
    path("pedidos_formulario/", views.pedidos_formulario, name="pedidos_formulario"),
    path("pedidos_guardar/", views.pedidos_guardar, name="pedidos_guardar"),
    path("pedidos_editar/<int:id>/", views.pedidos_editar, name="pedidos_editar"),
    path("pedidos_eliminar/<int:id>/", views.pedidos_eliminar, name="pedidos_eliminar"),
    path("usuarios/", views.usuarios, name="usuarios"),
    path("usuarios_formulario/", views.usuarios_formulario, name="usuarios_formulario"),
    path("usuarios_guardar/", views.usuarios_guardar, name="usuarios_guardar"),
    path("usuarios_editar/<int:id>/", views.usuarios_editar, name="usuarios_editar"),
    path("usuarios_eliminar/<int:id>/", views.usuarios_eliminar, name="usuarios_eliminar"),
    path("vacunas/", views.vacunas, name="vacunas"),
    path("estetica/", views.estetica, name="estetica"),
    path("servicios/", views.servicios, name="servicios"),
    path("vacunacion/", views.vacunacion, name="vacunacion"),
    path("historia/", views.historia, name="historia"),
    path("nuestroequipo/", views.nuestroequipo, name="nuestroequipo"),
    path("patrocinios/", views.patrocinios, name="patrocinios"),
    path("contactanos/", views.contactanos, name="contactanos"),
]
