from django.contrib import admin
from .models import Producto, Inventario, Empleado, Distribuidor, OrdenDistribuidor, DetalleOrden

# Registra los modelos
admin.site.register(Producto)
admin.site.register(Inventario)
admin.site.register(Empleado)
admin.site.register(Distribuidor)
admin.site.register(OrdenDistribuidor)
admin.site.register(DetalleOrden)
