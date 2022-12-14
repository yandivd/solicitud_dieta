from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Unidad_Organizativa(models.Model):
    nombre=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name="Unidad Organizativa"
        verbose_name_plural="Unidades Organizativas"
class Autoriza(models.Model):
    usuario=models.OneToOneField(User, on_delete=models.CASCADE)
    cargo=models.CharField(max_length=150)
    dependencia=models.CharField(max_length=100)

    def __str__(self):
        return self.usuario.first_name+' '+self.usuario.last_name

class Cargo_al_Presupuesto(models.Model):
    cuenta=models.CharField(max_length=20)

    def __str__(self):
        return self.cuenta

class Trabajador(models.Model):
    usuario=models.OneToOneField(User, on_delete=models.CASCADE)
    ci=models.CharField(max_length=11, unique=True)

    def __str__(self):
            return self.usuario.first_name+' '+self.usuario.last_name

    class Meta:
        verbose_name = "Trabajador"
        verbose_name_plural = "Trabajadores"

class PARLEG(models.Model):
    trabajador=models.ForeignKey(Trabajador, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.trabajador.usuario.first_name+' '+self.trabajador.usuario.last_name

class Solicitante(models.Model):
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)
    telf=models.CharField(max_length=100)
    cargo=models.CharField(max_length=100)
    unidad_organizativa=models.ForeignKey(Unidad_Organizativa, on_delete=models.CASCADE)
    def __str__(self):
        return self.usuario.first_name+' '+self.usuario.last_name

class Crea(models.Model):
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)
    unidad_organizativa=models.ForeignKey(Unidad_Organizativa, on_delete=models.CASCADE)
    def __str__(self):
        return self.usuario.username

class C_Contable(models.Model):
    nombre=models.CharField(max_length=4)
    def __str__(self):
        return self.nombre

class Solicitud(models.Model):
    numero=models.IntegerField()
    solicitante=models.ForeignKey(Solicitante, on_delete=models.CASCADE)
    trabajador=models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    unidad_organizativa=models.ForeignKey(Unidad_Organizativa, on_delete=models.CASCADE)
    c_contable=models.ForeignKey(C_Contable, on_delete=models.CASCADE)
    provincia=models.CharField(max_length=50)
    origen=models.CharField(max_length=50)
    prov_destino=models.CharField(max_length=50)
    destino=models.CharField(max_length=50)
    regreso=models.CharField(max_length=50)
    fecha_inicio=models.DateField()
    fecha_final=models.DateField()
    #nuevos models add
    parleg=models.ForeignKey(Trabajador, on_delete=models.CASCADE, related_name='Trabajador_parleg', null=True, blank=True)
    cargo_presupuesto=models.ForeignKey(Cargo_al_Presupuesto, on_delete=models.CASCADE)
    autoriza=models.ForeignKey(Autoriza, on_delete=models.CASCADE)
    estado=models.CharField(max_length=200)
    observaciones=models.CharField(max_length=500, blank=True, null=True)
    labor=models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return str(self.numero)

    class Meta:
        verbose_name="Solicitud"
        verbose_name_plural="Solicitudes"

class Modelo(models.Model):
    nombre=models.CharField(max_length=50)
    solicitante=models.CharField(max_length=50)
    unidad_organizativa=models.CharField(max_length=100)
    c_contable=models.CharField(max_length=4)
    consec=models.IntegerField()
    solicitudes=models.ManyToManyField(Solicitud)
    parleg=models.CharField(max_length=200, blank=True, null=True)
    autoriza=models.CharField(max_length=50)
    cargo_presupuesto=models.CharField(max_length=20)
    observaciones = models.CharField(max_length=500, blank=True, null=True)
    estado=models.CharField(max_length=10)
    #campos nuevos del autoriza y el solicita
    cargo_autoriza=models.CharField(max_length=100)
    dependencia_autoriza=models.CharField(max_length=100)
    cargo_solicita=models.CharField(max_length=100)
    area_trabajo_solicita=models.CharField(max_length=100)
    labor=models.CharField(max_length=500, blank=True, null=True)
    fecha=models.DateField(default=date.today())

    def __str__(self):
        return self.nombre

    

