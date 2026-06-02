from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Helado, Cliente
from .serializers import HeladoSerializer, ClienteSerializer
from .permissions import IsAdminOrReadOnly

class HeladoViewSet(viewsets.ModelViewSet):
    queryset           = Helado.objects.all().order_by("id")
    serializer_class   = HeladoSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields      = ["nombre"]
    ordering_fields    = ["id", "nombre", "precio"]

class ClienteViewSet(viewsets.ModelViewSet):
    queryset           = Cliente.objects.select_related("helado").all().order_by("nombre")
    serializer_class   = ClienteSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields   = ["helado", "activo"]
    search_fields      = ["nombre", "cedula"]
    ordering_fields    = ["id", "nombre", "creado_en"]

    def get_permissions(self):
        # GET /api/clientes/ es público sin token
        if self.action == "list":
            return [AllowAny()]
        return super().get_permissions()