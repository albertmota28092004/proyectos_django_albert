from django.db import models


# Create your models here

class Categoria(models.Model):
    nombre = models.CharField(max_length=254)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=254)
    precio = models.IntegerField()
    fecha_compra = models.DateField()
    stock = models.IntegerField(default=1)
    foto = models.ImageField(null=True, blank=True, upload_to='fotos_productos', default='fotos_productos/default.png')
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, default=1)

    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    nombre = models.CharField(max_length=254)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre


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
    email = models.EmailField(max_length=254, unique=True)
    rol = models.IntegerField(choices=ROLES, default=3)

    def __str__(self):
        return self.nick


class Pedido(models.Model):
    fecha = models.DateField()
    descripcion = models.TextField(null=True, blank=True)
    precio = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.usuario


class Cita(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_hora = models.DateTimeField(max_length=254)
    servicio = models.ForeignKey(Servicio, on_delete=models.DO_NOTHING)
    precio = models.IntegerField()
    cliente = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.usuario} - {self.servicio}'

class Venta(models.Model):
    fecha_venta = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    ESTADOS = (
        (1, 'Pendiente'),
        (2, 'Enviado'),
        (3, 'Rechazado'),
    )
    estado = models.IntegerField(choices=ESTADOS, default=1)

    def __str__(self):
        return f'{self.id}'

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.DO_NOTHING)
    producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING)
    cantidad = models.IntegerField()
    precio_historico = models.IntegerField()

    def __str__(self):
        return f'{self.id} -{self.venta}'

