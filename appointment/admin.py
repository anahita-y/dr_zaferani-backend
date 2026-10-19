from django.contrib import admin
from core.admin import SingletonAdmin
from .models import AppointmentPageSettings , AppointmentMethod

@admin.register(AppointmentPageSettings)
class AppointmentMethodAdmin(SingletonAdmin):
    pass


@admin.register(AppointmentMethod)
class AppointmentMethodAdmin(admin.ModelAdmin):
    list_display = ("title", "icon", "link", "order", "is_active")
    list_editable = ("order", "is_active")