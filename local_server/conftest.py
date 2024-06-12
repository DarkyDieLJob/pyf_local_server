import pytest
from ddf import G
from inventario.models import Articulo


@pytest.fixture
def articulo():
    return G(Articulo)

'''
@pytest.fixture
def marca():
    return G(Marca)

@pytest.fixture
def categoria():
    return G(Categoria)

@pytest.fixture
def cartel():
    return G(Cartel)

@pytest.fixture
def proveedor():
    return G(Proveedor)

@pytest.fixture
def articulo(marca, categoria):
    return G(
        Articulo,
        marca=marca, 
        categoria=categoria,
    )

@pytest.fixture
def codigo_barras(articulo):
    return G(
        CodigoBarras,
        articulo = articulo,
    )
    
@pytest.fixture
def articulo_proveedor(articulo, proveedor, cartel):
    return G(ArticuloProveedor,
        articulo=articulo,
        proveedor=proveedor,
        cartel=cartel,
    )
    '''