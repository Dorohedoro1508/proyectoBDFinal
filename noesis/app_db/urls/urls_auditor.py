from django.urls import path
from app_db.views import auditor_views

urlpatterns = [
    # Producto
    path('productos/', auditor_views.producto_list, name='auditor_producto_list'),

    # Inventario
    path('inventarios/', auditor_views.inventario_list, name='auditor_inventario_list'),

    # Empleado
    path('empleados/', auditor_views.empleado_list, name='auditor_empleado_list'),

    # Distribuidor
    path('distribuidores/', auditor_views.distribuidor_list, name='auditor_distribuidor_list'),

    # OrdenDistribuidor
    path('ordenes/', auditor_views.ordendistribuidor_list, name='auditor_ordendistribuidor_list'),

    # DetalleOrden
    path('detalles/', auditor_views.detalleorden_list, name='auditor_detalleorden_list'),

    # Dashboard
    path('dashboard/', auditor_views.auditor_dashboard, name='auditor_dashboard'),
]
