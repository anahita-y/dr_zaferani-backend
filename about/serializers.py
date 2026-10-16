from rest_framework import serializers
from .models import AboutPage , AboutSpecialty , AboutStat


class AboutSpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSpecialty
        fields = ["id" , "title" , "icon" , "order"]


class AboutStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutStat
        fields = ["id" , "value" , "label" , "icon" , "order"]


class AboutPageSerializer(serializers.ModelSerializer):
    specialties = AboutSpecialtySerializer(many = True , read_only = True)
    stats = AboutStatSerializer(many = True , read_only = True)

    class Meta:
        model = AboutPage
        fields = "__all__"