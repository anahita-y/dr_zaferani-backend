from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import faq_payload


class FAQView(APIView):
    def get(self , request):
        return Response(faq_payload())