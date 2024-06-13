from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include  # Asegúrate de importar include
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    re_path(r'^favicon\.ico$', serve, {
        'path': 'favicon.ico',
        'document_root': settings.STATIC_ROOT,
    }),
    path('admin/', admin.site.urls),
    path("reactpy/", include("reactpy_django.http.urls")),
    path('inventario/', include('inventario.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
