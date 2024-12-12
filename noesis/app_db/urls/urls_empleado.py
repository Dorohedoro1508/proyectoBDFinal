from django.urls import path
from app_db.views import empleado_views # type: ignore

urlpatterns = [
    # Producto
    path('productos/', empleado_views.producto_list, name='empleado_producto_list'),
    path('productos/new/', empleado_views.producto_create, name='empleado_producto_create'),
    path('productos/<int:pk>/edit/', empleado_views.producto_update, name='empleado_producto_update'),
    path('productos/<int:pk>/delete/', empleado_views.producto_delete, name='empleado_producto_delete'),

    # Inventario
    path('inventarios/', empleado_views.inventario_list, name='empleado_inventario_list'),
    path('inventarios/new/', empleado_views.inventario_create, name='empleado_inventario_create'),
    path('inventarios/<int:pk>/edit/', empleado_views.inventario_update, name='empleado_inventario_update'),
    path('inventarios/<int:pk>/delete/', empleado_views.inventario_delete, name='empleado_inventario_delete'),

    # OrdenDistribuidor
    path('ordenes/', empleado_views.ordendistribuidor_list, name='empleado_ordendistribuidor_list'),
    path('ordenes/new/', empleado_views.ordendistribuidor_create, name='empleado_ordendistribuidor_create'),
    path('ordenes/<int:pk>/edit/', empleado_views.ordendistribuidor_update, name='empleado_ordendistribuidor_update'),
    path('ordenes/<int:pk>/delete/', empleado_views.ordendistribuidor_delete, name='empleado_ordendistribuidor_delete'),

    # DetalleOrden
    path('detalles/', empleado_views.detalleorden_list, name='empleado_detalleorden_list'),
    path('detalles/new/', empleado_views.detalleorden_create, name='empleado_detalleorden_create'),
    path('detalles/<int:pk>/edit/', empleado_views.detalleorden_update, name='empleado_detalleorden_update'),
    path('detalles/<int:pk>/delete/', empleado_views.detalleorden_delete, name='empleado_detalleorden_delete'),

    # Dashboard
    path('dashboard/', empleado_views.empleado_dashboard, name='empleado_dashboard'),
]
