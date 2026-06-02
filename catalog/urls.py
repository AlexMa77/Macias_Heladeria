from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import HeladoViewSet, ClienteViewSet
from .services_views import cobros_view

router = DefaultRouter()
router.register(r"helados", HeladoViewSet,  basename="helados")
router.register(r"clientes", ClienteViewSet, basename="clientes")

urlpatterns = [
    path("heladeria/cobros/", cobros_view),   # POST — FOR
]

urlpatterns += router.urls