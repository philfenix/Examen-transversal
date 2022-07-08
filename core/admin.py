from django.contrib import admin

from core.views import catego
from .models import *

# Register your models here.

admin.site.register(producto)
admin.site.register(descuento)
# admin.site.register(categoria)
