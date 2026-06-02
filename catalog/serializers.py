from rest_framework import serializers
from .models import Helado, Cliente

class HeladoSerializer(serializers.ModelSerializer):
    total_clientes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model  = Helado
        fields = ["id", "nombre", "precio", "activo", "total_clientes"]

    def get_total_clientes(self, obj):
        return obj.clientes.filter(activo=True).count()

class ClienteSerializer(serializers.ModelSerializer):
    helado_nombre = serializers.CharField(source='helado.nombre', read_only=True)

    class Meta:
        model  = Cliente
        fields = ["id", "helado", "helado_nombre", "nombre", "cedula", "dias_atraso", "activo", "creado_en"]