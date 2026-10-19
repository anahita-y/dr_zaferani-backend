from rest_framework import serializers
from .models import AppointmentPageSettings , AppointmentMethod

class AppointmentPageSettingsSerializer(serializers.ModelSerializer):
    class Meta :
        model = AppointmentPageSettings
        exclude = ["id"]


class AppointmentMethodSerializer(serializers.ModelSerializer):
    lines = serializers.SerializerMethodField()

    class Meta:
        model = AppointmentMethod
        fields = ["id", "icon", "title", "value", "lines", "link"]


    def get_lines(self , obj):
        return [line.strip() for line in obj.value.splitlines() if line.strip()]
    
     