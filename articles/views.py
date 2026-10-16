from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Article, ArticlesPageSettings
from .serializers import (
    ArticleListSerializer , 
    ArticleDetailSerializer , 
    ArticlesPageSettingsSerializer ,
)


class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.filter(is_published = True).select_related("category")
    serializer_class = ArticleListSerializer


class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.filter(is_published = True).select_related("category")
    serializer_class = ArticleDetailSerializer
    lookup_field = "slug"


class ArticlesPageSettingsView(APIView):
    def get(self , request):
        obj = ArticlesPageSettings.objects.first()
        if obj is None:
            return Response({"detail": "تنظیمات صفحه مقالات هنوز وارد نشده است."},
                            status=status.HTTP_404_NOT_FOUND)
        return Response(ArticlesPageSettingsSerializer(obj).data)