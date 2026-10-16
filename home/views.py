from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import HomePage
from .serializers import HomePageSerializer


class HomePageView(APIView):
    def get(self, request):
        page = HomePage.objects.first()
        if page is None:
            return Response(
                {"detail": "محتوای صفحه اصلی هنوز وارد نشده است."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = HomePageSerializer(page, context={"request": request})
        return Response(serializer.data)