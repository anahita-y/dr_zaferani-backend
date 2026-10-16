from django.contrib import admin
from core.admin import SingletonAdmin
from .models import FAQSettings, FAQ


@admin.register(FAQSettings)
class FAQSettingsAdmin(SingletonAdmin):
    pass


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question" , "is_important" , "order" , "is_active")
    list_editable = ("is_important" , "order" , "is_active")
    list_filter = ("is_important" , "is_active")
    search_fields = ("question" , "answer")