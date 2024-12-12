import os
import django

# Cambia 'proyectoBD.settings' por el nombre correcto del módulo settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "noesis.settings")

django.setup()

# Importar los modelos después de la configuración de Django
from app_db.models import Producto, Inventario, Empleado, Distribuidor, OrdenDistribuidor, DetalleOrden

# Insertar datos en la tabla Producto
productos = [
    {"nom_pro": "Laptop Dell XPS 13", "des_pro": "Laptop ultraligera con procesador Intel i7", "pre_pro": 1500},
    {"nom_pro": "Monitor Samsung 24", "des_pro": "Monitor de 24 pulgadas Full HD", "pre_pro": 200},
    {"nom_pro": "Teclado Mecánico", "des_pro": "Teclado mecánico con retroiluminación RGB", "pre_pro": 120},
    {"nom_pro": "Mouse Inalámbrico", "des_pro": "Mouse ergonómico inalámbrico", "pre_pro": 30},
]

for prod in productos:
    Producto.objects.create(**prod)

# Insertar datos en la tabla Inventario
inventarios = [
    {"fec_inv": "2022-02-17", "can_inv": 25, "ubi_inv": "Almacén Central", "id_pro_id": 1},
    {"fec_inv": "2023-04-01", "can_inv": 10, "ubi_inv": "Almacén Este", "id_pro_id": 2},
    {"fec_inv": "2023-01-20", "can_inv": 15, "ubi_inv": "Almacén Oeste", "id_pro_id": 1},
    {"fec_inv": "2022-02-17", "can_inv": 25, "ubi_inv": "Almacén Central", "id_pro_id": 3},
    {"fec_inv": "2021-12-06", "can_inv": 30, "ubi_inv": "Almacén Este", "id_pro_id": 4},
]

for inv in inventarios:
    Inventario.objects.create(**inv)

# Insertar datos en la tabla Empleado
empleados = [
    {"nomb_emp": "Juan", "pue_emp": "Gerente", "fec_emp": "2020-04-12"},
    {"nomb_emp": "Laura", "pue_emp": "Jefe de operaciones", "fec_emp": "2019-10-05"},
    {"nomb_emp": "Alberto", "pue_emp": "Vendedor", "fec_emp": "2021-11-24"},
    {"nomb_emp": "Mariana", "pue_emp": "Encargada de inventarios", "fec_emp": "2020-04-12"},
    {"nomb_emp": "Adrian", "pue_emp": "Vendedor", "fec_emp": "2018-03-01"},
]

for emp in empleados:
    Empleado.objects.create(**emp)

# Insertar datos en la tabla Distribuidor
distribuidores = [
    {"nom_dis": "Apple", "tel_dis": "555888222", "dir_dis": "One Apple Park Way, Cupertino, California"},
    {"nom_dis": "Samsung", "tel_dis": "555321242", "dir_dis": "Alcobendas, Madrid"},
    {"nom_dis": "Dell", "tel_dis": "555689123", "dir_dis": "Round Rock, Texas"},
    {"nom_dis": "Logitech", "tel_dis": "555987547", "dir_dis": "Santa Fe, México D.F"},
]

for dist in distribuidores:
    Distribuidor.objects.create(**dist)

# Insertar datos en la tabla OrdenDistribuidor
ordenes = [
    {"fec_ord": "2024-09-17", "est_ord": "En espera", "id_dis_id": 2, "id_emp_id": 4},
    {"fec_ord": "2022-02-06", "est_ord": "Entregado", "id_dis_id": 3, "id_emp_id": 1},
    {"fec_ord": "2024-12-10", "est_ord": "Entregado", "id_dis_id": 4, "id_emp_id": 4},
    {"fec_ord": "2018-01-10", "est_ord": "Entregado", "id_dis_id": 1, "id_emp_id": 2},
]

for ord in ordenes:
    OrdenDistribuidor.objects.create(**ord)

# Insertar datos en la tabla DetalleOrden
detalles = [
    {"id_ord_id": 1, "id_pro_id": 1, "can_pro": 20, "pre_uni": 1000},
    {"id_ord_id": 1, "id_pro_id": 2, "can_pro": 30, "pre_uni": 100},
    {"id_ord_id": 2, "id_pro_id": 3, "can_pro": 15, "pre_uni": 60},
    {"id_ord_id": 2, "id_pro_id": 4, "can_pro": 17, "pre_uni": 15},
    {"id_ord_id": 3, "id_pro_id": 1, "can_pro": 14, "pre_uni": 1000},
    {"id_ord_id": 3, "id_pro_id": 3, "can_pro": 7, "pre_uni": 60},
    {"id_ord_id": 4, "id_pro_id": 2, "can_pro": 40, "pre_uni": 100},
    {"id_ord_id": 4, "id_pro_id": 4, "can_pro": 36, "pre_uni": 15},
]

for det in detalles:
    DetalleOrden.objects.create(**det)

print("Datos insertados correctamente.")
