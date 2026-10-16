from rest_framework import serializers
from .models import TestimonialsSettings , ReviewSubject , Testimonial


class TestimonialsSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestimonialsSettings
        exclude = ["id" , "notify_email" , "auto_publish"]


class ReviewSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewSubject
        fields = ["id" , "title"]


class TestimonialSerializer(serializers.ModelSerializer):
    subject = serializers.SerializerMethodField()

    class Meta:
        model = Testimonial
        fields = ["id" , "name" , "subject" , "rating" , "text" , "is_verified" , "date"]

    def get_subject(self , obj):
        return obj.subject.title if obj.subject else ""


class TestimonialCreateSerializer(serializers.ModelSerializer):
    subject = serializers.PrimaryKeyRelatedField(
        queryset = ReviewSubject.objects.filter(is_active = True) ,
        required = False , 
        allow_null=True ,
    )

    class Meta:
        model = Testimonial
        fields = ["name" , "subject" , "rating" , "text"]