from django.forms import ModelForm
from .models import *

class productoForm(ModelForm):
    class Meta:
        model =producto 
        fields = ['idProducto','nombreProducto','stockProducto','precioProducto','imagenProducto','descuento_aplicado']



class promocionesForm(ModelForm):
    class Meta:
        model = descuento
        fields = ['idDescuento','nombreDescuento','cantidadDescuento','estado']


# class categoriaForm(models.Model):
#     class Meta:
#         model = categoria
#         fields = ['idCategoria','nombreCategoria','descripcion_Categoria']


# python manage.py makemigrations
# python manage.py migrate
# python manage.py sqlmigrate core 0001
# python manage.py sqlmigrate core 0002
# python manage.py runserver
