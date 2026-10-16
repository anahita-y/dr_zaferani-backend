from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import gallery_payload


class GalleryView(APIView):
    def get(self , request):
        return Response(gallery_payload({"request": request}))