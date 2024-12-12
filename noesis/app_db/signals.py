from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Producto, Inventario, Empleado, Distribuidor, OrdenDistribuidor, DetalleOrden

@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    # Crear grupos
    admin_group, _ = Group.objects.get_or_create(name="Administrador")
    empleado_group, _ = Group.objects.get_or_create(name="Empleado")
    auditor_group, _ = Group.objects.get_or_create(name="Auditor")

    # Tablas a asignar permisos
    models = [Producto, Inventario, Empleado, Distribuidor, OrdenDistribuidor, DetalleOrden]
    content_types = [ContentType.objects.get_for_model(model) for model in models]

    # Asignar permisos al Administrador
    for ct in content_types:
        admin_group.permissions.add(*Permission.objects.filter(content_type=ct))

    # Asignar permisos al Empleado
    for model in [Producto, Inventario, OrdenDistribuidor, DetalleOrden]:
        ct = ContentType.objects.get_for_model(model)
        empleado_group.permissions.add(*Permission.objects.filter(content_type=ct))

    # Asignar permisos al Auditor (solo select)
    for ct in content_types:
        auditor_group.permissions.add(*Permission.objects.filter(content_type=ct, codename__startswith="view_"))
