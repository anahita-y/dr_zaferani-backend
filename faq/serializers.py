from rest_framework import serializers
from .models import FAQSettings, FAQ


class FAQSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQSettings
        exclude = ["id"]


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ["id" , "question" , "answer"]


def faq_payload(context=None):
    cfg = FAQSettings.objects.first()
    faqs = FAQ.objects.filter(is_active = True , is_important = True)[:FAQ.MAX_IMPORTANT]
    return {
        "settings": FAQSettingsSerializer(cfg).data if cfg else None ,
        "faqs": FAQSerializer(faqs , many=True).data ,
    }