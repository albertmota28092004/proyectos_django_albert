from django.urls import path

from . import views

app_name = "tienda"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("inicioAdmin/", views.inicioAdmin, name="inicioAdmin"),
    path("alimento/", views.alimento, name="alimento"),
    path("form/", views.alimento_crear_formulario, name="form"),
    path("editar/<int:id>/", views.alimento_editar_formulario, name="editar"),
    path("eliminar/<int:id>/", views.alimento_eliminar_formulario, name="eliminar"),
    path("alimento_guardar/", views.alimento_guardar, name="alimento_guardar"),
    path("alimento_buscar/", views.alimento_buscar, name="alimento_buscar"),
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
    path("delimpieza/", views.delimpieza, name="delimpieza"),
    path("vacunas/", views.vacunas, name="vacunas"),
    path("estetica/", views.estetica, name="estetica"),
    path("servicios/", views.servicios, name="servicios"),
    path("vacunacion/", views.vacunacion, name="vacunacion"),
    path("historia/", views.historia, name="historia"),
    path("nuestroequipo/", views.nuestroequipo, name="nuestroequipo"),
    path("patrocinios/", views.patrocinios, name="patrocinios"),
    path("contactanos/", views.contactanos, name="contactanos"),
]
