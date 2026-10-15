from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "icon", "order", "show_on_home", "is_active")
    list_editable = ("order", "show_on_home", "is_active")
    list_filter = ("show_on_home", "is_active")
    list_fields = ("title", "description")
