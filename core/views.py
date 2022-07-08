from django.shortcuts import render
from django.shortcuts import redirect,render
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import productoForm, promocionesForm
# Create your views here.

# Otros

def home(request):
    return render(request, 'core/home.html')

# def registro(request):
#     return render(request, 'core/registro.html')

def registro(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="login")
    return render(request, 'core/registro.html', {'form':form})
    

def suscribirse(request):
    return render(request, 'core/suscribirse.html')

def carro(request):
    return render(request, 'core/Carro_de_compras.html')

def mis_compras(request):
    return render(request, 'core/Mis_compras.html')

# Descuentos

def descuentos(request):
    return render(request, 'core/descuentos.html')

def descuentos_crud(request):
    Descuento= descuento.objects.all()
    return render(request, 'core/descuentos_crud.html', {'v_descuentos': Descuento})

def crearDescuento(request):
    datos = {"form":promocionesForm()}
    if request.method == "POST":
        form = promocionesForm(request.POST)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Descuento agregado!."
    return render(request, 'core/crearDescuento.html', datos)

def modificarDescuento(request, id):
    Descuento = descuento.objects.get(idDescuento=id)
    datos = {'form': promocionesForm(instance=Descuento)}
    if request.method == "POST":
        form = promocionesForm(request.POST, instance=Descuento)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Descuento Modificado"
            datos["form"] = form
    return render(request, 'core/modificarDescuento.html', datos)


def eliminarDescuento(request, id):
    Descuento = descuento.objects.get(idDescuento=id)
    Descuento.delete()
    return redirect(to = "descuentos_crud")


# Productos

# def catalogo(request):
#     Producto= producto.objects.filter(stockProducto = 20)
#     return render(request, 'core/catalogo.html', {'contexto': Producto})


def catalogo(request):
    Producto= producto.objects.all()
    return render(request, 'core/catalogo.html', {'contexto': Producto})

def catego(request):
    Producto= producto.objects.all()
    return render(request, 'core/catego.html', {'contexto': Producto})

def productos_crud(request):
    Producto= producto.objects.all()
    return render(request, 'core/productos_crud.html', {'contexto': Producto})

def crearProducto(request):
    datos = {"form":productoForm()}
    if request.method == "POST":
        form = productoForm(request.POST,files=request.FILES)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Producto agregado!."
    return render(request, 'core/crearProducto.html', datos)

def modificarProducto(request, id):
    Productos = producto.objects.get(idProducto=id)
    datos = {'form': productoForm(instance=Productos)}
    if request.method == "POST":
        form = productoForm(request.POST,files=request.FILES, instance=Productos)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Producto Modificado"
            datos["form"] = form
    return render(request, 'core/modificarProducto.html', datos)

def eliminarProducto(request, id):
    Productos = producto.objects.get(idProducto=id)
    Productos.delete()
    return redirect(to = "productos_crud")


# Categoría


# def crearCategoria(request):
#     datos = {"form":productoForm()}
#     if request.method == "POST":
#         form = productoForm(request.POST,files=request.FILES)
#         if form.is_valid:
#             form.save()
#             datos["mensaje"] = "Producto agregado!."
#     return render(request, 'core/crearProducto.html', datos)

# def modificarCategoria(request, id):
#     Categoria = categoria.objects.get(idCategoria=id)
#     datos = {'form': categoriaForm(instance=Categoria)}
#     if request.method == "POST":
#         form = categoriaForm(request.POST,files=request.FILES, instance=Categoria)
#         if form.is_valid:
#             form.save()
#             datos["mensaje"] = "Categoria Modificada"
#             datos["form"] = form
#     return render(request, 'core/modificarProducto.html', datos)

# def eliminarProducto(request, id):
#     Productos = producto.objects.get(idProducto=id)
#     Productos.delete()
#     return redirect(to = "productos_crud")


