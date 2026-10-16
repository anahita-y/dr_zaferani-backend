from rest_framework import serializers
from services.models import Service
from services.serializers import ServiceSerializer
from .models import HomePage


class HomePageSerializer(serializers.ModelSerializer):
    
    service = serializers.SerializerMethodField()

    class Meta:
        model = HomePage
        fields = "__all__"

    def get_services(self , obj):
        qs = Service.objects.filter(is_active = True , show_on_home = True)
        return ServiceSerializer(qs , many = True).data