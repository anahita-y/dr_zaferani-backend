from django.contrib import admin
from .models import HomePage

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ("doctor_name",)
    fieldsets = (
        ("بخش اصلی", {
            "fields": ("doctor_name", "subtitle", "biography", "doctor_image"),
        }),
        ("سابقه‌ی کار", {
            "fields": ("badge_text", "experience_years", "experience_label"),
        }),
        ("دکمه‌ی رزرو نوبت", {
            "fields": ("booking_button_text", "booking_button_icon", "booking_button_link"),
        }),
        ("دکمه‌ی دریافت مشاوره", {
            "fields": ("consult_button_text", "consult_button_icon", "consult_button_link"),
        }),
        ("بخش خدمات", {
            "fields": ("services_badge_text", "services_title", "services_description"),
        }),
        ("دکمه‌ی مشاهده همه خدمات", {
            "fields": ("services_button_text", "services_button_icon", "services_button_link"),
        }),
    )

    def has_add_permission(self, request):
        return not HomePage.objects.exists

    def has_delete_permission(self, request, obj = None):
        return False