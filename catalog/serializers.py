from rest_framework import serializers
from .models import Plan, Cliente

class PlanSerializer(serializers.ModelSerializer):
    total_clientes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model  = Plan
        fields = ["id", "nombre", "precio", "activo", "total_clientes"]

    def get_total_clientes(self, obj):
        return obj.clientes.filter(activo=True).count()

class ClienteSerializer(serializers.ModelSerializer):
    plan_nombre = serializers.CharField(source='plan.nombre', read_only=True)

    class Meta:
        model  = Cliente
        fields = ["id", "plan", "plan_nombre", "nombre", "cedula", "dias_atraso", "activo", "creado_en"]