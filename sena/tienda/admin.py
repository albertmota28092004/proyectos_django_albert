from django.contrib import admin

# Register your models here.

from .models import Categoria, Producto

class ProductoAdmin(admin.ModelAdmin):
    fields = ["categoria", "nombre", "precio", "fecha_compra"]
    list_display = ["id", "nombre", "categoria", "precio", "fecha_compra"]
    search_fields = ["nombre", "categoria__nombre", "categoria__descripcion"]
    list_filter = ["categoria", "fecha_compra"]

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "descripcion"]
    search_fields = ["nombre", "descripcion"]


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)