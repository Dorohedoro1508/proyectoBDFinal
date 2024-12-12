from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required, login_required, user_passes_test
from app_db.models import Producto, Inventario, Empleado, Distribuidor, OrdenDistribuidor, DetalleOrden # type: ignore


# Vistas para Producto
@permission_required('app_db.view_producto', raise_exception=True)
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'empleado/producto_list.html', {'productos': productos})

@permission_required('app_db.add_producto', raise_exception=True)
def producto_create(request):
    if request.method == "POST":
        nom_pro = request.POST.get("nom_pro")
        des_pro = request.POST.get("des_pro")
        pre_pro = request.POST.get("pre_pro")
        Producto.objects.create(nom_pro=nom_pro, des_pro=des_pro, pre_pro=pre_pro)
        return redirect('empleado_producto_list')
    return render(request, 'empleado/producto_form.html')

@permission_required('app_db.change_producto', raise_exception=True)
def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.nom_pro = request.POST.get("nom_pro")
        producto.des_pro = request.POST.get("des_pro")
        producto.pre_pro = request.POST.get("pre_pro")
        producto.save()
        return redirect('empleado_producto_list')
    return render(request, 'empleado/producto_form.html', {'producto': producto})

@permission_required('app_db.delete_producto', raise_exception=True)
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect('empleado_producto_list')
    return render(request, 'empleado/producto_confirm_delete.html', {'producto': producto})

# Vistas para Inventario
@permission_required('app_db.view_inventario', raise_exception=True)
def inventario_list(request):
    inventarios = Inventario.objects.select_related('id_pro').all()
    return render(request, 'empleado/inventario_list.html', {'inventarios': inventarios})

@permission_required('app_db.add_inventario', raise_exception=True)
def inventario_create(request):
    if request.method == "POST":
        fec_inv = request.POST.get("fec_inv")
        can_inv = request.POST.get("can_inv")
        ubi_inv = request.POST.get("ubi_inv")
        id_pro = request.POST.get("id_pro")
        producto = Producto.objects.get(pk=id_pro)
        Inventario.objects.create(fec_inv=fec_inv, can_inv=can_inv, ubi_inv=ubi_inv, id_pro=producto)
        return redirect('empleado_inventario_list')
    productos = Producto.objects.all()
    return render(request, 'empleado/inventario_form.html', {'productos': productos})

