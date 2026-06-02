from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def cobros_view(request):
    sabores = request.data.get("sabores", [])

    if not isinstance(sabores, list) or len(sabores) == 0:
        return Response(
            {"detail": "El campo 'sabores' debe ser una lista no vacía."},
            status=status.HTTP_400_BAD_REQUEST
        )

    total_cobro = 0
    detalle     = []

    for sabor in sabores:
        nombre      = sabor.get("nombre", "")
        cuota       = float(sabor.get("cuota", 0))
        descuento = int(sabor.get("descuento", 0))

        # Determinar porcentaje de recargo según días de atraso
        if descuento > 1 and descuento <= 3:
            descuento_apli = 0
        elif descuento >= 4 and descuento <= 6:
            descuento_apli = 10
        elif descuento >= 7 and descuento <= 10:
            descuento_apli = 15
        else:
            descuento_apli = 20

        recargo     = round(cuota * descuento_apli / 100, 2)
        cobro_helado = round(cuota + recargo, 2)
        total_cobro = round(total_cobro + cobro_helado, 2)

        detalle.append({
            "nombre":      nombre,
            "descuento_apli": descuento_apli,
            "total_cobro": cobro_helado,
        })

    return Response({
        "total_sabores": len(detalle),
        "total_cobro":  total_cobro,
        "detalle":      detalle,
    })