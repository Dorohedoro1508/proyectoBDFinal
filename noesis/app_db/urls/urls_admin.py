from django.urls import path
from app_db.views import admin_views # type: ignore

urlpatterns = [
    # Producto
    path('productos/', admin_views.producto_list, name='admin_producto_list'),
    path('productos/new/', admin_views.producto_create, name='admin_producto_create'),
    path('productos/<int:pk>/edit/', admin_views.producto_update, name='admin_producto_update'),
    path('productos/<int:pk>/delete/', admin_views.producto_delete, name='admin_producto_delete'),
    
    # Inventario
    path('inventarios/', admin_views.inventario_list, name='admin_inventario_list'),
    path('inventarios/new/', admin_views.inventario_create, name='admin_inventario_create'),
    path('inventarios/<int:pk>/edit/', admin_views.inventario_update, name='admin_inventario_update'),
    path('inventarios/<int:pk>/delete/', admin_views.inventario_delete, name='admin_inventario_delete'),

    # Empleado
    path('empleados/', admin_views.empleado_list, name='admin_empleado_list'),
    path('empleados/new/', admin_views.empleado_create, name='admin_empleado_create'),
    path('empleados/<int:pk>/edit/', admin_views.empleado_update, name='admin_empleado_update'),
    path('empleados/<int:pk>/delete/', admin_views.empleado_delete, name='admin_empleado_delete'),

    # Distribuidor
    path('distribuidores/', admin_views.distribuidor_list, name='admin_distribuidor_list'),
    path('distribuidores/new/', admin_views.distribuidor_create, name='admin_distribuidor_create'),
    path('distribuidores/<int:pk>/edit/', admin_views.distribuidor_update, name='admin_distribuidor_update'),
    path('distribuidores/<int:pk>/delete/', admin_views.distribuidor_delete, name='admin_distribuidor_delete'),

    # OrdenDistribuidor
    path('ordenes/', admin_views.ordendistribuidor_list, name='admin_ordendistribuidor_list'),
    path('ordenes/new/', admin_views.ordendistribuidor_create, name='admin_ordendistribuidor_create'),
    path('ordenes/<int:pk>/edit/', admin_views.ordendistribuidor_update, name='admin_ordendistribuidor_update'),
    path('ordenes/<int:pk>/delete/', admin_views.ordendistribuidor_delete, name='admin_ordendistribuidor_delete'),

    # DetalleOrden
    path('detalles/', admin_views.detalleorden_list, name='admin_detalleorden_list'),
    path('detalles/new/', admin_views.detalleorden_create, name='admin_detalleorden_create'),
    path('detalles/<int:pk>/edit/', admin_views.detalleorden_update, name='admin_detalleorden_update'),
    path('detalles/<int:pk>/delete/', admin_views.detalleorden_delete, name='admin_detalleorden_delete'),

    # Dashboard
    path('dashboard/', admin_views.admin_dashboard, name='admin_dashboard'),

    # Respaldos
    path('respaldos/descargar/', admin_views.descargar_respaldo, name='descargar_respaldo'),
    path('respaldos/subir/', admin_views.subir_respaldo, name='subir_respaldo'),

]
