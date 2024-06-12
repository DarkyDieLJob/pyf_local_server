from django.db import models

# Create your models here.

class Articulo(models.Model):
    codigo = models.CharField(verbose_name='código', max_length=20)
    descripcion = models.CharField(verbose_name='descripción', max_length=250)
    precio_base = models.FloatField(verbose_name='precio_base', default=0.0)
    iva = models.FloatField(default=1.0)
    constante = models.FloatField(default=1.0)
    ganancia = models.FloatField(default=1.0)

    def calcular_precios(self):
        self.precio_final = self.precio_base * self.iva * self.constante * self.ganancia
        self.precio_efectivo = self.precio_final * self.descuento_efectivo