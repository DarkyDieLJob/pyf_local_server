from django.db import models

# Create your models here.

class Articulo(models.Model):
    codigo = models.CharField(verbose_name='código', max_length=20)
    descripcion = models.CharField(verbose_name='descripción', max_length=250)
    precio_base = models.FloatField(verbose_name='precio_base', default=0.0)
    iva = models.FloatField(default=1.0)
    constante = models.FloatField(default=1.0)
    ganancia = models.FloatField(default=1.0)
    descuento_efectivo = models.FloatField(default=1.0)
    descuento_cantidad = models.FloatField(default=1.0)
    descuento_oferta = models.FloatField(default=1.0)
    cantidad = models.FloatField(default=1.0)
    stock = models.FloatField(default=1.0)
    
    precio_final = models.FloatField(default=0.0)
    precio_efectivo = models.FloatField(default=0.0)
    precio_cantidad = models.FloatField(default=0.0)
    precio_cantidad_efectivo = models.FloatField(default=0.0)
    
    trabajado = models.BooleanField(default=False)

    def generar_precios(self):
        self.precio_final = self.precio_base * self.iva * self.constante * self.ganancia
        self.precio_efectivo = self.precio_final * self.descuento_efectivo
        self.precio_cantidad = self.precio_final * self.cantidad * self.descuento_cantidad
        self.precio_cantidad_efectivo = self.precio_final * self.cantidad * self.descuento_cantidad * self.descuento_efectivo
        
    def actualizar_precio(self,precio_base):
        self.precio_base = precio_base
        self.generar_precios()
        
    def cargar_stock(self, stock):
        if self.stock < 0:
            self.stock = stock
        else:
            self.stock += stock
            
    def vender(self, cantidad):
        self.trabajado = True
        self.stock -= cantidad
        self.save()
        
    def devolver(self, cantidad):
        self.stock += cantidad
        self.save()
        
class CodigoBarras(models.Model):
    barras = models.IntegerField(default=0)
    Articulo = models.ManyToManyField(Articulo)
    

