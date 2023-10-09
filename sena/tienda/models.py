from django.db import models


# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=254)
    precio = models.IntegerField()
    fecha_compra = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    nombre = models.CharField(max_length=254)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre


"""class Pedido(models.Model):
    fecha = models.DateField(max_length=254)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.id
"""


class Usuario(models.Model):
    ROLES = (
        (1, 'Administrador'),
        (2, 'Empleado'),
        (3, 'Usuario'),
    )
    foto = models.ImageField(null=True, blank=True, upload_to='fotos', default='fotos/default.png')
    nombre = models.CharField(max_length=254)
    apellido = models.CharField(max_length=254)
    nick = models.CharField(max_length=254)
    password = models.CharField(max_length=254)
    rol = models.IntegerField(choices=ROLES, default=3)

    def __str__(self):
        return self.nick
