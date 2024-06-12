from django.urls import path, include
from rest_framework import routers
from .views import ArticuloView, CodigoBarrasView

router = routers.DefaultRouter()
router.register(r'articulos', ArticuloView, 'articulos')
router.register(r'codigos_barras', CodigoBarrasView, 'codigos-barras')
urlpatterns = [
    path('api/v1/', include(router.urls)),
]
