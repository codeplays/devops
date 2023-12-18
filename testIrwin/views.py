from rest_framework.views import APIView
from rest_framework.response import Response


class HomeView(APIView):
    """API for health Check"""
    #authentication_classes = [EquipoJWTAuthenticationClass]
    #permission_classes = (IsAuthenticated,)
    def get(self, request):
        return Response("Django blue green", status=200)