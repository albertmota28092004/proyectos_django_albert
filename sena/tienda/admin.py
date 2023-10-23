from django.contrib import admin
from django.utils.html import mark_safe

# Register your models here.

from .models import *


class ProductoAdmin(admin.ModelAdmin):
    fields = ["nombre", "precio", "fecha_compra"]
    list_display = ["id", "nombre", "precio", "fecha_compra"]
    search_fields = ["nombre"]
    list_filter = ["fecha_compra"]



class ServicioAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "descripcion"]
    search_fields = ["nombre", "descripcion"]


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["id", "nick", "foto", "sueldo", "rol", "nombre_completo", "ver_foto", "password"]

    def sueldo(self, obj):
        return f"$ {obj.id * 3}"

    def nombre_completo(self, obj):
        return mark_safe(f"<span style='color:red;'>{obj.nombre}</span> {obj.apellido}")

    def ver_foto(self, obj):
        try:
            return mark_safe(f"<img src='{obj.foto.url}' style='width:20%;'>")
        except Exception as e:
            return f"Error, el archivo fue eliminado."


class PedidoAdmin(admin.ModelAdmin):
    list_display = ["id", "usuario", "fecha", "descripcion", "precio"]


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Pedido, PedidoAdmin)
