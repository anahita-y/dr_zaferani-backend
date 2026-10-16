from django.contrib import admin
from core.admin import SingletonAdmin
from .models import ContactInfo , SocialLink , FooterLink


@admin.register(ContactInfo)
class ContactInfoAdmin(SingletonAdmin):
    pass


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("title" , "icon" , "url" , "order" , "is_active")
    list_editable = ("order" , "is_active")


@admin.register(FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ("title" , "group" , "link" , "order" , "is_active")
    list_editable = ("order" , "is_active")
    list_filter = ("group" ,)