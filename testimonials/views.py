from rest_framework import status
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.views import APIView
from .emails import send_new_testimonial_email
from .models import TestimonialsSettings , ReviewSubject , Testimonial
from .serializers import (
    TestimonialsSettingsSerializer , 
    ReviewSubjectSerializer ,
    TestimonialSerializer , 
    TestimonialCreateSerializer ,
)


class TestimonialRateThrottle(AnonRateThrottle):
    scope = "testimonial"


class TestimonialView(APIView):
    def get_throttles(self):
        if self.request.method == "POST":
            return [TestimonialRateThrottle()]
        return []

    def get(self , request):
        cfg = TestimonialsSettings.objects.first()
        testimonials = Testimonial.objects.filter(is_published = True).select_related("subject")
        total = testimonials.count()

        limit = request.query_params.get("limit")
        if limit and limit.isdigit():
            testimonials = testimonials[: int(limit)]

        return Response({
            "settings": TestimonialsSettingsSerializer(cfg).data if cfg else None ,
            "total": total ,
            "testimonials": TestimonialSerializer(testimonials , many = True).data ,
            "subjects": ReviewSubjectSerializer(ReviewSubject.objects.filter(is_active = True) , many = True).data ,
        })

    def post(self, request):
        serializer = TestimonialCreateSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        cfg = TestimonialsSettings.objects.first()
        auto_publish = bool(cfg and cfg.auto_publish)
        testimonial = serializer.save(is_published = auto_publish , is_verified = False)
        send_new_testimonial_email(testimonial , cfg)

        message = ("نظر شما ثبت شد. سپاسگزاریم!" if auto_publish
                   else "نظر شما ثبت شد و پس از تأیید در سایت نمایش داده می‌شود.")
        return Response({"detail": message} , status = status.HTTP_201_CREATED)