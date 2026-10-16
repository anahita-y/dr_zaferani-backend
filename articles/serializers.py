from rest_framework import serializers
from .models import Article , ArticleBlock , ArticleSource , ArticlesPageSettings


class ArticleBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleBlock
        fields = ["type" , "text" , "items"]

    def to_representation(self , instance):
        if instance.type == ArticleBlock.BlockType.LIST:
            items = [line.strip() for line in instance.items.splitlines() if line.strip()]
            return {"type": "list" , "items": items}
        return {"type": instance.type , "text": instance.text}


class ArticleSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleSource
        fields = ["title" , "url"]


class ArticleListSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    date = serializers.DateField(source = "published_at")
    readTime = serializers.CharField(source = "read_time")
    featured = serializers.BooleanField(source = "is_featured")
    image = serializers.ImageField(source = "cover_image")

    class Meta:
        model = Article
        fields = ["id" , "slug" , "title" , "excerpt" , "category" , "date" , "readTime" , "featured" , "image"]

    def get_category(self, obj):
        return obj.category.name if obj.category else ""


class ArticleDetailSerializer(ArticleListSerializer):
    content = ArticleBlockSerializer(source = "blocks" , many = True , read_only = True)
    sources = ArticleSourceSerializer(many = True , read_only = True)

    class Meta(ArticleListSerializer.Meta):
        fields = ArticleListSerializer.Meta.fields + ["content" , "sources"]


class ArticlesPageSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticlesPageSettings
        fields = ["title" , "description"]