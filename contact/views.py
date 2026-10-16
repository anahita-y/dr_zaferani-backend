from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ContactInfo , SocialLink , FooterLink
from .serializers import ContactInfoSerializer , SocialLinkSerializer , FooterLinkSerializer


class ContactView(APIView):
    def get(self , request):
        info = ContactInfo.objects.first()
        links = FooterLink.objects.filter(is_active=True)
        return Response({
            "info": ContactInfoSerializer(info , context={"request": request}).data if info else None ,
            "social_links": SocialLinkSerializer(SocialLink.objects.filter(is_active=True) , many = True).data ,
            "quick_links": FooterLinkSerializer(links.filter(group = FooterLink.Group.QUICK) , many = True).data ,
            "services_links": FooterLinkSerializer(links.filter(group = FooterLink.Group.SERVICES) , many = True).data ,
        })