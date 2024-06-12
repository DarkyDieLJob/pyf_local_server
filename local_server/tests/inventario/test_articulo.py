import pytest
from inventario.models import Articulo

from faker import Faker
from tests.inventario.custom_faker_proiders import CuitProvider



fake = Faker()
fake.add_provider(CuitProvider)

@pytest.mark.django_db
def test_articulo_creation(articulo):
    assert isinstance(articulo, Articulo)

'''
@pytest.mark.django_db
def test_marca_creation(marca):
    assert isinstance(marca, Marca)
    
@pytest.mark.django_db
def test_categoria_creation(categoria):
    assert isinstance(categoria, Categoria)

@pytest.mark.django_db
def test_cartel_creation(cartel):
    assert isinstance(cartel, Cartel)
    
@pytest.mark.django_db
def test_proveedor_creation(proveedor):
    assert isinstance(proveedor, Proveedor)
    
@pytest.mark.django_db
def test_articulo_creation(articulo):
    assert isinstance(articulo, Articulo)
    assert isinstance(articulo.marca, Marca)
    assert isinstance(articulo.categoria, Categoria)

@pytest.mark.django_db
def test_codigo_barras_creation(codigo_barras):
    assert isinstance(codigo_barras, CodigoBarras)
    assert isinstance(codigo_barras.articulo, Articulo)

@pytest.mark.django_db
def test_articulo_proveedor_creation(articulo_proveedor, articulo, proveedor, cartel):
    assert isinstance(articulo_proveedor, ArticuloProveedor)
    assert isinstance(articulo, Articulo)
    assert isinstance(proveedor, Proveedor)
    assert isinstance(cartel, Cartel)

@pytest.mark.django_db
def test_articulo_proveedor_creation_fail(articulo, proveedor, cartel):
    with pytest.raises(Exception):
        ArticuloProveedor.objects.create(
        articulo=articulo,
        proveedor=proveedor,
        codigo_base="CB123",
        descripcion="Descripción del artículo",
        precio_base=100.0,
        actualizado=25,
        codigo_final="CF123",
        precio_final=120.0,
        precio_contado=110.0,
        precio_cantidad=90.0,
        precio_cantidad_contado=80.0,
        cartel=cartel,
    )'''