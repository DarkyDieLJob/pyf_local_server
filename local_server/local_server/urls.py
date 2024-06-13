from django.contrib import admin
from django.urls import path, include  # Asegúrate de importar include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("reactpy/", include("reactpy_django.http.urls")),
    path('inventario/', include('inventario.urls')),
]
