from django.db import models
from django.utils.timezone import now

#Tabla Producto
class Producto(models.Model):
    id_pro = models.AutoField(primary_key=True)  # Auto incrementado por defecto
    nom_pro = models.CharField(max_length=20)   # Equivalente a VARCHAR(20)
    des_pro = models.CharField(max_length=50, blank=True, null=True)  # Puede ser nulo
    pre_pro = models.DecimalField(max_digits=10, decimal_places=2)  # Decimal con precisión

    def __str__(self):
        return self.nom_pro

#Tabla Inventario
class Inventario(models.Model):
    id_inv = models.AutoField(primary_key=True)
    fec_inv = models.DateField()  # Fecha
    can_inv = models.IntegerField()  # Entero
    ubi_inv = models.CharField(max_length=100, blank=True, null=True)  # Puede ser nulo
    id_pro = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Llave foránea

    def __str__(self):
        return f"Inventario {self.id_inv} - {self.ubi_inv}"

#Tabla Empleado
class Empleado(models.Model):
    id_emp = models.AutoField(primary_key=True)
    nomb_emp = models.CharField(max_length=50)
    pue_emp = models.CharField(max_length=30)
    fec_emp = models.DateField(blank=True, null=True)  # Puede ser nulo

    def __str__(self):
        return self.nomb_emp

#Tabla Distribuidor
class Distribuidor(models.Model):
    id_dis = models.AutoField(primary_key=True)
    nom_dis = models.CharField(max_length=50)
    tel_dis = models.BigIntegerField(blank=True, null=True)  # Entero largo para teléfonos
    dir_dis = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nom_dis

#Tabla Orden de distribución
class OrdenDistribuidor(models.Model):
    id_ord = models.AutoField(primary_key=True)
    fec_ord = models.DateField(blank=True, null=True)
    est_ord = models.CharField(max_length=20, blank=True, null=True)
    id_dis = models.ForeignKey(Distribuidor, on_delete=models.CASCADE)
    id_emp = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    def __str__(self):
        return f"Orden {self.id_ord} - Estado: {self.est_ord}"

#Tabla Detalle de orden
class DetalleOrden(models.Model):
    id_det = models.AutoField(primary_key=True)
    id_ord = models.ForeignKey(OrdenDistribuidor, on_delete=models.CASCADE)
    id_pro = models.ForeignKey(Producto, on_delete=models.CASCADE)
    can_pro = models.IntegerField()
    pre_uni = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle {self.id_det} - Orden {self.id_ord.id_ord}"
    
class BackupRecord(models.Model):
    nombre_archivo = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(default=now)

    def __str__(self):
        return self.nombre_archivo
