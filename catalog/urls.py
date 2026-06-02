from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PlanViewSet, SocioViewSet
from .services_views import cobros_view

router = DefaultRouter()
router.register(r"planes", PlanViewSet,  basename="planes")
router.register(r"clientes", SocioViewSet, basename="clientes")

urlpatterns = [
    path("heladeria/cobros/", cobros_view),   # POST — FOR
]

urlpatterns += router.urls