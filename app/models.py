from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Unidad_Organizativa(models.Model):
    nombre=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name="Unidad Organizativa"
        verbose_name_plural="Unidades Organizativas"
class PersonalCualificado(models.Model):
    usuario=models.OneToOneField(User, on_delete=models.CASCADE)
    permiso=models.CharField(max_length=100)
    unidad_organizativa=models.ForeignKey(Unidad_Organizativa, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.username

class Trabajador(models.Model):
    nombre_y_apellidos = models.CharField(max_length=80)
    ci=models.CharField(max_length=11, unique=True)

    def __str__(self):
            return self.nombre_y_apellidos

    class Meta:
        verbose_name = "Trabajador"
        verbose_name_plural = "Trabajadores"


class Provincia(models.Model):
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    nombre=models.CharField(max_length=30)
    provincia=models.ForeignKey(Provincia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name="Municipio"
        verbose_name_plural="Municipios"


class Solicitud(models.Model):
    numero=models.IntegerField()
    solicitante=models.ForeignKey(User, on_delete=models.CASCADE)
    trabajador=models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    unidad_organizativa=models.ForeignKey(Unidad_Organizativa, on_delete=models.CASCADE)
    c_contable=models.CharField(max_length=4)
    provincia=models.ForeignKey(Provincia, on_delete=models.CASCADE)
    origen=models.ForeignKey(Municipio, on_delete=models.CASCADE, related_name='municipio_origen')
    destino=models.ForeignKey(Municipio, on_delete=models.CASCADE, related_name='municipio_destino')
    regreso=models.ForeignKey(Municipio, on_delete=models.CASCADE, related_name='municipio_regreso')
    fecha_inicio=models.DateField()
    fecha_final=models.DateField()
    estado=models.CharField(max_length=20)

    def __str__(self):
        return str(self.numero)

    class Meta:
        verbose_name="Solicitud"
        verbose_name_plural="Solicitudes"
    

