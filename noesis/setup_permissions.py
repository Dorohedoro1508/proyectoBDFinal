import os
import django

# Configuración del entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'noesis.settings')
django.setup()

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from app_db.models import Producto, Inventario, Empleado, Distribuidor, OrdenDistribuidor, DetalleOrden

def create_groups_and_permissions():
    # Crear grupos
    admin_group, _ = Group.objects.get_or_create(name='Administrador')
    empleado_group, _ = Group.objects.get_or_create(name='Empleado')
    auditor_group, _ = Group.objects.get_or_create(name='Auditor')

    # Definir modelos y sus permisos
    modelos = [Producto, Inventario, Empleado, Distribuidor, OrdenDistribuidor, DetalleOrden]

    # Asignar permisos al grupo Administrador
    for modelo in modelos:
        content_type = ContentType.objects.get_for_model(modelo)
        permisos = Permission.objects.filter(content_type=content_type)
        admin_group.permissions.set(permisos)

    # Asignar permisos al grupo Empleado
    for modelo in [Producto, Inventario, OrdenDistribuidor, DetalleOrden]:
        content_type = ContentType.objects.get_for_model(modelo)
        permisos = Permission.objects.filter(
            content_type=content_type, codename__in=['add_' + modelo.__name__.lower(), 'change_' + modelo.__name__.lower(), 'view_' + modelo.__name__.lower()]
        )
        empleado_group.permissions.add(*permisos)

    # Asignar permisos al grupo Auditor
    for modelo in modelos:
        content_type = ContentType.objects.get_for_model(modelo)
        permisos = Permission.objects.filter(content_type=content_type, codename='view_' + modelo.__name__.lower())
        auditor_group.permissions.add(*permisos)

    print("Grupos y permisos configurados correctamente.")

if __name__ == "__main__":
    create_groups_and_permissions()
