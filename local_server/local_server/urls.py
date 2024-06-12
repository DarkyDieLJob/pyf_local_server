from django.contrib import admin
from django.urls import path, include  # Asegúrate de importar include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventario/', include('inventario.urls')),  # Aquí agregas las rutas de tu aplicación inventario
]
