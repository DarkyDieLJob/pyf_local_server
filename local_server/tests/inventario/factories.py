import factory

from inventario.models import Articulo

class ArticuloFactory(factory.Factory):
    class Meta:
        model = Articulo