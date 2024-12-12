from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required, user_passes_test
from app_db.models import Producto, Inventario, Empleado, Distribuidor, OrdenDistribuidor, DetalleOrden # type: ignore
import os
from django.http import HttpResponse
from django.utils.timezone import now
import shutil
from django.contrib import messages
from django.conf import settings



#Vistas para Producto
@permission_required('app_db.view_producto', raise_exception=True)
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'admin/producto_list.html', {'productos': productos})

@permission_required('app_db.add_producto', raise_exception=True)
def producto_create(request):
    if request.method == "POST":
        nom_pro = request.POST.get("nom_pro")
        des_pro = request.POST.get("des_pro")
        pre_pro = request.POST.get("pre_pro")
        Producto.objects.create(nom_pro=nom_pro, des_pro=des_pro, pre_pro=pre_pro)
        return redirect('admin_producto_list')
    return render(request, 'admin/producto_form.html')

@permission_required('app_db.change_producto', raise_exception=True)
def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.nom_pro = request.POST.get("nom_pro")
        producto.des_pro = request.POST.get("des_pro")
        producto.pre_pro = request.POST.get("pre_pro")
        producto.save()
        return redirect('admin_producto_list')
    return render(request, 'admin/producto_form.html', {'producto': producto})

@permission_required('app_db.delete_producto', raise_exception=True)
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect('admin_producto_list')
    return render(request, 'admin/producto_confirm_delete.html', {'producto': producto})


# Vistas para Inventario
@permission_required('app_db.view_inventario', raise_exception=True)
def inventario_list(request):
    inventarios = Inventario.objects.select_related('id_pro').all()
    return render(request, 'admin/inventario_list.html', {'inventarios': inventarios})

@permission_required('app_db.add_inventario', raise_exception=True)
def inventario_create(request):
    if request.method == "POST":
        fec_inv = request.POST.get("fec_inv")
        can_inv = request.POST.get("can_inv")
        ubi_inv = request.POST.get("ubi_inv")
        id_pro = request.POST.get("id_pro")
        producto = Producto.objects.get(pk=id_pro)
        Inventario.objects.create(fec_inv=fec_inv, can_inv=can_inv, ubi_inv=ubi_inv, id_pro=producto)
        return redirect('admin_inventario_list')
    productos = Producto.objects.all()
    return render(request, 'admin/inventario_form.html', {'productos': productos})

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
        return redirect('admin_inventario_list')
    productos = Producto.objects.all()
    return render(request, 'admin/inventario_form.html', {'inventario': inventario, 'productos': productos})

