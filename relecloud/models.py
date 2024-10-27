from django.db import models

# Create your models here.

class Destination(models.Model):
    name = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50
    )
    descrition = models.TextField(
        max_length=2000,
        null=False,
        blank=False
    )

class TipoCrucero(models.Model):
    name = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50
    )
    description = models.TextField(
        max_length=2000,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.name


class Crucero(models.Model):
    tipo_crucero = models.ForeignKey(TipoCrucero, on_delete=models.CASCADE)
    duracion_dias = models.PositiveIntegerField(
        null=False,
        blank=False
    )
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False
    )
    fecha_salida = models.DateField(
        null=False,
        blank=False
    )

    def __str__(self):
        return f'{self.tipo_crucero.name} - {self.duracion_dias} días - ${self.precio}'
