from django.contrib import admin
from django.utils.html import format_html
from core.admin import SingletonAdmin
from .models import GallerySettings, GalleryImage


@admin.register(GallerySettings)
class GallerySettingsAdmin(SingletonAdmin):
    pass
@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("preview" , "alt_text" , "show_on_home" , "order" , "is_active")
    list_editable = ("show_on_home" , "order" , "is_active")
    list_filter = ("show_on_home" , "is_active")

    @admin.display(description = "پیش‌نمایش")
    def preview(self , obj):
        if not obj.image:
            return "-"
        return format_html('<img src="{}" style="height:50px;border-radius:6px">' , obj.image.url)