@permission_required('app_db.delete_inventario', raise_exception=True)
def inventario_delete(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    if request.method == "POST":
        inventario.delete()
        return redirect('admin_inventario_list')
    return render(request, 'admin/inventario_confirm_delete.html', {'inventario': inventario})


# Vistas para Empleado
@permission_required('app_db.view_empleado', raise_exception=True)
def empleado_list(request):
    empleados = Empleado.objects.all()
    return render(request, 'admin/empleado_list.html', {'empleados': empleados})

@permission_required('app_db.add_empleado', raise_exception=True)
def empleado_create(request):
    if request.method == "POST":
        nomb_emp = request.POST.get("nomb_emp")
        pue_emp = request.POST.get("pue_emp")
        fec_emp = request.POST.get("fec_emp")
        Empleado.objects.create(nomb_emp=nomb_emp, pue_emp=pue_emp, fec_emp=fec_emp)
        return redirect('admin_empleado_list')
    return render(request, 'admin/empleado_form.html')

@permission_required('app_db.change_empleado', raise_exception=True)
def empleado_update(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == "POST":
        empleado.nomb_emp = request.POST.get("nomb_emp")
        empleado.pue_emp = request.POST.get("pue_emp")
        empleado.fec_emp = request.POST.get("fec_emp")
        empleado.save()
        return redirect('admin_empleado_list')
    return render(request, 'admin/empleado_form.html', {'empleado': empleado})

@permission_required('app_db.delete_empleado', raise_exception=True)
def empleado_delete(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == "POST":
        empleado.delete()
        return redirect('admin_empleado_list')
    return render(request, 'admin/empleado_confirm_delete.html', {'empleado': empleado})

# Vistas para Distribuidor
@permission_required('app_db.view_distribuidor', raise_exception=True)
def distribuidor_list(request):
    distribuidores = Distribuidor.objects.all()
    return render(request, 'admin/distribuidor_list.html', {'distribuidores': distribuidores})

@permission_required('app_db.add_distribuidor', raise_exception=True)
def distribuidor_create(request):
    if request.method == "POST":
        nom_dis = request.POST.get("nom_dis")
        tel_dis = request.POST.get("tel_dis")
        dir_dis = request.POST.get("dir_dis")
        Distribuidor.objects.create(nom_dis=nom_dis, tel_dis=tel_dis, dir_dis=dir_dis)
        return redirect('admin_distribuidor_list')
    return render(request, 'admin/distribuidor_form.html')

@permission_required('app_db.change_distribuidor', raise_exception=True)
def distribuidor_update(request, pk):
    distribuidor = get_object_or_404(Distribuidor, pk=pk)
    if request.method == "POST":
        distribuidor.nom_dis = request.POST.get("nom_dis")
        distribuidor.tel_dis = request.POST.get("tel_dis")
        distribuidor.dir_dis = request.POST.get("dir_dis")
        distribuidor.save()
        return redirect('admin_distribuidor_list')
    return render(request, 'admin/distribuidor_form.html', {'distribuidor': distribuidor})

@permission_required('app_db.delete_distribuidor', raise_exception=True)
def distribuidor_delete(request, pk):
    distribuidor = get_object_or_404(Distribuidor, pk=pk)
    if request.method == "POST":
        distribuidor.delete()
        return redirect('admin_distribuidor_list')
    return render(request, 'admin/distribuidor_confirm_delete.html', {'distribuidor': distribuidor})

# Vistas para OrdenDistribuidor
@permission_required('app_db.view_ordendistribuidor', raise_exception=True)
def ordendistribuidor_list(request):
    ordenes = OrdenDistribuidor.objects.select_related('id_dis', 'id_emp').all()
    return render(request, 'admin/ordendistribuidor_list.html', {'ordenes': ordenes})

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
        return redirect('admin_ordendistribuidor_list')
    distribuidores = Distribuidor.objects.all()
    empleados = Empleado.objects.all()
    return render(request, 'admin/ordendistribuidor_form.html', {'distribuidores': distribuidores, 'empleados': empleados})

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
        return redirect('admin_ordendistribuidor_list')
    distribuidores = Distribuidor.objects.all()
    empleados = Empleado.objects.all()
    return render(request, 'admin/ordendistribuidor_form.html', {'orden': orden, 'distribuidores': distribuidores, 'empleados': empleados})

@permission_required('app_db.delete_ordendistribuidor', raise_exception=True)
def ordendistribuidor_delete(request, pk):
    orden = get_object_or_404(OrdenDistribuidor, pk=pk)
    if request.method == "POST":
        orden.delete()
        return redirect('admin_ordendistribuidor_list')
    return render(request, 'admin/ordendistribuidor_confirm_delete.html', {'orden': orden})

# Vistas para DetalleOrden
@permission_required('app_db.view_detalleorden', raise_exception=True)
def detalleorden_list(request):
    detalles = DetalleOrden.objects.select_related('id_ord', 'id_pro').all()
    return render(request, 'admin/detalleorden_list.html', {'detalles': detalles})

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
        return redirect('admin_detalleorden_list')
    ordenes = OrdenDistribuidor.objects.all()
    productos = Producto.objects.all()
    return render(request, 'admin/detalleorden_form.html', {'ordenes': ordenes, 'productos': productos})

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
        return redirect('admin_detalleorden_list')
    ordenes = OrdenDistribuidor.objects.all()
    productos = Producto.objects.all()
    return render(request, 'admin/detalleorden_form.html', {'detalle': detalle, 'ordenes': ordenes, 'productos': productos})

@permission_required('app_db.delete_detalleorden', raise_exception=True)
def detalleorden_delete(request, pk):
    detalle = get_object_or_404(DetalleOrden, pk=pk)
    if request.method == "POST":
        detalle.delete()
        return redirect('admin_detalleorden_list')
    return render(request, 'admin/detalleorden_confirm_delete.html', {'detalle': detalle})

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Administrador').exists())
def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')

# Vistas para BackupRecord
# Descargar respaldo
def descargar_respaldo(request):
    # Directorio de respaldos
    backup_dir = os.path.join(settings.BASE_DIR, 'backups')
    os.makedirs(backup_dir, exist_ok=True)

    # Nombre del archivo de respaldo
    timestamp = now().strftime('%Y%m%d_%H%M%S')
    backup_file = os.path.join(backup_dir, f'respaldo_{timestamp}.sqlite3')

    # Ruta de la base de datos desde settings.py
    db_file = settings.DATABASES['default']['NAME']

    if not os.path.exists(db_file):
        return HttpResponse("El archivo de la base de datos no existe.", status=404)

    # Copiar el archivo de la base de datos al respaldo
    with open(db_file, 'rb') as db, open(backup_file, 'wb') as backup:
        backup.write(db.read())

    # Preparar la descarga
    with open(backup_file, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/x-sqlite3')
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(backup_file)}"'
        return response
    
# Subir respaldo
@user_passes_test(lambda u: u.groups.filter(name='Administrador').exists())
def subir_respaldo(request):
    if request.method == 'POST' and 'backup_file' in request.FILES:
        backup_file = request.FILES['backup_file']
        db_file = settings.DATABASES['default']['NAME']  # Ruta actual de la base de datos

        # Validar que el archivo subido tenga el formato correcto
        if not backup_file.name.endswith('.sqlite3'):
            messages.error(request, "El archivo no es un respaldo válido.")
            return redirect('subir_respaldo')

        # Guardar el archivo subido como la base de datos activa
        with open(db_file, 'wb') as destination:
            for chunk in backup_file.chunks():
                destination.write(chunk)

        messages.success(request, "La base de datos se restauró exitosamente.")
        return redirect('admin_dashboard')

    # Renderizar el formulario si no es un método POST
    return render(request, 'admin/subir_respaldo.html')
