from rest_framework import serializers
from articles.models import Article
from articles.serializers import ArticleListSerializer
from faq.serializers import faq_payload
from gallery.serializers import gallery_payload
from services.models import Service
from services.serializers import ServiceSerializer
from .models import HomePage


class HomePageSerializer(serializers.ModelSerializer):
    services = serializers.SerializerMethodField()
    articles = serializers.SerializerMethodField()
    gallery = serializers.SerializerMethodField()
    faq = serializers.SerializerMethodField()

    class Meta:
        model = HomePage
        fields = "__all__"

    def get_services(self , obj):
        qs = Service.objects.filter(is_activ = True , show_on_home = True)
        return ServiceSerializer(qs , many = True).data

    def get_articles(self , obj):
        qs = Article.objects.filter(is_published = True).select_related("category")
        featured = qs.filter(is_featured = True).first()
        latest = qs.exclude(pk = featured.pk) if featured else qs
        return {
            "featured": ArticleListSerializer(featured, context = self.context).data if featured else None ,
            "latest": ArticleListSerializer(latest[:4], many = True, context = self.context).data ,
        }

    def get_gallery(self, obj):
        return gallery_payload(self.context , home_only = True)

    def get_faq(self , obj):
        return faq_payload(self.context)