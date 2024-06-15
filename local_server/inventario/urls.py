from django.urls import path, include
from rest_framework import routers
from .views import ArticuloView, CodigoBarrasView, MiVista, IndexView

router = routers.DefaultRouter()
router.register(r'articulos', ArticuloView, 'articulos')
router.register(r'codigos_barras', CodigoBarrasView, 'codigos-barras')
urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('', IndexView, name='index'),
    path('listar_articulos/', MiVista.as_view(), name='listar-articulos'),
]
