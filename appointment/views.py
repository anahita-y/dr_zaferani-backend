from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AppointmentPageSettings , AppointmentMethod
from .serializers import AppointmentPageSettingsSerializer , AppointmentMethodSerializer

class AppointmentView(APIView):
    def get(self , request):
        cfg = AppointmentPageSettings.objects.first()
        methods = AppointmentMethod.objects.filter(is_active = True)
        return Response({
            "settings" : AppointmentPageSettingsSerializer(cfg).data if cfg else None ,
            "methods" : AppointmentMethodSerializer(methods , many = True).data ,
        })