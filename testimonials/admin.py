from django.contrib import admin
from core.admin import SingletonAdmin
from .models import TestimonialsSettings , ReviewSubject , Testimonial
from core.utils import to_jalali

@admin.register(TestimonialsSettings)
class TestimonialsSettingsAdmin(SingletonAdmin):
    pass


@admin.register(ReviewSubject)
class ReviewSubjectAdmin(admin.ModelAdmin):
    list_display = ("title" , "order" , "is_active")
    list_editable = ("order" , "is_active")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    
    list_display = ("name" , "subject" , "rating" , "is_verified" , "is_published" , "jalali_date")
    list_editable = ("is_verified" , "is_published")
    list_filter = ("is_published" , "is_verified" , "rating" , "subject")
    search_fields = ("name" , "text")
    actions = ["publish_selected" , "unpublish_selected"]
    @admin.display(description = "تاریخ (شمسی)", ordering = "date")
    def jalali_date(self, obj):
        return to_jalali(obj.date)
    
    @admin.action(description = "انتشار نظرهای انتخاب‌شده")
    def publish_selected(self, request, queryset):
        queryset.update(is_published = True)

    @admin.action(description = "مخفی کردن نظرهای انتخاب‌شده")
    def unpublish_selected(self, request, queryset):
        queryset.update(is_published=False)