from django.urls import path

from . import views

app_name = "tienda"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("inicioAdmin/", views.inicioAdmin, name="inicioAdmin"),
    path("alimento/", views.alimento, name="alimento"),
    path("form/", views.alimento_crear_formulario, name="form"),
    path("editar/<int:id>/", views.alimento_editar_formulario, name="editar"),
    path("eliminar/<int:id>/", views.alimento_eliminar_formulario, name="eliminar"),
    path("alimento_guardar/", views.alimento_guardar, name="alimento_guardar"),
    path("alimento_buscar/", views.alimento_buscar, name="alimento_buscar"),
    path("delimpieza/", views.delimpieza, name="delimpieza"),
    path("vacunas/", views.vacunas, name="vacunas"),
    path("estetica/", views.estetica, name="estetica"),
    path("salud/", views.salud, name="salud"),
    path("vacunacion/", views.vacunacion, name="vacunacion"),
    path("historia/", views.historia, name="historia"),
    path("nuestroequipo/", views.nuestroequipo, name="nuestroequipo"),
    path("patrocinios/", views.patrocinios, name="patrocinios"),
    path("contactanos/", views.contactanos, name="contactanos"),
]
