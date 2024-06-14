from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.response import Response
from .models import Articulo, CodigoBarras
from rest_framework.pagination import PageNumberPagination
from .serializers import ArticuloSerializer, CodigoBarrasSerializer
from django.views.generic import TemplateView

class ArticuloPagination(PageNumberPagination):
    page_size = 50  # Artículos por página

class ArticuloView(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    pagination_class = ArticuloPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['codigo', 'descripcion']
    ordering_fields = ['codigo', 'descripcion']
    
    
class CodigoBarrasPagination(PageNumberPagination):
    page_size = 50  # Códigos de barras por página

class CodigoBarrasView(viewsets.ModelViewSet):
    queryset = CodigoBarras.objects.all()
    serializer_class = CodigoBarrasSerializer
    pagination_class = CodigoBarrasPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['barras']
    ordering_fields = ['barras']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        articulos = instance.Articulo.all()
        serializer = ArticuloSerializer(articulos, many=True)
        return Response(serializer.data)

class MiVista(TemplateView):
    template_name = 'template.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['saludo'] = 'la puta madre!!'
        articulos = Articulo.objects.all()
        serializer = ArticuloSerializer(articulos, many=True)
        datos_limitados = [{campo: dato[campo] for campo in ['codigo','descripcion','precio_base']} for dato in serializer.data]
        context['datos'] = datos_limitados
        
        return context
    
def IndexView(request):
    return render(request, 'template.html')