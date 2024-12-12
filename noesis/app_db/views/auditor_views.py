from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required, user_passes_test
from app_db.models import Producto, Inventario, Empleado, Distribuidor, OrdenDistribuidor, DetalleOrden # type: ignore

# Vistas para Producto
@permission_required('app.view_producto', raise_exception=True)
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'auditor/producto_list.html', {'productos': productos})

# Vistas para Inventario
@permission_required('app.view_inventario', raise_exception=True)
def inventario_list(request):
    inventarios = Inventario.objects.select_related('id_pro').all()
    return render(request, 'auditor/inventario_list.html', {'inventarios': inventarios})

# Vistas para Empleado
@permission_required('app.view_empleado', raise_exception=True)
def empleado_list(request):
    empleados = Empleado.objects.all()
    return render(request, 'auditor/empleado_list.html', {'empleados': empleados})

# Vistas para Distribuidor
@permission_required('app.view_distribuidor', raise_exception=True)
def distribuidor_list(request):
    distribuidores = Distribuidor.objects.all()
    return render(request, 'auditor/distribuidor_list.html', {'distribuidores': distribuidores})

# Vistas para OrdenDistribuidor
@permission_required('app.view_ordendistribuidor', raise_exception=True)
def ordendistribuidor_list(request):
    ordenes = OrdenDistribuidor.objects.select_related('id_dis', 'id_emp').all()
    return render(request, 'auditor/ordendistribuidor_list.html', {'ordenes': ordenes})

# Vistas para DetalleOrden
@permission_required('app.view_detalleorden', raise_exception=True)
def detalleorden_list(request):
    detalles = DetalleOrden.objects.select_related('id_ord', 'id_pro').all()
    return render(request, 'auditor/detalleorden_list.html', {'detalles': detalles})

def auditor_dashboard(request):
    return render(request, 'auditor/dashboard.html')

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Auditor').exists())
def auditor_dashboard(request):
    return render(request, 'auditor/dashboard.html')