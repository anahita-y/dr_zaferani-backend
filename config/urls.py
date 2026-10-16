"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path("admin/", admin.site.urls) ,
    path("api/home/" ,  include("home.urls")) ,
    path("api/services/" , include("services.urls")) ,
    path("api/about/" , include("about.urls")) ,
    path("api/articles/" , include("articles.urls")) ,
    path("api/gallery/" , include("gallery.urls")) ,
    path("api/contact/" , include("contact.urls")) ,
    path("api/faq/" , include("faq.urls")) ,
    path("api/testimonials/" , include("testimonials.urls")) ,
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)


admin.site.site_header = "پنل مدیریت سایت دکتر زعفرانی"
admin.site.site_title = "مدیریت سایت"
admin.site.index_title = "مدیریت محتوا"