@permission_required('app_db.change_inventario', raise_exception=True)
def inventario_update(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    if request.method == "POST":
        inventario.fec_inv = request.POST.get("fec_inv")
        inventario.can_inv = request.POST.get("can_inv")
        inventario.ubi_inv = request.POST.get("ubi_inv")
        id_pro = request.POST.get("id_pro")
        inventario.id_pro = Producto.objects.get(pk=id_pro)
        inventario.save()
        return redirect('empleado_inventario_list')
    productos = Producto.objects.all()
    return render(request, 'empleado/inventario_form.html', {'inventario': inventario, 'productos': productos})

@permission_required('app_db.delete_inventario', raise_exception=True)
def inventario_delete(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    if request.method == "POST":
        inventario.delete()
        return redirect('empleado_inventario_list')
    return render(request, 'empleado/inventario_confirm_delete.html', {'inventario': inventario})

# Vistas para OrdenDistribuidor
@permission_required('app_db.view_ordendistribuidor', raise_exception=True)
def ordendistribuidor_list(request):
    ordenes = OrdenDistribuidor.objects.select_related('id_dis', 'id_emp').all()
    return render(request, 'empleado/ordendistribuidor_list.html', {'ordenes': ordenes})

@permission_required('app_db.add_ordendistribuidor', raise_exception=True)
def ordendistribuidor_create(request):
    if request.method == "POST":
        fec_ord = request.POST.get("fec_ord")
        est_ord = request.POST.get("est_ord")
        id_dis = request.POST.get("id_dis")
        id_emp = request.POST.get("id_emp")
        distribuidor = Distribuidor.objects.get(pk=id_dis)
        empleado = Empleado.objects.get(pk=id_emp)
        OrdenDistribuidor.objects.create(fec_ord=fec_ord, est_ord=est_ord, id_dis=distribuidor, id_emp=empleado)
        return redirect('empleado_ordendistribuidor_list')
    distribuidores = Distribuidor.objects.all()
    empleados = Empleado.objects.all()
    return render(request, 'empleado/ordendistribuidor_form.html', {'distribuidores': distribuidores, 'empleados': empleados})

@permission_required('app_db.change_ordendistribuidor', raise_exception=True)
def ordendistribuidor_update(request, pk):
    orden = get_object_or_404(OrdenDistribuidor, pk=pk)
    if request.method == "POST":
        orden.fec_ord = request.POST.get("fec_ord")
        orden.est_ord = request.POST.get("est_ord")
        id_dis = request.POST.get("id_dis")
        id_emp = request.POST.get("id_emp")
        orden.id_dis = Distribuidor.objects.get(pk=id_dis)
        orden.id_emp = Empleado.objects.get(pk=id_emp)
        orden.save()
        return redirect('empleado_ordendistribuidor_list')
    distribuidores = Distribuidor.objects.all()
    empleados = Empleado.objects.all()
    return render(request, 'empleado/ordendistribuidor_form.html', {'orden': orden, 'distribuidores': distribuidores, 'empleados': empleados})

@permission_required('app_db.delete_ordendistribuidor', raise_exception=True)
def ordendistribuidor_delete(request, pk):
    orden = get_object_or_404(OrdenDistribuidor, pk=pk)
    if request.method == "POST":
        orden.delete()
        return redirect('empleado_ordendistribuidor_list')
    return render(request, 'empleado/ordendistribuidor_confirm_delete.html', {'orden': orden})

# Vistas para DetalleOrden
@permission_required('app_db.view_detalleorden', raise_exception=True)
def detalleorden_list(request):
    detalles = DetalleOrden.objects.select_related('id_ord', 'id_pro').all()
    return render(request, 'empleado/detalleorden_list.html', {'detalles': detalles})

@permission_required('app_db.add_detalleorden', raise_exception=True)
def detalleorden_create(request):
    if request.method == "POST":
        id_ord = request.POST.get("id_ord")
        id_pro = request.POST.get("id_pro")
        can_pro = request.POST.get("can_pro")
        pre_uni = request.POST.get("pre_uni")
        orden = OrdenDistribuidor.objects.get(pk=id_ord)
        producto = Producto.objects.get(pk=id_pro)
        DetalleOrden.objects.create(id_ord=orden, id_pro=producto, can_pro=can_pro, pre_uni=pre_uni)
        return redirect('empleado_detalleorden_list')
    ordenes = OrdenDistribuidor.objects.all()
    productos = Producto.objects.all()
    return render(request, 'empleado/detalleorden_form.html', {'ordenes': ordenes, 'productos': productos})

@permission_required('app_db.change_detalleorden', raise_exception=True)
def detalleorden_update(request, pk):
    detalle = get_object_or_404(DetalleOrden, pk=pk)
    if request.method == "POST":
        detalle.can_pro = request.POST.get("can_pro")
        detalle.pre_uni = request.POST.get("pre_uni")
        id_ord = request.POST.get("id_ord")
        id_pro = request.POST.get("id_pro")
        detalle.id_ord = OrdenDistribuidor.objects.get(pk=id_ord)
        detalle.id_pro = Producto.objects.get(pk=id_pro)
        detalle.save()
        return redirect('empleado_detalleorden_list')
    ordenes = OrdenDistribuidor.objects.all()
    productos = Producto.objects.all()
    return render(request, 'empleado/detalleorden_form.html', {'detalle': detalle, 'ordenes': ordenes, 'productos': productos})

@permission_required('app_db.delete_detalleorden', raise_exception=True)
def detalleorden_delete(request, pk):
    detalle = get_object_or_404(DetalleOrden, pk=pk)
    if request.method == "POST":
        detalle.delete()
        return redirect('empleado_detalleorden_list')
    return render(request, 'empleado/detalleorden_confirm_delete.html', {'detalle': detalle})

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Empleado').exists())
def empleado_dashboard(request):
    return render(request, 'empleado/dashboard.html')
