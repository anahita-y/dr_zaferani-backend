from django.contrib import admin
from .models import Category , Article , ArticleBlock , ArticleSource , ArticlesPageSettings


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name" , "slug")
    prepopulated_fields = {"slug": ("name" , )}


class ArticleBlockInline(admin.StackedInline):
    model = ArticleBlock
    extra = 1


class ArticleSourceInline(admin.TabularInline):
    model = ArticleSource
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title" , "category" , "published_at" , "is_featured" , "is_published")
    list_filter = ("category" , "is_featured" , "is_published")
    search_fields = ("title" , "excerpt")
    prepopulated_fields = {"slug": ("title" ,)}
    inlines = [ArticleBlockInline , ArticleSourceInline]


@admin.register(ArticlesPageSettings)
class ArticlesPageSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self , request):
        return not ArticlesPageSettings.objects.exists()

    def has_delete_permission(self, request, obj = None):
        return False