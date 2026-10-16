from rest_framework import serializers
from .models import ContactInfo, SocialLink, FooterLink


class ContactInfoSerializer(serializers.ModelSerializer):
    latitude = serializers.FloatField(allow_null = True)
    longitude = serializers.FloatField(allow_null = True)
    map_url = serializers.SerializerMethodField()

    class Meta:
        model = ContactInfo
        exclude = ["id"]

    def get_map_url(self, obj):
        if obj.latitude is None or obj.longitude is None:
            return None
        return f"https://www.google.com/maps?q={obj.latitude},{obj.longitude}"


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = ["id" , "title" , "icon" , "url"]


class FooterLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterLink
        fields = ["id" , "title" , "link"]