from django.db import models

class Sucursal(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} - {self.ciudad}"

    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    puesto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    foto_perfil = models.ImageField(upload_to='img_empleados/', blank=True, null=True)
    id_sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='empleados')

    def __str__(self):
        return f"{self.nombre} - {self.puesto}"

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"