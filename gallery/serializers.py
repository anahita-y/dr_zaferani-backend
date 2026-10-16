from rest_framework import serializers
from .models import GallerySettings, GalleryImage


class GallerySettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GallerySettings
        exclude = ["id"]


class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ["id" , "image" , "alt_text"]


def gallery_payload(context, home_only=False):
    cfg = GallerySettings.objects.first()
    images = GalleryImage.objects.filter(is_active = True)
    if home_only:
        images = images.filter(show_on_home = True)[:GalleryImage.MAX_ON_HOME]
    return {
        "settings": GallerySettingsSerializer(cfg).data if cfg else None ,
        "images": GalleryImageSerializer(images , many = True , context = context).data ,
    }