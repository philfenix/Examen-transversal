from distutils.command.upload import upload
from django.db import models

# Create your models here.


# class categoria(models.Model):
#     idCategoria = models.IntegerField(primary_key=True)
#     nombreCategoria = models.CharField(max_length=20)
#     descripcion_Categoria = models.CharField(max_length=20)


class descuento(models.Model):
    idDescuento = models.IntegerField(primary_key=True)
    nombreDescuento = models.CharField(max_length=20)
    cantidadDescuento = models.IntegerField()
    estado = models.BooleanField()


class producto(models.Model):
    idProducto = models.IntegerField(primary_key=True)
    nombreProducto = models.CharField(max_length=20)
    stockProducto = models.IntegerField()
    precioProducto = models.IntegerField()
    imagenProducto = models.ImageField(upload_to= "productos",null = True)
    descuento_aplicado = models.ForeignKey(descuento, null=True, blank=True, on_delete=models.CASCADE )

