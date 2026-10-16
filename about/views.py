from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AboutPage
from .serializers import AboutPageSerializer


class AboutPageView(APIView):
    def get(self , request):
        page = AboutPage.objects.first()
        if page is None:
            return Response({"detail": "محتوای صفحه درباره دکتر هنوز وارد نشده است."} ,
                            status = status.HTTP_404_NOT_FOUND)
        return Response(AboutPageSerializer(page , context = {"request": request}).data)