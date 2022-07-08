from re import template
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('', home,name="home"),
    path('carro', carro,name="carro"),
    path('mis_compras', mis_compras,name="mis_compras"),
    path('suscribirse', suscribirse,name="suscribirse"),
   
 # Descuentos

    path('descuentos', descuentos,name="descuentos"),

    path('descuentos_crud', descuentos_crud,name="descuentos_crud"),
    path('crearDescuento', crearDescuento, name="crearDescuento"),
    path('modificarDescuento/<id>', modificarDescuento, name="modificarDescuento"),
    path('eliminarDescuento/<id>', eliminarDescuento, name="eliminarDescuento"),

 # Productos

    path('catalogo', catalogo,name="catalogo"),
    path('catego', catego,name="catego"),

    path('productos_crud', productos_crud,name="productos_crud"),
    path('crearproducto', crearProducto, name="crearProducto"),
    path('modificarProducto/<id>', modificarProducto, name="modificarProducto"),
    path('eliminarProducto/<id>', eliminarProducto, name="eliminarProducto"),

 # Categoría

   #  path('catalogo', catalogo,name="catalogo"),
   #  path('catego', catego,name="catego"),

   #  path('productos_crud', productos_crud,name="productos_crud"),
   #  path('crearproducto', crearProducto, name="crearProducto"),
   #  path('modificarProducto/<id>', modificarProducto, name="modificarProducto"),
   #  path('eliminarProducto/<id>', eliminarProducto, name="eliminarProducto"),

 # Registro

    path('registro', registro,name="registro"),
    path('login', LoginView.as_view(template_name="core/login.html"), name="login"),
    path('logout', LogoutView.as_view(template_name="core/logout.html"), name="logout"),

]