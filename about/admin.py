from django.contrib import admin
from .models import AboutPage , AboutSpecialty , AboutStat


class AboutSpecialtyInline(admin.TabularInline):
    model = AboutSpecialty
    extra = 1


class AboutStatInline(admin.TabularInline):
    model = AboutStat
    extra = 1


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ("doctor_name",)
    inlines = [AboutSpecialtyInline , AboutStatInline]

    fieldsets = (
        ("بخش اصلی" , {"fields": ("badge_text" , "doctor_name" , "doctor_name_en" , "short_bio" , "long_bio" , "doctor_image")}) ,
        ("کارت تجربه (بالا-چپ عکس)" , {"fields": ("experience_badge_value" , "experience_badge_label" , "experience_badge_icon")}) ,
        ("کارت افتخار (پایین-راست عکس)" , {"fields": ("award_title" , "award_subtitle" , "award_icon")}) ,
        ("دکمه رزرو نوبت" , {"fields": ("booking_button_text" , "booking_button_icon" , "booking_button_link")}) ,
    )

    def has_add_permission(self , request):
        return not AboutPage.objects.exists()

    def has_delete_permission(self , request , obj = None):
        return False