from rest_framework import serializers
from .models import Articulo, CodigoBarras

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'  # Esto incluirá todos los campos del modelo

class CodigoBarrasSerializer(serializers.ModelSerializer):
    Articulo = ArticuloSerializer(many=True, read_only=True)
    class Meta:
        model = CodigoBarras
        fields = '__all__'  # Esto incluirá todos los campos del modelo
